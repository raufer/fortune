from typing import Dict
from src.rebelion import random


headers = {
    'default': {
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
    },
    'wsj': {
        'authority': 'www.wsj.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'wsjregion=europe; ab_uuid=67638e1e-9b8e-488f-85c8-103dac7dd775; usr_bkt=ixi4E5ylqa; __gads=ID=0747bfb9ad2bbb8e:T=1574201653:S=ALNI_MbxHsQH65VEySrUFQ3n0BwxpLr-kQ; djvideovol=1; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; MicrosoftApplicationsTelemetryDeviceId=82fc70e1-9d59-65c1-5fec-478248d2f368; MicrosoftApplicationsTelemetryFirstLaunchTime=1574201655736; s_cc=true; kuid=uhzu3oakc; NaN_hash=ad3af6d1QERCCIGZ1574201660385; _mibhv=anon-1570264794463-1614985233_4171; _ncg_g_id_=5707e9dd-bb9a-45fd-99ba-39ae71fd911d; bkuuid=VqefnN0I99ejHjC5; cX_P=k1db462794l20kp6; cX_S=k36f0vhana9p42ru; OB-USER-TOKEN=0bb55319-30ee-4f4f-95d6-94ca3beb948f; _fbp=fb.1.1574201661480.1301116815; __qca=P0-614821272-1574201661138; cX_G=cx%3A1gz9pkubxe80j36kduh2kfibm5%3A29lvelyqak15f; vidoraUserId=9rs4oe3oh3jefbtigg6ul86qsf5jqc; djcs_route=69cbcfd1-72c2-44be-bbcf-ea820077c253; TR=V2-49c6288f00b98ae8d707a7518762ddc03a8a2108fa46ede5a9c41f65af9e56b3; optimizelyEndUserId=oeu1574203407377r0.8543075259068391; csrf_token=Covy2xyv-tmGR8oDuuKva1KFEHCIRwNfzYI0; Affc=; s_vnum=1605740105481%26vn%3D1; _ncg_id_=16e866a587d-6cccec50-9ae4-4c30-8ae1-761a79334a51; gdprApplies=true; GED_PLAYLIST_ACTIVITY=W3sidSI6ImVHN2ciLCJ0c2wiOjE1NzQzNDAxNDIsIm52IjowLCJ1cHQiOjE1NzQyNDk3MjYsImx0IjoxNTc0MjQ5NzI2fV0.; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18236%7CMCMID%7C33805723128523325444614507594128489084%7CMCAID%7CNONE%7CMCOPTOUT-1575592400s%7CNONE%7CMCAAMLH-1576190000%7C6%7CMCAAMB-1576190000%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.4.0; _ncg_sp_ses.5378=*; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _micpn=esp:-1::1575585202704; _parsely_session={%22sid%22:6%2C%22surl%22:%22https://www.wsj.com/news/business%22%2C%22sref%22:%22%22%2C%22sts%22:1575585203771%2C%22slts%22:1574258972521}; _parsely_visitor={%22id%22:%2220fc6d8d-7a1f-4aef-8111-d1051bd810f3%22%2C%22session_count%22:6%2C%22last_session_ts%22:1575585203771}; djcs_auto=M1575579824%2FiClc6jw4rbw2eTvFw1doJMLFULDw6w0o23A3gK7JOi%2B27TINgFKkzjc92QrN%2FLyituKOd43jjCRNqWPXlJqpRJOat7y0l3OuN4qssTVk1unN5x5oCK9gprFbk5XAhr0NW6W%2BOLFY1PVA5osPjDDfR%2FxJFg0zGM8TKBfz2KZTewEFuqd2WjeVLOpHt3DNafcf7By1k7V9Eda6Pj8eXuhxVObQdmJ%2BOCQT5D2h3Z%2BIR0HNI5Lq26yn7zR18Yg72MHB1kcmQBOs0uWrkeZNM7s57SyJgB8Hs5nMmZS9euwSMwb%2FHqWYrwBPeYqTPH8dvDHjRFO16zKiNMxQONZupFLN6Q%3D%3DG; djcs_session=M1575578628%2FdG7kOzKXs%2Bnt6GppLrk5%2BJaKspqXmQUxqwIumZ1OESJ0AGaRTUK%2FApAfLd%2FO740HbUgmrd8aGNfn0M1caZzORiAI8ks402oAKD7PAkS7%2Fv2tz7HOwXNIuAUnjtpqVMBDSsbaImXUCMIhvB2rTwyrQj3NMbVytmjZbYAyLT%2Fgs7cm40oQM4xnKwi2nRhESX4UymcG%2FcLP%2BHfohjnc2Qtvc85N%2FFm3Pxdjj8REC90tbe%2BtaE90Eb2f%2BhWhQNbibYs51rzhCqj7d%2BY96u3MM%2BzjYO6Rj61m0SZnv%2FExVoHA3KVOFk3nRdkBZnPKnVh39zMkp3b6eASyQnubr2h1kob47HyUZV2qEBfe%2Fs3VgkDdxE9P8QJ2DoNJi%2Flqm7iw3Ce0JYBVqpwybi4ISDMEn6PTMjGdZh0277HOiwoDpY%2FIgb8JE4Igk8qZ9XmYY510BiocKF9ZqCTJy7RjnG9V79DMoEqZ%2BhKz1zVmVBe8raNAK8dAwH6gfU22KoMxsIKiKXPATm82jnPSdBMTebjeSAJ1tmmIWEX0lTYZfYewTiA1xfg%3DG; usr_prof_v2=eyJwIjp7InBzIjowLjgzLCJxIjowLjk0fSwiaWMiOjV9; utag_main=v_id:016e85bb128c0047f2a7da85205803078001407000ac2$_sn:5$_se:5$_ss:0$_st:1575587335430$vapi_domain:wsj.com$ses_id:1575585200652%3Bexp-session$_pn:5%3Bexp-session$_prevpage:WSJ_Article_Markets_How%20Johnson%20%26amp%3B%20Johnson%20Shares%20Can%20Get%20Well%20%3Bexp-1575589135438; _ncg_sp_id.5378=f3aaa8bf-5d3d-425d-b241-59415eb48247.1574201660.6.1575585536.1574258972.c19fd8fd-faf5-4dcb-b562-900982d4ee94; _tq_id.TV-63639009-1.1fc3=ec0d254e4bf775bd.1574201661.0.1575585536..; ResponsiveConditional_initialBreakpoint=md; s_tp=5866; s_ppv=WSJ_Article_Markets_How%2520Johnson%2520%2526amp%253B%2520Johnson%2520Shares%2520Can%2520Get%2520Well%2520%2C17%2C17%2C977',
    }
}


def make_headers(source: str = 'default') -> Dict:
    """
    General header to use in crawling requests

    There is a need to bypass possible crawling detection
    Some amount of randomization must be involved
    """
    return headers[source]
