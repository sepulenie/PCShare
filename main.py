import os 

screenshots_path = r"d:/YandexDisk/GameScreenshots/Twitter/"

screenshots = [screenshot for screenshot in os.listdir(screenshots_path) if os.path.isfile(os.path.join(screenshots_path, screenshot))]
for screenshot in files