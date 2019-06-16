#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------- #
import collections
import copy
import json
import logging
import os
import time

__author__ = "Sveinn Floki Gudmundsson"
__email__ = "svefgud@gmail.com"
__version__ = "0.0.1"

Name = 'gasvaktin'
Logger = None  # declarative main logger

# logger function extention variables
debug = None
info = None
warning = None
error = None
critical = None
exception = None
log = None

# logger configuration
Log_Config = {
    'filename': '{name}.{role}{format}.log',
    'loglevel': logging.DEBUG,
    'format': (
        '[%(asctime)s.%(msecs)03d] '
        '[%(levelname)s] %(message)s '
        '(%(filename)s:%(lineno)d)'
    ),
    'format_colored': (  # https://misc.flogisoft.com/bash/tip_colors_and_formatting
        '\033[32m[%(asctime)s.%(msecs)03d]\033[0m '
        '\033[240;1m[\033[0m%(levelname)s\033[240;1m]\033[0m %(message)s '
        '(%(filename)s:%(lineno)d)'
    ),
    'json_format': ['ts', 'level', 'msg', 'pathname', 'lineno'],
    'time_format': '%Y-%m-%dT%H:%M:%S'
}


class JSONFormatter(logging.Formatter):
    '''formats log records to single line minified JSON format'''

    def __init__(self, recordfields=None):
        # https://docs.python.org/3/library/logging.html#logrecord-objects
        if recordfields is not None:
            assert(type(recordfields) is list)
            for recordfield in recordfields:
                assert(type(recordfield) is str)
            self.recordfields = recordfields
        else:
            self.recordfields = ['ts', 'level', 'msg', 'pathname', 'lineno']

    def format(self, record):
        '''override ancestor class function to generate minified JSON string from log record'''
        if (len(self.recordfields) > 0):
            fields = []
            timestamp = '%s.%03d' % (  # isoformatted timestamp with msecs
                time.strftime('%Y-%m-%dT%H:%M:%S', self.converter(record.created)),
                record.msecs
            )
            if 'ts' not in self.recordfields:
                fields.append(('ts', timestamp))  # we always want the timestamp right?
            for recordfield in self.recordfields:
                if recordfield == 'ts':
                    fields.append((recordfield, timestamp))
                elif hasattr(record, recordfield) and getattr(record, recordfield) is not None:
                    fields.append((recordfield, getattr(record, recordfield)))
            if 'msg' not in self.recordfields:
                fields.append(('msg', record.msg))  # we always want the msg right?
            # we use OrderedDict to ensure specified key order in json record
            data = collections.OrderedDict(fields)
        else:
            data = collections.OrderedDict([('ts', timestamp), ('msg', record.msg)])
        return json.dumps(data, separators=(',', ':'))


