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
appointment_date = u'05-24'
appointment_time = u'05-24'

def login():
    try:
        while b.is_element_present_by_value(u'登录'):
            print("in the start of loop of login")
            sleep(5)
            b.find_link_by_text(u"登录").click()
            b.fill('orderwebUser.userName',loginuserName)
            b.fill('loginuserPassword',loginuserPassword)
            b.fill('logincertCode', loginuserPassword)
            sleep(10)
            b.find_by_value(u'登录').click()
            print("click login button")
            sleep(5)
            if b.is_element_present_by_value(u'注销退出'):
                print("already logined !")
                break
    except Exception:
        print("error occur")

def expert_choose():
    doctor_flag = False
    hospital_flag = False
    try:
        b.click_link_by_text(u'我的专家')

        element1 = b.find_by_id('ctl00_ContentPlaceHolder1_divdoctorlist')
        element2 = element1.find_by_css('div.content_doctor') + element1.find_by_css('div.content_doctor_even')
        for each2 in element2:
            element3 = each2.find_by_css('div.content_doctor_action')
            element4 = each2.find_by_css('div.content_doctor_detail')
            element5 = element4.find_by_css('div.content_doctor_detail_top')
            element6 = element5.find_by_tag('p')
            for each6 in element6:
                if each6.text == doctorname:
                    doctor_flag = True
                if each6.text == hospitalname:
                    hospital_flag = True
            if doctor_flag == True and hospital_flag == True:
                element7 = element3.find_by_css('div.content_doctor_action_bottom')
                break

        button_appointment = element7.find_by_value(u'预约')
        button_appointment.click()

    except Exception:
        print("error occur")

def date_choose():
    dict_date = {}

    while dict_date == {}:
        try:
            element1 = b.find_by_id('divorder_content')
            element2 = element1.find_by_css('div.order_date_date')
            for each2 in element2:
                element3 = each2.find_by_tag('ul')
                element4 = element3.find_by_tag('li')
                for each4 in element4:
                    element5 = each4.find_by_tag('span')
                    date = element5.value[element5.value.find(u'月')-2:element5.value.find(u'星期')+3]
                    element6 = each4.find_by_tag('img')
                    for each6 in element6:
                        if each6.outer_html.find('onclick') != -1:
                            dict_date.setdefault(date,each6)
        except Exception:
            print("error occurs")
        if dict_date != {}:
            break
        else:
            b.reload()

    try:
        button_order = dict_date.get(date_determine(dict_date.keys()),0)
        button_order.click()
    except Exception:
        print("error occurs")

def time_choose():
    dict_time = {}
    order_time = ''
    order_button = []
    try:
        element1 = b.find_by_id('divorder_content')
        element2 = element1.find_by_css('div.order_time_list')
        element3 = element2.find_by_tag('ul')
        element4 = element3.find_by_tag('li')
        for each4 in element4:
            if each4.outer_html.find('order_time_list_content_time')!= -1:
                order_time = each4.text
            if each4.outer_html.find('onclick')!= -1:
                order_button = each4
            if order_time != '' and order_button != []:
                dict_time.setdefault(order_time,order_button)
                order_time = ''
                order_button = []
    except Exception:
        print("error occurs")

    try:
        button_order = dict_time.get(time_determine(dict_time.keys()),0)
        button_order.click()
    except Exception:
        print("error occurs")

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
    b.fill('txtVerifyCode','')
    sleep(15)
    element1 = b.find_by_css('div.doctor_qryy_confirm')
    button = element1.find_by_tag('img')
    button.click()
    element2 = b.find_by_css('div.doctor_yycg_ok')
    element3 = element2.find_by_tag('img')
    for each3 in element3:
        if each3.outer_html.find('AgreeNotice')!= -1:
            button_confirm = each3

    button_confirm.click()


def yuyue():
    global b
    b = Browser(driver_name="chrome")
    b.visit(base_url)
    login()
    expert_choose()
    date_choose()
    time_choose()
    reservation_confirm()

    sleep(30)
    b.quit()

if __name__ == "__main__":
    yuyue()