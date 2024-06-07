import time
from selenium import webdriver
from PIL import ImageGrab

# 브라우저 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 1000)

# 웹사이트 도메인 입력
driver.get('https://tickets.interpark.com/goods/24000549')

# 팝업 창 닫기
driver.find_element_by_xpath('//div[@class="popupCheck"]').click()

# 로그인
def login(username, password):
    driver.find_element_by_link_text('로그인').click()
    driver.find_element_by_id("userId").send_keys(username)
    driver.find_element_by_id("userPwd").send_keys(password + Keys.ENTER)

# 사용자 아이디 비밀번호 입력
login('tomotny', 'wlghks12!')

# 날짜 선택
def select_date(day):
    try:
        date_xpath = f"//li[normalize-space(text())='{day}']"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        driver.find_element(By.XPATH, date_xpath).click()
    except Exception as e:
        print("Error clicking the date:", e)

# 원하는 날짜 입력
select_date(00)

button_xpath = '//a[@class="sideBtn is-primary"]'
driver.find_element(By.XPATH, button_xpath).click()

# X 축과 Y 축으로 이미지 캡처
def capture_region(x, y):
    screenshot = ImageGrab.grab()
    return screenshot.crop((x, y, x + 215, y + 72))  # 215x72 크기로 잘라냄

# 캡처할 영역의 X, Y 좌표 지정
x_coordinate = 125
y_coordinate = 72

# 이미지 캡처 및 저장
captured_image = capture_region(x_coordinate, y_coordinate)
captured_image.save("captured_image.png")

# WebDriver 종료
driver.quit()
