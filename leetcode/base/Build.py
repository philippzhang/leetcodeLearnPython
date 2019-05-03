from queue import Queue

from leetcode.base.StringUtil import changeStr, judgeNumber
from leetcode.base.structure.ListNode import ListNode
from leetcode.base.structure.TreeNode import TreeNode


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
    if data == '[]':
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
    if data is None or len(data) == 0 or data == "null" or data.find("[") < 0:
        return None
    if data == '[]':
        return None
    data = data[1:-1]
    arr = data.split(',')
    root = TreeNode(arr[0])
    q = Queue()
    q.put(root)
    i = 1
    while not q.empty() and i < len(arr):
        node = q.get()
        if i < len(arr) and arr[i] is not None and arr[i] != 'null':
            node.left = TreeNode(int(arr[i]))
            q.put(node.left)
        if i+1 < len(arr) and arr[i+1] is not None and arr[i+1] != 'null':
            node.right = TreeNode(int(arr[i+1]))
            q.put(node.right)
        i += 2
    return root
