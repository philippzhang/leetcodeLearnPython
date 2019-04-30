from leetcode.base.structure.ListNode import ListNode


def buildList(data):
    if data is None or len(data) == 0 or data == "null" or data.find("[") < 0:
        return None
    # arr = []
    data = data[1:-1]
    arr = data.split(',')

    ret = []
    for i in range(len(arr)):
        d = arr[i].strip()
        if d.find("\"") < 0:
            ret.append(int(d))
        else:
            ret.append(d)
    return ret


def buildListNode(data):
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
