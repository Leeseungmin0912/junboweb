import re
from django.db import models

class FraudCase(models.Model):
    category = models.CharField(max_length=50, verbose_name="사기 유형")
    target_info = models.CharField(max_length=100, verbose_name="사기 의심 정보")
    description = models.TextField(verbose_name="피해 상세 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    # 데이터를 저장(save)하기 직전에 하이픈을 제거하는 로직 추가
    def save(self, *args, **kwargs):
        # 숫자만 남기고 저장
        self.target_info = re.sub(r'[^0-9]', '', self.target_info)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.category}] {self.target_info}"