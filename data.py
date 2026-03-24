import locale
from datetime import datetime

from faker import Faker


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
ORDER_FORM_URL = BASE_URL + 'order/'


class MainPageData:
    MAIN_PAGE_TITLE = 'undefined'
    FIRST_ORDER_BUTTON = 1
    SECOND_ORDER_BUTTON = 2
    MAIN_TITLE_H1 = 'Привезём его прямо к вашей двери,'

    class FAQAccordion:
        FAQ = {
            ('Сколько это стоит? И как '
             'оплатить?'): ('Сутки — 400 рублей. '
                            'Оплата курьеру — '
                            'наличными или картой.'),
            ('Хочу сразу несколько самокатов! Так '
             'можно?'): ('Пока что у нас так: один заказ — '
                         'один самокат. Если хотите '
                         'покататься с друзьями, можете просто'
                         ' сделать несколько заказов — '
                         'один за другим.'),
            ('Как рассчитывается время '
             'аренды?'): ('Допустим, вы оформляете заказ на 8 мая. '
                          'Мы привозим самокат 8 мая в течение дня. '
                          'Отсчёт времени аренды начинается с момента, '
                          'когда вы оплатите заказ курьеру. '
                          'Если мы привезли самокат 8 мая в 20:30, '
                          'суточная аренда закончится 9 мая в 20:30.'),
            ('Можно ли заказать самокат '
             'прямо на сегодня?'): ('Только начиная с завтрашнего дня. '
                                    'Но скоро станем расторопнее.'),
            ('Можно ли продлить заказ или вернуть самокат '
             'раньше?'): ('Пока что нет! Но если что-то '
                          'срочное — всегда можно позвонить '
                          'в поддержку по красивому номеру 1010.'),
            ('Вы привозите зарядку вместе с '
             'самокатом?'): ('Самокат приезжает к вам с полной зарядкой. '
                             'Этого хватает на восемь суток — даже если '
                             'будете кататься без передышек и во сне. '
                             'Зарядка не понадобится.'),
            ('Можно ли отменить '
             'заказ?'): ('Да, пока самокат не привезли. Штрафа не будет, '
                         'объяснительной записки тоже не попросим. '
                         'Все же свои.'),
            ('Я жизу за МКАДом, '
             'привезёте?'): ('Да, обязательно. Всем самокатов! И Москве, '
                             'и Московской области.'),
        }


class OrderScooterForm:

    FIELDS = {
        'Имя': 1,
        'Фамилия': 2,
        'Адрес': 3,
        'Станция метро': 4,
        'Телефон': 5,
    }

    RENTAL_PERIOD = {
        'сутки': 1,
        'двое суток': 2,
        'трое суток': 3,
        'четверо суток': 4,
        'пятеро суток': 5,
        'шестеро суток': 6,
        'семеро суток': 7,
    }

    SCOOTER_COLOR = {
        'чёрный жемчуг': 1,
        'чсерая безысходность': 2,
    }

    def __init__(self):
        self.template_data = {
            'Имя': None,
            'Фамилия': None,
            'Адрес': None,
            'Станция метро': None,
            'Телефон': None,
            'Дата доставки': None,
            'Срок аренды': None,
            'Цвет': None,
            'Комментарий': None,
        }


class OrderScooterData:

    def __init__(self, locale='ru_RU'):
        self.template_data = OrderScooterForm().template_data
        self.faker = Faker(locale)

    @property
    def first_name(self):
        return self.faker.first_name()

    @property
    def last_name(self):
        return self.faker.last_name()

    @property
    def address(self):
        return self.faker.address()[:49].replace('/', '')

    @property
    def metro(self):
        return 'Черкизовская'

    @property
    def phone_number(self):
        return self.faker.numerify("89#########")

    @property
    def date_of_pick_up(self):
        pattern = "%d.%m.%Y"

        start_date = datetime.now()
        end_date = datetime(2026, 12, 31)

        random_date = self.faker.date_between_dates(
            date_start=start_date,
            date_end=end_date
        )

        return random_date.strftime(pattern)

    @property
    def rental_period(self):
        periods = list(OrderScooterForm.RENTAL_PERIOD)
        return self.faker.random_element(elements=periods)

    @property
    def scooter_color(self):
        colors = list(OrderScooterForm.SCOOTER_COLOR)
        return self.faker.random_element(elements=colors)

    @property
    def comments_for_courier(self):
        return self.faker.sentence()

    @property
    def expected_data(self):
        self.template_data['Имя'] = self.first_name
        self.template_data['Фамилия'] = self.last_name
        self.template_data['Адрес'] = self.address
        self.template_data['Станция метро'] = self.metro
        self.template_data['Телефон'] = self.phone_number
        self.template_data['Дата доставки'] = self.date_of_pick_up
        self.template_data['Срок аренды'] = self.rental_period
        self.template_data['Цвет'] = self.scooter_color
        self.template_data['Комментарий'] = self.comments_for_courier
        return self.template_data

    def __str__(self):
        return str(self.template_data)


form_data = OrderScooterData()