class ColoredFormatter(logging.Formatter):
    '''formats log records to contain bash colors in our self-constructed needs'''

    prefix = '\033['
    suffix = '\033[0m'

    color_map = {  # https://misc.flogisoft.com/bash/tip_colors_and_formatting
        'default': 39,
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'lightgray': 37,
        'darkgray': 90,
        'lightred': 91,
        'lightgreen': 92,
        'lightyellow': 93,
        'lightblue': 94,
        'lightmagenta': 95,
        'lightcyan': 96,
        'white': 97
    }
    background_map = {
        'default': 49,
        'black': 40,
        'red': 41,
        'green': 42,
        'yellow': 43,
        'blue': 44,
        'magenta': 45,
        'cyan': 46,
        'lightgray': 47,
        'darkgray': 100,
        'lightred': 101,
        'lightgreen': 102,
        'lightyellow': 103,
        'lightblue': 104,
        'lightmagenta': 105,
        'lightcyan': 106,
        'white': 107
    }
    styling_set_map = {
        'bold': 1,
        'dim': 2,
        'underline': 4,
        'blink': 5,
        'invert': 7,
        'hidden': 8
    }
    styling_reset_map = {
        'all': 0,
        'bold': 21,
        'dim': 22,
        'underline': 24,
        'blink': 25,
        'invert': 27,
        'hidden': 28
    }

    def __init__(self, patern, datefmt=None, level_styles=None):
        logging.Formatter.__init__(self, patern, datefmt)
        if level_styles is not None:
            self.assert_valid_styles(level_styles)
            self.level_styles = level_styles
        else:
            self.level_styles = {
                'debug': {'color': 'lightgreen'},
                'info': {'color': 'default'},
                'warning': {'color': 'yellow'},
                'error': {'color': 'red'},
                'critical': {'color': 'red', 'bold': True}
            }

    def assert_valid_styles(self, styles):
        assert(type(styles) is dict)
        for name in styles:
            assert(type(name) is str)
            for style in styles[name]:
                assert(type(style) is dict)
                for key in style.keys():
                    assert(type(key) is str)
                    value = style[key]
                    if key in ('color', 'background'):
                        assert(type(value) in (str, int))
                    else:
                        assert(key in self.styling_set_map.keys())
                        assert(type(value) is bool)

    def get_style_codes(self, style):
        style_codes = []
        for key in style.keys():
            if key == 'color':
                if type(style[key]) is str:
                    style_codes.append(self.color_map[style[key]])
                elif type(style[key]) is int:
                    style_codes.append(style[key])
            elif key == 'background':
                if type(style[key]) is str:
                    style_codes.append(self.background_map[style[key]])
                elif type(style[key]) is int:
                    style_codes.append(style[key])
            elif key in self.styling_set_map.keys() and style[key] is True:
                style_codes.append(self.styling_set_map[key])
        return style_codes

    def format(self, record):
        colored_record = copy.copy(record)
        # set styles for message based on levelname
        level_style_codes = []
        level_style = self.level_styles.get(colored_record.levelname.lower(), {'color': 'default'})
        level_style_codes = self.get_style_codes(level_style)
        seq_msg = ';'.join(str(x) for x in level_style_codes)
        colored_message = colored_record.msg
        colored_record.msg = '{0}{1}m{2}{3}'.format(
            self.prefix, seq_msg, colored_message, self.suffix
        )
        # set styles for levelname based on levelname, also always use bold
        seq_lvl = seq_msg
        if self.styling_set_map['bold'] not in level_style_codes:
            seq_lvl = ';'.join(
                str(x) for x in (level_style_codes + [self.styling_set_map['bold']])
            )
        colored_record.levelname = '{0}{1}m{2}{3}'.format(
            self.prefix, seq_lvl, colored_record.levelname, self.suffix
        )
        return logging.Formatter.format(self, colored_record)


def configure_logger(name, role, config, output_dir='./', log_to_cli=False, log_to_file=True):
    logger = logging.getLogger(name)
    log_level = config['loglevel']
    logger.setLevel(log_level)
    if log_to_cli:
        # setup streamhandler to terminal
        streamhandler = logging.StreamHandler()
        formatter_console = ColoredFormatter(config['format_colored'], config['time_format'])
        streamhandler.setFormatter(formatter_console)
        logger.addHandler(streamhandler)
    if log_to_file:
        if not os.path.exists(output_dir):
            # create log output directory
            logger.info('Creating directory "%s" ..' % (os.path.abspath(output_dir), ))
            os.makedirs(output_dir)
        # setup readable log file handler
        log_file_readable = os.path.join(
            output_dir, config['filename'].format(name=name, role=role, format='')
        )
        file_handler_readable = logging.FileHandler(
            log_file_readable, 'a', encoding='utf-8', delay='true'
        )
        file_handler_readable.setLevel(log_level)
        formatter_readable = logging.Formatter(config['format'], config['time_format'])
        file_handler_readable.setFormatter(formatter_readable)
        logger.addHandler(file_handler_readable)
        # setup minified-single-line-json log file handler
        log_file_json = os.path.join(
            output_dir, config['filename'].format(name=name, role=role, format='.json')
        )
        file_handler_json = logging.FileHandler(
            log_file_json, 'a', encoding='utf-8', delay='true'
        )
        file_handler_json.setLevel(log_level)
        formatter_json = JSONFormatter(config['json_format'])
        file_handler_json.setFormatter(formatter_json)
        logger.addHandler(file_handler_json)
    return logger


def init(role, output_dir='./logs/', log_to_cli=True, log_to_file=True):
    global Name, Logger, Log_Config
    global debug, info, warning, error, critical, exception, log
    assert(role in ('cli', 'api', 'cron', 'hook'))

    if Logger is not None:
        Logger.warning('logger already initialized')

    output_dir_abs = os.path.abspath(output_dir)
    if output_dir.startswith('./'):
        output_dir_abs = os.path.join(os.path.dirname(os.path.realpath(__file__)), output_dir)

    # create main logger
    Logger = configure_logger(Name, role, Log_Config, output_dir_abs, log_to_cli, log_to_file)
    # extend log functions
    debug = Logger.debug
    info = Logger.info
    warning = Logger.warning
    error = Logger.error
    critical = Logger.critical
    exception = Logger.exception
    log = Logger.log

    return Logger
