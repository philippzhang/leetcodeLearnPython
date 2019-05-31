import os
import time

from leetcode.base.Format import formatObj
from leetcode.base.NoImplException import NoImplException
from leetcode.base.Utilitys import getAllLCFileName, funcInvoke


def main():
    path = os.getcwd()
    packageList = getAllLCFileName(path)
    successCount = 0
    failCount = 0
    noCount = 0
    failList = []
    noList = []
    start_time = time.time()  # 开始时间
    for i in range(len(packageList)):
        packageName = packageList[i]
        try:
            flag = funcInvoke("leetcode." + packageName + ".Main.Main", path + "/" + packageName)
            if flag:
                successCount += 1
            else:
                failCount += 1
                failList.append(packageName[2:])
        except NoImplException as e:
            noCount += 1
            noList.append(packageName[2:])

    end_time = time.time()  # 结束时间
    print("总题数:" + str(len(packageList)) + ", 正确数:" + str(successCount) + ", 错误数:" + str(failCount) + ", 未做数:" + str(failCount))
    if len(failList) > 0:
        print("错误题目: " + formatObj(failList))
    if len(noList) > 0:
        print("未做题目: " + formatObj(noList))
    print("计算时长:%dms" % (end_time - start_time))  # 结束时间-开始时间


if __name__ == "__main__":
    main()
