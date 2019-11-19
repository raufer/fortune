from src.rebelion import random
from typing import Dict


def make_headers() -> Dict:
    """
    General header to use in crawling requests

    There is a need to bypass possible crawling detection
    Some amount of randomization must be involved
    """
    headers = {
        'authority': 'seekingalpha.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': random.user_agent(),
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'crfgL0cSt0r=true; machine_cookie=5691420493913; _gcl_au=1.1.504033141.1570281037; _ga=GA1.2.873643888.1570281038; _fbp=fb.1.1570281037929.366137510; __gads=ID=d3c3ff443f712eea:T=1570281037:S=ALNI_MZFpd2I1lj3gmVbZSZS_NpyySB_3A; _pxvid=868183fd-e771-11e9-9cdc-0242ac12000e; h_px=1; _hjid=7cbbfe32-7546-4454-b4e2-f47acb6b67c4; _igt=ee428eda-e3ea-40f5-ea1c-bf441b0dd0c7; __adroll_fpc=7ba3f523b7c534c32601d29e08c4417c-s2-1571227330648; _lo_uid=178184-1572261346543-2b74abfac4c61921; lo_session_in=1; _lo_v=1; __lotl=https%3A%2F%2Fseekingalpha.com%2F; user_id=50368805; user_nick=rauferreira; user_devices=; u_voc=; marketplace_author_slugs=; has_paid_subscription=false; user_perm=; sapu=101; user_remember_token=d8af3084f5ed201562c3d03b9323acafb55b9c58; _sapi_session_id=eyJzZXNzaW9uX2lkIjoiYmJmNTJmZTUxZmZkOGM4ZjZhYjg4M2Y0ODY4OGU0ZmUiLCJvbW5pYXV0aC5zdGF0ZSI6IjZiMzdkMTQwZjhkNjUzZjFmZTgwYjg0ZGUyZjcxYzA5YmUzMzg5YmU0MWJjZGNiYyJ9--339c5a2f011f4bdc5e78764beda344116fb25840; portfolio_sort_type=a_z; user_cookie_key=ja5mkm; mnet_session_depth=2%7C1573857872056; __aaxsc=0; _gid=GA1.2.1023044106.1574115369; gk_user_access=1**1574118752; gk_user_access_sign=64844ea82361dded899e782a9ee65670cf5f9852; _ig=a00b60a7-43f5-4cfd-9803-9f4de0cce418; aasd=1%7C1574120360035; _dc_gtm_UA-142576245-1=1; _gat_UA-142576245-4=1; __ar_v4=F6X65CJ4K5E43AFRH5CGQD%3A20191117%3A3%7CULCHBRH4ZZGFXDWGQTC6RG%3A20191115%3A3%7CHWYEUMZG3RCB3IJESAMRSO%3A20191115%3A6%7CRFXAEISDJFDZDINVACZG6X%3A20191115%3A6; _px2=eyJ1IjoiYTRkYjgzZTAtMGE1Yy0xMWVhLTk0MzEtNzViYmE1MTFlZWU3IiwidiI6Ijg2ODE4M2ZkLWU3NzEtMTFlOS05Y2RjLTAyNDJhYzEyMDAwZSIsInQiOjE1NzQxMjA4NjU4NzYsImgiOiIwYjZjNzI0OWZmMmM1MzU4MDU2MmUyMDBhNDEzZGVmYmVkNjIxNzRlNzg5YzBhNzlhYzQ3ZWY0ZTM2OTc4NGE3In0=; _px=4VNIbIRGys1QIli15gmSe+YZre/3mwpGUd5Y2vIWszCpv7mwi+4y3zT5WibuDX3P+BO7F3uS7PIPyffenglfVw==:1000:CFXCwEcshoGb/DM/hBD5hENQsg2BEaj1PcyofWMrFadBoe0oQJCy+0Mv0JlblUzI8Rl4oOEdDs2sNTNlZmwvzgHjlXmhw8aEN/rXp7X4T1jjfv+PW8yEpru+GNZKLQpQjEyloMkLTyz5KrdOse5ogQ6dvTtfsmgC0jQCGHWlDGq2SXCdr0xfke23gPxrWkmRhZmzQFURkETipIWdeES+5JeVjB7LChHW3Y72WDlLEP6r9+GL9mixqjk2Zd8pOm12TgZf9gCcJb3U+W1sL+yiEQ==; _pxde=15c3e9632fd4f2257eac52bfb69a8bafc4d76027511a60465a3b2983395da4c8:eyJ0aW1lc3RhbXAiOjE1NzQxMjAzNzA4NDEsImZfa2IiOjB9',
        'if-none-match': 'W/"2979e3cd52cffe1082aaea6ab5cb31d6"',
    }
    return headers

