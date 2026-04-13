from django.shortcuts import render
from .models import FraudCase


def index(request):
    search_result = None
    query = None

    if request.method == "POST":
        # 'search_query'라는 이름으로 넘어온 값이 있는지 확인
        query = request.POST.get("search_query")
        if query:
            # 승인된(is_approved=True) 데이터 중에서 검색
            search_result = FraudCase.objects.filter(fraud_info=query, is_approved=True).first()

            # 만약 검색 결과가 없으면 '결과 없음'을 알리기 위해 빈 객체라도 전달하거나 로직 처리
            if not search_result:
                search_result = "no_result"

    # POST든 GET이든 상관없이 항상 index.html을 리턴해야 합니다.
    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': query
    })
