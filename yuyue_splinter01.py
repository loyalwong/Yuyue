# coding=utf-8
from splinter.browser import Browser
from time import sleep

#网址
base_url = "http://yuyue.shdc.org.cn/"
#用户名，密码
loginuserName = "15921615178"
loginuserPassword = "87994566"
#医生
doctorname = u"赵琳"
hospitalname = u"医院：新华医院"
appointment_weekday = u'星期三'
appointment_date = u'06-07'
appointment_time = u'2017-06-07 09:00-10:00'

def login():
    try:
        while browser.find_link_by_text(u"登录"):
            browser.find_link_by_text(u"登录").click()
            browser.fill('orderwebUser.userName',loginuserName)
            browser.fill('loginuserPassword',loginuserPassword)
            browser.fill('logincertCode', loginuserPassword)
            browser.find_by_value(u'登录').click()
            if browser.is_element_present_by_value(u'注销'):
                break
    except Exception:
        print("error occur")

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


def date_choose():
    element1 = browser.find_by_name("schedule")
    for element2 in element1:
        schedule_date = element2.text.split('\n')[0]
        schedule_weekday = element2.text.split('\n')[1]
        if (schedule_weekday == appointment_weekday and appointment_weekday != u'' and \
                        schedule_date == appointment_date and appointment_date != u'') or \
                (schedule_weekday == appointment_weekday and appointment_weekday != u'' and appointment_date == u'') or \
                (schedule_date == appointment_date and appointment_date != u'' and appointment_weekday == u''):
            element3 = element2
            break
    element3.click()


def time_choose():
    element1 = browser.find_by_id('confirm_Number')
    element2 = element1.first.find_by_css('ul.selecttime')
    element3 = element2.first.find_by_tag('li')
    for element4 in element3:
        if element4.find_by_tag('label').first.text == appointment_time:
            element5 = element4.find_by_tag('input').first
            break
    element5.click()
    if browser.find_link_by_partial_text(u"下一步") != []:
        browser.click_link_by_partial_text(u"下一步")


def date_determine(date):
    if len(date) == 1:
        return date
    else:
        for each in date:
            if each == appointment_date:
                return each

def time_determine(time):
    if len(time) == 1:
        return time
    else:
        for each in time:
            if each == appointment_time:
                return each

def reservation_confirm():
    browser.fill('certCode', loginuserPassword)
    browser.find_by_name(u"获取短信验证码").first.click()

    if browser.find_link_by_partial_text(u"提交") != []:
        browser.click_link_by_partial_text(u"提交")


def yuyue():
    global browser
    browser = Browser(driver_name="chrome")
    browser.visit(base_url)
    login()
    expert_choose()
    date_choose()
    time_choose()
    reservation_confirm()

    sleep(30)
    browser.quit()

if __name__ == "__main__":
    yuyue()