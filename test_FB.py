from seleniumbase import BaseCase


class FbTestClass(BaseCase):
    def test_fb(self):
        self.open("https://www.facebook.com")
        self.send_keys('//*[@id="email"]', "alkimcevik@gmail.com")
        self.send_keys('//*[@id="pass"]', "ifwtfacebook1984")
        self.click("_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy")
        self.sleep(10000)
