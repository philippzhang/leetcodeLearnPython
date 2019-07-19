import math

from leetcode.base.Stack import Stack
from leetcode.base.structure.ListNode import ListNode
from leetcode.base.structure.Node import Node
from leetcode.base.structure.TreeNode import TreeNode
import json


def printObj(obj):
    _printObjCore(obj, None)


def _printObjCore(obj, ext):
    if obj is None:
        print("null")
        return
    t = type(obj)
    if t == int or t == float or t == bool:
        print(obj)
    elif t == str:
        print(obj)
    elif t == list:
        print("[", end='')
        for i in range(len(obj)):
            item = obj[i]
            tt = type(item)
            if item is None:
                print("null", end='')
                if i < len(obj) - 1:
                    print(',', end='')
            elif tt == int or tt == float:
                print(item, end='')
                if i < len(obj) - 1:
                    print(',', end='')
            elif tt == bool:
                if item:
                    print('true', end='')
                else:
                    print('false', end='')
                if i < len(obj) - 1:
                    print(',', end='')
            elif tt == str:
                print(item, end='')
                if i < len(obj) - 1:
                    print(',', end='')
            elif tt == list:
                if i == 0:
                    print()
                if i < len(obj) - 1:
                    _printObjCore(item, ",")
                else:
                    _printObjCore(item, None)
            elif tt == TreeNode:
                if i == 0:
                    print()
                _printObjCore(item, None)
                print()
            elif tt == Node:
                if i == 0:
                    print()
                _printObjCore(item, None)
                print()
            elif tt is not None:
                raise ValueError('未定义的List泛型，打印失败!')

        print("]", end='')
        if ext is not None:
            print(ext, end='')
        print()
    elif t == ListNode:
        print("[", end='')
        print(obj.val, end='')
        p = obj.next
        while p:
            print(",", end='')
            print(p.val, end='')
            p = p.next
        print("]", end='')
        if ext is not None:
            print(ext, end='')
        print("")
    elif t == TreeNode:
        _printTreeNode(obj)
    elif t == Node:
        _printMultiNode(obj)
    elif t == dict:
        j = json.dumps(obj, separators=(',', ':'))
        print(j)
    else:
        raise ValueError('未定义的类型，打印失败!')


def judgePrint(obj):
    if obj is None:
        return False
    t = type(obj)
    if t == ListNode or t ==TreeNode or t == Node:
        return True
    elif t == list:
        for i in range(len(obj)):
            item = obj[i]
            tt = type(item)
            if tt == list or tt == ListNode or tt == TreeNode or tt == Node:
                return True
    return False


def _printTreeNode(root):
    if root is None:
        return
    globalStack = Stack()
    globalStack.push(root)
    depth = _getDepth(root)
    nBlank = int(math.pow(2, depth + 1))
    ndot = nBlank * 2
    isRowEmpty = False
    for i in range(ndot):
        print('.', end='')
    print("")
    while not isRowEmpty:
        localStack = Stack()
        isRowEmpty = True
        for i in range(nBlank):
            print(' ', end='')
        while not globalStack.isEmpty():
            temp = globalStack.pop()
            if temp is not None:
                print(temp.val, end='')
                print(' ', end='')
                localStack.push(temp.left)
                localStack.push(temp.right)
                if temp.left is not None or temp.right is not None:
                    isRowEmpty = False
            else:
                print('# ', end='')
                localStack.push(None)
                localStack.push(None)
            for i in range(nBlank * 2 - 2):
                print(' ', end='')
        print("")
        nBlank //= 2
        while not localStack.isEmpty():
            globalStack.push(localStack.pop())
    for i in range(ndot):
        print('.', end='')
    print("")


def _getDepth(root):
    if root is not None:
        lDepth = _getDepth(root.left)
        rDepth = _getDepth(root.right);
        return (lDepth if lDepth > rDepth else rDepth) + 1
    return 0


def _printMultiNode(root):
    if root is None:
        return
    globalStack = Stack()
    globalStack.push(root)
    depth = _getMultiDepth(root)
    nBlank = int(math.pow(2, depth + 1))
    ndot = nBlank * 2
    isRowEmpty = False
    for i in range(ndot):
        print('.', end='')
    print("")
    while not isRowEmpty:
        localStack = Stack()
        isRowEmpty = True
        for i in range(nBlank):
            print(' ', end='')
        while not globalStack.isEmpty():
            temp = globalStack.pop()
            if temp is not None:
                print(temp.val, end='')
                print(' ', end='')
                if temp.children is not None:
                    for child in temp.children:
                        localStack.push(child)
                        isRowEmpty = False

            else:
                print('# ', end='')
                localStack.push(None)
                localStack.push(None)
            for i in range(nBlank * 2 - 2):
                print(' ', end='')
        print("")
        nBlank //= 2
        while not localStack.isEmpty():
            globalStack.push(localStack.pop())
    for i in range(ndot):
        print('.', end='')
    print("")


def _getMultiDepth(root):
    if root is None:
        return 0
    if not root.children:
        return 1
    return max(_getMultiDepth(child) + 1 for child in root.children)
