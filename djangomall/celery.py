import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangomall.settings')

# 创建 Celery 示例，传递项目名作为参数
app = Celery('djangomall')
app.config_from_object('django.conf:settings', namespace='CELERY')
# 自动查找应用下的 tasks.py 文件
app.autodiscover_tasks()