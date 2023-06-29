import requests
import pprint
from lxml import etree
import re
import time
import csv

f = open('政策数据.csv', 'a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['索引号', '发布机构', '发布日期', '政策标题', '政策详情url'])
csv_writer.writeheader() # 写入表头

headers = {
    'Referer': 'https://www.gd.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}




def get_policy_data():
    url = 'https://www.gd.gov.cn/gkmlpt/api/all/5?'
    params = {
        'page': page,
        'sid': '2'
    }

    response = requests.get(url=url, headers=headers, params=params).json()
    #pprint.pprint(response)
    policy_data = response['articles']
    for policy in policy_data:
        dit = {
            '索引号': policy['identifier'],
            '发布机构': policy['publisher'],
            '发布日期': policy['created_at'],
            '政策标题': policy['title'],
            '政策详情url': policy['url']
        }

        str = (policy['url'])
        lst = str.split('\r')

# 定义一个函数获取正文内容和附件链接

        # 获取每一页的正文
        file_name = '正文内容和附件链接.txt'
        for url_1 in lst:
            response_1 = requests.get(url=url_1, headers=headers).text
            data_page = etree.HTML(response_1)  # 解析html数据，便于操作
            data_list = data_page.xpath('/html/body/div[2]/div[4]/div[3]/div[3]/div[2]//text()')
            data_string = ''.join(data_list)
            data_content = re.sub(r'\s+', '', data_string)
            #print(f'政策正文内容: {data_content}')

            # 爬取附件链接
            detail_url = data_page.xpath('/html/body/div[2]/div[4]/div[3]/div[3]/div[2]/p[20]/a/@href')
            #print(f'正文附件链接: {detail_url}')

            # 本地新建文件
            # with open(file=file_name, mode='a', encoding='utf8') as f:
            #     f.write(data_content)
            # with open(file=url_name, mode='a', encoding='utf8') as f:
            #     for item in detail_url:
            #         f.write(item + '\n')

            article = f'\n{data_content}\n{detail_url}'
            with open(file=file_name, mode='a', encoding='utf8') as f:
                f.write(article)

        dit = {
            '索引号': policy['identifier'],
            '发布机构': policy['publisher'],
            '发布日期': policy['created_at'],
            '政策标题': policy['title'],
            '政策详情url': policy['url'],
        }
        print(dit)
        csv_writer.writerow(dit)


for page in range(1, 2):
    # 每1小页有20条数据，每100条数据为1大页
    print(f'正在爬取第{page}-{page*5}页的内容')
    get_policy_data()  # 下载数据
    time.sleep(1)
