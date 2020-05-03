from selenium import webdriver


import time

class BotWhats:
    def __init__(self):
        self.mensage=["Bom dia"]
        self.group=["Grupo01","Grupo02"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def SendMensage(self):

        #< span  dir = "auto"   title = "Grupo01"  class ="_1wjpf _3NFp9 _3FXB1" > Família Bezerra < / span >

        #< div  tabindex = "-1"  class ="_1Plpp" > < div tabindex="-1" class ="_3F6QL _2WovP" >
        #<span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for  group in self.group:
            group=self.driver.find_element_by_xpath(f"//span[@title='{group}']")
            time.sleep(5)
            group.click()
            chat=self.driver.find_element_by_class_name('_1Plpp')
            chat.click()
            chat.send_keys(self.mensage)
            send_button=self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(5)
            send_button.click()
            time.sleep(5)

bot = BotWhats()
bot.SendMensage()
