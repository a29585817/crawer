from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#悠遊卡
CHROMEDRIVER = "chromedriver.exe"
CARD_NUMBER = ""
BIRTHDAY = ""

class Card:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER)

    def run(self):
        self.go_to_website()    
        self.enter_card_number()
        self.enter_birthday()
        self.select_search_range()
        self.click_search()
        self.get_data()

    def go_to_website(self):
        self.driver.get("https://ezweb.easycard.com.tw/search/CardSearch.php")

    def enter_card_number(self):
        cardnumber_input = self.driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[1]/input")
        cardnumber_input.send_keys(CARD_NUMBER)

    def enter_birthday(self):
        birthday_input = self.driver.find_element_by_xpath("/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[2]/input")
        birthday_input.send_keys(BIRTHDAY)

    def select_search_range(self):
        button = self.driver.find_element_by_id("date1m")
        button.send_keys(Keys.SPACE)

    def wait_for_robot_check(self):
        input("press enter when done with robot check....")

    def click_search(self):
        self.driver.find_element_by_id("btnSearch").click()
    
    def get_data(self):
        self.driver.implicitly_wait(3)
        rows = self.driver.find_elements_by_class_name("r1")    

        for row in rows:
            print(row.text)


if __name__ == "__main__":
    c = Card()
    c.run()