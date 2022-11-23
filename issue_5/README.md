### Устанавливаем пакеты:  
pip install pytest-cov  
### Меняем рабочую директорию:  
cd C:\Users\Anton\PycharmProjects\Avito_Homeworks\test_issue_5  
### Запускаем тесты:  
pytest -v  
### Проверяем покрытие:  
pytest -v --cov
### Отчет по покрытию (html):  
pytest --cov . --cov-report html
