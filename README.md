# Render 배포 연습 앱

Streamlit으로 만든 간단한 웹 앱입니다. 이름을 입력하면 인사말을 보여주며, `APP_GREETING` 환경변수 값에 따라 인사 문구가 바뀝니다. GitHub 저장소와 Render 환경변수를 연결해 배포를 연습할 수 있습니다.

## 1. 로컬에서 실행하기

Python 3.10 이상을 권장합니다.

```bash
# 가상환경 생성 예시 (Windows)
python -m venv .venv
.venv\Scripts\activate

# 패키지 설치
python -m pip install -r requirements.txt
```

### 로컬 환경변수 설정

환경변수 `APP_GREETING`은 앱이 사용자에게 보여줄 인사말입니다. 환경변수를 설정하지 않으면 기본 문구 `안녕하세요`가 사용됩니다.

Windows PowerShell:

```powershell
$env:APP_GREETING="반갑습니다"
streamlit run app.py
```

Windows 명령 프롬프트(cmd):

```bat
set APP_GREETING=반갑습니다
streamlit run app.py
```

브라우저에서 Streamlit이 안내하는 주소(보통 `http://localhost:8501`)를 엽니다. 앱의 **환경변수 설정 확인** 부분에서 환경변수를 읽었는지 확인할 수 있습니다.

## 2. GitHub에 올리기

이 폴더에서 아래 명령을 실행합니다. `<GitHub 저장소 주소>`는 GitHub에서 만든 저장소의 URL로 바꿔 주세요.

```bash
git init
git add app.py requirements.txt .gitignore README.md
git commit -m "Add Render deployment practice app"
git branch -M main
git remote add origin <GitHub 저장소 주소>
git push -u origin main
```

## 3. Render에 배포하기

1. Render에 로그인한 뒤 **New → Web Service**를 선택합니다.
2. GitHub 계정을 연결하고 위 저장소를 선택합니다.
3. 다음 설정을 입력합니다.

| 설정 | 입력값 |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT` |

4. **Environment Variables** 항목에서 환경변수 `APP_GREETING`을 추가합니다.

| Key | Value 예시 |
|---|---|
| `APP_GREETING` | `반갑습니다` |

5. **Create Web Service**를 눌러 배포합니다.
6. 배포가 완료되면 Render가 제공하는 `onrender.com` 주소를 열어 앱을 확인합니다. 화면의 **환경변수 설정 확인**에서 `APP_GREETING` 값이 표시되는지 확인합니다.

Render는 웹 서비스가 `0.0.0.0`에 바인딩하고 Render가 지정한 `PORT` 환경변수의 포트를 사용하도록 요구합니다. 위 Start Command에 이 설정이 포함되어 있습니다.

### 환경변수 값을 나중에 변경하기

1. Render 대시보드에서 해당 Web Service를 엽니다.
2. **Environment** 또는 **Environment Variables**에서 `APP_GREETING`의 값을 수정합니다.
3. 저장 후 서비스가 새 설정으로 재시작 또는 재배포되었는지 확인합니다.
4. 앱 화면에서 변경된 인사말을 확인합니다.

## 4. 파일 설명

- `app.py`: Streamlit 화면, 인사말 기능, `APP_GREETING` 환경변수 읽기
- `requirements.txt`: 앱 실행에 필요한 Python 패키지
- `.gitignore`: Git에 포함하지 않을 가상환경, 캐시, 비밀정보 파일
- `README.md`: 로컬 환경변수 설정과 GitHub·Render 배포 안내

## 참고

Render 무료 웹 서비스는 일정 시간 요청이 없으면 일시 중지될 수 있습니다. 다시 접속할 때 앱이 깨어나는 동안 첫 화면이 늦게 열릴 수 있습니다. 비밀번호나 API 키 등 민감한 값은 코드나 GitHub에 넣지 말고 Render 환경변수에 등록하세요. 이 예제의 `APP_GREETING`은 화면에 표시되는 공개 문구이므로 비밀정보가 아닙니다.
