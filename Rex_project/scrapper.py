import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.rit.edu/dubai/directory")

# Click the "Load More" button 5 times
for i in range(5):
    load_more_button = driver.find_element(By.XPATH, '//button[text()="Load More"]')
    load_more_button.click()
    time.sleep(2)  # Wait for the new content to load

# Scrape the data
employees = driver.find_elements(By.CLASS_NAME, 'views-row')

data = []
for employee in employees[:180]:  # Limit to 180 employees
    name = employee.find_element(By.CLASS_NAME, 'field-name-title').text
    title = employee.find_element(By.CLASS_NAME, 'field-name-field-job-title').text
    email = employee.find_element(By.CLASS_NAME, 'field-name-field-email').text
    data.append([name, title, email])

# Write data to CSV
with open('rit_employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Title", "Email"])
    writer.writerows(data)

# Close the driver
driver.quit()

