

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