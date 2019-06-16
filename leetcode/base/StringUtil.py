import re


def judgeNumber(temp):
    value = re.compile(r'^[-+]?[0-9]+\.*[0-9]*$')
    return value.match(temp)


def judgeINumber(temp):
    value = re.compile(r'^I[0-9]=.+$')
    return value.match(temp)


def changeStr(temp):
    if temp is None or len(temp) == 0 or temp == "null":
        return "null"
    if temp.startswith("\""):
        temp = temp[1:]
    if temp.endswith("\""):
        temp = temp[0:-1]

    return temp


def isEqual(a, b):
    return abs(a - b) < 0.000001


def sortJson(jsonNode):
    if jsonNode is None:
        return
    elif isinstance(jsonNode, list):
        for item in jsonNode:
            sortJson(item)
    elif isinstance(jsonNode, dict):
        newJsonNode = sorted(jsonNode)
        for key in newJsonNode:
            v = jsonNode[key]
            del jsonNode[key]
            sortJson(v)
            jsonNode[key] = v
    else:
        return
