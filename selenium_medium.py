from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


PATH = "chromedriver"

# driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title = driver.title
# driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

# time.sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.get("https://medium.com/@ozbillwang/vercel-two-use-cases-i-learned-recently-e0e07b21ede5")  
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     driver.maximize_window()
#     # Wait to load page
#     # time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# driver.quit()

# url_to_open='https://medium.com/@ozbillwang/vercel-two-use-cases-i-learned-recently-e0e07b21ede5'
url_to_open='https://medium.com/p/3f4d13258591'

num_iterations = 5

# Loop to open URL, perform actions, and close browser
for i in range(num_iterations):
    # Create a new instance of the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # You can use other browser drivers as well

    # Open the URL
    driver.get(url_to_open)

    # Perform some actions (you can add your specific actions here)
    # For example, printing the page title
    print("Iteration:", i + 1, "- Page Title:", driver.title)
    driver.maximize_window()
    
    # element=driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[4]/div/div/p/span/a')
    # element.click()

    # singin=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div[2]/div[4]/button/div')
    # singin.click()

    # email=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div/p/input')
    # email.send_keys("caixinemail@gmail.com")

    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for a moment (you can adjust this as needed)
    login_element = driver.find_element(By.CSS_SELECTOR('[data-testid="headerSignInButton"]'))
    time.sleep(1)
    login_element.click()
    time.sleep(1)

    # Close the browser
    driver.quit()

    # Wait for a moment before starting the next iteration (optional)
    time.sleep(1)