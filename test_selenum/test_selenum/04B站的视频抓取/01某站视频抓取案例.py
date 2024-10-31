#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/31 15:09
@Author  : admin
@File    : 01某站视频抓取案例.py
@Project : test_selenum



"""
import requests

url1 = 'https://xy27x128x216x6xy.mcdn.bilivideo.cn:4483/upgcxcode/47/51/504135147/504135147-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1730366843&gen=playurlv2&os=mcdn&oi=3395563658&trid=0000cc3167ceaeb544bbad5c3be72080e434u&mid=43205338&platform=pc&og=hw&upsig=3979c3d28e395257d8ae61fe297b950a&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50005370&bvc=vod&nettype=0&orderid=0,3&buvid=9091B11E-7DE3-215F-E6BD-3B9A9C2DBC5630146infoc&build=0&f=u_0_0&agrr=1&bw=110969&logo=A0020000'
url2 = 'https://xy36x163x204x37xy.mcdn.bilivideo.cn:8082/v1/resource/504135147-1-30280.m4s?agrr=1&build=0&buvid=9091B11E-7DE3-215F-E6BD-3B9A9C2DBC5630146infoc&bvc=vod&bw=15835&deadline=1730366843&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50005370&mid=43205338&nbs=1&nettype=0&og=hw&oi=3395563658&orderid=0%2C3&os=mcdn&platform=pc&sign=f9c560&traceid=trONLNvnwVEdcu_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=54e354e6539dc367c0845439a2263092'

headers = {
    "Cookie":"LIVE_BUVID=AUTO9216362008911008; CURRENT_FNVAL=4048; _uuid=BECDB2102-68103-E1A9-2BEE-9C66E52B109E143831infoc; buvid_fp=4dd51b670f7b4ba8537cece2307ff8b3; rpdid=|(JJmllYJYl)0J'u~u)Jl~)Y|; buvid4=69A5E170-8FA3-65A0-9268-E73E4EF7BEC547454-024080902-zg1/HB0gIqauL5J06rQxFQ%3D%3D; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=43205338; DedeUserID__ckMd5=a01600c5b3d2915c; buvid3=9091B11E-7DE3-215F-E6BD-3B9A9C2DBC5630146infoc; b_nut=1729903830; bp_t_offset_43205338=992419427158851584; home_feed_column=5; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; SESSDATA=47e4c0b7%2C1745810466%2C461d3%2Aa1CjAfcNzeqztAs7TCf-GUy1ObePy5qBeyj7ExWXf0CfRAIJiFNmZZFyGtZDLxPR2mVrQSVnhZellyZ1g5Q3RuVE9GQ2NxZTBOVVdiWmlHa2pkTXVteFBlSGtzVUYxSU9WUkdsS2lvM0w0aTJsX0xKcjdiQjdTa21LTG02aXJ6RTQ1dkZWbkVzdzVBIIEC; bili_jct=9a6761c75f4cd839c90e25d9274e60c7; sid=6bnv70of; bsource=search_baidu; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA2MTgxNDMsImlhdCI6MTczMDM1ODg4MywicGx0IjotMX0.Sos8op4qb3GukPb7K7bKO1EnV541gOxJ8bLI-IMasSQ; bili_ticket_expires=1730618083; b_lsid=D10F72559_192E17AB3B4; browser_resolution=1920-150",
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    "Referer":'https://www.baidu.com/link?url=ss_0PtSB9uBLLPNrfPGszQTMraN7yvO90KAVz7y-F27YzH83-9jbG8zZKju2sh-d&wd=&eqid=c14a4b980011e698000000066722dcac'
}

sp1 = requests.get(url=url1,headers=headers)
sp2 = requests.get(url=url2,headers=headers)

with open('sp1.mp4','wb') as f:
    f.write(sp1.content)

with open('sp2.mp4','wb') as f:
    f.write(sp2.content)


from moviepy.editor import ffmpeg_tools
# 将两个视频进行合成
ffmpeg_tools.ffmpeg_merge_video_audio('sp1.mp4','sp2.mp4','天地龙鳞.mp4')