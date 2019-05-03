import math

from leetcode.base.Stack import Stack
from leetcode.base.structure.ListNode import ListNode
from leetcode.base.structure.TreeNode import TreeNode


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
            elif tt == int:
                print(item, end='')
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
        printTreeNode(obj)


def printTreeNode(root):
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
