import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建Chrome浏览器实例
driver = webdriver.Chrome()

# 打开天眼查网站
driver.get('https://www.tianyancha.com/')
driver.maximize_window()

# 等待页面加载
time.sleep(1)

# 点击右上角的登录/注册按钮
login_button = driver.find_element(By.XPATH, '//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div/div[5]/span')
login_button.click()

# 跳转到输入账号密码登录页面,已弃用，扫码登录更快捷
# time.sleep(1)
# login_change = driver.find_element(By.XPATH, '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[2]')
# login_change.click()


# 获取cookie
time.sleep(10)
coo = driver.get_cookies()
print(coo)
#driver.refresh()
# coo2 = driver.get_cookies()
# print(coo2)
driver.quit()

cookies = [{'domain': '.tianyancha.com', 'httpOnly': False, 'name': 'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963368'}, {'domain': '.tianyancha.com', 'expiry': 1722523367, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22distinct_id%22%3A%221655292%22%2C%22first_id%22%3A%221890274d52c638-01838bf989de25d-26031f51-1327104-1890274d52d521%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5MDI3NGQ1MmM2MzgtMDE4MzhiZjk4OWRlMjVkLTI2MDMxZjUxLTEzMjcxMDQtMTg5MDI3NGQ1MmQ1MjEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxNjU1MjkyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221655292%22%7D%2C%22%24device_id%22%3A%221890274d52c638-01838bf989de25d-26031f51-1327104-1890274d52d521%22%7D'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'tyc-user-info-save-time', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963367047'}, {'domain': '.tianyancha.com', 'expiry': 1722523357, 'httpOnly': False, 'name': 'TYCID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '07101fc015c211eeb6f299fda7edc6be'}, {'domain': '.tianyancha.com', 'expiry': 1688049758, 'httpOnly': False, 'name': 'bannerFlag', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'HWWAFSESID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '35474208c73ce003ed6'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'auth_token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTE3MjQ3MzA3MCIsImlhdCI6MTY4Nzk2MzM2NywiZXhwIjoxNjkwNTU1MzY3fQ.d2xA5f8XdgKcnt4ujomMJr1QVSI2bGQ7B-oWM7BzZkAG0feVSnyHqSKdpEPsiG7hblh2DOT9eam7NzXcjzAqXQ'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'tyc-user-info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22state%22%3A%220%22%2C%22vipManager%22%3A%220%22%2C%22mobile%22%3A%2215172473070%22%7D'}, {'domain': '.tianyancha.com', 'expiry': 1719499367, 'httpOnly': False, 'name': 'Hm_lvt_e92c8d65d92d534b0fc290df538b4758', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963359'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tjtkYxnkuwCsaOKyNk0V-QSc'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'HWWAFSESTIME', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963357560'}, {'domain': '.tianyancha.com', 'expiry': 1687967999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}]
