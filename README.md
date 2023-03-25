Объект тестирования: https://b2c.passport.rt.ru

Требования по проекту(исправленные): https://docs.google.com/document/d/1JnEf-mD7B9mRvY6DlyozvA14CFmSIdAS/edit?usp=sharing&ouid=109513607894983774171&rtpof=true&sd=true

Тест-кейсы, покторым составлены тесты: https://docs.google.com/spreadsheets/d/16bxmH_b3VrxgFuauM_f4fxSZ1B0lW21hfE96kIa92Vc/edit?usp=sharing

Для начала работы с тестами необходимо:

Скачать репозиторий к себе на компьютер.

Скачать актуальный Selenium WebDriver с сайта: https://chromedriver.chromium.org/downloads (выбрать версию соответствующую версии вашего браузера).

Установить все необходимые пакеты: pytest, selenium.

В файле conftest.py указать путь расположения файла chromedriver.exe на вашем компьютере.

Для запуска тестов через терминал необходимо ввести команду:
pytest -v --driver Chrome --driver-path chromedriver.exe ui_tests.py
