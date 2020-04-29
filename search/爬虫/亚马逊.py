import requests
url='https://www.amazon.cn/dp/B07NZZ6Q8Y/ref=s9_acsd_hps_bw_c2_x_0_t?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-8&pf_rd_r=GXZMAF8GXR06ZYNPVF8X&pf_rd_t=101&pf_rd_p=d36c24cb-2322-4e4e-a536-20e23ff9dce3&pf_rd_i=1337022071'
kv={'User-Agent':'Mozilla/5.0'}
r=requests.get(url,headers=kv)
print(r.status_code)
print(r.encoding)
r.encoding=r.apparent_encoding
print(r.text[1000:2000])
print(r.request.headers)
