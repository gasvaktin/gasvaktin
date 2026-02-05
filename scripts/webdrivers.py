#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_n1_browser_instance(headless=True):
    """
    Run Selenium Webdriver browser instance for N1 webpage.

    N1 webserver might be practicing some anti-bot tactics, I am as of now unaware what kind of
    handshake shenanigans they've possibly implemented, but it results in python requests throwing
    the following SSL error:
        SSLError(SSLError(1, '[SSL] record layer failure (_ssl.c:2657)'))
    """
    res_data = {'error': None, 'html': None}
    options = Options()
    if headless is True:
        options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get('https://www.n1.is/thjonusta/eldsneyti/daeluverd/')
        wait = WebDriverWait(driver, 15)
        el_target = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#composer-render-target'))
        )
        el_render_req = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()='Höfuðborgarsvæðið']"))
        )
        res_data['html'] = el_target.get_attribute('innerHTML')
    except Exception as e:
        res_data['error'] = f'An error occurred: {e}'
    finally:
        driver.quit()
    return res_data


def run_orkan_browser_instance(headless=True):
    """
    Run Selenium Webdriver browser instance for Orkan webpage.

    Orkan moved to a client side rendered website via the Blazor JS front-end library.
    To begin with we were able to receive server side rendered webpage by providing a well known
    google bot webscraper user-agent string, this however stopped working in 2025-07, we still got
    server side rendered page, but the price data table we were parsing prices out of was no longer
    included in the server side rendered HTML.

    I made a couple of attempting to do manual Blazor socket interaction to retrieve the required
    data, but those attempts were unfortunately fruitless, I'm guessing I'd need to dig deeper into
    the Blazor client engine to figure out how to properly manipulate the socket connection to
    serve the appropriate price data table elements, which I'm currently not motivated enough to
    start the process of doing.

    I was hesitant to begin running a full browser instance for this, and attempted for a month to
    get in touch with someone at Orkan to resolve this by either fixing the SSR so it again would
    include the price data table or get an alternative webpage to fetch or even perhaps get access
    to a data API, but unfortunately I never got any replies from Orkan.

    See https://github.com/gasvaktin/gasvaktin/issues/16 for more info.

    So here we are, settling for running a full Selenium Webdriver Firefox browser instance in
    headless mode, have it render the client until the appropriate elements have finished
    rendering to DOM, then we grab the HTML for those elements and return in a string, because when
    extracting data from HTML the tools within lxml are superior to what Selenium provides.

    Usage:  res_data = run_orkan_browser_instance(headless: bool = True)
    Before: @headless is an optional boolean parameter, default True, set it to false to disable
            webdriver headless mode if needed when debugging
    After:  @res_data is a dict containing 'error' and 'html' values, if the webdriver process went
            smooth @res_data['error'] is None and @res_data['html'] is a string containing rendered
            HTML whith the appropriate DOM elements, else @res_data['html'] is None and
            @result_data['error'] is a string containing exception info
    """
    res_data = {'error': None, 'html': None}
    options = Options()
    if headless is True:
        options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get('https://www.orkan.is/orkustodvar/')
        # wait for a specific element to get rendered to DOM, with timeout of 15 seconds
        wait = WebDriverWait(driver, 15)
        el_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.prices__list')))
        # element got rendered in time and all is well, receive rendered HTML via innerHTML
        res_data['html'] = el_table.get_attribute('innerHTML')
    except Exception as e:
        res_data['error'] = f'An error occurred: {e}'
    finally:
        driver.quit()
    return res_data


if __name__ == '__main__':
    res_data = run_orkan_browser_instance()
    print(res_data['html'])
