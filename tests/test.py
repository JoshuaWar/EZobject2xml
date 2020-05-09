from EZobject2xml import *

class theSubObject():
    def __init__(self,theInt):
        self.myInt = theInt
        self.myFloat = 3.456

class theObject():
    def __init__(self):
        self.myString = str()
        self.myInt = int()
        self.myFloat = float()
        self.myBool = bool()
        self.myTuple = tuple()
        self.mySubObject = theSubObject(0)
        self.myList = list()
        self.myList2 = list()
        self.myComplex = complex(0,0)
        self.mySet = set()
        self.myDictionnary = dict()
        self.myNone = None

#the object to save        
myObject1 = theObject()
myObject1.myString = 'this is the string'
myObject1.myInt = 15
myObject1.myFloat = 15.168
myObject1.myBool = True
myObject1.myTuple = (12,15,19)
myObject1.mySubObject = theSubObject(2)
myObject1.myList.append('string2')
myObject1.myList.append((325,12,15,17,18))
myObject1.myList.append(theSubObject(24))
myObject1.myList2.append('azerty')
myObject1.myList2.append('azerty2')
myObject1.myList2.append(theSubObject(4))
myObject1.myList.append(myObject1.myList2)
myObject1.myComplex = complex(10,45)
myObject1.mySet = {1,2,3,4,99,myObject1.myComplex}
myObject1.myDictionnary = {1:'a',2:'b',3:'z',4:myObject1.myList2}

#initializing the tool
myxmltool = xmltool()

#saving the object to xml
if myxmltool.saveObject2xml(myObject1,'test1.xml'):
    print("The object 1 is well saved to test1.xml")
else:
    print("The object 1 is NOT well saved to test1.xml")
    
#loading data to a new object
myObject2 = theObject()
myInitDataList = initDataList()
myInitDataList.addInitData(theSubObject,(0))
if myxmltool.loadObjectFromXml(myObject2,'test1.xml',myInitDataList):
    print("The object 2 is well loaded from test1.xml")
else:
    print("The object 2 is NOT well loaded from test1.xml")

#controling the data
if myxmltool.saveObject2xml(myObject2,'test2.xml'):
    print("The object 2 is well saved to test1.xml")
else:
    print("The object 2 is NOT well saved to test2.xml")

print("Please control if test1.xml is the same than text2.xml")

help(myxmltool)
