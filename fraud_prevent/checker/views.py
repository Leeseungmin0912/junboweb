from django.shortcuts import render, redirect
from .models import FraudCase
import re

def index(request):
    search_result = None
    raw_query = ""
    message = None # 등록 완료 메시지용

    if request.method == "POST":
        # 1. 제보 등록 로직 (form에 'action_type'이 'report'일 때)
        if request.POST.get("action_type") == "report":
            fraud_info = request.POST.get("fraud_info")
            fraud_type = request.POST.get("fraud_type")
            description = request.POST.get("description")
            
            if fraud_info and fraud_type:
                # 데이터 저장 (기본적으로 승인 대기 상태: is_approved=False)
                FraudCase.objects.create(
                    fraud_info=fraud_info,
                    fraud_type=fraud_type,
                    description=description,
                    is_approved=False 
                )
                message = "제보가 접수되었습니다. 관리자 승인 후 리스트에 반영됩니다."

        # 2. 조회 로직 (form에 'action_type'이 'search'일 때)
        elif request.POST.get("action_type") == "search":
            raw_query = request.POST.get("search_query", "").strip()
            clean_query = re.sub(r'[^0-9]', '', raw_query)
            
            if clean_query:
                all_cases = FraudCase.objects.filter(is_approved=True)
                for case in all_cases:
                    db_value = case.fraud_info if case.fraud_info else ""
                    if re.sub(r'[^0-9]', '', db_value) == clean_query:
                        search_result = case
                        break
                if search_result is None:
                    search_result = "no_result"

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': raw_query,
        'message': message
    })
