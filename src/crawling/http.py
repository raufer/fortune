from typing import Dict
from src.rebelion import random

headers = {
    'default': {
        'user-agent': random.user_agent()
    },
    'fool': {
        'user-agent': random.user_agent()
    },
    'seekingalpha': {
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
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'wsjregion=europe; ab_uuid=67638e1e-9b8e-488f-85c8-103dac7dd775; usr_bkt=ixi4E5ylqa; __gads=ID=0747bfb9ad2bbb8e:T=1574201653:S=ALNI_MbxHsQH65VEySrUFQ3n0BwxpLr-kQ; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; MicrosoftApplicationsTelemetryDeviceId=82fc70e1-9d59-65c1-5fec-478248d2f368; MicrosoftApplicationsTelemetryFirstLaunchTime=1574201655736; s_cc=true; kuid=uhzu3oakc; NaN_hash=ad3af6d1QERCCIGZ1574201660385; _mibhv=anon-1570264794463-1614985233_4171; _scid=fb997afd-4b8d-49b8-8604-79df8b9bbc36; _ncg_g_id_=5707e9dd-bb9a-45fd-99ba-39ae71fd911d; bkuuid=VqefnN0I99ejHjC5; cX_P=k1db462794l20kp6; cX_S=k36f0vhana9p42ru; OB-USER-TOKEN=0bb55319-30ee-4f4f-95d6-94ca3beb948f; _fbp=fb.1.1574201661480.1301116815; __qca=P0-614821272-1574201661138; cX_G=cx%3A1gz9pkubxe80j36kduh2kfibm5%3A29lvelyqak15f; vidoraUserId=9rs4oe3oh3jefbtigg6ul86qsf5jqc; djcs_route=69cbcfd1-72c2-44be-bbcf-ea820077c253; TR=V2-49c6288f00b98ae8d707a7518762ddc03a8a2108fa46ede5a9c41f65af9e56b3; optimizelyEndUserId=oeu1574203407377r0.8543075259068391; s_vnum=1605740105481%26vn%3D1; _ncg_id_=16e866a587d-6cccec50-9ae4-4c30-8ae1-761a79334a51; ki_t=1575586439511%3B1575586439511%3B1575586439511%3B1%3B1; ki_r=; DJCOOKIE=fp_axes_width%3Dat16units; DJSESSION=country%3Dus%7C%7Ccontinent%3D%7C%7Cregion%3D; ccpaApplies=true; _mibhv=anon-1570264794463-1614985233_4171; _micpn=esp:-1::1578009362250; _micpn=esp:-1::1578009362250; GED_PLAYLIST_ACTIVITY=W3sidSI6ImVHN2ciLCJ0c2wiOjE1NzgwMDkzOTMsIm52IjoxLCJ1cHQiOjE1NzgwMDkzNjUsImx0IjoxNTc4MDA5MzkzfSx7InUiOiJnL0VLIiwidHNsIjoxNTc4MDA5MzY1LCJudiI6MSwidXB0IjoxNTc4MDA5MzU5LCJsdCI6MTU3ODAwOTM2NX1d; gdprApplies=false; djcs_auto=M1578258224%2Fhz4aCaHeeuzNvMoKuBtd4DY6OrMumSxx5X%2BHtoGNNxw6erGjAZR36%2Fppeeeka7tF62ZKukU9Kht4%2BrHJeBBThmIxIDneYzD%2Fd5sKSC8bP7lieHjdH4olAlqYNkvFFQvjAoANw5fZusunCRS%2FGQtZhF00TNv24Lm5fojenXSfArXdkiMZbh%2B8Hc35YcGFYB%2F0p%2FxgEl%2FpJY%2FchGHcs2%2FS1jeUM68M6v%2F3PZQMs6iZTnGG8yG8B6ctCZFIEfideENCuMxMOhxWS3psiPLL7U0JhhkC0nIbAEGIdCX9nDwmvLtBn%2BcCVPOXD90q%2FEHWcybj1KNoV4Xs8871Dkiizf%2BhTw%3D%3DG; djcs_session=M1578257028%2FiLMckgBoo0vjpsBn9lUIjcXqDZAsN6KYbETMRAt9UuGJUIP%2FDno5lk5fw7JG5JTJTzs%2F7KAhoB2OC1uB0EgA53Qqrb7Y8tz4M3pUA8BL%2F6MQh%2FbeFiUsbKsMWhIXIUOSFJR7L9wFGswXfJDP5Bqgki1NJqDkH%2FWp0fqbDwbQPz4SR9yW6kOqhg%2FgNxMchjbwFEF52PalvsDbqvBEt4n5mTnUYWZ1kj25sVQeyddBAkGS2MZIjI%2FnynDrPvPzak7Q6ak7diblZYvYZMK377ysKrO54GOQh5Au2TATm%2BuBSJ7i0dHXNDEMnIJT6I7bEQ9OCUBk5eNjRISwLXtSLnWwn5oKb%2BOvBW13D6b5%2Bajp9vOumokkVyMUuN761EnyjxPlqDUC%2FXRc2oGegvizXIR8FPLb3jTsPf%2FZZkJJAUEQhf59wgRK67woHxPnBdsD5bju4QSLGByLGGw16cplD2881jKyff05WvQmmpeMWcSn4hjx7fApNaAXs%2Fx2%2F%2FRIcetzR8YRvCiAcqyoJNhyRNVMJr46p7g1LG1ywwWKgf9doB4%3DG; usr_prof_v2=eyJwIjp7InBzIjowLjUxLCJxIjowLjgzfSwiY3AiOnsiZWMiOiJMYXBzaW5nIiwicGMiOjAuMTQ5NzEsInBzciI6MC4yODM1MiwidGQiOjQ3LCJhZCI6MCwicWMiOjc4LCJxbyI6OTUsInNjZW4iOnsiY2hlIjowLjE0Mzc2LCJjaG4iOjAuMTAwNTYsImNoYSI6MC4xOTQyMiwiY2hwIjowLjE1NjM1fX0sImljIjo1fQ%3D%3D; utag_main=v_id:016e85bb128c0047f2a7da85205803078001407000ac2$_sn:7$_se:1$_ss:1$_st:1578265860092$vapi_domain:wsj.com$ses_id:1578264060092%3Bexp-session$_pn:1%3Bexp-session$_prevpage:WSJ_Article_Markets_Vanguard%E2%80%99s%20Asia%20Head%20Leaves%20Investing%20Giant%20After%20Leading%20China%20Push%20%3Bexp-1578267660104; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18267%7CMCMID%7C33805723128523325444614507594128489084%7CMCAID%7CNONE%7CMCOPTOUT-1578271260s%7CNONE%7CMCAAMLH-1578868860%7C6%7CMCAAMB-1578868860%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.4.0; _ncg_sp_ses.5378=*; hok_seg=8ljs5iat1cy0,8m5oogcu3a7n; _tq_id.TV-63639009-1.1fc3=ec0d254e4bf775bd.1574201661.0.1578264061..; _ncg_sp_id.5378=f3aaa8bf-5d3d-425d-b241-59415eb48247.1574201660.6.1578264062.1574258972.c19fd8fd-faf5-4dcb-b562-900982d4ee94; _parsely_session={%22sid%22:9%2C%22surl%22:%22https://www.wsj.com/articles/vanguards-asia-head-leaves-investing-giant-after-leading-china-push-11577969213%22%2C%22sref%22:%22%22%2C%22sts%22:1578264062729%2C%22slts%22:1578045921866}; _parsely_visitor={%22id%22:%2220fc6d8d-7a1f-4aef-8111-d1051bd810f3%22%2C%22session_count%22:9%2C%22last_session_ts%22:1578264062729}; ResponsiveConditional_initialBreakpoint=md; s_tp=5947; s_ppv=WSJ_Article_Markets_Vanguard%25u2019s%2520Asia%2520Head%2520Leaves%2520Investing%2520Giant%2520After%2520Leading%2520China%2520Push%2520%2C27%2C27%2C1599',
    },
    'bloomberg': {
        'authority': 'www.bloomberg.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pt;q=0.7,de;q=0.6',
        'cookie': 'bbAbVisits=; euconsent=BAAAAAAOsuCVWAdACBENBt-AAAAtF7_______9______9uz_Ov_v_f__33e8__9v_l_7_-___u_-33d4u_1vf99yfm1-7etr3tp_87ues2_Xur__79__3z3_9pxP78k89r7337Ew_v-_v8b7JCKN4A; _gcl_au=1.1.1682337966.1575589038; bdfpc=004.1419417053.1575589038167; _ga=GA1.2.967977455.1575589038; _reg-csrf=s%3AYBpf0jnzqBFi4gvawtYOdka5.rLNS8TlvQ9W6EiG0MXlzcTWzPdZ9hUomuV7FkfyKFk0; agent_id=aec658be-317a-4e56-84e0-d1e5c41d5b7a; session_id=c80135b5-6e14-4ca3-9254-a9bab9492d82; session_key=296b628d0254a54e8b5aaedd71eb83d8b530bbbb; _user_newsletters=[]; _pxvid=2d9f6fca-17b8-11ea-9594-0242ac12000a; notice_gdpr_prefs=0|1|2:; notice_behavior=expressed|eu; notice_preferences=2:; _fbp=fb.1.1575589039441.2389037; _pxhd=121d696ecf7217a2e6911a91f03e01468dd8bdcb1f1df9501495d2d926c73a5b:2d9f6fca-17b8-11ea-9594-0242ac12000a; __tbc=%7Bjzx%7Dt_3qvTkEkvt3AGEeiiNNgA_-rBL3o-JUI_IOc8tHwfcPi7ZxCnsLlBD30VXzu7S0RTQoSxhrZ2TT6hkjoakGnpIK2PDJWTMolt-QYBKxLQ9bCtabSq2l1pZhDJ3T2LqCjylU0Z664w9lha1BgkmqDg; xbc=%7Bjzx%7DB898b9ALuN__WgJU656gmq0Bse-kBt92_JPrbB71kZpMhP9YaDQtbKpijra2rqLpukrhB8mnfaUCptxLY68RVXbzW3iSZfGaITsf1DkFMWedhxsxAgTUmwsQuyBsZp_pSjT-kcEUMrQR3wBBs5XuyJzclRq3O4UkwBuetIRtSOdsOuG4iYFSqNgSD2CaQBpRmVYrzI4mhsFK2O2kyJaXBO4Bp5KdGiT3r1nixHFzLKcgmY_4k7GGVNeLbxBGU53kRWwBI5PTms_yjRvEgpkfMKdQhrOz8FabXobdTz1odHNPGpBTY6BCujyZEWIi4h-FQtD5GKBWP_qQfXHq5SF6uRk2ph7xNW42IyYRdAEZO-4UOcsIU3U7gbx7MtTgOW7IGp29FwWhf8c_tB273kHg-qbdeUSmmdjzK9NDxao2kz0; permutive-session=%7B%22session_id%22%3A%22e00ae504-e58f-480b-93cb-82885780c613%22%2C%22last_updated%22%3A%222019-12-05T23%3A37%3A19.611Z%22%7D; __sppvid=dd88e01a-4691-4894-a5dc-f368b93df75f; _parsely_visitor={%22id%22:%22934b2aac-62fd-458e-a855-3c77252dc599%22%2C%22session_count%22:1%2C%22last_session_ts%22:1575589040140}; bbAbVisits=; _parsely_slot_click={%22url%22:%22https://www.bloomberg.com/europe%22%2C%22x%22:585%2C%22y%22:116%2C%22xpath%22:%22//body/div[4]/div[1]/ul[1]/li[3]/a[1]%22%2C%22href%22:%22https://www.bloomberg.com/markets/stocks%22}; trc_cookie_storage=taboola%2520global%253Auser-id%3Dfe996379-7e9c-40e2-94fd-6d1918ba7284-tuct491dc15; optimizelyEndUserId=oeu1575589288903r0.4624210967823976; __stripe_mid=408921e4-b306-444b-baa6-0a3e7f6dc730; _geoip_country=GB; opt-reg-modal-triggered=true; _breg-uid=5CEB83E67F1C4D7E86B55B4817FAC227; _user-status=logged_in; _sp_id.3377=e0f452e3-cd5c-47e0-9e4e-395905937f26.1575589289.1.1575589440.1575589289.e28bd932-93ee-43e7-9f4e-ade73e292a9c; _breg-user=%7B%7D; _subscriptions-data=[{"product":"BBG","type":"DIGITAL","entitlements":["bbg-digital"]}]; _subscriptions=bbg-digital; _linked-accounts=; _user-role=Consumer; _li_dcdm_c=.bloomberg.com; _lc2_duid=b1166d620485--01dxm89gk7rgat6tm1gq0g77nb; bb_geo_info={"country":"GB","region":"Europe"}|1578611330468; _gid=GA1.2.630553705.1578190887; DigiTrust.v1.identity=eyJpZCI6IkV0M2NlWEhVNU5pVitDek12RkFadHBmUitaWmYwRjRXZ0JLcUlNbGozNjVPQzRrekJzaFA1T3pwM3dvYWtHRE5pa1V2MmZUOHA4SnlJYVVhU3VGVXdwNEViZmtxSURVS2ZrUTNGUEphU0xmbTZaZCtpVEZPVEdIRU9zSVNCWm9UcCs3UkNWSzk5TEhYWGg0NENlVGhuWE13bkdEeE5rempCenh5UW5pT0psd0xKclo4VGRpTkFDQ0hkRWIzU2oveFJXN2Z1d1ZyK3VFeEdmOEoxR1dYZGhzMFBQNVdDTnd3OXhMTUU2K2tObEljZjZOTHJkV1g2TEtpazcwVW5KWW9HaHd4UlZ1M2FNMVhSdGpGM0xES0xpRWppSllhd21HRXNrbDVtNlZjSHdkSTdUNlI4RlUrZW42ejcwaTdCUnVSTDRHSTgxYU1YWXdIS005RFo5dFJvdz09IiwidmVyc2lvbiI6MiwicHJvZHVjZXIiOiIxQ3JzZFVOQW82IiwicHJpdmFjeSI6eyJvcHRvdXQiOmZhbHNlfSwia2V5diI6NH0%3D; com.bloomberg.player.volume.level=1; com.bloomberg.player.volume.muted=false; __gads=ID=6eaadd196e1bc139:T=1578265997:S=ALNI_MYsaXrq1sVkZNy03jUzXMdUguJMFg; euconsent=BAAAAAAOsuCVWAdACBENBt-AAAAtF7_______9______9uz_Ov_v_f__33e8__9v_l_7_-___u_-33d4u_1vf99yfm1-7etr3tp_87ues2_Xur__79__3z3_9pxP78k89r7337Ew_v-_v8b7JCKN4A; bb-mini-player-viewed=true; GED_PLAYLIST_ACTIVITY=W3sidSI6IlBOaWUiLCJ0c2wiOjE1NzgyNzAwODEsIm52IjowLCJ1cHQiOjE1NzgyNjYzOTcsImx0IjoxNTc4MjY2NDY1fV0.; _last-refresh=2020-1-6%200%3A21; _user-ip=109.151.148.81; _reg-csrf-token=tT3hw8zO-Pain0ldcV9OayeB4UbvNQsSouUs; _subscriber-data={"introPeriodStatus":"beginning-of-intro","billingPeriod":"Month","subscriptionType":"DIGITAL","subscriptionStatus":"active","offerType":"SINGLE","daysSubscribed":31,"subscriptionProvider":"ZUORA","subscriber":true}; _tb_sess_r=https%3A//www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch; _tb_t_ppg=https%3A//www.bloomberg.com/vendors/taboola_loader.html; _pxff_tm=1; _px2=eyJ1IjoiZWMwMDQ5YjAtMzAyMC0xMWVhLThiM2YtOTVhZWRmYzMwNTk2IiwidiI6IjJkOWY2ZmNhLTE3YjgtMTFlYS05NTk0LTAyNDJhYzEyMDAwYSIsInQiOjE1NzgyNzMxNTU3NDksImgiOiIzNjc3ZjExZmVjMDQwMjgwODM4Yjc2M2JhMWRjMzhiZGQzYmQ0ZmQxZTdjZDI5NDZkZTJiNDY0YmNiZDQyM2RmIn0=; _px3=61856f3036f94a662406142ab177d11c7d6c7cfa3f4c0f0e207515b8841d8f80:Ia6+PGgleD0NPLLfN2Mpy7bV5aoVGMP//H3hdZ1LRm5eNS5BrlP+ScpuLQehs9RfrWgPgB2rCuKJpQTnaSTQ9Q==:1000:2x784gazC4CsDCRHmyHKAsxRDXp5A9IlZmeak2ipLU2nEQmBOdSuxcA8F0NGaP6yGZ1r9+IZAG9jkbvP41O8fFGANJITM06Qt/hm+32t3VQoMetcF0gAwEBJvBvJPys4B9LvW4a9EMZQCFJsKD4rTKrBY+gdtFGUSQVdPy1gb6k=; _pxde=12eb0de8170fc9fdd1b65a859afd24b75a746f16246bcaccfe68ab9b78eaec59:eyJ0aW1lc3RhbXAiOjE1NzgyNzI4NTczNTMsImZfa2IiOjAsImlwY19pZCI6W119',
    }
}


def make_headers(source: str = 'default') -> Dict:
    """
    General header to use in crawling requests

    There is a need to bypass possible crawling detection
    Some amount of randomization must be involved
    """
    return headers[source]
