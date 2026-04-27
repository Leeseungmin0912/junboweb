from django.contrib import admin
from .models import FraudCase

@admin.register(FraudCase)
class FraudCaseAdmin(admin.ModelAdmin):
    # 목록에서 승인 여부를 바로 볼 수 있게 설정
    list_display = ('fraud_info', 'fraud_type', 'is_approved', 'created_at')
    # 승인 여부를 목록에서 즉시 수정 가능하게 설정
    list_editable = ('is_approved',)
    # 승인된 것과 안 된 것을 필터링해서 보기
    list_filter = ('is_approved', 'fraud_type')