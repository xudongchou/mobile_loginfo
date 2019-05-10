'''
LOG_LEVEL 日志级别设置
优先级是下面的字符，顺序是从低到高：
V — 明细 verbose(最低优先级)
D — 调试 debug
I — 信息 info
W — 警告 warn
E — 错误 error
F — 严重错误 fatal
S — 无记载 silent
example:
LOG_LEVEL='*E:' 展示级别大于等于E级别的日志 即 error  fatal silent 级别的日志

FIND_FIXAPP 获取指定app的日志
格式如下 '|find ""'
双引号里面为app所在的包名
可以使用aapt命令获取  aapt dump badging appname  例如 合伙人app包名为格式如下 com.creditease.vip_xzbx
'''


LOG_LEVEL='' #格式 '*E:' 不设置程序默认为info级别日志
FIND_FIXAPP=''  #格式如下 '|find "com.creditease.vip_xzbx"'
REDIRECT='>'

