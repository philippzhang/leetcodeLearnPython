from leetcode.base import Build, StringUtil
from leetcode.base.Build import buildList, buildListNode, buildTreeNode, buildMultiTree
from leetcode.base.Format import formatObj
from leetcode.base.PrintObj import printObj
from leetcode.base.StringUtil import changeStr
from leetcode.base.Utilitys import funcListTest


class CallBack(object):
    def __init__(self):
        pass

    def printInput(self, dataList, paramLength):
        """
        打印输入参数方法
        :param dataList:    #读入数据列表
        :param paramLength: #算法方法中参数个数（不含self)
        :return:
        """
        if len(dataList) == 0:
            return
        for i in range(paramLength):
            printObj(dataList[i])

    def inputBuild(self, paramTypes, inputObjArr, dataList, tempList):
        """
        入参构建方法
        :param paramTypes:   算法方法中参数列表
        :param inputObjArr:  调用算法的参数值列表
        :param dataList:     读入数据列表
        :param tempList:     临时缓存，用于数据传递
        :return:
        """
        i = 0
        for k in paramTypes:
            data = dataList[i]
            item_type = k
            if item_type == 'List':
                inputObjArr.append(buildList(data))
            elif item_type == 'int':
                inputObjArr.append(int(data))
            elif item_type == 'float':
                inputObjArr.append(float(data))
            elif item_type == 'bool':
                inputObjArr.append(bool(data))
            elif item_type == 'str':
                inputObjArr.append(changeStr(data))
            elif item_type == 'ListNode':
                inputObjArr.append(buildListNode(data))
            elif item_type == 'TreeNode':
                inputObjArr.append(buildTreeNode(data))
            elif item_type == 'Node':
                inputObjArr.append(buildMultiTree(data))
            else:
                raise ValueError('未定义的类型，构建失败!')
            i += 1

    def printOutput(self, outputObj):
        """
        打印输出参数方法
        :param outputObj: #算法输出值
        :return:
        """
        print("格式输出:")
        printObj(outputObj)

    def outputVerify(self, inputObjArr, trueResultList, outputObj, dataList, tempList):
        """
        输出参数验证方法
        :param inputObjArr:     #调用算法的参数值列表
        :param trueResultList:  #正确结果集，如果存在多个正确值，任意结果均正确
        :param outputObj:       #算法输出值
        :param dataList:        #读入数据列表
        :param tempList:        #临时缓存，用于数据传递
        :return:
        """
        resultFlag = False

        testResult = formatObj(outputObj)

        for i in range(len(trueResultList)):
            # 答案
            trueResult = trueResultList[i].strip()
            if trueResult == "null" and outputObj is None:
                self.printOutVerify(trueResultList, None, True)
                return True
            try:
                if outputObj is not None and type(outputObj) == list:
                    disOrder = False
                    j = len(inputObjArr)
                    while j < len(dataList):
                        if dataList[j] == "$disorder":  # List 无序标志
                            disOrder = True
                            break
                        j += 1
                    if disOrder:
                        trueResultsList = Build.buildList(trueResult)
                        resultFlag = sorted(outputObj) == sorted(trueResultsList)
                    else:
                        resultFlag = trueResult == testResult
                elif outputObj is not None and type(outputObj) == float:
                    testResultFloat = outputObj
                    trueResultFloat = float(trueResult)
                    resultFlag = StringUtil.isEqual(testResultFloat, trueResultFloat)
                else:
                    resultFlag = trueResult == testResult
                if resultFlag:
                    self.printOutVerify(trueResultList, testResult, resultFlag)
                    return True
            except Exception as e:
                print('outputVerify(Exception):\t', str(e))
                self.printOutVerify(trueResultList, str(e), False)
                return False

        self.printOutVerify(trueResultList, testResult, resultFlag)
        return resultFlag

    def printOutVerify(self, trueResultList, testResult, resultFlag):
        """
        打印输出校验结果
        :param trueResultList: #正确结果集，如果存在多个正确值，任意结果均正确
        :param testResult:     #算法运行结果
        :param resultFlag:     #验证结果
        :return:
        """
        print("输出结果:")
        print(testResult)
        print("预期结果" + (" (以下任意结果均正确) " if len(trueResultList) > 1 else "") + ":")

        for i in range(len(trueResultList)):
            print(trueResultList[i])
        print("验证结果: ", end='')
        if resultFlag:
            print("正确")
        else:
            print("错误")

    def inputVerify(self, inputObjArr, trueInputResult, outputObj, inputIndex, tempList):
        """
        输入参数验证方法
        :param inputObjArr:      #调用算法的参数值列表
        :param trueInputResult:  #正确输入结果
        :param outputObj:        #算法输出值
        :param inputIndex:       #需要验证的入参参数序号
        :param tempList:         #临时缓存，用于数据传递
        :return:
        """
        try:
            inputObj = inputObjArr[inputIndex]
            testInputResult = formatObj(inputObj);
            resultFlag = trueInputResult == testInputResult
            self.printInputVerify(trueInputResult, testInputResult, resultFlag)
            return resultFlag;
        except Exception as e:
            print('inputVerify(Exception):\t', str(e))
            self.printInputVerify(trueInputResult, str(e), False)
            return False

    def printInputVerify(self, trueInputResult, testInputResult, resultFlag):
        """
        打印输入校验结果
        :param trueInputResult:  #正确结果
        :param testInputResult:  #输入结果
        :param resultFlag:       #验证结果
        :return:
        """
        print("入参输出:")
        print(testInputResult)
        print("入参预期结果:")
        print(trueInputResult)
        print("入参验证结果: ", end='')
        if resultFlag:
            print("正确")
        else:
            print("错误")

    def funcListTest(self, funcList, paramList, path):
        """
        :type funcList: List  #方法组
        :type paramList: List #参数组
        :rtype: List
        """
        retList = funcListTest(funcList, paramList, path)
        return retList
