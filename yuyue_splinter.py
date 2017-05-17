# coding=utf-8
from splinter import Browser

base_url = "http://yuyue.shdc.org.cn/"
loginuserName = "15921615178"
loginuserPassword = "87994566"
doctorname = u"赵琳"
appointment_weekday = u'星期三'
appointment_date = u'05-24'


browser = Browser('chrome')

browser.visit(base_url)
browser.find_link_by_text(u"登录").click()
browser.find_by_css("#loginbox > div.title").click()
browser.find_by_id("loginuserName").click()
browser.find_by_id("loginuserName").clear()
browser.find_by_id("loginuserName").send_keys(loginuserName)
browser.find_by_id("loginuserPassword").click()
browser.find_by_id("loginuserPassword").clear()
browser.find_by_id("loginuserPassword").send_keys(loginuserPassword)
browser.find_by_id("logincertCode").click()
browser.find_by_id("logincertCode").clear()
browser.find_by_id("logincertCode").send_keys("712129")
browser.find_by_xpath(u"//input[@value='登录']").click()
browser.find_link_by_text(u"个人中心").click()
browser.find_link_by_text(u"医生关注").click()
browser.find_link_by_text(doctorname).click()
element1 = browser.find_by_name("schedule")
for element2 in element1:
    schedule_date = element2.text.split('\n')[0]
    schedule_weekday = element2.text.split('\n')[1]
    if ( schedule_weekday == appointment_weekday and appointment_weekday != u'' and \
          schedule_date == appointment_date and appointment_date != u'') or \
        (schedule_weekday == appointment_weekday and appointment_weekday != u'' and appointment_date == u'') or \
        (schedule_date == appointment_date and appointment_date != u'' and appointment_weekday == u''):
        appointment = element2
        break
appointment.click()
element4 = browser.find_by_tag('label')
element5 = browser.find_by_name('orderTimeXY1')
element3 = browser.find_elements_by_class_name('selecttime')


browser.quit()