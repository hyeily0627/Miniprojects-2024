# Miniprojects-2024
IoT 개발자 미니프로젝트 리포지토리 

**참고**
<자리이동 컴퓨터 세팅> 
- 깃허브데스트탑 정리 
  1. 각 리포지토리 커밋 안된거 확인하기
  2. 파일 > 옵션 > 계정 > sign out of github.com > save 
  3. 각 리포지토리 선택후 - repository(또는 오른쪽마우스) - remove(체크박스 선택안함) 
  4. 제어판 - 사용자계정 - windows 자격증명에 깃허브가 있으면 삭제 
- (개발툴) 비쥬얼스튜디오 로그아웃 / 비쥬얼스튜디오코드 로그아웃 
- (작업물) Source 폴더 : shift delete로 완전 삭제 
- (개인정보) 웹브라우저 캐시 및 로그인 정보 삭제 

## day 01
- IoT 프로젝트 개요 
![IoT프로젝트](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/mp001.png)

1. IoT 기기 구성 - 아두이노, 라즈베리파이 등 IoT 장비들과 연결하여 사용
2. 서버 구성 - IoT 기기와 통신, DB구성, 데이터 수집 앱 개발
3. 모니터링 구성 - 실시간 모니터링/제어 앱

- 조별 미니프로젝트
    - 마감일 : 05월 28일 (40시간)
    - 구체적으로 어떤 디바이스 구성, 데이터 수집내용, 모니터링 계획
    - 8월말 정도에 끝나는 프로젝트 일정 계획 
    - 요구사항 리스트, 기능명세, UI/UX 디자인, DB설계를 문서 하나로 정리(A4 4-5장 정도?) 
        - 요구사항 리스트 : 
        - 기능명세 :
        - UI/UX 디자인 : 16일에 내용 전달
        - DB설계 : 
    - 5월 28일 오후 각 조별로 파워포인트, 프레젠테이션 할 수 있도록 준비(10분 내외)

** 스마트팩토리 키트 구매 
https://www.devicemart.co.kr/goods/view?no=15305433

**UI디자인
https://www.figma.com/
  **피그마 단축키**
    V - 선택도구
    A - 직선도구
    T - 텍스트도구
    Space + Drag - 마우스 커서에 따라 원하는 영역으로 이동
    Ctrl + R - 레이어 이름 변경
    Ctrl + G - 객체 그룹화
    Ctrl + Shift + G - 객체 그룹 해제
    Ctrl + D - 선택한 객체 복사
    Ctrl + [ - 선택한 객체 뒤로 보내기
    Ctrl + ] - 선택한 객체 앞으로 보내기
https://app.moqups.com/
https://ovenapp.io/
https://www.miricanvas.com/

**파워포인트 
https://www.miricanvas.com 미리캔버스
https://prezi.com/ko/ 프레지

** 컴퓨터 원격데스크탑 앱
애니데스크, https://anydesk.com/ko/
크롭 리모트데스트탑, https://remotedesktop.google.com/?hl=ko&pli=1
VNC, https://www.realvnc.com/en/connect/download/viewer/


## day 02
- 미니프로젝트
  - 프로젝트 문서 
  - UI/UX 디자인 툴 설명 
  - 노션 등 팀프로젝트 워크 프레임
  - 라즈베리파이(RPi) 리셋팅, 네트워크 설정, VNC(OS UI 작업)

- 스마트홈 연동 클래스 미니 프로젝트 
  1. 요구사항 정의, 기능 명세, 일정정리 
  2. UI/UX 디자인
  3. DB설계 
  4. 라즈베리파이(RPi) 세팅 (네트워크 세팅)
  5. 라즈베리파이 RPi GPIO에 IoT디바이스 연결(카메라, HDT센서(온습도센서), LED센서 등) 
  6. RPi 데이터 전송을 위한 파이썬 프로그래밍
  7. PC(Server) 데이터 수신 C# 프로그래밍 
  8. 모니터링 앱 개발(수신 및 송신)


## day 03
- 미니 프로젝트
  - 실무 프로젝트 문서  
  - Jira 사용법 https://www.atlassian.com/software/jira (노션 보다 쉬움)
  - 조별로 진행 

- 스마트홈 연동 클래스 미니 프로젝트 
  - RPi 셋팅 ~ 진행 
    - sudo apt-get update 하고 sudo apt-get upgrade 하기 (주기적으로)
    - sudo apt-get install fonts-nanum 

