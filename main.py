import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options=Options()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")

chrome_driver_path="C:\\Users\\USER\\Desktop\\my_python\\chromedriver.exe"
website_URL='https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'


driver=webdriver.Chrome(service_log_path=chrome_driver_path,options=options)
driver.get(website_URL)

sign_in=driver.find_element(by=By.LINK_TEXT,value="Sign in")
sign_in.click()
time.sleep(1)
username=driver.find_element(by=By.NAME,value="session_key")
username.send_keys("preetrajgupta2002@gmail.com")
password=driver.find_element(by=By.NAME,value="session_password")
password.send_keys("@preet00")
time.sleep(1)
submit=driver.find_element(by=By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
print(submit)
submit.click()
time.sleep(3)
apply=driver.find_element(By.CSS_SELECTOR,"div .jobs-apply-button--top-card button")
apply.click()
ph_no=driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3408585864-77801731-phoneNumber-nationalNumber")
ph_no.send_keys("9339606331")
next=driver.find_element(By.ID,"ember396")
next.click()
time.sleep(1)
choose=driver.find_element(By.ID,"ember397")
choose.click()
next.click()
select_element=driver.find_element(By.ID,"text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3408585864-77801779-multipleChoice")
select = Select(select_element)
select.select_by_value("No")
review=driver.find_element(By.ID,"ember401")
review.click()

submit_applicaton=driver.find_element(By.ID,"ember411")
submit_applicaton.click()



