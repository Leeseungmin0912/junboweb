import re
from django.shortcuts import render
from .models import FraudCase


# checker/views.py 예시

def index(request):
    search_result = None
    report_success = False

    if request.method == 'POST':
        action_type = request.POST.get('action_type')

        # [조회하기 로직]
        if action_type == 'search':
            query = request.POST.get('query', '')
            # 하이픈, 공백 등 숫자 이외의 모든 문자 제거
            clean_query = re.sub(r'[^0-9]', '', query)

            # 데이터베이스에서 숫자만 추출된 값으로 검색
            # (DB에도 숫자만 저장되어 있어야 정확합니다)
            search_result = FraudCase.objects.filter(fraud_info=clean_query).exists()
            if not search_result:
                search_result = "no_result"

        # [제보하기 로직]
        elif action_type == 'report':
            fraud_info = request.POST.get('fraud_info', '')
            # 저장할 때도 숫자만 남겨서 저장
            clean_info = re.sub(r'[^0-9]', '', fraud_info)

            FraudCase.objects.create(
                fraud_type=request.POST.get('fraud_type'),
                fraud_info=clean_info,  # 숫자만 저장!
                description=request.POST.get('description')
            )
            report_success = True

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'report_success': report_success
    })