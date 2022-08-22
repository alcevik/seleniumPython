from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.bumble.com/")
        self.click('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        self.switch_to_window()
        self.sleep(10000)


        count = 0;

        while count != 100:
            self.click('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
            self.wait(40)
            count += 1






            #self.driver.delete_all_cookies()
            #capabilities = self.driver.capabilities
            #self.driver.find_elements_by_partial_link_text("GitHub")