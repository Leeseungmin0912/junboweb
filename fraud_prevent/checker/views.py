from django.shortcuts import render
from .models import FraudCase
import re

def index(request):
    search_result = None
    raw_query = ""

    if request.method == "POST":
        # 사용자가 입력한 값 가져오기
        raw_query = request.POST.get("search_query", "").strip()
        
        # 입력값에서 숫자만 추출 (예: 010-1234 -> 0101234)
        clean_query = re.sub(r'[^0-9]', '', raw_query)
        
        if clean_query:
            # 승인된 모든 데이터를 가져와서 비교
            all_cases = FraudCase.objects.filter(is_approved=True)
            
            for case in all_cases:
                # DB의 fraud_info가 None일 경우를 대비해 빈 문자열 처리
                db_info = case.fraud_info if case.fraud_info else ""
                clean_db_info = re.sub(r'[^0-9]', '', db_info)
                
                if clean_db_info == clean_query:
                    search_result = case
                    break
            
            # 검색 결과가 없으면 'no_result' 문자열 전달
            if search_result is None:
                search_result = "no_result"

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': raw_query
    })
