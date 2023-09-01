from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3688583763&distance=25&f_AL=true&geoId=106591199"
           "&keywords=python%20developer&location=Helsinki%2C%20Uusimaa%2C%20Finland&refresh=true")

# Get reject cookie button
time.sleep(2)
reject_cookies = driver.find_element(By.XPATH, '''//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]''')
reject_cookies.click()

# Get login button
time.sleep(2)
login = driver.find_element(By.LINK_TEXT, value="Sign in")
login.click()

# Sign in
time.sleep(2)
sign_in = driver.find_element(By.XPATH, '''//*[@id="username"]''')
sign_in.send_keys("jintao.aalto@gmail.com")

pass_word = driver.find_element(By.ID, "password")
pass_word.send_keys("%TGB6yhn1234")

sign_in_button = driver.find_element(By.XPATH, '''//*[@id="organic-div"]/form/div[3]/button''')
sign_in_button.click()

# Save the first job
time.sleep(3)
#
# job_save.click()

# Find all the job on the page

jobs_listing = driver.find_elements(By.CSS_SELECTOR, value=".job-card-list__title")
# job.click()
for job in jobs_listing:
    print(job.text)
    job.click()
    time.sleep(2)
    job_save = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    job_save.click()
    # # Get cookies to click on
# cookie = driver.find_element(By.ID, "cookie")
#
# # Get price dic of afforded items
#
# prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#
# for price in prices[:-1]:
#     price_names.append(price.text.split("-")[0].strip())
#     price_values.append(int(price.text.split("-")[1].strip().replace(",", "")))
#
# for n in range(len(price_names)):
#     price_dic[price_names[n]] = price_values[n]
#
# timeout = time.time() + 5  # 5 seconds to check items to buy
# time_min = time.time() + 60 * 5  # 5 mins break

