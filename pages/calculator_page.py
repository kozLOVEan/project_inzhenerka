from playwright.sync_api import Page, expect

class CalculatorPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Основные элементы
        self.hide_countertop_toggle = page.locator('img.style_toggleMobileImg__frfAM')
        self.countertop_size_control = page.locator('[data-testid="size-control"]')
        self.countertop_type_dropdown = page.get_by_test_id('countertop-type-u')
        self.thickness = page.locator('styles_option__wjG5E')
        self.plinth_toggle = page.get_by_test_id('top-button')
        self.add_island_button = page.locator('style_productItem__jkBaY style_active__aWECM')
        self.sink_grooves_toggle = page.locator('style_optionsItem__mB2jK')
        self.color_dropdown = page.locator('style_circle__2HuHY')
        self.calculate_button = page.get_by_test_id('calc-button')
        self.tabletop_display = page.get_by_test_id('size-control')
        self.countertop_type = page.locator("[data-testid*='countertop-type-u']")
        self.thickness_dropdown = page.locator("[data-testid*='thickness']").first
        self.width_input = page.locator("[data-testid*='width']").first
        self.height_input = page.locator("[data-testid*='height']").first
        self.material_dropdown = page.locator("[data-testid*='material']").first
        self.add_to_cart_btn = page.locator("[data-testid*='add-to-cart']")
        self.thickness_dropdown = page.locator('button.styles_selectBlock__A3JGJ')
        self.countertop_type = page.locator("[data-testid*='countertop-type']")

    def select_u_shaped_countertop(self):
        "Выбрать П-образную столешницу"
        # Пробуем разные селекторы для нахождения кнопки
        selectors = [
            '[data-testid="countertop-type-u"]',
            '[data-testid*="u-shaped"]',
            'button:has-text("П-образная")',
            'div:has-text("П-образная")',
            '[class*="u-shaped"]'
        ]
        
        for selector in selectors:
            elements = self.page.locator(selector)
            if elements.count() > 0:
                print(f"Найдена кнопка по селектору: {selector}")
                elements.first.click()
                break
        else:
            raise Exception("Не найдена кнопка выбора П-образной столешницы")
        
        # Ждем появления элементов П-образной столешницы
        self.page.wait_for_selector(".c-U-outerMiddle", state="visible", timeout=10000)

    def is_u_shaped_countertop_visible(self):
        "Проверить, что отображается П-образная столешница"
        u_shaped_indicators = [
            ".c-U-outerMiddle",
            ".c-U-outerLeft", 
            ".c-U-outerLeftBottom",
            ".c-U-innerLeft",
            ".c-U-innerMiddle",
            ".c-U-innerRight",
            ".c-U-outerRightBottom",
            ".c-U-outerRight"
        ]
        
        visible_elements = []
        for selector in u_shaped_indicators:
            element = self.page.locator(selector)
            if element.count() > 0 and element.first.is_visible():
                visible_elements.append(selector)
        
        print(f"Видимые элементы П-образной столешницы: {len(visible_elements)}")
        for element in visible_elements:
            print(f"  - {element}")
        
        return len(visible_elements) >= 3
    
    def select_thickness(self, thickness: str):
        "Выбрать толщину столешницы"
        expect(self.thickness_dropdown).to_be_visible()
        self.thickness_dropdown.click()
        
        # Ждем появления опций
        self.page.wait_for_selector('button.styles_options__1Rp-f', state='visible', timeout=5000)
        
        # Выбираем нужную толщину по тексту в span
        thickness_option = self.page.locator(f'span.styles_optionNumber__hhWkC:has-text("{thickness}")')
        expect(thickness_option).to_be_visible()
        thickness_option.click()
        
    def toggle_plinth(self, enable=True):
        "Отключить плинтус"
        # Ищем кнопку которая имеет data-testid="top-button" И содержит текст "Плинтус"
        plinth_button = self.page.locator('[data-testid="top-button"]:has-text("Плинтус")')
        expect(plinth_button).to_be_visible()
        plinth_button.click()
            
    def add_island(self):
        "Добавить остров"
        # Выбираем первый элемент product-item"
        island_item = self.page.locator('[data-testid="product-item"]:has-text("Остров")')
        expect(island_item).to_be_visible()
        island_item.click()
        
    def add_water_drain_groove(self):
        "Добавить проточку для стока воды"
        water_groove_item = self.page.locator('div.style_optionsItem__mB2jK:has-text("Проточки для стока воды")')
        expect(water_groove_item).to_be_visible()
        
        # Кликаем на иконку плюса
        plus_icon = water_groove_item.locator('img[src*="plus-blue"]')
        plus_icon.click()
        self.page.wait_for_timeout(500)
            
    def select_color(self, color_name: str):
        "Выбрать цвет по названию"
        color_element = self.page.locator(f'div.stoneName:has-text("{color_name}")')
        expect(color_element).to_be_visible()
        color_element.click()
        self.page.wait_for_timeout(500)
        
    def calculate_order(self):
        "Нажать кнопку 'Рассчитать'"
        expect(self.calculate_button).to_be_visible()
        self.calculate_button.click()
        self.page.wait_for_url("https://dev.topklik.online/", timeout=15000)
        self.page.wait_for_timeout(3000)

        
    def toggle_hide_countertop(self):
        "Переключить скрытие столешницы"
        self.hide_countertop_toggle.click()