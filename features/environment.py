from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import ClientConfig
import tempfile, shutil


from app.application import Application
from support.logger import logger

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ## CHROME ##
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    ## FIREFOX ##
    # context.driver = webdriver.Firefox()


    ## HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )
    # context.driver.set_window_size(1920, 1080)



    ### BROWSERSTACK ###
   # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
   #  bs_user = 'nicoolumese_7cY5dg'
   #  bs_key = 'YHgF8m3qX8JfM2PCeXPs'
   #  url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
   #
   #  options = Options()
   #  # bstack_options = {
    #     "os" : "Samsung",
    #     "osVersion" : "13",
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name,
    # }


    # bstack_options = {
    #     'deviceName': 'Samsung Galaxy S22 Ultra',  # Replace with desired device
    #     'platformName': 'Android',  # Or 'iOS'
    #     'browserName': 'Chrome',  # Mobile Chrome browser
    #     'sessionName': scenario_name,
    #     'interactiveDebugging': True
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)



    ### Chrome Mobile Emulation ###
    # mobile_emulation = {"deviceName": "iPhone SE"}
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver,10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: , {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'Started failed: , {step}')

def after_scenario(context, feature):
    context.driver.quit()




def _make_driver():
    opts = Options()

    # fresh throwaway profile so Google Password Manager isn’t active
    tmp_profile = tempfile.mkdtemp(prefix="chrome-prof-")
    opts.add_argument(f"--user-data-dir={tmp_profile}")

    # kill password prompts/leak checks
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False
    })
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--disable-infobars")
    opts.add_argument("--incognito")
    opts.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck,PasswordManagerOnboarding")

    driver = webdriver.Chrome(options=opts)
    driver._tmp_profile = tmp_profile   # keep for cleanup
    return driver

def before_all(context):
    context.driver = _make_driver()
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()
    try:
        context.driver.quit()
    finally:
        # remove the temp Chrome profile folder
        if hasattr(context.driver, "_tmp_profile"):
            shutil.rmtree(context.driver._tmp_profile, ignore_errors=True)