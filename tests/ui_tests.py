
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_pass, invalid_email, invalid_pass, valid_phone, invalid_phone, valid_login, invalid_login, valid_ls, invalid_ls



def test_autorization():
    '''Проверка доступности страницы авторизации.'''
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Авторизация'

def test_auth_by_phone_valid_data():
    '''Проверка авторизации по валидному номеру телефона существующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(valid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "logout-btn")))

def test_auth_by_phone_invalid_data():
    '''Проверка авторизации по телефону с валидным данным несуществующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(
           invalid_phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(
           invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_phone_invalid_pass():
    '''Проверка авторизации по телефону с некорректным паролем существующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(
        valid_phone)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(
        invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_email_valid_data():
    '''Проверка авторизации по электронной почте существующего пользователя. '''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(valid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "logout-btn")))

def test_auth_by_email_invalid_data():
    '''Проверка авторизации по почте с валидным данным несуществующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_email_invalid_pass():
    '''Проверка авторизации по почте с некорректным паролем существующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_login_valid_data():
    '''Проверка авторизации по логину с корректными данными.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_login)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(valid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "logout-btn")))

def test_auth_by_login_invalid_data():
    '''Проверка авторизации по логину с валидным данным несуществующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(invalid_login)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_login_invalid_pass():
    '''Проверка авторизации по логину с некорректным паролем существующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_login)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_ls_valid_data():
    '''Проверка авторизации по лицевому счету c корректными данными.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="t-btn-tab-ls"]'))).click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_ls)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(valid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "logout-btn")))

def test_auth_by_ls_invalid_data():
    '''Проверка авторизации по лицевому счету c некорректными данными.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="t-btn-tab-ls"]'))).click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(invalid_ls)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_auth_by_ls_invalid_pass():
    '''Проверка авторизации по лицевому счету с некорректным паролем существующего пользователя.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//div[@id="t-btn-tab-ls"]'))).click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(valid_ls)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(invalid_pass)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))

def test_registration():
    '''Проверка перехода на страницу регистрации.'''
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

def test_registration_by_mail():
   '''Проверка регистрации нового пользователя с использованием электронной почты.'''
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()

   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Иван")
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Иванов")
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys("wiyene7000@asoflex.com")
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Qwerty123!")
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys("Qwerty123!")
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
   assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == 'Подтверждение email'