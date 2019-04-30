def judgeNumber(temp):
    return temp.match("-?[0-9]+.*[0-9]*")


def judgeINumber(temp):
    return temp.match("^I[0-9]=.+$")


def chageStr(temp):
    if temp is None or len(temp) == 0 or temp == "null":
        return "null"
    if temp.startswith("\""):
        temp = temp[1:]
    if temp.endswith("\""):
        temp = temp[0:-1]

    return temp
