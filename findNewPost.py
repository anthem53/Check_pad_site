import datetime

def getTempNew():
    try:
        with open("tempNewResult.txt","r", encoding="utf-8") as file:
            a = file.readlines()

            return a
       
    except FileNotFoundError:
        print(">>>>  There is no password file.")
        raise FileNotFoundError


def getOldContent ():
    try:
        with open("result.txt","r", encoding="utf-8") as file:
            a = file.readlines()

            return a
       
    except FileNotFoundError:
        print(">>>>  There is no password file.")
        raise FileNotFoundError
    
def parseLine(s):
    temp = s.split(' ')
    num = int(temp[0])
    day = temp[-1].strip()
    title = ' '.join(temp[1:-1])

    day = day.replace("-","")
    date_format = '%Y%m%d'
    try:
        date_obj = datetime.datetime.strptime(day, date_format)
    except ValueError:
        print("Incorrect data format, should be YYYYMMDD")

    return (num, title, date_obj)

def parse_fileContent(fileContent : str):
    result = []
    fileContentStr = fileContent.split('\n')
    for s in fileContentStr:
        s = s.strip()
        if s != "":
            result.append(parseLine(s))

    return result

def find_newPost(old,cur):
    result = parse_fileContent(old)
    tempNew = parse_fileContent(cur)


    for t in result:
        if t in tempNew:
            tempNew.remove(t)
        else:
            pass
    return tempNew


if __name__ == "__main__":
    old = getOldContent()
    next = getTempNew()

    newItems =find_newPost("".join(old),"".join(next))
    print(newItems)