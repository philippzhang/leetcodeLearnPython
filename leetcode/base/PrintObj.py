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
        pass

def _getDepth(root):
    pass

