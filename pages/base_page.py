from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def __init__(self):
        # Initialize the driver using webdriver-manager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.timeout = 10

    def find(self, by, locator):
        """Find an element with a given locator."""
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        """Click an element identified by a locator."""
        self.find(by, locator).click()

    def write(self, by, locator, text):
        """Write text into an input field identified by a locator."""
        self.find(by, locator).clear()
        self.find(by, locator).send_keys(text)

    def get_text(self, by, locator):
        """Get the text of an element identified by a locator."""
        return self.find(by, locator).text

    def is_element_visible(self, by, locator):
        """Check if an element is visible on the page."""
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by, locator)))
            return True
        except:
            return False
