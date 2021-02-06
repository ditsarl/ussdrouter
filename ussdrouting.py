# coding: utf-8

def goBack(str, keyword='00'):

  strArray = str.split('*')
  newStrArray = []

  for i in range(len(strArray)):
    
    if strArray[i] == keyword:
        newStrArray = newStrArray[slice(0, -1)]
    else:
        newStrArray.append(strArray[i])

  return "*".join(newStrArray)


def goToHome(str, keyword='0'):

  strArray = str.split('*')
  newStr = str

  for i in reversed(range(len(strArray))):
    if strArray[i] == keyword:
      newStr = "*".join(strArray[i+1:])
      break

  return newStr

def ussdRouter(str, goToHomeKeyword='0', goBackKeyword='00'):
  return goBack(goToHome(str, goToHomeKeyword), goBackKeyword)
