from leetcode.base.StringUtil import changeStr, judgeNumber
from leetcode.base.structure.ListNode import ListNode


def buildList(data):
    """
    构建list
    :param data:
    :return:
    """

    if data is None or len(data) == 0 or data == "null" or data.find("[") < 0:
        return None
    if data == '[]':
        return []
    data = data.strip()
    data = data[1:-1]
    if data.find('[') >= 0:
        arr = []
        dataBuffer = []
        count = 0
        for i in range(len(data)):
            c = data[i]
            dataBuffer.append(c)
            if c == '[':
                count += 1
            elif c == ']':
                count -= 1
            elif c == ',' or count == 0:
                del dataBuffer[len(dataBuffer) - 1]
                arr.append("".join([str(x) for x in dataBuffer]))
                dataBuffer = []
    else:
        arr = data.split(',')

    ret = []
    for i in range(len(arr)):
        d = arr[i].strip()
        if d.find('[') >= 0:
            ret.append(buildList(d))
        elif judgeNumber(d):
            ret.append(int(d))
        else:
            ret.append(changeStr(d))
    return ret


def buildListNode(data):
    """
    构建链表
    :param data:
    :return:
    """
    if data is None or len(data) == 0 or data == "null" or data.find("[") < 0:
        return None
    data = data[1:-1]
    arr = data.split(',')
    ret = []
    for i in range(len(arr)):
        d = arr[i].strip()
        if d.find("\"") < 0:
            ret.append(ListNode(int(d)))
        else:
            ret.append(ListNode(d))
        if i > 0:
            ret[i - 1].next = ret[i]

    return ret[0]


def buildTreeNode(data):
    """
    构建树
    :param data:
    :return:
    """
    pass
