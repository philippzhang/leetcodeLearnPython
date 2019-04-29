def buildList(data):
    if data is None or len(data) == 0 or data == "null" or data.find("[") < 0:
        return None
    # arr = []
    data = data[1:-2]
    arr = data.split(',')

    ret = []
    for i in range(len(arr)):
        d = arr[i].strip()
        if d.find("\"") < 0:
            ret.append(int(d))
        else:
            ret.append(d)
    return ret
