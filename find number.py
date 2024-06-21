# ++=== AmiraliZandi +~{&**
def find_num(mylist):
    myDic={}
    for item in mylist:
        try:
            myDic[item]+=1
        except KeyError:
            myDic[item]=1

    return myDic

nums = find_num([0,2,3,4,3,2,4,])
print (nums)
