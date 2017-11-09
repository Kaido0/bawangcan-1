#coding:gbk

#���� by Master_13
#@20171109
#1. ֻ����û�б�����
#2. ����֧�֡��ƽ��油��������Զ���ѡ
#3. ����Ȧ�����ײͻ�Զ����ԣ����ֹ�ȥ��վ�ϱ���

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def process_category(url,driver):
    driver.get(url)
    try:
        #һֱ��鿴���࣬�������л
        while(1):
            more=driver.find_element_by_class_name("monad-more")
            more.click()
            time.sleep(2)
    except:
        pass
    all_event_url=[]
    elements=driver.find_elements_by_class_name("monad-default")
    for e in elements:
        monadd=e.find_element_by_class_name("monad-data")
        if monadd.text.find(u'�ѱ���')==-1:    #��δ����
            a = e.find_element_by_tag_name("a")
            event_url= a.get_attribute("href")
            title=a.get_attribute("title")
            all_event_url.append((str(event_url),title))                

    total=len(all_event_url)
    print "��ʼ����"+str(total)+"���..."
    cnt=0
    no=0
    for url in all_event_url:
        driver.get(url[0])
        no+=1
        try:
            big_btn=driver.find_element_by_class_name("big-btn")
            big_btn.click()
            try:    #ͬ��ƽ��油
                sel=Select(driver.find_element_by_class_name("J_applyExtendInfo"))
                sel.select_by_index(1)                
            except:
                pass
            ok=driver.find_element_by_id("J_pop_ok")
            ok.click()
            cnt+=1
            print str(no)+" success:"+url[1].encode('utf8')
        except:
            print str(no)+' failed:'+url[1].encode('utf8')
        time.sleep(3)
    return;

def main():
    print '����ִ�С���'

    print sys.argv
    print len(sys.argv)
    dper= sys.argv[1]
    print "your dper is:"+dper
    

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=opts)
    driver.maximize_window()

    driver.get("http://s.dianping.com/event/119124")
    driver.add_cookie({'name':'dper', 'value':dper,'path':'/'})
    category_urls=[]
    category_urls.append("http://s.dianping.com/event/shanghai/c1") #��ʳ
    category_urls.append("http://s.dianping.com/event/shanghai/c6") #����
    #category_urls.append("http://s.dianping.com/event/shanghai/c2")#����
    category_urls.append("http://s.dianping.com/event/shanghai/c99")#����
    for url in category_urls:
        process_category(url, driver)
    driver.quit()


if __name__ == '__main__':
    main()
