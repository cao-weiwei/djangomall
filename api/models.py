from django.db import models


class Integration(models.Model):
    # 应用或 API 名称
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=256, null=True, blank=True)
    secret = models.CharField(max_length=256, null=True, blank=True)
    token = models.CharField(max_length=128, null=True, blank=True)
    # 刷新时间
    refreshed_at = models.DateTimeField(null=True, blank=True)
    # 其他参数
    parameters = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

