import datetime
import requests
import time

def get_today_bing_wallpaper():
    today = datetime.datetime.today()
    if int(today.month) < 10:
        month = f"0{today.month}"
    else:
        month = today.month
    url = f"https://api.mcloc.cn/bing/img/{today.year}/{month}/{today.day}/{today.year}-{month}-{today.day}_uhd.jpg"
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    respone = requests.get(url=url,headers=headers).content
    with open(f"{today.year}-{month}-{today.day}_uhd.jpg", 'wb') as f:
        f.write(respone)
        print(f"{today.year}-{month}-{today.day}_uhd.jpg保存成功！")
    
    
if __name__=="__main__":
    get_today_bing_wallpaper()
    # 设置定时任务，每天更新壁纸
while True:
    time.sleep(24 * 60 * 60)  # 一天的秒数
    with open(img_path, "wb") as f:
        f.write(requests.get(img_url).content)

# 设置定时任务，每天更新壁纸
#while True:
#    time.sleep(24 * 60 * 60)  # 一天的秒数
#    with open(img_path, "wb") as f:
#        f.write(requests.get(img_url).content)
