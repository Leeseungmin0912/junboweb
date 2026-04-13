from django.shortcuts import render
from .models import FraudCase
import re  # <-- 이 줄이 반드시 맨 위에 있어야 합니다!

def index(request):
    search_result = None
    query = None

    if request.method == "POST":
        raw_query = request.POST.get("search_query", "").strip()
        # 숫자만 추출
        query = re.sub(r'[^0-9]', '', raw_query) 
        
        if query:
            # 승인된 데이터만 가져오기
            all_cases = FraudCase.objects.filter(is_approved=True)
            for case in all_cases:
                # DB 데이터에서도 숫자만 추출해서 비교
                db_info_cleaned = re.sub(r'[^0-9]', '', case.fraud_info)
                if db_info_cleaned == query:
                    search_result = case
                    break
            
            if not search_result:
                search_result = "no_result"

    return render(request, 'index.html', {
        'search_result': search_result,
        'query': raw_query
    })
