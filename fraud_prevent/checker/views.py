from django.shortcuts import render
from .models import FraudCase
import re # 숫자만 추출하기 위해 추가

def index(request):
    search_result = None
    query = None

    if request.method == "POST":
        raw_query = request.POST.get("search_query", "").strip()
        # 1. 사용자가 입력한 값에서 숫자만 추출 (하이픈, 공백 제거)
        query = re.sub(r'[^0-9]', '', raw_query) 
        
        if query:
            # 2. DB에 있는 모든 데이터를 가져와서 숫자만 남긴 뒤 비교
            # (데이터가 아주 많지 않을 때 가장 확실한 방법입니다)
            all_cases = FraudCase.objects.filter(is_approved=True)
            for case in all_cases:
                # DB 저장값에서도 숫자만 추출
                db_info_cleaned = re.sub(r'[^0-9]', '', case.fraud_info)
                if db_info_cleaned == query:
                    search_result = case
                    break
            
            if not search_result:
                search_result = "no_result"

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': raw_query # 화면에는 사용자가 입력한 그대로 보여줌
    })
