from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import tempfile
import os
KAFKA_URL = "https://perf.invhub.fseng.net/kafka-ui/login"
ORACLE_URL = "https://perf.invhub.fseng.net/pgadmin/browser/"
USERNAME = "Admin"
PASSWORD = "rFt9f7YcvzZlI7kL"
Total_rows = 14

# rows = driver.find_elements(By.XPATH, "//table//tr")

# total_rows = int(len(rows))

def login(driver, wait):
    driver.get(KAFKA_URL)
    # Wait for login page to load and input to be visible
    username_input = wait.until(EC.visibility_of_element_located((By.ID, 'username')))
    username_input.send_keys(USERNAME)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
    password_input.send_keys(PASSWORD)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

def click_topics(driver, wait):
    topics_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Topics']")))
    topics_link.click()
    time.sleep(2)
    # Optionally, wait for the page content to update

def clean_up_policy_delete(driver, wait):
    try:
        click_topics(driver, wait)
        titles = ["connect-configs","connect-offsets","connect-status"]
        for title in titles:
            xpath =f"//a[@title='{title}']"
            click_connect_offsets = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            click_connect_offsets.click()
            click_three_dots=wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@class='sc-gjLLEI fJrYZu']/button[@aria-label='Dropdown Toggle'])[2]")))
            click_three_dots.click()
            time.sleep(5)
            click_edit_settings=wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(., 'Edit settings')]")))
            click_edit_settings.click()
            click_clean_up_policy=wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='topicFormCleanupPolicy']")))
            click_clean_up_policy.click()
            time.sleep(2)
            click_clean_up_policy_delete=wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@value='delete']")))
            click_clean_up_policy_delete.click()
            time.sleep(2)
            click_update_topic=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            click_update_topic.click()
            time.sleep(2)
            click_topics(driver, wait)
    except Exception as e:
        print(f"Error in clean_up_policy_delete: {e}")
def clean_up_policy_compact(driver, wait):
    try:
        click_topics(driver, wait)
        titles = ["connect-configs","connect-offsets","connect-status"]
        for title in titles:
            xpath =f"//a[@title='{title}']"
            click_connect_offsets = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            click_connect_offsets.click()
            click_three_dots=wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@class='sc-gjLLEI fJrYZu']/button[@aria-label='Dropdown Toggle'])[2]")))
            click_three_dots.click()
            time.sleep(5)
            click_edit_settings=wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(., 'Edit settings')]")))
            click_edit_settings.click()
            click_clean_up_policy=wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='topicFormCleanupPolicy']")))
            click_clean_up_policy.click()
            time.sleep(2)
            click_clean_up_policy_compact=wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@value='compact']")))
            click_clean_up_policy_compact.click()
            time.sleep(2)
            click_update_topic=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            click_update_topic.click()
            time.sleep(2)
            click_topics(driver, wait)
    except Exception as e:
        print(f"Error in clean_up_policy_delete: {e}")
def restart_connectors(driver, wait):
    click_KafkaConnect = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Kafka Connect']")))
    click_KafkaConnect.click()
    time.sleep(5)
    for i in range(2, 3):
            try:  
                click_3dotsicon = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//button[@aria-label='Dropdown Toggle'])[{i}]")))   
                click_3dotsicon.click()
                time.sleep(5)
                click_restart = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//li[@class='szh-menu__item' and text()='Restart Connector'])")))
                click_restart.click()
                time.sleep(5)
    
            except Exception as e:
                print(f"Error clicking connector {i}: {e}")
                continue
def process_clear_messages(driver, wait):
    for i in range(4, Total_rows+3):
        try:
            three_dots_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//button[@class='sc-cyZbeP eicGGV'])[{i}]")))
            time.sleep(5)
            three_dots_btn.click()

            parent_li = wait.until(EC.presence_of_element_located((By.XPATH, f"(//div[contains(text(),'Clear Messages')])[{i-2}]/..")))
            class_value = parent_li.get_attribute("class")
            print(f"row {i-2}, class: {class_value}")

            if class_value == "szh-menu__item szh-menu__item--disabled":
                print("Clear Messages is disabled")
                click_topics(driver, wait)
                time.sleep(5)
                continue
            else:
                # Click the enabled "Clear Messages"
                parent_li.click()
                confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Confirm')]")))
                confirm_btn.click()
                # Optionally, wait for confirmation to disappear or update
        except Exception as e:
            print(f"Error on item {i}: {e}")
            click_topics(driver, wait)  # Try to recover by returning to topics
def clean_data_oracle(driver, wait):
    driver.get(ORACLE_URL)
    # Wait for the Oracle page to load and input to be visible
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    username_input.send_keys(USERNAME)      
    password_input = wait.until(EC.visibility_of_element_located((By.name, 'password')))
    password_input.send_keys(PASSWORD)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiButton-label']")))
    login_button.click()
    time.sleep(2)
    click_on_servers= wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='directory-toggle']")))
    click_on_servers.click()
    db_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
    db_password.send_keys(PASSWORD)
    click_ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class=\"//i[@class='directory-toggle']\"]")))
    click_ok_button.click()
    time.sleep(2)
    click_on_public = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='file-entry directory active depth-6']")))
    click_on_public.click()
    click_on_query_tool = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-label='Query Tool']")))
    click_on_query_tool.click()
    time.sleep(2)
def main():
    options = Options()
    options.add_argument("--headless=new")  # Or "--headless" if error persists
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_tmp = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={chrome_tmp}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    try:
        login(driver, wait)
        clean_up_policy_delete(driver, wait)
        click_topics(driver, wait)
        process_clear_messages(driver, wait)
        clean_up_policy_compact(driver, wait)
        # restart_connectors(driver, wait)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
