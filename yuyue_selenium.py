# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

base_url = "http://yuyue.shdc.org.cn/"
loginuserName = "15921615178"
loginuserPassword = "87994566"
doctorname = u"赵琳"
appointment_weekday = u'星期三'
appointment_date = u'05-24'

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get(base_url)
driver.find_element_by_link_text(u"登录").click()
driver.find_element_by_css_selector("#loginbox > div.title").click()
driver.find_element_by_id("loginuserName").click()
driver.find_element_by_id("loginuserName").clear()
driver.find_element_by_id("loginuserName").send_keys(loginuserName)
driver.find_element_by_id("loginuserPassword").click()
driver.find_element_by_id("loginuserPassword").clear()
driver.find_element_by_id("loginuserPassword").send_keys(loginuserPassword)
driver.find_element_by_id("logincertCode").click()
driver.find_element_by_id("logincertCode").clear()
driver.find_element_by_id("logincertCode").send_keys("712129")
driver.find_element_by_xpath(u"//input[@value='登录']").click()
driver.find_element_by_link_text(u"个人中心").click()
driver.find_element_by_link_text(u"医生关注").click()
driver.find_element_by_link_text(doctorname).click()
element1 = driver.find_elements_by_name("schedule")
for element2 in element1:
    schedule_date = element2.text.split('\n')[0]
    schedule_weekday = element2.text.split('\n')[1]
    if ( schedule_weekday == appointment_weekday and appointment_weekday != u'' and \
          schedule_date == appointment_date and appointment_date != u'') or \
        (schedule_weekday == appointment_weekday and appointment_weekday != u'' and appointment_date == u'') or \
        (schedule_date == appointment_date and appointment_date != u'' and appointment_weekday == u''):
        element_appointment = element2
        break
element_appointment.click()
element3 = driver.find_elements_by_class_name('selecttime')
element4 = driver.find_elements_by_tag_name('label')
element5 = driver.find_elements_by_name('orderTimeXY1')

driver.find_element_by_link_text(u"下一步").click()
driver.find_element_by_id(u"王忠").click()

#driver.find_element_by_id("tijiaoImage").click()
#driver.find_element_by_id("certCode").clear()
#driver.find_element_by_id("certCode").send_keys("07")
#driver.find_element_by_id("userPhoneVerifyCode").clear()
#driver.find_element_by_id("userPhoneVerifyCode").send_keys("0322")
#driver.find_element_by_id("tijiaoImage").click()