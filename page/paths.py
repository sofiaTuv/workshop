from selenium.webdriver.common.by import By


class Paths:
    BUTTON_ADD_CUST = (By.XPATH, '//button[@ng-class="btnClass1"]')
    POSTCODE = (By.XPATH, '//input[@ng-model="postCd"]')
    FIRST_NAME = (By.XPATH, '//input[@ng-model="fName"]')
    LAST_NAME = (By.XPATH, '//input[@ng-model="lName"]')
    ADD_BUTTON = (By.XPATH, '//button[@type="submit"]')
    CUSTOMERS = (By.XPATH, '//button[@ng-class="btnClass3"]')
