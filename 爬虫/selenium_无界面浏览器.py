from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def share_browser():
    # 确保此路径正确指向 msedgedriver.exe
    driver_path = r'E:\Promgram Files\JetBrains\PyCharm 2024.1\bin\msedgedriver.exe'

    # 设置 Edge 以无头模式运行
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    # 创建 Service 对象，并确保 executable_path 指向 msedgedriver.exe
    service = Service(executable_path=driver_path)

    # 初始化 WebDriver
    driver = webdriver.Edge(service=service, options=options)

    return driver

driver = share_browser()
# 自动化任务
driver.get("http://baidu.com")
driver.save_screenshot('baidu.png')
print(driver.title)

# 关闭浏览器
driver.quit()
