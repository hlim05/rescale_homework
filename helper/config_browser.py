from selenium import webdriver


def initiate_driver(project_name, test_name):
    '''
    Can support other browsers by putting in the if statements here.
    '''

    options = webdriver.ChromeOptions()
    prefs = {'safebrowsing.enabled': 'false'}
    # Have chrome run incognito for caching stuffs
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)

    return driver
