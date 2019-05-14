from queue import Queue

from leetcode.base.Stack import Stack
from leetcode.base.StringUtil import changeStr
from leetcode.base.structure.ListNode import ListNode
from leetcode.base.structure.TreeNode import TreeNode


def formatObj(obj):
    dataBuffer = []
    formatObjCore(obj, dataBuffer)
    return "".join([str(x) for x in dataBuffer])


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
            elif tt == int or tt == float:
                dataBuffer.append(item)
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == bool:
                if item:
                    dataBuffer.append("true")
                else:
                    dataBuffer.append("false")
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == str:
                dataBuffer.append(changeStr(item))
                if i < len(obj) - 1:
                    dataBuffer.append(',')
            elif tt == list:
                formatObjCore(item, dataBuffer)
                if i < len(obj) - 1:
                    dataBuffer.append(',')

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
    elif t == TreeNode:
        if t is None:
            dataBuffer.append("null")
            return
        dataBuffer.append("[")
        dataBuffer.append(_levelOrderFormat(obj))
        dataBuffer.append("]")


def _levelOrderFormat(root):
    current = root
    stringBuffer = []
    if current is not None:
        q = Queue()
        s = Stack()
        q.put(current)
        while not q.empty():
            current = q.get()
            if current is not None:
                s.push(current)
                if current.left is not None:
                    q.put(current.left)
                else:
                    q.put(None)
                if current.right is not None:
                    q.put(current.right)
                else:
                    q.put(None)
            else:
                s.push(None)
        while not s.isEmpty():
            if s.peek() is None:
                s.pop()
            else:
                break
        while not s.isEmpty():
            treeNode = s.pop()

            item = (str(treeNode.val) + ",") if treeNode is not None else "null,"
            stringBuffer.insert(0, item)

    s = "".join([str(x) for x in stringBuffer])
    if len(s) > 0:
        s = s[0:-1]
    return s
