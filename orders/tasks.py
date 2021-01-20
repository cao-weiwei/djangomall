from django.core.mail import send_mail

from celery import shared_task


# 最大重试次数 3 次
@shared_task(bind=True, max_retries=3)
def send_order_mail(self, order):
    number_of_success_email = 0
    try:
        number_of_success_email = send_mail(
            '实验楼 - 订单',
            '编号：{id}；订单总价：{total}'.format(**order),
            'no-reply@example.com',
            ['shiyanlou@example.com'],
            fail_silently=False,
        )
    except Exception as e:
        # 重试等待时间 3 秒
        self.retry(exc=e, countdown=3)
    return number_of_success_email
