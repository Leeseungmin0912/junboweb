from django.shortcuts import render
from .models import FraudCase
import re

def index(request):
    search_result = None
    raw_query = ""
    message = None

    if request.method == "POST":
        action = request.POST.get("action_type")

        # 1. 조회하기 로직
        if action == "search":
            raw_query = request.POST.get("search_query", "").strip()
            clean_query = re.sub(r'[^0-9]', '', raw_query)
            
            if clean_query:
                # 승인된 데이터 전체에서 숫자만 비교
                all_cases = FraudCase.objects.filter(is_approved=True)
                for case in all_cases:
                    db_val = re.sub(r'[^0-9]', '', case.fraud_info if case.fraud_info else "")
                    if db_val == clean_query:
                        search_result = case
                        break
                
                if search_result is None:
                    search_result = "no_result"

        # 2. 제보하기 로직
        elif action == "report":
            f_info = request.POST.get("fraud_info")
            f_type = request.POST.get("fraud_type")
            desc = request.POST.get("description")
            
            if f_info and f_type:
                FraudCase.objects.create(
                    fraud_info=f_info,
                    fraud_type=f_type,
                    description=desc,
                    is_approved=False # 관리자 승인 대기
                )
                message = "제보가 성공적으로 접수되었습니다. 관리자 승인 후 반영됩니다."

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': raw_query,
        'message': message
    })
