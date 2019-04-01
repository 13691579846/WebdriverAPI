
import configparser

class HandleIniFile(object):

     @staticmethod
     def handIniFile(iniPath):
         f = configparser.ConfigParser()
         f.read(iniPath)

         return f

     @staticmethod
     def getAllSection(f):
         sectionsName = f.sections()
         return sectionsName
     @staticmethod
     def getAllOption(f, sectionName):
         opentionName = f.options(sectionName)
         return opentionName

     @staticmethod
     def getValueOfValue(f, sectionName, optionName):
         value = f.get(sectionName, optionName)
         return value

if __name__=='__main__':
    f = HandleIniFile.handIniFile('WebElement.ini')
    sectionName = HandleIniFile.getAllSection(f)
    optionName = HandleIniFile.getAllOption(f, sectionName[0])
    value = HandleIniFile.getValueOfValue(f, sectionName[0], optionName[1])
    print(sectionName)
    print(optionName)
    print(value)