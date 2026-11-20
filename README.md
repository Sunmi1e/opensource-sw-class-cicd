# opensource-sw-class-cicd
opensoruce class cicd

## 실행 방법

Python 3.14 환경에서 프로젝트 루트를 기준으로 실행합니다.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python -m pytest -q
python -m pytest --cov=orderlab --cov-report=xml
python generate_report.py
```

macOS/Linux에서는 `source .venv/bin/activate`를 사용합니다.
보고서는 `site/index.html`에 생성됩니다.

## CI/CD

Push/PR에서 lint 및 Ubuntu/Windows 테스트를 실행합니다. OS별 coverage.xml을 artifact로 저장하고, main 브랜치 Push에서 모든 검사가 성공한 경우에만 Pages에 배포합니다. GitHub 저장소 Settings → Pages → Build and deployment → Source를 GitHub Actions로 설정하세요.

PDF의 Level 1~5를 누적 구현했습니다. 원본 ZIP의 `test/`, `ci.yaml` 이름을 유지했습니다. PDF의 실습 요구사항에 따라 50,001원 경계, 100% 할인, CSV 오류 및 GET JSON 검증을 보완했습니다. 샘플 CSV는 PDF fixture의 데이터를 사용했습니다. `pyproject.toml`, `.gitignore`, `test/conftest.py`를 추가했습니다. 선택 사항인 Conda CI는 포함하지 않았습니다.

검증: Python 3.13.5에서 pytest 19개 통과, orderlab 구문 커버리지 100%, HTML 생성 확인. Ruff 및 Python 3.14/GitHub Actions 실제 실행은 확인하지 못했습니다. 워크플로의 Action 버전은 PDF를 따릅니다.
