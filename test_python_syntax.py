from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = current_time.hour >= 22 or current_time.hour < 6
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = current_time.hour >= 22 or current_time.hour < 6

    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Найдите пользователя с именем "Olga"
    suitable_users = [user for user in users if user["name"] == "Olga"]
    assert suitable_users == [{"name": "Olga", "age": 45}]

    # Найдите всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_readable_function(func_name, **kwargs):
    # Преобразовать имя функции в читаемый формат
    readable_func_name = func_name.replace('_', ' ').title()

    # Сформировать строку с аргументами функции
    args_str = ', '.join([f"{key}={value}" for key, value in kwargs.items()])

    # Вывести читаемое имя функции и значения аргументов
    print(f'"{readable_func_name} [{args_str}]"')


# Функции, которые будут вызывать print_readable_function
def open_browser(browser_name):
    actual_result = None
    assert actual_result == f"Open Browser [Chrome]"
    print_readable_function(open_browser.__name__, browser_name=browser_name)


def go_to_companyname_homepage(page_url):
    actual_result = None
    assert actual_result == f"Go To Companyname Homepage [https://companyname.com]"
    print_readable_function(go_to_companyname_homepage.__name__, page_url=page_url)


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    assert actual_result == f"Find Registration Button On Login Page [https://companyname.com/login, Register]"
    print_readable_function(find_registration_button_on_login_page.__name__, page_url=page_url, button_text=button_text)


# Вызываем функцию test_readable_function
test_readable_function()

