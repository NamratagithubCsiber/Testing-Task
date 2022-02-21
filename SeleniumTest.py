from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
import time
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

wd = webdriver.Edge(executable_path="C:\\Users\\Namrata\Downloads\\edgedriver_win64\\msedgedriver.exe")
print(wd.title)
print(wd.current_url)
wd.get("https://www.thesparksfoundationsingapore.org/")
print("\nTest Cases")

# TestCase 1: Title Verification
print("\nTestCase 1:")
if wd.title:
    print("\nTitle Verified Successfully: ", wd.title)
else:
    print("\nTitle Verification Failed!\n")

# TestCase 2: To find logo of the webpage
print("\nTestCase 2:")
try:
    wd.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Tested Successfuly! The logo is present\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo is present!\n')

# TestCase 3: Check if navbar present
print("TestCase 3:")
try:
    wd.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: Home button
print("TestCase 4:")
try:
    wd.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link is working!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 5: About Us Page
print("TestCase 5:")
try:
    wd.find_element_by_link_text('About Us').click()
    time.sleep(4)
    wd.find_element_by_link_text('Corporate Partners').click()
    time.sleep(4)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(4)

# TestCase 6: Policy page testing
print('TestCase 6:')
try:
    wd.find_element_by_link_text('Policies and Code').click()
    time.sleep(4)
    wd.find_element_by_link_text("Policies").click()
    time.sleep(4)
    wd.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(4)
    print('Policy Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Programs page verification
print('TestCase 7:')
try:
    wd.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(4)
    wd.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(4)
    wd.find_element_by_link_text('Student SOS Program').click()
    time.sleep(4)
    print('Programs Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 8: Test Contact us Page
print("TestCase 8:")
try:
    wd.find_element_by_link_text("Contact Us").click()
    time.sleep(4)
    info = wd.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(4)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Incorrect!')
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")

# TestCase 9: Links Page
print("TestCase 9:")
try:
    wd.find_element_by_link_text('LINKS').click()
    time.sleep(4)
    wd.find_element_by_link_text('Software & App').click()
    time.sleep(4)
    wd.find_element_by_link_text('AI in Education').click()
    time.sleep(4)
    print('LINKS Verfication Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 10: Check the Form 
print("TestCase 10:")
try:
    wd.find_element_by_link_text('Join Us').click()
    time.sleep(4)
    wd.find_element_by_link_text('Why Join Us').click()
    time.sleep(4)
    wd.find_element_by_name('Name').send_keys('Namrata Desai')
    time.sleep(4)
    wd.find_element_by_name('Email').send_keys('namudesai99@gmail.com')
    time.sleep(4)
    select = Select(wd.find_element_by_class_name('form-control'))
    time.sleep(4)
    select.select_by_visible_text('Intern')
    time.sleep(4)
    wd.find_element_by_class_name('button-w3layouts').click()
    time.sleep(4)
    print("Form Verification Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(4)
cls=wd.close()