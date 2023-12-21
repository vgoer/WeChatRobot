import random
import requests

from chinese_calendar import is_workday
from robot import Robot

class MaRen:
    @staticmethod
    def ma(robot: Robot) -> None:

        receivers = robot.config.REPORT_REMINDERS
        if not receivers:
            receivers = ["filehelper"]
        #  骂人业务
        for receiver in receivers:

            arr = ['大傻春', '大傻柱', '白傻子']

            robot.sendTextMsg(random.choice(arr), receiver)



    @staticmethod
    def fxxkyou(robot: Robot) -> None:
        receivers = robot.config.REPORT_REMINDERS
        if not receivers:
            receivers = ["filehelper"]
        #  骂人业务
        for receiver in receivers:

            # 骂人等级
            level = [ 'max', 'min']

            url = "https://my.wulvxinchen.cn/fxxkyou/api.php?level=" +  level[0]

            resp = requests.get(url)

            if resp.status_code == 200:
                robot.sendTextMsg(resp.text, receiver)

