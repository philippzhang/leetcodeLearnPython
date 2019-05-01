from leetcode.base.StringUtil import changeStr
from leetcode.base.structure.ListNode import ListNode


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
        dataBuffer.append(changeStr(obj))
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

    elif t == ListNode:
        dataBuffer.append("[")
        dataBuffer.append(obj.val)
        p = obj.next
        while p:
            dataBuffer.append(",")
            dataBuffer.append(p.val)
            p = p.next
        dataBuffer.append("]")
