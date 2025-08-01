import pyautogui
import webbrowser as w
import pyperclip
import re
import time
import easyocr
hacking=["Dior", "알바몬", "대성마이맥", "GS25", "GS SHOP", "일상카페", "올리브영", "티파니엔코", "머스트잇", "adidas"]#서비스 명칭
def naver():#브라우저를 얼고 더보기 누르기 자동화 밑 드래그 이후 복사 이후 복사된 항목 t변수 저장 데이터 처리
    w.open_new('https://nid.naver.com/internalToken/view/tokenList/pc/ko#')
    pyautogui.PAUSE = 4
    pyautogui.moveTo(949, 885)
    pyautogui.PAUSE = 0.5
    pyautogui.scroll(-10000)
    pyautogui.click()
    pyautogui.scroll(-10000)
    pyautogui.click()
    pyautogui.scroll(10000)
    pyautogui.moveTo(480, 762)
    pyautogui.dragTo(1501, 1079, 4, button='left')
    pyautogui.hotkey('ctrl', 'c')
    t=pyperclip.paste()
    if "최근 이용일" in t:
            t=t.split("최근 이용일",1)[1]
    lines=t.strip().split('\n')
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
    if 1 <= len(hacking+service_names)-len(set(hacking+service_names)):
        sum_set_names=[]
        sum_nasmes=hacking+service_names
        for i in sum_nasmes:
            if sum_nasmes.count(i) ==2:
                sum_set_names.append(i)
        sum_set_names=list(set(sum_set_names))
        return_nasmes=[len(hacking+service_names)-len(set(hacking+service_names))]
        for i in sum_set_names:
            return_nasmes.append(i)
        if "adidas" in return_nasmes:
            adidas=return_nasmes.index("adidas")
            return_nasmes[adidas]="아디다스"
        if "Dior" in return_nasmes:
            Dior=return_nasmes.index("Dior")
            return_nasmes[Dior]="디올"
        return return_nasmes
    
    return len(hacking+service_names)-len(set(hacking+service_names))

def google():#로그인된 서비스 버튼 클릭 이후 그래그 이후 저장 값 변수저장 및 데이터 처리
    w.open_new('https://myaccount.google.com/connections?filters=3,4&hl=ko')
    time.sleep(3)
    pyautogui.moveTo(531,670)
    pyautogui.click()
    pyautogui.moveTo(279,702)
    pyautogui.dragTo(1917,1071, 4, button='left')
    pyautogui.hotkey('ctrl', 'c')
    text=pyperclip.paste()
    if "done" in text:
        text=text.split("done",1)[1]
    if "개인정보처리방침" in text:
        text=text.split("개인정보처리방침",1)[0]
    text=text.strip().splitlines()
    text2=[]
    for i in range(0,len(text),2):
        text2.append(text[i])
    if 1 <= len(hacking+text2)-len(set(hacking+text2)):
        sum_set_names=[]
        sum_nasmes=hacking+text2
        for i in sum_nasmes:
            if sum_nasmes.count(i) ==2:
                sum_set_names.append(i)
        sum_set_names=list(set(sum_set_names))
        return_nasmes=[len(hacking+text2)-len(set(hacking+text2))]
        for i in sum_set_names:
            return_nasmes.append(i)
        if "adidas" in return_nasmes:
            adidas=return_nasmes.index("adidas")
            return_nasmes[adidas]="아디다스"
        if "Dior" in return_nasmes:
            Dior=return_nasmes.index("Dior")
            return_nasmes[Dior]="디올"
        return return_nasmes
    return len(hacking+text2)-len(set(hacking+text2))

def dark(): #스크롤 이후 캡쳐로 저장 이후 이미지에서 텍스트 추출 이후 추출 데이터 처리
    w.open_new('https://myactivity.google.com/dark-web-report/dashboard?hl=ko&utm_source=google-account&utm_medium=web&utm_campaign=my_account_dark_web_report_member_card')
    time.sleep(5)
    pyautogui.moveTo(277,522)
    pyautogui.scroll(-300)
    time.sleep(1)
    pyautogui.screenshot('Dark.png', region=(277, 522, 1277, 350))
    reader = easyocr.Reader(['ko'])
    result = reader.readtext('Dark.png')
    hacking=[]
    for detection in result:
        hacking.append(detection[1])
    return hacking[-1][3]

def hibp(mail):#매개변수로 받은 값 자동 입력 및 값 복사
    w.open_new('https://haveibeenpwned.com')ㅇㅇ
    pyautogui.moveTo(632,729)
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite(mail, interval=0.1)
    pyautogui.moveTo(1227,739)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(919,373)
    pyautogui.dragTo(1005, 371, 2, button='left')
    pyautogui.hotkey('ctrl', 'c')
    hibp_sum=pyperclip.paste()
    return hibp_sum