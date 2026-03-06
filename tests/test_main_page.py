import data


def test_main_page_is_available(driver):
    driver.get(data.BASE_URL)

    assert driver.title == 'undefined'
