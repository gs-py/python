
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome (optional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver
webdriver_service = Service(r"C:\Users\gladw\SDK\chrome driver\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

def get_flipkart_price(url):
    try:
        driver.get(url)
        # Wait until the element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div._30jeq3'))
        )
        return price_element.text
    except Exception as e:
        print(f"Error fetching Flipkart details: {e}")
        return None

def get_amazon_price(url):
    try:
        driver.get(url)
        # Wait until the element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.a-price-whole'))
        )
        return price_element.text
    except Exception as e:
        print(f"Error fetching Amazon details: {e}")
        return None

def compare_prices():
    flipkart_url = "https://www.flipkart.com/apple-iphone-14-purple-128-gb/p/itm0b581eba85e08?pid=MOBGHWFHQFSQYBFU&marketplace=FLIPKART"
    amazon_url = "https://www.amazon.in/Apple-iPhone-14-128GB-Purple/dp/B0BDJ213TX/ref=sr_1_3?s=electronics&sr=1-3"
    
    print("Fetching Flipkart price...")
    flipkart_price = get_flipkart_price(flipkart_url)
    print("Flipkart price:", flipkart_price)
    
    print("Fetching Amazon price...")
    amazon_price = get_amazon_price(amazon_url)
    print("Amazon price:", amazon_price)
    
    driver.quit()

if __name__ == "__main__":
    compare_prices()