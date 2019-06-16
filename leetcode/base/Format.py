from queue import Queue

from leetcode.base.Stack import Stack
from leetcode.base.StringUtil import changeStr
from leetcode.base.structure.ListNode import ListNode
from leetcode.base.structure.Node import Node
from leetcode.base.structure.TreeNode import TreeNode
import json
import hashlib


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
        dataBuffer.append(_levelOrderTreeNodeFormat(obj))
        dataBuffer.append("]")
    elif t == Node:
        if t is None:
            dataBuffer.append("null")
            return
        dataBuffer.append(_levelOrderNodeFormat(obj))
    else:
        raise ValueError('未定义的类型，转换失败!')


def _levelOrderTreeNodeFormat(root):
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


def _levelOrderNodeFormat(root):
    jsonObject = _node2JsonObject(root)
    _nodeAddId(jsonObject)
    _sortJson(jsonObject)
    return json.dumps(jsonObject, separators=(',', ':'))


def _node2JsonObject(node):
    jsonObject = {}
    children = []
    if node.children is not None:
        for child in node.children:
            if child is not None:
                children.append(_node2JsonObject(child))
    jsonObject["children"] = children
    jsonObject["val"] = node.val
    return jsonObject


def _nodeAddId(root):
    if root is not None:
        q = Queue()
        q.put(root)
        index = 1
        while not q.empty():
            current = q.get()
            if current is not None:
                current["$id"] = str(index)
                index = index + 1
                if current["children"] is not None:
                    for child in current["children"]:
                        q.put(child)


def _sortJson(jsonNode):
    if jsonNode is None:
        return
    elif isinstance(jsonNode, list):
        for item in jsonNode:
            _sortJson(item)
    elif isinstance(jsonNode, dict):
        newJsonNode = sorted(jsonNode)
        for key in newJsonNode:
            v = jsonNode[key]
            del jsonNode[key]
            _sortJson(v)
            jsonNode[key] = v
    else:
        return
