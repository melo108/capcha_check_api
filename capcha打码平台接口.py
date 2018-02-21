import json, time, requests
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


######################################################################

class YDMHttp:

    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = requests.post(self.apiurl,data=data)
        response_data = json.loads(response.text)
        if response_data['ret'] == 0:
            print('获取积分',response_data['ret'])
            return response_data['balance']
        else:
            return None


    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = requests.post(self.apiurl,data=data)
        response_data = json.loads(response.text)
        if response_data['ret'] == 0:
            print('登陆成功',response_data['uid'])
            return response_data['uid']
        else:
            return None


    def decode(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        files = {'file':open(filename,'rb')}
        response = requests.post(self.apiurl,files=files,data=data)
        response_data = json.loads(response.text)
        if response_data['ret'] == 0:
            print('识别成功',response_data['text'])
            return response_data['text']

######################################################################

# 用户名
username = 'UserName'
# 密码
password = 'pwd'
# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appid = 1
# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
appkey = '22cc5376925e9387a23cf797cb9ba745'
# 图片文件
filename = 'getimage.jpg'

# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype = 3004
# 超时时间，秒
timeout = 60


if __name__ == '__main__':

    if (username == 'username'):
        print('输入用户名密码')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)
        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)
        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        text = yundama.decode(filename, codetype, timeout)
        print('text: %s' % (text, ))

    # ######################################################################