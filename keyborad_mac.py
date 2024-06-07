import keyboard
import time
import selenium

def check_exit():
    if keyboard.is_pressed('esc'):  # ESC 키가 눌렸는지 확인
        print("Exiting...")
        exit(0)  # 프로그램 종료

try:
    while True:
        time.sleep(3)  # 25초 대기
        check_exit()  # 종료 조건 확인
        keyboard.press_and_release('a')  # F5 키 누름
        print("F5 pressed")
        check_exit()  # 종료 조건 확인
except KeyboardInterrupt:
    print("Program terminated")
