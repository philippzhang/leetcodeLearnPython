import sys
import time
import types
import os

from leetcode.base.Build import buildList, buildListNode, buildTreeNode
from leetcode.base.Format import formatObj
from leetcode.base.StringUtil import judgeINumber, changeStr


def test(obj, path):
    testList = _readMdFile(path)
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
                resultFlag = testObj(obj, path, algorithmClassName, algorithmFuncName, dataList)
                if not resultFlag:
                    testFlag = False

                print("-----------------------------")
                jCount += 1

    if not testFlag:
        print("存在错误!")
        print("-----------------------------")

    return testFlag


def testObj(obj, path, algorithmClassName, algorithmFuncName, dataList):
    testFlag = True
    pathArr = path.split("/")
    package = pathArr[-2] + "." + pathArr[-1] + "." + algorithmClassName + "." + algorithmClassName

    al = getObject(package)

    objFunc = getattr(al, algorithmFuncName)
    code = objFunc.__code__
    co_consts = code.co_consts[0]
    if co_consts is None:
        print("未定义注释!")
        return False
    co_consts = co_consts.strip()
    co_arr = co_consts.split('\n')

    invokeFlag = True
    inputObjArr = []
    tempList = []
    # if not hasattr(objFunc, "paramTypes") or not hasattr(objFunc, "rtype"):
    #     print("未使用@typeassert定义方法的参数类型!")
    #     return False
    #
    # paramTypes = objFunc.paramTypes
    # rtype = objFunc.rtype

    print("输入:")
    paramLength = len(co_arr) - 1

    paramTypes = []
    rtype = None
    for j in range(len(co_arr)):
        co = co_arr[j].strip()
        if co.startswith('@') or co.startswith('#') or len(co) == 0:
            continue
        co_type = co.split(':')[-1].strip()
        k = co_type.find('#')
        co_type = co_type[0:k] if k >= 0 else co_type
        k = co_type.find('[')
        co_type = co_type[0:k] if k >= 0 else co_type
        co_type = co_type.strip()
        if co.startswith(':type') or co.startswith(':param'):
            paramTypes.append(co_type)
        elif co.startswith(':rtype') or co.startswith(':return'):
            rtype = co_type

    try:
        obj.printInput(dataList, paramLength)
    except Exception as e:
        print('printInput(Exception):\t', str(e))
        testFlag = False
        invokeFlag = False

    try:
        obj.inputBuild(paramTypes, inputObjArr, dataList, tempList)
    except Exception as e:
        print('inputBuild(Exception):\t', str(e))
        testFlag = False
        invokeFlag = False

    if algorithmFuncName == 'funcListTest':
        inputObjArr.append(path)

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
            obj.printOutput(outputObj)
        except Exception as e:
            print('printOutput(Exception):\t', str(e))
            testFlag = False

    trueResultOutputList = []
    for k in range(paramLength, len(dataList)):
        trueResult = dataList[k]
        if len(trueResult) > 0:
            if trueResult.startswith("="):
                trueResult = trueResult[1:]
                if len(trueResult):
                    trueResultOutputList.append(trueResult)
            elif judgeINumber(trueResult):

                # 验证输入参数

                inputIndex = int(trueResult[1:2])
                trueInputResult = trueResult[3:-1]
                if len(trueInputResult) > 0 and 0 <= inputIndex < len(inputObjArr):
                    try:
                        resultFlag = obj.inputVerify(inputObjArr, trueInputResult, outputObj, inputIndex, tempList)
                        if not resultFlag:
                            testFlag = False
                    except Exception as e:
                        print('inputVerify(Exception):\t', str(e))
                        testFlag = False
                        obj.printInputVerify(trueInputResult, str(e), False)

    if testFlag and len(trueResultOutputList) > 0:
        # 验证输出结果
        try:
            resultFlag = obj.outputVerify(inputObjArr, trueResultOutputList, outputObj, dataList, tempList)
            if not resultFlag:
                testFlag = False
        except Exception as e:
            print('outputVerify(Exception):\t', str(e))
            testFlag = False
            obj.printOutVerify(trueResultOutputList, str(e), False)

    print("计算时长:%dms" % (end_time - start_time))  # 结束时间-开始时间

    return testFlag


def getAllLCFileName(path):
    ret = []
    for i in os.listdir(path):
        temp_dir = os.path.join(path, i)
        if os.path.isdir(temp_dir):
            packageName = temp_dir.split("/")[-1]
            if packageName.startswith("lc"):
                ret.append(packageName)
    ret.sort()
    return ret


def funcInvoke(className, path):
    al = getObject(className)
    flag = test(al, path)
    return flag


