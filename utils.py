
import requests
from bs4 import BeautifulSoup


def filter_data(total):
    new_data = []
    for i in total:
        i_ = {}
        i_['id'] = i['articles'][0]['id']
        i_['title'] = i['articles'][0]['title']
        i_['detail'] = i['articles'][0]['description']
        i_['category'] = i['articles'][0]['category']['name']
        i_['url'] = i['articles'][0]['detailUrl']
        i_['image'] = i['articles'][0]['fullAvatarUrl']
        i_['published_date'] = i['articles'][0]['publishDate']
        new_data.append(i_)
    return new_data
def filter_data_vnexpress(total):
    new_data = []
    for i in total:
        try:
            i_ = {}
            i_['id'] = i['article_id']
            i_['title'] = i['title']
            i_['detail'] = i['lead']
            i_['category'] = i['article_category']['cate_name']
            i_['url'] = i['share_url']
            i_['image'] = i['thumbnail_url']
            i_['published_date'] = i['publish_time']
            new_data.append(i_)
        except:
            print(i)
    return new_data
def crawl_vietnamnet():
    url_1 = "https://vietnamnet.vn/newsapi/ArticlesByZone/GetsByMultipleZones?q=-00000F-0-16-1-2287779,2288288,2288206,2288025,2288306,2288172,2288004,2288182,2288384,2288241,2288299-260||000002-00002P-0-15-3--350,260,420,550,500|000003-000014-0-18-5--350,260,420,550,500|000001-00000P-0-12-2--350,260,420,550,500|00M7F7-000005-0-12-7--350,260,420,550,500|00000T-00001E-0-11-4--350,260,420,550,500|00000E-00001Q-0-15-6--350,260,420,550,500|000009-00000O-0-15-8--350,260,420,550,500|000005-000015-0-15-10--350,260,420,550,500|000004-00000W-0-15-9--350,260,420,550,500|00087U-0008IS-0-15-20--350,260,420,550,500|000007-00003G-0-15-11--350,260,420,550,500|00000W-00000Z-0-15-13--350,260,420,550,500|000006-000016-0-15-12--350,260,420,550,500|000008-000018-0-15-14--350,260,420,550,500|00000B-00001R-0-15-15--350,260,420,550,500|00000U-00001T-0-15-16--350,260,420,550,500|00000R-00001W-0-15-17--350,260,420,550,500|000079-0008W1-0-15-1--350,260,420,550,500|000078-0008QN-0-11-19--350,260,420,550,500|00002F-00087L-0-11-1--350,260,420,550,500|00003A-00088T-0-11-1--350,260,420,550,500|000036-00004E-0-11-18--350,260,420,550,500|&e=1&r=1"
    url_2 = "https://vietnamnet.vn/newsapi/ArticlesByZone/GetsByMultipleZones?q=-00ZSHX-0-2-0--760,260,350,140,420|-000025-0-5-0--760,260,350,140,420|&e=1&r=1"
    url_3 = "https://vietnamnet.vn/newsapi/ArticlesByZone/GetsByMultipleZones?q=00087L-0008OV-0-1-0--350,260,420,550,500|011G37-00Z9IQ-0-1-0--350,260,420,550,500|00002S-00000Q-0-1-0--350,260,420,550,500|000872-0008UT-0-2-0--350,260,420,550,500|00088M-0008DQ-0-2-20--350,260,420,550,500|00086N-000045-0-1-0--350,260,420,550,500|00MV5E-00LIPY-0-2-1--350,260,420,550,500|"
    url_4 = "https://vietnamnet.vn/newsapi/ArticlesByZone/GetsByMultipleZones?q=00002R-00004H-0-1-0--350,260,420,550,500|&e=1&r=1&rpr=1"

    payload = {}
    headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Referer': 'https://vietnamnet.vn/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"'
    }
    total = []
    for url in [url_1, url_2, url_3, url_4]:
        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()['data']['model']
        total += response
    return filter_data(total)
    
def crawl_vnexpress():
    url = 'https://gw.vnexpress.net/ar/get_basic?article_id=4755330,4755411,4755711,4755826,4755853,4755869,4755948,4755984,4756003,4756019&data_select=article_id,myvne_token,article_category,article_type,privacy,title,lead,share_url,thumbnail_url,new_privacy,publish_time,original_cate,off_thumb,iscomment&thumb_size=490x294&thumb_quality=100&thumb_dpr=1,2&thumb_fit=crop'
    
    payload = {}
    headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Referer': 'https://vnexpress.net/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    total = response.json()['data']
    return filter_data_vnexpress(total)



