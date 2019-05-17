from selenium.webdriver.support.ui import Select
from selenium import webdriver


list = [4038, 4036]

username = input("Type your username: ")
password = input("Type in your password: ")

browser = webdriver.Chrome("C:\\Users\Andrew\\Desktop\Coddeeeeee witttht Andrew\\chrome\\chromedriver.exe")
browser.get("https://sms.schoolsoft.se/engelska/jsp/Login.jsp")
select = Select(browser.find_element_by_xpath("//select[@id='usertype']"))

# select by visible text
select.select_by_visible_text('Student')

element = browser.find_element_by_name("ssusername")
element.send_keys(username)
element = browser.find_element_by_name("sspassword")
element.send_keys(password)

browser.find_element_by_xpath('/html/body/div/div/div[3]/form/div[2]/input').click()

print("Status: On schoolsoft first page.")

nextoption = input("What page do you want to see? (Eg. Grades, Forum etc.")

if nextoption == "Grades":
    browser.find_element_by_xpath('//*[@id="menu_gradesubject"]').click()
if nextoption == "Forum":
    browser.find_element_by_xpath('//*[@id="menu_forum_list"]').click()

nextoption2 = input("Do you want to see any specific subject? Write the subject then!")

if nextoption2 == "Art":
    browser.find_element_by_xpath('//*[@id="menu_gradesubject4036"]').click()

if nextoption2 == "Biology":
    browser.find_element_by_xpath('//*[@id="menu_gradesubject4050"]').click()



k=input("press close to exit")
