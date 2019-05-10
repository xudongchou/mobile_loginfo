"""
@project:code
@author:zhouxudong
@file:mobile_info.py
@ide:PyCharm
@time:2019/5/9 10:29
@month:五月
"""
import  subprocess
import os
from datetime import datetime
import settings
def get_loginfo():
    cmd='adb devices'
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    sout,serr=res.communicate()
    resout=sout.decode().split()
    device=resout[-2]
    print(device)
    if device:
        print("手机设备连接成功")
    else:
        print("手机设备连接失败，请检查手机是否连接或者重新安装驱动")
    now_time=datetime.now().strftime('%Y%m%d%H%M%S')
    print(now_time)
    if not settings.LOG_LEVEL:
       LOG_LEVEL='*I:'
    if settings.FIND_FIXAPP:
        find_fixapp=settings.FIND_FIXAPP.split('"')[1]
        logcat = 'adb logcat ' + settings.LOG_LEVEL +settings.FIND_FIXAPP+ settings.REDIRECT + device + '_' +find_fixapp+ '_'+now_time + '.txt'
    else:
        logcat='adb logcat '+settings.LOG_LEVEL+settings.REDIRECT +device+'_'+now_time+'.txt'
    os.system(logcat)
if __name__=='__main__':
    get_loginfo()