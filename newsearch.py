import requests
import json
import time
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
class University():
        def __init__(self,schoolID):
            self.Uni = schoolID
        
        def searching(self, name):
            parts = name.split(" ")
            self.found = None
            if(len(parts)==1):
                one = parts[0]
                names = self.lookLast(one)
                if(names is False):
                    names = self.lookFirst(one)
                    if(names is False):
                        return "error"
                    else:
                        return names
                else:
                    return names
            firstN = parts[0]
            lastN = parts[1]

            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=" + lastN + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            self.found = self.lookFull(name)
            if("Error" in str(self.found)):
                print(" Searching --- %s seconds ---" % (time.time() - start_time))
                return "Error not found!"
            else:
                print("Searching --- %s seconds ---" % (time.time() - start_time))
                return self.temp_list[self.found]

        
        def lookFull(self, name):
            for i in range(0, len(self.temp_list)):
                print(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'])
                if (name == (self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'])):
                    print(" Look --- %s seconds ---" % (time.time() - start_time))
                    return i
            print("Look Function--- %s seconds ---" % (time.time() - start_time))
            return "Error" 

        def lookLast(self, name):
            firstNames = []
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=" + name + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            for i in range(0, len(self.temp_list)):
                if(name == (self.temp_list[i]['tLname'])):
                    firstNames.append(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'] +": " + self.temp_list[i]['tDept'])
            if(len(firstNames)==0):
                return False
            else:
                return firstNames

        def lookFirst(self, name):
            lastNames = []
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherfirstname_sort_s+asc&query=" + name + "&queryoption=TEACHER&queryBy=schoolId&sid=" + str(self.Uni))
            temp_jsonpage = json.loads(page.content)
            self.temp_list = temp_jsonpage['professors']
            for i in range(0,len(self.temp_list)):
                if(name == (self.temp_list[i]['tFname'])):
                    lastNames.append(self.temp_list[i]['tFname'] + " " + self.temp_list[i]['tLname'] + ": " + self.temp_list[i]['tDept'])
            if(len(lastNames)==0):
                return False
            else:
                return lastNames
