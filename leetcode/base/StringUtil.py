import re

@staticmethod
def judgeNumber(str):
    return re.match("-?[0-9]+.*[0-9]*")

@staticmethod
def judgeINumber(str):
    return re.match("^I[0-9]=.+$")