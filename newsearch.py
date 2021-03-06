import requests
import json

class University():
        def __init__(self,schoolID):
            self.Uni = schoolID
        
        def searching(self, name):
            parts = name.split(" ")
            self.found = None
            if(len(parts)==1):
                one = parts[0]
                namesF = self.lookLast(one)
                namesL = self.lookFirst(one)
                namesF.extend(namesL)
                if(len(namesF)==0):
                    return "error"
                else:
                    return namesF
            firstN = parts[0]
            lastN = parts[1]

            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=" + lastN + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            self.found = self.lookFull(name)
            if("Error" in str(self.found)):
                return "Error not found!"
            else:
                return self.temp_list[self.found]

        
        def lookFull(self, name):
            for i in range(0, len(self.temp_list)):
                print(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'])
                if (name == (self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'])):
                    return i
            return False 

        def lookLast(self, name):
            firstNames = []
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=" + name + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            for i in range(0, len(self.temp_list)):
                if(name == (self.temp_list[i]['tLname'])):
                    firstNames.append(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'] +": " + self.temp_list[i]['tDept'])
            return firstNames

        def lookFirst(self, name):
            lastNames = []
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherfirstname_sort_s+asc&query=" + name + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            for i in range(0,len(self.temp_list)):
                if(name == (self.temp_list[i]['tFname'])):
                    lastNames.append(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'] + ": " + self.temp_list[i]['tDept'])
            return lastNames
