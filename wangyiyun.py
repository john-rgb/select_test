#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import csv
from bs4 import BeautifulSoup
import random
# import lxml
def GetListOfSong(weburl,key):
    '''
    :param weburl: the main page of the begaining
    :param key:the key word you want to search
    :return:the detail link of all you searched
    '''
    browser=webdriver.Firefox()
    browser.get(weburl)
    keywords = key
    send_keywords=keywords
    browser.find_element_by_id("srch").send_keys(send_keywords)
    time.sleep(1)
    browser.find_element_by_id("srch").send_keys(Keys.ENTER)
    time.sleep(1)
    for handle in browser.window_handles:
        # print(handle)
        browser.switch_to.window(handle)
    iframe=browser.find_element_by_class_name('g-iframe')
    browser.switch_to.frame(iframe)
    js="window.scrollTo(0,document.body.scrollHeight)"
    browser.execute_script(js)# go to bottom of the page(important)
    time.sleep(1)
    ended='js-disabled'#the button of next page sign that the last one
    s=browser.find_element_by_class_name('znxt')
    urls=[]
    link=browser.find_elements_by_xpath("//*[contains(@href,'song?id=')]")#use xpath locate the link of the song detail
    for url in link:
        urls.append(url.get_attribute('href'))
    while ended not in s.get_attribute('class'):#get all link of every page
        s.click()
        browser.execute_script(js)
        time.sleep(1)
        s = browser.find_element_by_class_name('znxt')
        print(s.get_attribute('class'))
        link = browser.find_elements_by_xpath("//*[contains(@href,'song?id=')]")
        for url in link:
            urls.append(url.get_attribute('href'))
    time.sleep(0.3)
    return urls
def WriteCsv(data_list,name):#rite songname artist album to csv
    '''
    :param data_list: the data that you want write to csv
    :param name: the name of save file
    :return:null
    '''
    headers=['songname','singer','Album']#write songname artist album to csv
    filename=name+'.csv'
    with open(filename, 'w',newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        for i in write_list:
            try:
                f_csv.writerow(i)
            except:
                continue
            # f_csv.writerows(data_list)
def GetDetail(url,proxy):
    '''
    :param url: the page of detail
    :param proxy: the random proxy
    :return: list of songname artist album
    '''
    write_list=[]
    # print(proxy)
    print(url)
    httpproxy_handler=urllib.request.ProxyHandler(proxy)#66ip.cn set proxy ip
    nullhttpproxy_handler=urllib.request.ProxyHandler({})
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
    req=urllib.request.Request(url)
    openner=urllib.request.build_opener(nullhttpproxy_handler)
    openner.addheaders=[headers]
    f=openner.open(req)
    soup=BeautifulSoup(f.read(),'lxml')#get html
    song_name=soup.find('div','tit').em.string
    write_list.append(song_name)
    s=soup.find_all('a','s-fc7')
    print(s)
    artist = ''
    album = ''
    for i in s:
        if 'artist'in str(i):
            artist=i.string
            print(artist)
        if 'album'in str(i):
            album=i.string
    if artist:
        # print(artist)
        write_list.append(artist)
    else:
        write_list.append('null')
    if album:
        write_list.append(album)
    else:
        write_list.append('null')
    print(write_list)
    return write_list


if __name__=='__main__':
    search_name=input('>>')
    write_list=[]
    proxy_list=[{'http':'59.172.27.6:38380'},{'http':'59.172.27.6:38380'},{'http':'120.79.212.174:8000'}]#successed proxy

    urllist=GetListOfSong("https://music.163.com/",search_name)
    for url in urllist:
        p = random.choice(proxy_list)#get the proxy by randomly
        writedata=GetDetail(url,p)
        write_list.append(writedata)
    WriteCsv(write_list,search_name)