## 3일차
- 미니프로젝트
    - 실무 프로젝트 문서
    - Jira 사용법 
    - 조별로 진행

- 라즈베리파이 셋팅 
    1. RPi 기본 구성 - RPi + MicroSD + Power
    2. RPi 기본 셋팅
      - [x] 최신 업그레이드
      - [x] 한글화
      -  [x] 키보드 변경
      -  [x] 화면사이즈 변경(RealVNC사용)
      -  [x] Pi Apps 앱설치 도우미 앱
      -  [x] Github Desktop, VS Code
      -  [x] 네트워크 확인
        - RealVNC Server 자동실행 설정
          : sudo nano /etc/rc.local 들어가서 sudo iwconfig wlan0 power off 입력 후 저장 

- 스마트홈 연동 클래스 미니프로젝트
    - RPi 셋팅... 진행

# 4일차 
- 라즈베리파이 IoT 장비 설치
- [x] 라즈베리파이 카메라
    - 설치 : 검은색 커버(?) 살짝 열고 파란띠부분이 usb 포트쪽으로 

    ![카메라](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/camera.png)
    
    - 명령 : sudo libcamera-hello -t 0 / 콘솔에서 컨트롤 c 하면 카메라 종료

    ![카메라](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/camera.jpg)

  - [x] GPIO HAT

  - [x] 브레드보드와 연결

    ![GPIO구조](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/GPIO.png)

    - 설치 
    ![GPIO](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/GPIO.jpg)
    ![GPIO1](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/GPIO1.jpg)
    ![GPIO2](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/GPIO2.jpg)
 
  - [x] RGB LED 모듈(led_blink.py)
      - V - 5V 연결
      - R - GPIO4 연결
      - B - GPIO5 연결
      - G - GPIO6 연결

  ![LED](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/LED_RED.mp4)

  [-] 서보모터

## 5일차
- 라즈베리파이 IoT장비 설치
  - [x] DHT11 센서(dht11_test.py)
        - GND - GND 8개중 아무대나 연결
        - VCC - 5V 연결
        - S - GPIO18 연결

  ![temphumid](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/temp.jpg)

## 6일차 ## 7일차 
- 네트워크 공사! 개인공유기, pc, 라즈베리파이 
  - 라즈베리파이 VNC Viewer로 컨트롤(HDMI 제거)
    - 키보드 오류 : 오른쪽 상단 키보드키 -> 키보드-영어(미국식)클릭 후 아래의 키보드 아이콘 -> 한국어- 한국어(101-104키 호환)으로 설정 

- 스마트홈 연동 클래스 미니프로젝트
  - 온습도 센서, RGB LED 센서 
  - 라즈베리파이 VNC Viewer로 컨트롤(HDMI 제거) => Window 통신! 
    - 키보드 오류 : 오른쪽 상단 키보드키 -> 키보드-영어(미국식)클릭 후 아래의 키보드 아이콘 -> 한국어- 한국어(101-104키 호환)으로 설정
    - RPI -> 기본설정 -> 키보드와 마우스 -> 키보드 - > keyboardLayout 에서 모델을 101로 
    - 한/영 변환 ctlr + space 

- IoT 기기간 통신방법
  - Modbus : 시리얼 통신으로 데이터 전송(구식방법)
  - OPC UA : Modbus통신의 불편한 점을 개선(했지만 불편함)
  - MQTT : 가장 편리, AWS IoT, Azure IoT 클라우드 산업계 표준으로 사용 
    => 폴더에 05.온습도 경고앱.pdf 꼭 읽어보기 

    ![MQTT](https://raw.githubusercontent.com/hyeily0627/Miniprojects-2024/main/images/MQTT.png)

- MQTT 통신
  - [x] Mosquitto Broker 설치
        - mosquitto.conf : listener 1883 0.0.0.0, allow_anonymous true
        - 방화벽 인바운드 열기
  - [ ] RPi : paho-mqtt 패키지 설치, 송신(publisher)
    - Win : MQTT.NET Nuget패키지 설치, 수신(subcriber)

## 8일차 
- 스마트홈 연동 클래스 미니프로젝트 
  - [] WPF MQTT 데이터 DB로 저장 
  - [] MQTT 데이터 실시간 모니터링 
  - [] MQTT로 RPi 제어(LED제어)
  - [] WPF MQTT 데이터 히스토리 확인 
