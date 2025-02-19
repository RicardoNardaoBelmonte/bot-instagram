import webbrowser
import pyautogui
import time

def logout():
    pyautogui.click(90,957, duration=2)
    pyautogui.click()
    pyautogui.move(0,-55, duration=1)
    pyautogui.click()

while True:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab("https://www.instagram.com")
    time.sleep(1)
    pyautogui.click(1159,357,duration=1)
    pyautogui.typewrite('')
    time.sleep(1)
    pyautogui.click(1143,412,duration=1)
    pyautogui.typewrite('')
    time.sleep(1)
    pyautogui.click(1183,464, duration=1)
    time.sleep(5)
    pyautogui.click(1119,656, duration=1)
    #clicando em search
    time.sleep(5)
    pyautogui.click(114,341, duration=1)
    time.sleep(1)
    #clicando em barra de pesquisa
    pyautogui.click(324,257, duration=1)
    pyautogui.typewrite('')
    pyautogui.move(0,50, duration=2)    
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(733,908, duration=1)
    time.sleep(3)
    time.sleep(1)
    if pyautogui.pixelMatchesColor(912,828,(255, 48, 64)):
        logout()
        time.sleep(86400)
    else:
        pyautogui.click(908,825, duration=1)
        time.sleep(5)
        pyautogui.click(1106,952, duration=1)
        time.sleep(1)
        pyautogui.typewrite('Amazing Publication')
        pyautogui.press('Enter')
        time.sleep(1)
        logout()
        time.sleep(86400)
