# The bicycle for the Yandex.Samokat service

## The stack
python==3.13
allure-pytest==2.15.3
pytest==9.0.2
selenium==3.141.0
urllib3==1.26.16

## Acknowledgements

The Praktikum team

[Artem Yaroshenko whom power is unlimited.](https://github.com/eroshenkoam)

My Tomcat that get me up early.
Your 4 a.m. song is so cool.

## How to use allure report

1. Install `allure` to start tests by `pytest` with the command

   ```bash
    pytest tests.py --alluredir=allure_results 
   ```

2. Start the allure server for watching a report

   ```bash
    allure serve allure_results
   ```
