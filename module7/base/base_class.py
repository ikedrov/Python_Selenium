import datetime


class Base:

    def __init__(self, browser):
        self.browser = browser

    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Current url {get_url}')

    def assert_text(self, word, result):
        word_value = word.text
        assert word_value == result
        print('Word value ok')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = 'screenshot'+now_date+'.png'
        self.browser.save_screenshot('/Users/ivankedrov/Python_Selenium/module7/screen' + screenshot_name)

    def assert_url(self, result):
        assert_url = self.browser.current_url
        assert assert_url == result
        print('Url value ok')