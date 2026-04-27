from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver
driver = webdriver.Chrome()

# Open the local HTML file
driver.get("file:///workspaces/DEVOPSENDSEM/index.html")

# Find the input field and enter text
name_input = driver.find_element(By.ID, "nameInput")
name_input.send_keys("Selenium Tester")

# Find the button and click it
greet_button = driver.find_element(By.ID, "greetButton")
greet_button.click()

# Wait a bit for the result
time.sleep(1)

# Check the result
result_div = driver.find_element(By.ID, "result")
result_text = result_div.text
print("Result text:", result_text)

# Assert the expected result
expected = "Hello, Selenium Tester! Welcome to Selenium testing."
if expected in result_text:
    print("Test passed!")
else:
    print("Test failed!")

# Close the browser
driver.quit()