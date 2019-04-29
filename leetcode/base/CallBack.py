from leetcode.base.Build import buildList
from leetcode.base.Format import formatObj
from leetcode.base.PrintObj import printObj
from leetcode.base.Typeassert import typeassert


class CallBack(object):
    def __init__(self):
        pass

    def printInput(self, dataList, paramLength):
        if len(dataList) == 0:
            return
        for i in range(paramLength):
            printObj(dataList[i])

    def inputBuild(self, paramTypes, inputObjArr, dataList, tempList):
        i = 0
        for k in paramTypes:
            if k != "self":
                data = dataList[i]
                item_type = paramTypes[k]
                if item_type == list:
                    inputObjArr.append(buildList(data))
                elif item_type == int:
                    inputObjArr.append(int(data))
                i += 1

    def printOutput(self, outputObj):
        print("格式输出:")
        printObj(outputObj)

    def outputVerify(self, inputObjArr, trueResultList, outputObj, dataList, tempList):

        resultFlag = False;

        testResult = formatObj(outputObj)

        for i in range(len(trueResultList)):
            trueResult = trueResultList[i]
            if trueResult == "null" and outputObj is None:
                self.printOutVerify(self, trueResultList, None, True)
                return True
            try:
                resultFlag = trueResult == testResult
                if resultFlag:
                    self.printOutVerify(self, trueResultList, testResult, resultFlag)
                    return True
            except Exception as e:
                print('outputVerify(Exception):\t', str(e))
                self.printOutVerify(self, trueResultList, str(e), False)
                return False

        self.printOutVerify(self, trueResultList, testResult, resultFlag)
        return resultFlag;

    def printOutVerify(self, trueResultList, testResult, resultFlag):
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
        try:
            inputObj = inputObjArr[inputIndex]
            testInputResult = formatObj(inputObj);
            resultFlag = trueInputResult == testInputResult
            self.printInputVerify(self, trueInputResult, testInputResult, resultFlag)
            return resultFlag;
        except Exception as e:
            print('inputVerify(Exception):\t', str(e))
            self.printInputVerify(self, trueInputResult, str(e), False)
            return False

    def printInputVerify(self, trueInputResult, testInputResult, resultFlag):
        print("入参输出:")
        print(testInputResult)
        print("入参预期结果:")
        print(trueInputResult)
        print("入参验证结果: ", end='')
        if resultFlag:
            print("正确")
        else:
            print("错误")

    @typeassert(object, list, list, rtype=list)
    def funcListTest(self, funcList, paramList):
        pass
