from main import *

class TestUi:
    #---------test1 positive login----------
    def test_1p(self):
        driver.get(our_url)
        driver.maximize_window()
        time.sleep(2)
        login(driver, 'standard_user', 'secret_sauce')
        time.sleep(2)
        driver.close()

    #---------test2 negative login----------
    def test_2n(self):
        driver.get(our_url)
        driver.maximize_window()
        time.sleep(2)
        login(driver, 'chen_da', 'secret_speed')
        time.sleep(2)
        driver.close()

    #---------test3 full payment-----------
    def test_fullpay(self):
        driver.get(our_url)
        driver.maximize_window()
        time.sleep(2)
        login(driver, 'standard_user', 'secret_sauce')
        time.sleep(2)
        add_chart(driver, '#item_4_title_link > div', '#add-to-cart-sauce-labs-backpack')
        time.sleep(2)
        my_cart(driver)
        time.sleep(2)
        checkout_info(driver, 'chen', 'davidzon', '12345')
        time.sleep(2)
        driver.close()

    #---------test4 sort price -----------
    def test_sort_price(self):
        driver.get(our_url)
        driver.maximize_window()
        time.sleep(2)
        login(driver, 'standard_user', 'secret_sauce')
        time.sleep(2)
        price_sort(driver)
        time.sleep(2)
        driver.close()

