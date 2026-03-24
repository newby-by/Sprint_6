# The bicycle for the Yandex.Samokat service

 <img src="./resource/python-logo-only.svg" width="30" height="30">  

 <img src="./resource/1280px-Selenium_Logo.png" width="30" height="30">  

 <img src="./resource/images.jfif" width="30" height="30"> 

## The stack
python==3.13

allure-pytest==2.15.3

pytest==9.0.2

selenium==3.141.0

urllib3==1.26.16

webdriver-manager

## Acknowledgements

The Praktikum team

[Artem Yaroshenko whom power is unlimited.](https://github.com/eroshenkoam)

My Tomcat that get me up early.
Your 4 a.m. song is so cool.

## How to choose a browser

You can start tests with different browsers. Now we included two browsers: `chrome` and `firefox`.
The command is

```bash
   pytest --br=gecko
```

The default browser is `chrome`

```bash
   pytest
```

## How to use allure report

1. Install `allure` to start tests by `pytest` with the command

   ```bash
    pytest tests.py --alluredir=allure_results 
   ```

2. Start the allure server for watching a report

   ```bash
    allure serve allure_results
   ```

## Test cases

1. Test FAQ `test_main_page.py`.
   There is a chapter of «Вопросы о важном» bottom of the main page.
   The chapter includes eight questions and is made with vertically collapsing accordions.
   We made tests to check opening elements and each has an expected text.

2. Test order scooter `test_order_form.py`.
   Use two button on page. Fill up the form.
   Check on the popup window the message is showed up with succeeded text.

3. Test the logo app `test_header.py`.
   Check if click on the logo, it's redirected to the main page «Самокат».

4. Test the logo Yandex `test_header.py`.
   Check: if click on the logo Yandex, it's redirected to the main page «Дзена».
