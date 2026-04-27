from django.shortcuts import render
from .models import FraudCase

def index(request):
    search_result = None
    query = None
    report_success = False  # 제보 성공 여부를 화면에 알려주기 위한 변수

    if request.method == "POST":
        # HTML에서 심어둔 action_type (search 인지 report 인지) 가져오기
        action_type = request.POST.get("action_type")

        # 1️⃣ [조회하기] 버튼을 눌렀을 때
        if action_type == "search":
            query = request.POST.get("query", "").strip() # HTML의 name="query"와 맞춤
            if query:
                # 입력한 번호와 일치하고, 관리자가 승인(is_approved=True)한 것만 검색
                search_result = FraudCase.objects.filter(fraud_info=query, is_approved=True).first()

                # 검색 결과가 없으면 특수 신호를 보냄
                if not search_result:
                    search_result = "no_result"

        # 2️⃣ [제보 등록하기] 버튼을 눌렀을 때
        elif action_type == "report":
            fraud_type = request.POST.get("fraud_type", "").strip()
            fraud_info = request.POST.get("fraud_info", "").strip()
            description = request.POST.get("description", "").strip()

            # 빈칸이 없으면 DB에 저장 (is_approved는 모델 기본값 False로 들어감)
            if fraud_type and fraud_info and description:
                FraudCase.objects.create(
                    fraud_type=fraud_type,
                    fraud_info=fraud_info,
                    description=description
                )
                report_success = True

    return render(request, 'checker/index.html', {
        'search_result': search_result,
        'query': query,
        'report_success': report_success,
    })