from playwright.sync_api import Page

class ResultsPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Элементы результатов расчета
        self.material_text = page.locator('//td[contains(., "Материал")]/following-sibling::td')
        self.countertop_type_text = page.locator('//td[contains(., "Тип столешницы")]/following-sibling::td')
        self.options_text = page.locator('//td[contains(., "Опции")]/following-sibling::td')
        self.total_price_text = page.locator('//td[contains(., "Итоговая стоимость")]/following-sibling::td')
        
    def get_material(self) -> str:
        return self.material_text.text_content()
    
    def get_countertop_type(self) -> str:
        return self.countertop_type_text.text_content()
    
    def get_options(self) -> str:
        return self.options_text.text_content()
    
    def get_total_price(self) -> str:
        return self.total_price_text.text_content()