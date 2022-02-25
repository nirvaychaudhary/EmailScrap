import re
import json

def Emailtype(strs):
    
    if len(strs.split('@')[0]) > 8:
        return 'Human'
    else:
        return 'Non-Human' 

fileToRead = 'websiteData.txt'
fileToWrite = 'extracted_data.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)

if listEmail:
    temp_json = {}
    uniqEmail = list(set(listEmail))
    for item in uniqEmail:
        temp2_json = {}
        temp2_json['occurence']=listEmail.count(item)
        temp2_json['EmailType']=Emailtype(item)
        temp_json[item] = temp2_json
    print("temp_json:::", temp_json)
    print(uniqEmail,"emails are collected!")
    print('list email::: ',listEmail)
    with open('result.json', 'w') as outfile:
        json.dump(temp_json, outfile)
else:
    print("No email found.")

  
  