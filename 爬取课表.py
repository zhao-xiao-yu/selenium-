from selenium import webdriver
from time import sleep
import csv

bro = webdriver.Chrome(executable_path='chromedriver.exe')
#网址
index_url="https://jw.tskjxy.com.cn{}"
bro.get(index_url.format('/jwglxt/xtgl/login_slogin.html'))


userName_tag = bro.find_element_by_name("yhm")
password_tag = bro.find_element_by_id("mm")
sleep(1)

xuehao = "账号"
pwd = "密码"
#用户名
userName_tag.send_keys(xuehao)
sleep(2)
#登录密码
password_tag.send_keys(pwd)
sleep(1)

#点击登录按钮
btn = bro.find_element_by_id('dl')
btn.click()
sleep(3)
#获取当前网页的的url
new_url = bro.current_url
# print(new_url)
#点击查询课表a
bta = bro.find_element_by_xpath('/html/body/div[3]/div/nav/ul/li[3]/a')
bta.click()
sleep(2)
#点击当前课表
bta2 = bro.find_element_by_xpath('//*[@id="cdNav"]/ul/li[3]/ul/li[1]/a')
subUrl = bta2.get_attribute("onclick")
bta2.click()
sleep(2)

#获取课表url
hand = bro.window_handles#获取当前的所有句柄
# print(hand)#打印当前的所有句柄
bro.switch_to_window(hand[1])#转换窗口至最高的句柄
result_url = bro.current_url#获取当前句柄之后的url
# print(bro.current_url)#打印当前句柄之后的url

course=[]   #存放课程
time=[] #存放时间
teacher=[]  #存放老师
classroom=[]    #存放教室

for i in range(1,7): #天数
    for j in range(1,10): #第几节课
        c_name=bro.find_elements_by_xpath('//*[@id="'+str(i)+'-'+str(j)+'"]/div/span')
        c_time=bro.find_elements_by_xpath('//*[@id="'+str(i)+'-'+str(j)+'"]/div/p[1]')
        c_classroom=bro.find_elements_by_xpath('//*[@id="'+str(i)+'-'+str(j)+'"]/div/p[2]')
        c_teacher=bro.find_elements_by_xpath('//*[@id="'+str(i)+'-'+str(j)+'"]/div/p[3]')
        for element in c_name:
            course.append(element.text)
        for element in c_time:
            time.append(element.text+" 星期"+str(i))
        for element in c_classroom:
            classroom.append(element.text)
        for element in c_teacher:
            teacher.append(element.text)

with open('./kcb_data.csv','a',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    # writerow()只能放一个参数
    writer.writerow(['course','time','classroom','teacher'])
    for i in range(len(course)):
        item = [course[i],time[i],classroom[i],teacher[i]]
        writer.writerow(item)
sleep(1)
bro.quit()