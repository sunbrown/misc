#!\\usr\\bin\\python3
# -*- coding: utf-8 -*-
# @Time    : 2019\\11\\1 19:00
# @Author  : Brown
# @FileName: 复制文件夹.py
# @Software: PyCharm
import os, shutil

a = ['1991231',
     '2093095',
     '2122800',
     '2132566',
     '2152335',
     '2329508',
     '2376803',
     '2544731',
     '2581303',
     '2592989',
     '2620866',
     '3769787',
     '3919953',
     '3998400',
     '4006623',
     '4167937',
     '4399643',
     '4416986',
     '4796058',
     '4795222',
     '4911355',
     '4992558',
     '5253413',
     '5563204',
     '5704589',
     '5744701',
     '5961179',
     '5994628',
     '6176680',
     '6410192',
     '6383289',
     # '648489',
     '1421108',
     '1462782',
     '1553220',
     '1719192',
     '2112824',
     '2133032',
     '2210982',
     '2287024',
     '2414491',
     '2556195',
     '2586632',
     '2669539',
     # '2829729',
     '2939642',
     '2956820',
     '3028313',
     '3217787',
     '3778630',
     '3808658',
     '3910608',
     '4027681',
     '4230344',
     '4279035',
     '4288242',
     '4883390',
     '4913106',
     '4957746',
     '4984908',
     '5049219',
     '5121559',
     '5703009',
     '5986460',
     '6100377',
     '6203991',
     '1008090',
     '4577147',
     '6330212']
b = [
     # '1179645',
     '1934249',
     '2024147',
     '2201288',
     '3655682',
     '3778737',
     '3824073',
     '4031200',
     '4040596',
     '4168477',
     '4162272',
     '4380303',
     '4389989',
     '4458695',
     '4600986',
     '4657283',
     '4866145',
     '5189051',
     '5423508',
     '5507488',
     '5594980',
     '5769556',
     '5803981',
     '5897912',
     '5945642',
     '6020378',
     '6026894',
     '6126364',
     # '1141076',
     # '1373888',
     # '2863840',
     '3807147',
     '4726908',
     '4793248',
     '5166366',
     '5178111',
     '5212985',
     '5436564',
     '5458070',
     '5477549',
     '5603064',
     '5662341']

des_path1 = 'E:\\a'
des_path2 = 'E:\\b'

# for i in a:
#     path1 = 'E:\\肖练\\有病人文件夹\\src\\粘液癌，单纯'
#     path2 = 'E:\\肖练\\有病人文件夹\\src\\粘液癌，混合'
#     try:
#         shutil.copytree(os.path.join(path1, i), os.path.join(des_path1, i))
#     except Exception:
#         shutil.copytree(os.path.join(path2, i), os.path.join(des_path1, i))
#     except Exception:
#         print(i)
        
for i in b:
    path1 = 'E:\\肖练\\有病人文件夹\\src\\粘液癌，单纯'
    path2 = 'E:\\肖练\\有病人文件夹\\src\\粘液癌，混合'
    try:
        shutil.copytree(os.path.join(path1, i), os.path.join(des_path2, i))
    except Exception:
        shutil.copytree(os.path.join(path2, i), os.path.join(des_path2, i))
    except Exception:
        print(i)



