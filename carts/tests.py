from django.test import TestCase


class CartsViewTests(TestCase):
    def test_carts(self):
        r = self.client.get('/carts/')
        self.assertEqual(r.status_code, 200)


class CartsViewTests(TestCase):
    def test_drf_cartlines(self):
        # 登录后请求购物车列表
        self.client.login(email='weiwei.cao.cn@gmail.com', password='123456')
        r = self.client.get('/api/cartlines/')
        self.assertEqual(r.status_code, 200)
        # 返回的空数组
        self.assertEqual(r.json, [])