def crawl_content_vietnamnet(url):
    url = f"https://vietnamnet.vn{url}"
    payload = {}
    headers = {
    'priority': 'u=0, i',
    'referer': 'https://vietnamnet.vn/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    # tìm thẻ id="maincontent"
    maincontent = soup.find('div', id='maincontent')
    if maincontent is None:
        return ""
    maincontent = maincontent.find_all('p')
    content = ""
    for p in maincontent:
        content += p.text
        
    return content
def crawl_content_vnexpress(url):

    url = "https://vnexpress.net/thanh-nien-new-zealand-bi-phat-vi-ve-bay-o-trung-tam-tp-hcm-4756019.html"
    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_gcl_au=1.1.251592455.1712434601; fosp_aid=sbkv7ubp8wpwg9fx.1702921256.des; orig_aid=sbkv7ubp8wpwg9fx.1702921256.des; cto_bundle=wRUiJF8xVk5nM0NjekhTYnZ3Wmk2YTg5RXRsZnZzaUxjRmoyZnBUSmxHZ1V3NTU5YWxaMTZjdmVMSzBVbVRlTkxwbXU0NzdxelBPYW91VmFvSnZ3WEclMkJSNGNTRHQ1Q3BQaTNvZk16eWlna09LVXF6YzJ3MUZ2U0I2eWFiNVAxM2kzc3czd1BXYnhhckN1RGJqN1RtOENONVNrdyUzRCUzRA; cto_bidid=NX6hlF9LdTdMRExjNmhQMFl0UEZMWWQlMkIwUFVpUW02UXJzMFhFNlphNU5LM2N6dyUyRkRaZHNSNllWamFOUGx3QmRjelBlOHRoUWxra1UzQWlUaHRIQjA2QWFnTzR0SmNnamt5ZUxUUGt4Q1lQYmhUMlUlM0Q; _ga_FY6LLK54WZ=GS1.2.1712434602.1.0.1712434602.60.0.0; _ga_16R86549YC=GS1.2.1712434602.1.0.1712434602.60.0.0; ajs_group_id=null; login_system=1; fpt_uuid=%22d1a2db37-62dd-4e5a-be15-adebd19da673%22; __gads=ID=4c501212c86f7fd2:T=1712434604:RT=1712434604:S=ALNI_Mb99oaO3C6IPq4I27CulngeSR5oIg; __gpi=UID=00000de3215603a1:T=1712434604:RT=1712434604:S=ALNI_MZP0XuOmv5wM6aCRuHPyd-mVXNSNA; __eoi=ID=65e680fc3070731d:T=1712434604:RT=1712434604:S=AA-AfjYJ-KLxgphoJ4bGkfW5nC9f; trc_cookie_storage=taboola%2520global%253Auser-id%3Ddcf1e08e-4a1b-4d7f-9a3c-9393bbf371a1-tuctc781eef; FCNEC=%5B%5B%22AKsRol-Ck7SrW5H5lFekKsBZmZyrFlmu76bvJT5dGwRHFzyM8_0B-VLwNpmU1lTzY2fcC8PopcROS6oyHOziWVbVVkRJHcxoOBeiER9cXksxrkNYeBN8HAtt89akFNO-eoSVs0g56yn3OJpcsbkG-JMk88foA401Xw%3D%3D%22%5D%5D; _sharedid=554b2744-fcd8-4186-b313-a4656f6656e7; _sharedid_cst=kSylLAssaw%3D%3D; _pubcid=dca679cd-8455-4b7a-b4de-afe2966fdfe5; _pubcid_cst=zix7LPQsHA%3D%3D; _cc_id=cac84314baf9f147571701508801d737; _au_1d=AU1D-0100-001712434608-U080N4RR-6363; _ga=GA1.1.194327546.1712434601; fosp_uid=sbkv7ubp8wpwg9fx.1702921256.des; _ga_7V7K8QPGYM=GS1.2.1716831062.1.0.1716831062.60.0.0; device_env=4; sw_version=1; _gid=GA1.2.1883267079.1717846810; fosp_loc=24-2-VN; _ps_track_sbkv7ubp8wpwg9fx.1702921256.des=1; _gtm_ps_track=1; _ga_MPQLNMB143=GS1.2.1717846819.1.1.1717846910.60.0.0; _gat_t3=1; _dc_gtm_UA-50285069-28=1; _ga_DD32PR27WT=GS1.2.1717848592.1.0.1717848592.60.0.0; _ga_DQJ7NF9DN2=GS1.1.1717846811.3.1.1717848592.60.0.0; _ga=GA1.2.194327546.1712434601; _gat_UA-50285069-28=1; _gat_UA-169360081-2=1; _ga_57577CKS2C=GS1.1.1717846811.3.1.1717848592.60.0.0; _gat_ab=1; _ga_W7FX4429ZK=GS1.2.1717846823.2.1.1717848600.60.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    # tìm tất cả thẻ p có class="Normal"
    maincontent = soup.find_all('p', class_='Normal')
    content = ""
    for p in maincontent:
        content += p.text
    return content


