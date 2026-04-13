from django.contrib import admin
from .models import FraudCase

# 관리자 페이지에서 FraudCase 모델을 관리할 수 있도록 등록
admin.site.register(FraudCase)