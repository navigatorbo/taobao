from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options


def search():
    driver.find_element_by_id('q').send_keys('python')
    driver.find_element_by_class_name('btn-search').click()
    # 为了避免报错，可以在这异常设置
    time.sleep(10)
    while 1:
        start = time.process_time()
        try:
            token=driver.find_element_by_xpath('//div[@id="mainsrp-pager"]/div/div/div/div[1]').text
            print('已定位到元素,元素为'+token)
            end=time.process_time()
            break
        except:
            print('还未定义到元素')
    print('定位耗时时间'+str(end-start))
    token=int(re.compile('\d+').search(token).group(0))
    return token

#翻页
def next_page():
    token=search()
    num =0
    while num != token-1:
        driver.get('https://s.taobao.com/search?q=python&s={}'.format(44*num))
        driver.implicitly_wait(10)
        num+=1
        print('第 %d 页'% num)
        drop_down()
        get_product()

#模拟鼠标滑动，处理部分图片不显示问题
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        j=x/10
        js='document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

#解析爬取的数据，优化：可以选择数据的存储方式
def get_product():
    lis = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for li in lis:
        #标题
        info = li.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        #价格
        price = li.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price')+'元'
        #付款数
        deal = li.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        #图片
        image= li.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        #商品信息
        name = li.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        print(info+'|'+price+'|'+deal+'|'+image+'|'+name)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')
    next_page()

  # keyword = input('请输入你想要的商品信息：')

    # option = webdriver.ChromeOptions()
    # # 开发者模式的开关，设置一下，打开浏览器就不会识别为自动化测试工具了
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # driver = webdriver.Chrome(chrome_options=option)

    # 修改本地IP进行反爬测试
    # chrome_option = Options()
    # chrome_option.add_argument("--disable-extensions")
    # chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # # path为chromedriver的路径
    # driver = webdriver.Chrome(executable_path="F:\python\python_environment\chromedriver.exe",
    #                            chrome_options=chrome_option)
