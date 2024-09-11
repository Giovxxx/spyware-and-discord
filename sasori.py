import pyautogui


# Cattura uno screenshot
screenshot = pyautogui.screenshot()

# Salva lo screenshot
screenshot_file = 'sgoks.png'
screenshot.save(screenshot_file)

print(f'Screenshot salvato come {screenshot_file}')
