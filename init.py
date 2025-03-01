import requests
import json

def fetch_articles(begin=0, count=5):
    fakeid = "公众号ID"
    url = f"https://mp.weixin.qq.com/cgi-bin/appmsg?sub=list&search_field=null&begin={begin}&count={count}&query=&type=9&free_publish_type=1&sub_action=list_ex&token=55508355&lang=zh_CN&f=json&ajax=1&action=list_ex&fakeid="+fakeid

    headers = {
        'Cookie': '',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'mp.weixin.qq.com',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    
    # 提取文章总数
    total_count = data.get('app_msg_cnt', 0)
    
    # 提取所有文章的链接
    articles = []
    for article in data.get('app_msg_list', []):
        articles.append({
            'title': article.get('title'),
            'link': article.get('link')
        })
    
    return total_count, articles

def main():
    begin = 0
    count = 5
    total_count = None
    
    # 创建或打开文件用于保存链接
    with open('articles.txt', 'w', encoding='utf-8') as f:
        while True:
            total, articles = fetch_articles(begin, count)
            
            if total_count is None:
                total_count = total
                print(f'总文章数：{total_count}')
            
            if not articles:
                break
                
            for article in articles:
                f.write(f"{article['link']}\n")
            
            begin += count
            if begin >= total_count:
                break

if __name__ == "__main__":
    main()