def funcListTest(funcList, paramList, path):
    retList = []
    packageName = path.split("/")[-1]
    for i in range(len(funcList)):
        funcName = funcList[i]
        params = paramList[i]
        if i == 0:
            # 第一个值是构造方法
            className = "leetcode." + packageName + "." + funcName + "." + funcName

            clazz = _get_Class(className)
            vClazz = clazz.__dict__
            initFunc = vClazz.get("__init__")
            code = initFunc.__code__
            co_consts = code.co_consts[0]
            co_consts = co_consts.strip()
            if co_consts is None:
                print("未定义注释!")
                return False
            co_arr = co_consts.split('\n')

            inputObjArr = []
            jj = 0
            for j in range(len(co_arr)):
                co = co_arr[j].strip()
                if co.startswith('@') or co.startswith('#') or len(co) == 0:
                    continue
                co_type = co.split(':')[-1].strip()
                k = co_type.find('#')
                co_type = co_type[0:k] if k >= 0 else co_type
                k = co_type.find('[')
                co_type = co_type[0:k] if k >= 0 else co_type
                co_type = co_type.strip()
                if co.startswith(':type') or co.startswith(':param'):
                    param = params[jj]
                    if co_type == 'int':
                        inputObjArr.append(int(param))
                    elif co_type == 'str':
                        inputObjArr.append(changeStr(param))
                    elif co_type == 'list':
                        inputObjArr.append(buildList(formatObj(param)))
                    elif co_type == 'ListNode':
                        inputObjArr.append(buildListNode(formatObj(param)))
                    elif co_type == 'TreeNode':
                        inputObjArr.append(buildTreeNode(formatObj(param)))
                jj += 1

            al = clazz(*inputObjArr)
            retList.append(None)
        else:
            objFunc = getattr(al, funcName)
            inputObjArr = []
            code = objFunc.__code__
            co_consts = code.co_consts[0]
            co_consts = co_consts.strip()
            if co_consts is None:
                print("未定义注释!")
                return False
            co_arr = co_consts.split('\n')
            jj = 0
            for j in range(len(co_arr)):
                co = co_arr[j].strip()
                if co.startswith('@') or co.startswith('#') or len(co) == 0:
                    continue

                co_type = co.split(':')[-1].strip()
                k = co_type.find('#')
                co_type = co_type[0:k] if k >= 0 else co_type
                k = co_type.find('[')
                co_type = co_type[0:k] if k >= 0 else co_type
                co_type = co_type.strip()
                if co.startswith(':type') or co.startswith(':param'):
                    param = params[jj]
                    if co_type == 'int':
                        inputObjArr.append(int(param))
                    elif co_type == 'str':
                        inputObjArr.append(changeStr(param))
                    elif co_type == 'list':
                        inputObjArr.append(buildList(formatObj(param)))
                    elif co_type == 'ListNode':
                        inputObjArr.append(buildListNode(formatObj(param)))
                    elif co_type == 'TreeNode':
                        inputObjArr.append(buildTreeNode(formatObj(param)))
                jj += 1

            outputObj = objFunc(*inputObjArr)
            retList.append(outputObj)

    return retList


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


def _get_func(fullFuncName):
    """Retrieve a function object from a full dotted-package name."""
    # Parse out the path, module, and function
    lastDot = fullFuncName.rfind(u".")
    funcName = fullFuncName[lastDot + 1:]
    modPath = fullFuncName[:lastDot]
    aMod = _get_mod(modPath)
    aFunc = getattr(aMod, funcName)
    # Assert that the function is a *callable* attribute.
    assert callable(aFunc), u"%s is not callable." % fullFuncName
    # Return a reference to the function itself,
    # not the results of the function.
    return aFunc


def _get_Class(fullClassName, parentClass=None):
    """Load a module and retrieve a class (NOT an instance).
    If the parentClass is supplied, className must be of parentClass
    or a subclass of parentClass (or None is returned).
    """
    aClass = _get_func(fullClassName)
    # Assert that the class is a subclass of parentClass.
    if parentClass is not None:
        if not issubclass(aClass, parentClass):
            raise TypeError(u"%s is not a subclass of %s" %
                            (fullClassName, parentClass))
    # Return a reference to the class itself, not an instantiated object.
    return aClass


def applyFuc(obj, strFunc, arrArgs):
    objFunc = getattr(obj, strFunc)
    # code = objFunc.__code__
    # co_consts = code.co_consts[0]

    return objFunc(*arrArgs)


def getObject(fullClassName):
    clazz = _get_Class(fullClassName)
    return clazz()


def _readMdFile(path):
    listTemp = []
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
                    listTemp.append(line.rstrip())
            if i == 2:
                break
    flag = False
    ret = []
    listNew = []
    for i in range(len(listTemp)):
        if not flag:
            flag = True
        if listTemp[i] == '---':
            flag = False
            ret.append(listNew)
            listNew = []
        if flag:
            listNew.append(listTemp[i])

    if len(listNew) > 0:
        ret.append(listNew)
    return ret
