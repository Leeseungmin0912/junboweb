from django.shortcuts import render
from .models import FraudCase
import re


def index(request):
    results = None
    if request.method == 'POST':
        query = request.POST.get('query')

        # 정규표현식을 사용하여 숫자만 남기고 모든 특수문자(하이픈 등) 제거
        clean_query = re.sub(r'[^0-9]', '', query)

        # DB에서도 하이픈이 제거된 상태로 저장되어 있다면 아래와 같이 검색
        results = FraudCase.objects.filter(target_info=clean_query)

    return render(request, 'checker/index.html', {'results': results})