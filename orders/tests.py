from django.test import TestCase

from .models import Order

# 导入 factory boy
import factory


# 继承 DjangoModelFactory 定义
class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer_note = ''


class OrderModelTests(TestCase):
    def test_customer_note_field(self):
        # order = Order.objects.create()
        order = OrderFactory()

        # 检查 customer_node 的值是空字符串
        self.assertEqual(order.customer_note, '')

        # 设置 customer_node 的值，再次检查
        order.customer_note = 'shiyanlou'
        order.save()
        self.assertEqual(order.customer_note, 'shiyanlou')