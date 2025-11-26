from playwright.sync_api import Page

class AuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('input[type="text"]')
        self.password_input = page.locator('input[type="password"]')
        self.submit_button = page.locator('button[type="button"]')

    def navigate(self):
        self.page.goto('https://dev.topklik.online/', wait_until="commit", timeout=20000)
        # Ждем загрузки DOM
        self.page.wait_for_timeout(3000)
        return self

    def login(self, email: str, password: str):
        # Ждем появления элементов формы
        self.page.wait_for_timeout(2000)
        
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        
        # Ждем завершения авторизации
        self.page.wait_for_timeout(5000)