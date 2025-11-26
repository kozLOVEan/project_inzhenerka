import pytest
import allure
from pages.auth_page import AuthPage
from pages.calculator_page import CalculatorPage
from pages.results_page import ResultsPage
from playwright.sync_api import Page, expect

class TestTopklik:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.auth_page = AuthPage(page)
        self.calculator_page = CalculatorPage(page)
        self.results_page = ResultsPage(page)
        
    @allure.feature('Авторизация')
    @allure.story('Успешная авторизация')
    def test_successful_auth(self):
        with allure.step("Выполнить авторизацию"):
            self.auth_page.navigate().login(
                "tester@inzhenerka.tech", 
                "LetsTest!"
            )
            
        with allure.step("Проверить успешную авторизацию"):
            assert self.calculator_page.calculate_button.is_visible()
            
    @allure.feature('Функциональность калькулятора')
    @allure.story('Переключатель "Скрыть столешницу"')
    def test_hide_countertop_toggle(self):
        with allure.step("Выполнить авторизацию"):
            self.auth_page.navigate().login(
            "tester@inzhenerka.tech",
            "LetsTest!"
        )
    
        with allure.step("Найти переключатель"):
            hide_toggle = self.page.get_by_test_id("hide-countertop")
    
        with allure.step("Кликнуть на переключатель"):
            hide_toggle.click()
    
        with allure.step("Проверить, что столешница скрыта'"):
            show_button = self.page.locator('[data-testid="show-main"]')
            expect(show_button).to_be_visible()
            
    @allure.feature('Функциональность калькулятора')
    @allure.story('Переключение на П-образную столешницу')
    def test_u_shaped_countertop(self):
        with allure.step("Выполнить авторизацию"):
            self.auth_page.navigate().login(
                "tester@inzhenerka.tech",
                "LetsTest!"
            )
        
        with allure.step("Выбрать П-образную столешницу"):
            self.calculator_page.select_u_shaped_countertop()
        
        with allure.step("Проверить, что отображается П-образная столешница"):
            is_u_shaped = self.calculator_page.is_u_shaped_countertop_visible()
            assert is_u_shaped, "П-образная столешница должна отображаться с характерными элементами"
            
            # Дополнительная проверка основных элементов
            expect(self.page.locator(".c-U-outerMiddle")).to_be_visible()
            expect(self.page.locator(".c-U-innerMiddle")).to_be_visible()
            
    @allure.feature('E2E сценарий')
    @allure.story('Полный расчет заказа')
    def test_complete_order_calculation(self):
        with allure.step("Выполнить авторизацию"):
            self.auth_page.navigate().login(
                "tester@inzhenerka.tech",
                "LetsTest!"
            )
        
        with allure.step("Собрать заказ"):
            with allure.step("Выбрать П-образную столешницу"):
                self.calculator_page.select_u_shaped_countertop()
            
            with allure.step("Отключить плинтус"):
                self.calculator_page.toggle_plinth(enable=False)
            
            with allure.step("Добавить остров"):
                self.calculator_page.add_island()
            
            with allure.step("Добавить проточку для стока воды"):
                self.calculator_page.add_water_drain_groove()
            
            with allure.step("Выбрать цвет N-103 Gray Onix"):
                self.calculator_page.select_color("N-103 Gray Onix")
            
            with allure.step("Нажать кнопку 'Рассчитать'"):
                self.calculator_page.calculate_order()
        
        with allure.step("Проверить страницу расчета"):
            expect(self.page).to_have_url("https://dev.topklik.online/")
            
            with allure.step("Проверить состав заказа"):
                order_list = self.page.get_by_test_id("order-list").first
                expect(order_list).to_be_visible()
                
                # Проверяем наличие всех элементов в заказе
                expect(order_list).to_contain_text("П-образная столешница")
                expect(order_list).to_contain_text("Остров")
                expect(order_list).to_contain_text("Проточки для стока воды")
                expect(order_list).to_contain_text("N-103 Gray Onix")
            
            with allure.step("Проверить цену"):
                price_button = self.page.get_by_test_id("price-button")
                expect(price_button).to_be_visible()
                expect(price_button).to_contain_text("384 100 ₽")