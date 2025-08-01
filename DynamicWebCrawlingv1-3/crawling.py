# google_crawling.py,nevercrawling.py 합치고 출력을 json으로
import pygetwindow as gw
import pyautogui
import pyperclip
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def activate_chrome():
    chrome_windows=[w for w in gw.getWindowsWithTitle("Chrome") if w.visible]
    if chrome_windows:
        chrome_windows[0].activate()
        chrome_windows[0].maximize()
        time.sleep(1)

def copy_page():
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.5)
    return pyperclip.paste()

def process_naver(text):
    if "최근 이용일" in text:
        text=text.split("최근 이용일",1)[1]
    if "이용약관" in text:
        text=text.split("이용약관",1)[0]

    lines=text.strip().split('\n')
    service_names=[]
    i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line.startswith("http") or re.match(r'^\d{4}\.\s\d{2}\.\s\d{2}\.$',line):
            i+=1
            continue
        service_names.append(line)
        if i+1<len(lines) and lines[i+1].strip()==line:
            i+=2
        else:
            i+=1
        while i<len(lines) and (lines[i].strip().startswith("http") or
                                re.match(r'^\d{4}\.\s\d{2}\.\s\d{2}\.$',lines[i].strip()) or
                                lines[i].strip()==""):
            i+=1
    return service_names

def process_google(text):
    if "done" in text:
        text=text.split("done",1)[1]
    if "개인정보처리방침" in text:
        text=text.split("개인정보처리방침",1)[0]
    text=text.replace('\n\n','\n')
    return text.strip().splitlines()

def run(url,mode):
    options=Options()
    options.debugger_address="localhost:9222"
    driver=webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    activate_chrome()
    text=copy_page()
    driver.quit()

    if mode=="naver":
        return process_naver(text)
    elif mode=="google":
        return process_google(text)
    else:
        return []

# 실행 및 결과 저장
naver_services=run("https://nid.naver.com/internalToken/view/tokenList/pc/ko#", "naver")
google_services=run("https://myaccount.google.com/permissions", "google")

# all_services=["[Naver 서비스 목록]"]+naver_services+["","\n[Google 서비스 목록]"]+google_services
# JSON 형태로 변환: {"google": {"서비스명": true, ...}, "naver": {...}}
result_json={
    "google":{name:True for name in google_services},
    "naver":{name:True for name in naver_services}
}

# 출력
print(json.dumps(result_json,ensure_ascii=False,indent=2))
# # 파일 저장
# with open("all_services.txt","w",encoding="utf-8") as f:
#     for s in all_services:
#         f.write(s+"\n")


# print("모든 서비스명이 all_services.txt 파일에 저장되었습니다.")
