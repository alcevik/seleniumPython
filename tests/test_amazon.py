from seleniumbase import BaseCase


class HomeTest(BaseCase):

    def test_home_page(self):
        # open the amazon main page
        self.goto("https://www.amazon.com/")

        # click on "Sign in"
        self.click('//*[@id="nav-link-accountList"]/span')
        print(self.get_title())
        # assert title
        self.assert_title("Amazon Sign-In")
