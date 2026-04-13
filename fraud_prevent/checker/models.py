from django.db import models


class FraudCase(models.Model):
    # 기존 필드들
    fraud_type = models.CharField(max_length=50, default='기타')
    fraud_info = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    # 승인 여부 필드 추가 (기본값은 False로 설정하여 검토 대기 상태로 만듦)
    is_approved = models.BooleanField(default=False, verbose_name="승인 여부")

    def __str__(self):
        return f"[{'승인' if self.is_approved else '대기'}] {self.fraud_info}"