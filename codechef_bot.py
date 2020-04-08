import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class chefBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get("https://www.codechef.com")
        time.sleep(1)
        username = self.driver.find_element_by_xpath('/html/body/section/div/div/ul/div[1]/form[1]/div/div[1]/input')
        password = self.driver.find_element_by_xpath('/html/body/section/div/div/ul/div[1]/form[1]/div/div[2]/input')
        login_button = self.driver.find_element_by_xpath('/html/body/section/div/div/ul/div[1]/form[1]/div/input[4]')
        
        username.send_keys('Raviwarlord')
        password.send_keys('TanX@23298')
        login_button.click()
    
    def go_to_account_section(self):
        hidden_button = self.driver.find_element_by_xpath('/html/body/section/div/div/ul/li[1]/span[2]/a/i')
        hidden_button.click()
        account_button = self.driver.find_element_by_xpath('/html/body/section/div/div/ul/li[1]/span[2]/ul/li[1]/a')
        account_button.click()
        
    def get_links(self):
        hrefs = []
        parent = self.driver.find_element_by_class_name('problems-solved')
        links = parent.find_elements_by_tag_name('a')
        for link in links:
            tmp = link.get_attribute('href')
            hrefs.append(tmp)
        return hrefs
    
    def get_ac_code_link(self, link):
        self.driver.get(link)
        time.sleep(3)
        select = Select(self.driver.find_element_by_id('status'))
        select.select_by_value('15')
        go_button = self.driver.find_element_by_xpath('/html/body/center/center/table/tbody/tr/td/div/div/div/div/div[2]/div/form/table/tbody/tr/td[3]/input')
        go_button.click()
        time.sleep(3)
        sol_link = self.driver.find_element_by_xpath('/html/body/center/center/table/tbody/tr/td/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[8]/ul/li/a').get_attribute('href')
        return sol_link
    


def driver_code():
    bot = chefBot()
    bot.login()
    time.sleep(3)
    bot.go_to_account_section()
    links = bot.get_links()
    for link in links:
        tmp = bot.get_ac_code_link(link)
        bot.driver.get(tmp)
        time.sleep(3)
        bot.driver.find_element_by_xpath('/html/body/main/div/section/div/section[1]/aside/div/div/div[2]/ul/li[2]/a/i').click()