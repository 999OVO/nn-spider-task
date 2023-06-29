import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pprint
import csv


keyword = input('请输入你想要查询的公司名称：')

f = open(f'{keyword}专利数据.csv', 'a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['申请日', '专利名称', '专利类型', '专利状态', '申请号', '公开（公布）号', '公开（公告）日', '发明人', '详情页url'])
csv_writer.writeheader() # 写入表头


def get_company_patents(company_name):
    # 使用cookie免登陆
    driver = webdriver.Chrome()
    driver.get('https://www.tianyancha.com/')
    driver.implicitly_wait(10)
    cookies = [{'domain': '.tianyancha.com', 'httpOnly': False, 'name': 'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963368'}, {'domain': '.tianyancha.com', 'expiry': 1722523367, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22distinct_id%22%3A%221655292%22%2C%22first_id%22%3A%221890274d52c638-01838bf989de25d-26031f51-1327104-1890274d52d521%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5MDI3NGQ1MmM2MzgtMDE4MzhiZjk4OWRlMjVkLTI2MDMxZjUxLTEzMjcxMDQtMTg5MDI3NGQ1MmQ1MjEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxNjU1MjkyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221655292%22%7D%2C%22%24device_id%22%3A%221890274d52c638-01838bf989de25d-26031f51-1327104-1890274d52d521%22%7D'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'tyc-user-info-save-time', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963367047'}, {'domain': '.tianyancha.com', 'expiry': 1722523357, 'httpOnly': False, 'name': 'TYCID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '07101fc015c211eeb6f299fda7edc6be'}, {'domain': '.tianyancha.com', 'expiry': 1688049758, 'httpOnly': False, 'name': 'bannerFlag', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'HWWAFSESID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '35474208c73ce003ed6'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'auth_token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTE3MjQ3MzA3MCIsImlhdCI6MTY4Nzk2MzM2NywiZXhwIjoxNjkwNTU1MzY3fQ.d2xA5f8XdgKcnt4ujomMJr1QVSI2bGQ7B-oWM7BzZkAG0feVSnyHqSKdpEPsiG7hblh2DOT9eam7NzXcjzAqXQ'}, {'domain': '.tianyancha.com', 'expiry': 1690555367, 'httpOnly': False, 'name': 'tyc-user-info', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '%7B%22state%22%3A%220%22%2C%22vipManager%22%3A%220%22%2C%22mobile%22%3A%2215172473070%22%7D'}, {'domain': '.tianyancha.com', 'expiry': 1719499367, 'httpOnly': False, 'name': 'Hm_lvt_e92c8d65d92d534b0fc290df538b4758', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963359'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'tjtkYxnkuwCsaOKyNk0V-QSc'}, {'domain': 'www.tianyancha.com', 'httpOnly': False, 'name': 'HWWAFSESTIME', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1687963357560'}, {'domain': '.tianyancha.com', 'expiry': 1687967999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}]

    driver.delete_all_cookies()
    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    driver.refresh()
    driver.get('https://www.tianyancha.com/')
    driver.maximize_window()
    time.sleep(5)

    # # 在搜索框中输入企业名称
    driver.find_element(By.XPATH, '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/div[1]/input').send_keys(keyword)
    # 点击搜索按钮（可直接点击预览框，已弃用）
    #driver.find_element(By.XPATH, '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/button/span').click()

    # 等待搜索结果加载
    time.sleep(5)
    # 点击预览框第一个结果
    driver.find_element(By.XPATH, '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/div[2]/ul/li[1]').click()

# 使用requests爬取数据
    url = 'https://capi.tianyancha.com/cloud-intellectual-property/patent/patentListV6'
    headers = {
        'Host': 'capi.tianyancha.com',
        'Origin': 'https://www.tianyancha.com',
        'Referer': 'https://www.tianyancha.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
# 定义一个函数爬取专利数据

    def get_patent_info():
        params = {
            '_': '1687967817985',
            'id': '24416401',
            ' pageSize': '10',
            'pageNum': '1',
            'type': '-100',
            'lprs': '-100',
            'applyYear': '-100',
            'pubYear': '-100',
            'fullSearchText': '',
            'sortField': '',
            'sortType': '-100'
        }
        response = requests.get(url=url, headers=headers, params=params).json()
        #pprint.pprint(response)
        patent_data = response['data']['items']
        for patent in patent_data:
            link_url = 'https://zhuanli.tianyancha.com/' + str(patent['uuid'])
            dit = {
                '申请日': patent['applicationTime'],
                '专利名称': patent['patentName'],
                '专利类型': patent['patentType'],
                '专利状态': patent['lprs'],
                '申请号': patent['patentNum'],
                '公开（公布）号': patent['pubnumber'],
                '公开（公告）日': patent['pubDate'],
                '发明人': patent['inventor'],
                '详情页url': link_url
            }
            print(dit)
            csv_writer.writerow(dit)

    for page in range(1, 11):
        print(f'正在爬取第{page}页的内容')
        time.sleep(1)
        get_patent_info()  # 下载数据

    # 关闭浏览器
    driver.quit()


# 使用示例
company_name = keyword
get_company_patents(company_name)
