# coding=utf-8
from splinter.browser import Browser
from time import sleep
from random import random
import binascii
from PIL import Image


# 网址
base_url = "http://yuyue.shdc.org.cn/"

def read_config():
    global loginuserName,loginuserPassword, doctorname, hospitalname, appointment_weekday, appointment_date, appointment_time
    config_file = open('yuyue.cfg', mode='r', encoding='utf-8')
    for each in config_file:
        if each[0] == '#' or each == '\n':
            continue
        else:
            param = each.split('=')[0].strip()
            value = each.split('=')[1].lstrip().rstrip('\n')
            if param == 'base_url':
                base_url = value
            elif param == 'loginuserName':
                loginuserName = value
            elif param == 'loginuserPassword':
                loginuserPassword = value
            elif param == 'doctorname':
                doctorname = value
            elif param == 'hospitalname':
                hospitalname = value
            elif param == 'appointment_weekday':
                appointment_weekday = value
            elif param == 'appointment_date':
                appointment_date = value
            elif param == 'appointment_time':
                appointment_time = value

def logincertcode_get():
    certcode_image = logincertcode_image_from_cache()
    logincertcode_image_file_save(certcode_image,'verifycode.jpg')
    logincertCode = ''
    return logincertCode


def logincertcode_image_file_save(image,filename):
    fout = open(filename, 'wb')
    fout.write(image)
    fout.close()


def logincertcode_image_from_cache():
    browser.execute_script('''window.open("about:blank","blank");''')
    browser.windows.current = browser.windows[1]
    browser.visit("chrome://view-http-cache/")
    browser.find_link_by_partial_text('http://yuyue.shdc.org.cn/verifycode.xujie').first.click()
    file_cache = browser.html
    browser.windows.current.close()
    file_cache1 = file_cache[file_cache.rfind('00000000:'):file_cache.find('</pre><hr /><pre></pre><table>')].split('\n')
    file_cache2 = ''
    for line in file_cache1:
        file_cache2 = file_cache2 + line[9:57].replace(' ','')
    file_cache3 = binascii.unhexlify(file_cache2)
    return file_cache3


def login():
    try:
        if browser.find_link_by_text(u"登录"):
            loginned = 0
            browser.find_link_by_text(u"登录").click()
            browser.fill('orderwebUser.userName', loginuserName)
            browser.fill('loginuserPassword', loginuserPassword)
#            logincertCode = logincertcode_get()
            logincertCode = loginuserPassword
            browser.fill('logincertCode', logincertCode)
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
    element3 = browser.find_by_css('dl.docinfo')
    for element4 in element3:
        element5 = element4.find_by_xpath('dd').first.find_by_xpath('p').first
        if doctorname in element5.text:
            element6 = element5.find_by_xpath('a').first
            break
    if element6 != []:
        element6.click()
        return True
    else:
        return False


def date_choose():
    element1 = browser.find_by_name("schedule")
    date_available = []
    date_chosen = ''
    for element2 in element1:
        date_available.append(element2.text)
    date_chosen = date_determine(date_available)
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


def date_determine(date_available,mode=2):
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
        date_cmp = []
        for each1 in date_available:
            date_cmp.append(each1.split('\n')[0])
        date_cmp_chosen = sorted(date_cmp, reverse=False)[0]
        for each1 in date_available:
            date_cmp_chosen == each1.split('\n')[0]
            date_chosen = each1
            break
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
    time_chosen = time_determine(time_available)
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


def time_determine(time_available,mode = 2):
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
    read_config()
    browser.visit(base_url)
    while login():
        read_config()
        if expert_choose():
            if date_choose():
                if time_choose():
                    reservation_confirm()
                    sleep(60*random())
    browser.quit()


if __name__ == "__main__":
    yuyue()
