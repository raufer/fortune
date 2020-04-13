from typing import Dict
from src.rebelion import random

headers = {
    'default': {
        'user-agent': random.user_agent()
    },
    'fool': {
        'authority': 'www.fool.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
    },
    'seekingalpha': {
        'authority': 'seekingalpha.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'machine_cookie=3053511083315',
    },
    'wsj': {
        'authority': 'www.wsj.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'referer': 'https://www.wsj.com/news/markets?mod=breadcrumb',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'DJSESSION=country%3Dus%7C%7Ccontinent%3D%7C%7Cregion%3D; wsjregion=na%2Cus; ccpaApplies=true; ab_uuid=c52a448b-8281-44c7-a744-f1ccefc68e9f; usr_bkt=2qgQ1WCa3A; __gads=ID=3e7c59545d2666b2:T=1586109768:S=ALNI_MYZ53akiJqPDVzuXUXuvINlfvujEw; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; MicrosoftApplicationsTelemetryDeviceId=f1b8b56b-9356-33b7-6162-61f698dcd201; MicrosoftApplicationsTelemetryFirstLaunchTime=1586109772436; kuid=uhzu3oakc; s_cc=true; _scid=6d55e67a-eb7e-4588-a3b7-0b5f21c908c7; _mibhv=anon-1570264794463-1614985233_4171; bkuuid=VqefnN0I99ejHjC5; cX_P=k1db462794l20kp6; cX_S=k8nct6m3x9hf78qe; OB-USER-TOKEN=0bb55319-30ee-4f4f-95d6-94ca3beb948f; _fbp=fb.1.1586109779779.1668488049; __qca=P0-760477952-1586109779700; cX_G=cx%3A1gz9pkubxe80j36kduh2kfibm5%3A29lvelyqak15f; vidoraUserId=81dg5ivbt3jrhph1a95la0gsbfdcj5; _ncg_g_id_=e04a6810-8659-4be5-b2c7-fa65b92677f0; optimizelyEndUserId=oeu1586636105309r0.47113820691543284; djcs_route=f9f355f6-a0c9-48b4-a707-3bb9c451ceeb; csrf_token=hCZ2T10X-xihCX7K_ZSqFEgvvICp-oV9aKLU; Affc=; s_vnum=1618172148788%26vn%3D1; s_vmonthnum=1588287600791%26vn%3D1; TR=V2-01ed257b90057f8b957d4cefa29ea7ce1bb80f926765bd074600a791f2a7aeb0; _micpn=esp:-1::1586636088409; _ncg_id_=16fd5316cdd-a701d576-d8fd-4fc3-a25d-039a3cf2e047; GED_PLAYLIST_ACTIVITY=W3sidSI6ImVHN2ciLCJ0c2wiOjE1ODY2Mzg2MzEsIm52IjoxLCJ1cHQiOjE1ODY2Mzg2MTIsImx0IjoxNTg2NjM4NjMwfV0.; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18366%7CMCMID%7C21246730943920439144263200056451306691%7CMCAAMLH-1587397333%7C6%7CMCAAMB-1587397333%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1586799733s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _ncg_sp_ses.5378=*; _tq_id.TV-63639009-1.5378=ed22fc9b1cfbb219.1586792535.0.1586792535..; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://www.wsj.com/articles/goldman-sachs-lifts-the-veil-to-woo-skeptical-shareholders-11578394803%22%2C%22sref%22:%22%22%2C%22sts%22:1586792537121%2C%22slts%22:1586636090200}; _parsely_visitor={%22id%22:%2241430612-1441-4199-a84c-0a3bd8c7c2f3%22%2C%22session_count%22:3%2C%22last_session_ts%22:1586792537121}; ResponsiveConditional_initialBreakpoint=md; djcs_auto=M1586725424%2FpqqHzbnN06%2BkKL%2FO3etl4rjBjCPI7hjiXdpDOTTrnk9aUVV1hl4x3IQ9H1eHxzIo4KnfTluHRc3ypK4tpTT6gprDzHOkZoWwKqMsM9rDmfvy3pyrXwN0irg9CC3uQUXHPafstGskLXTO%2BzmFyrtjxtPw%2BA3Ki4rzsqDlHbxjEI278WpObow55hmKGww9iGGfcFMY22w2VmGIWK0LivBsODFAV8LfmB3YNoUQtRT%2FkUDk9M6vkAzRAepkqZe4ImP2pmf2u5Kci5O10dKomC7MfyUgHwSS4xmHRjZb6bzrfdbzeJqxjhh6s%2FPNx94kVB8JY%2Fp0whJuUP4wO2tq5hWPLA%3D%3DG; djcs_session=M1586789028%2F3E6ml4MNS9dIgzzZwRFMwdrm02xangtw3OsQ2mdEs3Ds31LaKB9Ln554%2BD9puVqEUd%2Br4mvDTYUS7G55DXdcXCX1N92%2FoRrl4v9liDy19egi7aZqmIlykmREBj%2F0qTmO9t7h%2FT%2FoKBV8HNCHnnG5y4SS3ESfZbGOcBnTUOS2E5WWrqrELj2LyMu7zdq%2Btvdd5J4xvuqQ9rYP5K1lOlG78cl8c2FMw5mwN1e%2BQtrLcnu1HA%2BB5b9Jm7scUJrnlsCEa3A2Iaz4xNFUD%2FktDvCyMjqbMhrVB%2BUD1luIz%2Bxu%2BGhCoa4r9Guotus7YUoMtxCR7hMP9CaQIH%2BFFFW9VzNOFdZyzl3aGvfk1YSXj06Uh4Wz1A9YtfIU7BLglT7C8z22cgV0LcbSQEDde7U47IJG6DexD1WOZmRZMUYh2V%2FTSDn7xBAdkDkpEWDA0eI9WokthPovRHRJl82TW7Cvu2cTjEFAMaL2JatombHYP9P4owijCbs%2BHZHW19mgKj%2BtPwjIovQ0qnhSPn185M1eRPHnf98j6NZvFrKXMjQvmZuS5RU%3DG; usr_prof_v2=eyJwIjp7InBzIjowLjgyLCJxIjowLjkyfSwiY3AiOnsiZWMiOiJHcm93aW5nIiwicGMiOjAuMjk3MDksInBzciI6MC4xNzE1NywidGQiOjY3LCJhZCI6MywicWMiOjk1LCJxbyI6OTksInNjZW4iOnsiY2hlIjowLjI5MjA5LCJjaG4iOjAuMjkzNDYsImNoYSI6MC4zMDg0OCwiY2hwIjowLjMxMjMzfX0sImljIjo3fQ%3D%3D; utag_main=v_id:01714b827e8200138293c230113003079001407100b78$_sn:3$_se:3$_ss:0$_st:1586794403551$vapi_domain:wsj.com$ses_id:1586792531309%3Bexp-session$_pn:3%3Bexp-session$_prevpage:WSJ_Article_Markets_Goldman%20Sachs%20Lifts%20the%20Veil%20to%20Woo%20Skeptical%20Shareholders%20%3Bexp-1586796203563; _ncg_sp_id.5378=f3aaa8bf-5d3d-425d-b241-59415eb48247.1574201660.6.1586792604.1574258972.c19fd8fd-faf5-4dcb-b562-900982d4ee94; _tq_id.TV-63639009-1.1fc3=867f7684ca0f8f36.1586109780.0.1586792604..; s_tp=4895; s_ppv=WSJ_Article_Markets_Goldman%2520Sachs%2520Lifts%2520the%2520Veil%2520to%2520Woo%2520Skeptical%2520Shareholders%2520%2C60%2C23%2C2958',
    },
    'bloomberg': {
        'authority': 'www.bloomberg.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': '_pxhd=df3dcf88e4c8c93866a875f24e7452a5c73ff7c8d3b49b936b5cd0c68f191af1:7eff98d1-7da4-11ea-9a0f-1f8ee13c9df4; _px2=eyJ1IjoiNjY3ZjhhYjAtN2RhMi0xMWVhLTk5MjItYjFmYzJmMjM2ODM0IiwidiI6ImQwMmVkYjUxLTc3NjctMTFlYS1iOTNlLTE3NzI5MmU5NzQ2NCIsInQiOjE1ODY3OTk2MTM3NjYsImgiOiJmZTM5M2NlODBlYzliZmU2ZGQxY2FlZWEwMTIwZjMwNzFkYzY1YTNjNDI2YmQ2MjFkZTM4MjMwOWQ4YTA3ZDk5In0=; _px3=b00e2eabf9edd1e61a9de8eb0b3ead0c2a2e815291e700fc3ae14a59431bf7a6:PZmhrcmJvLJvWoF8o0mgfYUiClgydlgBRW0c9pO49wue+bxXlneXwvg2aciREnaQlwyZ2mDwmqxzpRRupoNpDA==:1000:3aoMphBloznXggbkqRSF9Sid6HQOX2NDIP4PTRevzamcOJ3iumj7YUnVHfKGXWMOdhtrvy9DH/Q/D0r4UhFMe2K5RNqyd/a3hMyB183/yYCOeW+GwQVwjOkRyOnvVk2XyUJU6Q+tOZfR6oxlEZ0dOKWTEYIv2wQkXjGdiVKFkNY=; _pxde=e0787d65bc34a535b1910244b2dca392171086a9d6b90a23aae3a1fe89aea028:eyJ0aW1lc3RhbXAiOjE1ODY3OTkzMTM3NjYsImZfa2IiOjAsImlwY19pZCI6W119',
    }
}


def make_headers(source: str = 'default') -> Dict:
    """
    General header to use in crawling requests

    There is a need to bypass possible crawling detection
    Some amount of randomization must be involved
    """
    return headers[source]
