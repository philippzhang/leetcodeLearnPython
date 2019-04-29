from leetcode.base.StringUtil import chageStr


def formatObj(obj):
    dataBuffer = []
    formatObjCore(obj, dataBuffer)
    str1 = ""
    return str1.join([str(x) for x in dataBuffer])


def formatObjCore(obj, dataBuffer):
    if obj is None:
        dataBuffer.append("null")
        return
    t = type(obj)
    if t == int or t == float or t == bool:
        dataBuffer.append(obj)
    elif t == str:
        dataBuffer.append(chageStr(obj))
    elif t == list:
        dataBuffer.append("[")
        for i in range(len(obj)):
            item = obj[i]
            tt = type(item)
            if item is None:
                dataBuffer.append("null")
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == int:
                dataBuffer.append(item)
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == str:
                dataBuffer.append(item)
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == list:
                formatObjCore(item, dataBuffer)

        dataBuffer.append("]")
