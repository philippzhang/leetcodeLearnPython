import sys, types
import time

from leetcode.base import StringUtil


class Utilitys(object):

    @staticmethod
    def readMdFile(path):

        list = []
        with open(path + "/README.md") as f_name:
            flag = False
            i = 0
            for line in f_name:
                if line.startswith("# 测试用例"):
                    flag = True

                if flag and line.startswith("```"):
                    i += 1
                else:
                    if i == 1 and line != '' and not line.startswith('#'):
                        list.append(line.rstrip())
                if i == 2:
                    break
        flag = False
        ret = []
        listNew = []
        for i in range(len(list)):
            if not flag:
                flag = True
            if list[i] == '---':
                flag = False
                ret.append(listNew)
                listNew = []
            if flag:
                listNew.append(list[i])

        if len(listNew) > 0:
            ret.append(listNew)
        return ret

    @staticmethod
    def test(obj, path):
        testList = Utilitys.readMdFile(path)
        classList = testList[0]
        algorithmRemark = classList[0]

        print(algorithmRemark)
        print("-----------------------------")

        testFlag = True

        if len(classList) <= 1:
            print("未定义算法主类和方法!")
            print("-----------------------------")
            return False
        for i in range(1, len(classList)):
            funcStr = classList[i]
            if len(funcStr) == 0:
                continue
            funcRemark = ''

            index = funcStr.find("#")

            if index >= 0:
                funcRemark = funcStr[index + 1:]
                funcStr = funcStr[0:index]

            funcArr = funcStr.split(".")
            if len(funcArr) < 2:
                print("方法参数定义错误,应该是: className.funcName")
                return False

            algorithmClassName = funcArr[0]

            algorithmFuncName = funcArr[1].strip()
            if len(funcRemark) == 0:
                funcRemark = algorithmFuncName
            else:
                funcRemark = algorithmFuncName + " " + funcRemark

            print(funcRemark)
            print("-----------------------------")

            jCount = 1
            for j in range(1, len(testList)):
                dataList = testList[j]
                if len(dataList) > 0:
                    print("第{}组数据:".format(jCount))
                    resultFlag = Utilitys.testObj(obj, path, algorithmClassName, algorithmFuncName, dataList)
                    if not resultFlag:
                        testFlag = False

                    print("-----------------------------")
                    jCount += 1

        if not testFlag:
            print("存在错误!")
            print("-----------------------------")

        return testFlag

    @staticmethod
    def _get_mod(modulePath):
        try:
            aMod = sys.modules[modulePath]
            if not isinstance(aMod, types.ModuleType):
                raise KeyError
        except KeyError:
            # The last [''] is very important!
            aMod = __import__(modulePath, globals(), locals(), [''])
            sys.modules[modulePath] = aMod
        return aMod

    @staticmethod
    def _get_func(fullFuncName):
        """Retrieve a function object from a full dotted-package name."""
        # Parse out the path, module, and function
        lastDot = fullFuncName.rfind(u".")
        funcName = fullFuncName[lastDot + 1:]
        modPath = fullFuncName[:lastDot]
        aMod = Utilitys._get_mod(modPath)
        aFunc = getattr(aMod, funcName)
        # Assert that the function is a *callable* attribute.
        assert callable(aFunc), u"%s is not callable." % fullFuncName
        # Return a reference to the function itself,
        # not the results of the function.
        return aFunc

    @staticmethod
    def _get_Class(fullClassName, parentClass=None):
        """Load a module and retrieve a class (NOT an instance).
        If the parentClass is supplied, className must be of parentClass
        or a subclass of parentClass (or None is returned).
        """
        aClass = Utilitys._get_func(fullClassName)
        # Assert that the class is a subclass of parentClass.
        if parentClass is not None:
            if not issubclass(aClass, parentClass):
                raise TypeError(u"%s is not a subclass of %s" %
                                (fullClassName, parentClass))
        # Return a reference to the class itself, not an instantiated object.
        return aClass

    @staticmethod
    def applyFuc(obj, strFunc, arrArgs):
        objFunc = getattr(obj, strFunc)
        # code = objFunc.__code__
        # co_consts = code.co_consts[0]
        paramTypes = objFunc.bound_types
        rtype = objFunc.rtype
        for k in paramTypes:
            if k != "self":
                item_type = paramTypes[k]
                if item_type == list:
                    print("list")
                elif item_type == int:
                    print("int")
                # print(item_type)

        return objFunc(*arrArgs)

    @staticmethod
    def getObject(fullClassName):
        clazz = Utilitys._get_Class(fullClassName)
        return clazz()

    @staticmethod
    def testObj(obj, path, algorithmClassName, algorithmFuncName, dataList):
        testFlag = True
        pathArr = path.split("/")
        package = pathArr[-2] + "." + pathArr[-1] + "." + algorithmClassName + "." + algorithmClassName

        al = Utilitys.getObject(package)

        objFunc = getattr(al, algorithmFuncName)

        invokeFlag = True
        inputObjArr = []
        tempList = []
        paramTypes = objFunc.paramTypes
        rtype = objFunc.rtype

        print("输入:")
        paramLength = len(paramTypes) - 1
        try:
            obj.printInput(obj, dataList, paramLength)
        except Exception as e:
            print('printInput(Exception):\t', str(e))
            testFlag = False
            invokeFlag = False

        try:
            obj.inputBuild(obj, paramTypes, inputObjArr, dataList, tempList)
        except Exception as e:
            print('inputBuild(Exception):\t', str(e))
            testFlag = False
            invokeFlag = False

        start_time = time.time()  # 开始时间
        try:
            if invokeFlag:
                outputObj = objFunc(*inputObjArr)
        except Exception as e:
            print('invoke(Exception):\t', str(e))
            testFlag = False
        end_time = time.time()  # 结束时间
        if rtype is not None:
            # 打印输出
            try:
                obj.printOutput(obj, outputObj)
            except Exception as e:
                print('printOutput(Exception):\t', str(e))
                testFlag = False

        trueResultOutputList = []
        for k in range(paramLength, len(dataList)):
            trueResult = dataList[k]
            if len(trueResult) > 0:
                if trueResult.startswith("="):
                    trueResult = trueResult[1:]
                    if trueResult.startswith("="):
                        trueResultOutputList.append(trueResult)
                elif StringUtil.judgeINumber(trueResult):

                    # 验证输入参数

                    inputIndex = int(trueResult[1:2])
                    trueInputResult = trueResult[3:-1]
                    if len(trueInputResult) > 0 and 0 <= inputIndex < len(inputObjArr):
                        try:
                            resultFlag = obj.inputVerify(obj, inputObjArr, trueInputResult, outputObj, inputIndex, tempList)
                            if not resultFlag:
                                testFlag = False
                        except Exception as e:
                            print('inputVerify(Exception):\t', str(e))
                            testFlag = False
                            obj.printInputVerify(obj, trueInputResult, str(e), False)

        if len(trueResultOutputList) > 0:
            # 验证输出结果
            try:
                resultFlag = obj.outputVerify(obj, inputObjArr, trueResultOutputList, outputObj, dataList, tempList)
                if not resultFlag:
                    testFlag = False
            except Exception as e:
                print('outputVerify(Exception):\t', str(e))
                testFlag = False
                obj.printOutVerify(obj, trueResultOutputList, str(e), False)

        print("计算时长:%dms" % (end_time - start_time))  # 结束时间-开始时间

        return testFlag
