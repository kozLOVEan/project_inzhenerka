# project_inzhenerka
Итоговый проект на боевом продукте от компании-партнера: SaaS сервис

# Установка

1. Клонировать репозиторий
2. Установить зависимости:
bash
pip install -r requirements.txt
playwright install

Запуск тестов
bash
# Все тесты
pytest tests/

# С генерацией Allure отчета
pytest tests/ --alluredir=allure-results
allure serve allure-results

# С HTML отчетом
pytest tests/ --html=report.html
Структура
pages/ - Page Object модели

tests/ - тесты

.github/workflows/ - CI/CD конфигурация

text

## Запуск тестов

1. Установите зависимости:
```bash
pip install -r requirements.txt
playwright install
Запустите тесты:

bash
pytest tests/ --alluredir=allure-results
Просмотрите отчет Allure:

bash
allure serve allure-results