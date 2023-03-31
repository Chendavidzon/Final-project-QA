import requests


class TestApi:
    # 1 - Get.http request to the site for mango return status code of success
    def test_1(self):
        res = requests.get('https://fruityvice.com/api/fruit/mango')
        assert 400 > res.status_code >= 200
        print(f' Success!  status code is -> {res.status_code}')


    #2 - Check that kiwi have id of 66
    def test_2(self):
        res = requests.get('https://fruityvice.com/api/fruit/kiwi')
        kiwi = res.json()
        expected = 66
        actual = kiwi['id']
        assert actual == expected
        print(' kiwi id is-> 66 ')