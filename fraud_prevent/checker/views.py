from django.shortcuts import render, redirect
from .models import FraudCase


def index(request):
    search_result = None

    if request.method == "POST":
        # 1. 사용자가 '조회'를 한 경우
        if "search_query" in request.POST:
            query = request.POST.get("search_query")
            # '승인된(is_approved=True)' 데이터 중에서만 검색함
            search_result = FraudCase.objects.filter(fraud_info=query, is_approved=True).first()

        # 2. 사용자가 사기 사례를 '등록' 요청한 경우
        elif "fraud_info" in request.POST:
            FraudCase.objects.create(
                fraud_type=request.POST.get("fraud_type"),
                fraud_info=request.POST.get("fraud_info"),
                description=request.POST.get("description"),
                is_approved=False  # 사용자가 등록하면 자동으로 '미승인' 상태
            )
            return render(request, 'checker/index.html', {'message': '등록 요청이 완료되었습니다. 관리자 검토 후 반영됩니다.'})

    return render(request, 'checker/index.html', {'search_result': search_result})