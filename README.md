# Flask Portfolio Blog
> 경량 프레임워크인 Flask를 활용하여 구축한 개인 포트폴리오 블로그 웹 애플리케이션입니다.

## 📸 Visual Demonstration
![placeholder](./images/demo.gif)

## 💡 Motivation & Problem
이 프로젝트는 오픈소스 프로그래밍 수업의 핵심 과제 작업으로 시작하였습니다.

코드 악취(Code Smell)를 식별하고 리팩토링하는 경험 등 협업 시 가장 중요한 능력을 쌓고자 진행하게 되었습니다.

## 🛠 Tech Stack & Rationale
* **Python 3 & Flask**: 가볍고 직관적인 아키텍처로 웹 서버와 라우팅 구조를 가장 빠르게 구축하고 학습할 수 있어 선택했습니다.
* **Jinja2**: 화면(View)과 비즈니스 로직(Controller)의 물리적 분리를 구현하기 위해 템플릿 엔진으로 채택했습니다.
* **Flasgger (Swagger UI)**: 백엔드 API 명세를 직관적으로 확인하고 바로 동작을 테스트하기 위해 도입했습니다.
* **Pytest**: 코드 수정 및 리팩토링 시, 인증(Login/Logout) 및 주요 라우팅 기능이 의도대로 동작하는지 보장하기 위해 사용했습니다.

## ✨ Key Features
* **게시물 관리 (Post Management)**: 블로그 게시글 목록 및 상세 내용 조회
* **사용자 인증 (Authentication)**: 세션(Session) 기반의 관리자 로그인 및 로그아웃 시스템
* **권한 제어 (Authorization)**: 로그인된 사용자만 접근할 수 있는 새 글 작성 기능 보호
* **자동화된 API 명세 (API Documentation)**: Docstring 기반의 OpenAPI(Swagger) 문서 자동 생성

## 🚀 Getting Started Guide
터미널(또는 명령 프롬프트)을 열고 아래 명령어를 순서대로 복사 및 붙여넣기 하세요.

```bash
# 1. 저장소 클론 및 폴더 이동
git clone <your-repository-url>
cd flask-blog

# 2. 가상환경 생성 및 활성화
python3 -m venv venv
# macOS/Windows의 경우: venv\Scripts\activate
source venv/bin/activate

# 3. 의존성 라이브러리 설치
pip install -r requirements.txt

# 4. 플라스크 애플리케이션 실행
python app/app.py

# 이제 브라우저를 열고 다음 주소로 접속하여 구동을 확인합니다.
# 블로그 홈: http://127.0.0.1:5000
# API 문서 (Swagger UI): http://127.0.0.1:5000/apidocs/
```

## 🧠 Lessons Learned / Challenges
가장 시사점이 컸던 기술적 도전은 **비대해진 코드(Code Bloater)와 뷰 결합도 완화 과정**이었습니다.
초기에는 `post_controller` 내에 반환될 HTML 태그들이 문자열 형태로 심하게 하드코딩되어 있었습니다. 이는 코드를 읽기 어렵게 만들고 중복을 유발했습니다. 이를 해결하기 위해 HTML 구조를 분리하고 `Jinja2` 템플릿 엔진 구조로 렌더링하는 뷰(View) 템플릿 추출 리팩토링을 수행했습니다. 이 과정을 통해 뷰 계층과 컨트롤러 계층을 분리하는 MVC 패턴의 중요성을 깨닫고, 향후 유지보수를 위한 올바른 아키텍처 설계 방향을 배울 수 있었습니다.