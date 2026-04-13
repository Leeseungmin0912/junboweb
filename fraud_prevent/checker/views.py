from django.shortcuts import render
from .models import FraudCase

def index(request):
    search_result = None
    query = None

    if request.method == "POST":
        query = request.POST.get("search_query", "").strip() # 공백 제거
        if query:
            # 입력한 번호와 일치하고, 관리자가 승인(is_approved=True)한 것만 검색
            search_result = FraudCase.objects.filter(fraud_info=query, is_approved=True).first()
            
            # 검색 결과가 없으면 특수 신호를 보냄
            if not search_result:
                search_result = "no_result"

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': query
    })
