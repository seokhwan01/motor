import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
IN1 = 17  # L298N IN1 -> GPIO17
IN2 = 18  # L298N IN2 -> GPIO18

# GPIO 초기화
GPIO.setmode(GPIO.BCM)  # GPIO 번호 모드 설정
GPIO.setup(IN1, GPIO.OUT)  # IN1을 출력으로 설정
GPIO.setup(IN2, GPIO.OUT)  # IN2를 출력으로 설정

# 모터 제어 함수
def motor_forward():
    """모터 전진"""
    GPIO.output(IN1, GPIO.HIGH)  # IN1에 전압 출력
    GPIO.output(IN2, GPIO.LOW)  # IN2에 전압 출력 중지
    print("모터 전진 중...")

def motor_backward():
    """모터 후진"""
    GPIO.output(IN1, GPIO.LOW)  # IN1에 전압 출력 중지
    GPIO.output(IN2, GPIO.HIGH)  # IN2에 전압 출력
    print("모터 후진 중...")

def motor_stop():
    """모터 정지"""
    GPIO.output(IN1, GPIO.LOW)  # IN1에 전압 출력 중지
    GPIO.output(IN2, GPIO.LOW)  # IN2에 전압 출력 중지
    print("모터 정지")

try:
    # 모터 작동 예제
    
    motor_forward()  # 모터를 전진 시킴
    time.sleep(1.0) 
    motor_stop()
    time.sleep(0.5)


    motor_backward()

    time.sleep(1.2)    # 2초 동안 전진
     # 모터를 후진 시킴
        # 2초 동안 후진
    motor_stop()     # 모터를 정지
finally:
    GPIO.cleanup()  # GPIO 핀 초기화

