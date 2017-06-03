# coding=utf-8
from splinter.browser import Browser
from time import sleep
from random import random
import urllib.request


# 网址
base_url = "http://yuyue.shdc.org.cn/"
# 用户名，密码
loginuserName = "15921615178"
loginuserPassword = "87994566"
# 医生
doctorname = u"赵琳"
hospitalname = u"医院：新华医院"
appointment_weekday = u'星期三'
appointment_date = u'06-08'
appointment_time = u'2017-06-07 09:00-10:00'


def login():
    try:
        if browser.find_link_by_text(u"登录"):
            loginned = 0
            browser.find_link_by_text(u"登录").click()
            browser.fill('orderwebUser.userName', loginuserName)
            browser.fill('loginuserPassword', loginuserPassword)
            browser.fill('logincertCode', loginuserPassword)
            urllib.request.urlretrieve("http://yuyue.shdc.org.cn/verifycode.xujie?id=%27+%20Math.random()",
                                       "local-filename.jpg")
            browser.find_by_value(u'登录').click()
            if browser.is_element_present_by_text(u'注销'):
                loginned = 1
        elif browser.is_element_present_by_text(u'注销'):
            loginned = 1
    except Exception:
        if browser.is_element_present_by_text(u'注销'):
            loginned = 1
    if loginned == 1:
        return True
    else:
        return False


def expert_choose():
    if browser.find_link_by_partial_text(u"个人中心") != []:
        browser.click_link_by_partial_text(u"个人中心")
    element1 = browser.find_link_by_partial_text(u"医生关注")
    if element1 != []:
        for element2 in element1:
            if element2.visible:
                element2.click()
                break
    if browser.find_link_by_partial_text(doctorname) != []:
        browser.click_link_by_partial_text(doctorname)
        return True
    else:
        return False


def date_choose():
    element1 = browser.find_by_name("schedule")
    date_available = []
    date_chosen = ''
    for element2 in element1:
        date_available.append(element2.text)
    date_chosen = date_determine(date_available,1)
    element3 = False
    for element2 in element1:
        if element2.text == date_chosen:
            element3 = element2
            break
    if element3:
        element3.click()
        return True
    else:
        return False


def date_determine(date_available,mode=1):
    date_chosen = ''
    if mode == 1:  #accroding setting date & weekday
        for each1 in date_available:
            schedule_date = each1.split('\n')[0]
            schedule_weekday = each1.split('\n')[1]
            if (schedule_weekday == appointment_weekday and appointment_weekday != u'' and \
                             schedule_date == appointment_date and appointment_date != u'') or \
                     (schedule_weekday == appointment_weekday and appointment_weekday != u'' and appointment_date == u'') or \
                     (schedule_date == appointment_date and appointment_date != u'' and appointment_weekday == u''):
                 date_chosen = each1
                 break
    elif mode == 2:  # according to available earliest date
        date_chosen = ''
    else:
        date_chosen = ''
    return date_chosen


def time_choose():
    element1 = browser.find_by_id('confirm_Number')
    element2 = element1.first.find_by_css('ul.selecttime')
    element3 = element2.first.find_by_tag('li')
    time_available = []
    time_chosen = ''
    for element4 in element3:
        time_available.append(element4.find_by_tag('label').first.text)
    time_chosen = time_determine(time_available,2)
    for element4 in element3:
        if element4.find_by_tag('label').first.text == time_chosen:
            element5 = element4.find_by_tag('input').first
            break
    if element5:
        element5.click()
        if browser.find_link_by_partial_text(u"下一步") != []:
            browser.click_link_by_partial_text(u"下一步")
        return True
    else:
        return False


def time_determine(time_available,mode = 1):
    if mode == 1:  #accroding setting date & weekday
        time_chosen = appointment_time
    elif mode == 2:  # according to available earliest time
        time_chosen = sorted(time_available,reverse=False)[0]
    elif mode == 3:
        time_chosen = ''
    else:
        time_chosen = ''
    return time_chosen

def reservation_confirm():
    browser.fill('certCode', loginuserPassword)
    browser.find_by_id('sendPhoneCode').first.click()

    sleep(30)
    browser.fill('phoneCode',loginuserPassword)

    if browser.find_link_by_partial_text(u"提交") != []:
        browser.click_link_by_partial_text(u"提交")


def yuyue():
    global browser
    browser = Browser(driver_name="chrome")
    browser.visit(base_url)
    while login():
        if expert_choose():
            if date_choose():
                if time_choose():
                    reservation_confirm()
                    sleep(60*random.random())
    browser.quit()


if __name__ == "__main__":
    yuyue()
