# 🛡️ 사기 피해 방지 플랫폼 (Fraud Prevention Platform)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white">
</p>

## 📌 프로젝트 소개
본 프로젝트는 사이버 범죄(사기) 피해를 예방하기 위해 구축된 **공익 목적의 웹 서비스**입니다. 유명 사기 피해 정보 공유 사이트인 **'더치트'**를 모델로 하여 개발되었으며, 사용자가 의심되는 전화번호나 계좌번호를 실시간으로 조회하고 새로운 피해 사례를 제보할 수 있는 환경을 제공합니다. 

무분별한 허위 제보를 방지하기 위해 **관리자 승인 시스템**을 도입하여 데이터의 신뢰성과 무결성을 확보한 것이 특징입니다.

- **실시간 서비스 주소:** [https://junboweb.onrender.com](https://junboweb.onrender.com)

## 🛠️ 기술 스택 (Tech Stack)
- **Backend:** `Python`, `Django`
- **Frontend:** `HTML`, `CSS`
- **Database:** `PostgreSQL` (배포 환경), `SQLite` (로컬 환경)
- **Deployment:** `Render` (PaaS), `GitHub`

## ✨ 주요 기능 (Key Features)
1. **의심 번호 조회 (Search)**
   - 전화번호 또는 계좌번호 입력 시 DB 내 피해 사례와 대조.
   - '안전' 또는 '위험' 상태를 사용자에게 직관적인 UI로 제공.
2. **피해 사례 제보 (Report)**
   - 사기 유형, 연락처/계좌번호, 상세 피해 내용을 포함한 새로운 사례 제보 기능.
3. **관리자 검증 및 승인 (Admin Approval)**
   - 제보된 데이터는 관리자 페이지(`/admin`)에서 검토 후 승인(`is_approved`) 처리된 데이터만 일반 사용자 조회 결과에 노출.

## 🚨 트러블슈팅 및 문제 해결 (Troubleshooting)

### 1. 403 Forbidden (CSRF 권한 오류)
- **문제:** 배포 환경에서 폼 제출 시 보안 토큰 검증 실패로 데이터 전송 차단.
- **원인:** HTTPS 환경에서의 `CSRF_TRUSTED_ORIGINS` 설정 누락 및 브라우저 쿠키 충돌.
- **해결:** - `settings.py`에 Render 도메인을 신뢰할 수 있는 출처로 등록.
  - 보안 쿠키 관련 설정(`CSRF_COOKIE_SECURE` 등)을 추가하여 프록시 환경 대응 완료.

### 2. 500 Internal Server Error (데이터 규격 불일치)
- **문제:** 하이픈(`-`)이 포함된 번호 입력 시 조회 실패 및 서버 에러 발생.
- **원인:** DB 저장 형식과 사용자 입력 형식의 불일치.
- **해결:** 백엔드(`views.py`)에서 **정규표현식(`re.sub`)을 활용한 데이터 정제(Sanitization)** 로직 적용. 모든 입력을 숫자 전용 데이터로 표준화하여 시큐어 코딩 실천.

## 💡 배운 점 (Insights)
- **배포 프로세스 이해:** 단순 코딩을 넘어 클라우드(Render) 환경의 배포 흐름과 서버 보안 설정의 중요성을 체득했습니다.
- **문제 해결 역량:** 시스템 로그를 분석하여 500/403 에러의 근본 원인을 추적하고 논리적으로 해결하는 트러블슈팅 능력을 배양했습니다.
- **공익적 서비스 설계:** 실제 서비스 모델(더치트)을 분석하며 사용자 경험(UX)과 데이터 신뢰성 사이의 균형을 고민해 보았습니다.
