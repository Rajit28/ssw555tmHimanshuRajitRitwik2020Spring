#   CS-555
#   Parser for Gedcom files
from prettytable import PrettyTable

class individuals(object):

    def __init__(self, arg):
        self.id = arg
        self.name = ""
        self.gender = ""
        self.birthday = ""
        self.alive = True
        self.age = 0
        self.death = "NA"
        self.children = "NA"
        self.spouse = "NA"

    def addName(self, name):
        self.name = name
    def addGender(self, gender):
        self.gender = gender
    def addBirthday(self, birthday):
        self.birthday = birthday
    def addAlive(self, alive):
        self.alive = alive
    def addAge(self, age):
        self.age = age
    def addDeath(self, death):
        self.death = death
    def addChildren(self, children):
        self.children = children
    def addSpouse(self, spouse):
        self.spouse = spouse

class families(object):
    def __init__(self, arg):
        self.id = arg
        self.married = "NA"
        self.divorced = "NA"
        self.husbandId = "NA"
        self.husbandName = "NA"
        self.wifeId = "NA"
        self.wifeName = "NA"
        self.children = []

    def addMarried(self, date):
        self.married = date
    def addDivorced(self, divorced):
        self.divorced = divorced
    def addHusband(self, id_, husbandName):
        self.husbandId = id_
        self.husbandName = husbandName
    def addWife(self, id_, wifeName):
        self.wifeId = id_
        self.wifeName = wifeName
    def addChildren(self, child):
        self.children.append(child)
        
def findPerson(id_, listPeople):
    found = ""
    for person in listPeople:
        if person.id == id_:
            found = person
            break;
    return found

def findFam(id_, listFam):
    found = ""
    for fam in listFam:
        if fam.id == id_:
            found = fam
            break;
    return found

def convertMonth(month):
    allMonth = {'JAN':'01', 'FEB':'02', 'MAR':'03',
                'APR':'04', 'MAY':'05', 'JUN':'06',
                'JUL':'07', 'AUG':'08', 'SEP':'09',
                'OCT':'10', 'NOV':'11', 'DEC':'12'}

    return allMonth[month]

def prettyOutput(listIndividuals, listFamilies):
    ind = PrettyTable(["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"])
    fam = PrettyTable(["ID","Married","Divorce","Husband ID","Husband Name","Wife ID","Wife Name","Children"])
    for p in listIndividuals:
        ind.add_row([p.id, p.name, p.gender, p.birthday, str(p.age), str(p.alive), p.death, p.children, p.spouse])
    for p in listFamilies:
        fam.add_row([p.id, p.married, p.divorced, p.husbandId, p.husbandName, p.wifeId, p.wifeName, p.children])

    print("Individuals")
    print(ind)
    print("Families")
    print(fam)




if __name__ == "__main__":
    level=tag=argument = "Not Available"
    set_of_valid_tags = { '0' :['HEAD','NOTE','TRLR'], '1':['BIRT','CHIL','DIV','HUSB','WIFE','MARR','NAME','SEX','DEAT','FAMC','FAMS'], '2' :['DATE']}
    list_of_people = []
    list_of_fams = []
    try:
        with open('ssw555tmHimanshuRajitRitwik2020Spring.ged') as file_variable:
            birth = False
            death = False
            married = False
            divorced = False
            currentTag = ""

            for line in file_variable:
                line=line.strip()
                #print("-->{}".format(line))
                line_arguments = line.split(" ")
                length_of_line_arguments = len(line_arguments)
                if length_of_line_arguments == 3 and line_arguments[0] == '0' and line_arguments[2] in {'INDI','FAM'}:
                    level, tag, argument = line_arguments
                    valid_tags = 'Y'
                    if argument == 'INDI':
                        currentId = tag.strip('@')
                        newIndividual = individuals(currentId)
                        list_of_people.append(newIndividual)
                        currentTag = 'INDI'
                    elif argument == 'FAM':
                        currentId = tag.strip('@')
                        newFam = families(currentId)
                        list_of_fams.append(newFam)
                        currentTag = 'FAM'

                elif length_of_line_arguments >= 2:
                    level, tag = line_arguments[0],line_arguments[1]
                    argument = " ".join(line_arguments[2:])

                    if level in set_of_valid_tags and tag in set_of_valid_tags[level]:
                        valid_tags ='Y'
                        if currentTag == 'INDI':
                            if birth == True and tag == 'DATE':
                                birthday = line_arguments[4] + '-' + convertMonth(line_arguments[3]) + '-'+ line_arguments[2] 
                                p = findPerson(currentId, list_of_people)
                                p.addBirthday(birthday)
                                age = int(line_arguments[4])
                                p.addAge(2020-age)
                                birth = False
                            elif death == True and tag == 'DATE':
                                deathday =  line_arguments[4] + '-' + convertMonth(line_arguments[3]) + '-'+ line_arguments[2]
                                p = findPerson(currentId, list_of_people)
                                p.addDeath(deathday)
                                p.addAlive(False)
                                death = False
                            elif tag == 'NAME':
                                #name = line_arguments[2] + " " + line_arguments[3]
                                name = " ".join(line_arguments[2:])
                                p = findPerson(currentId, list_of_people)
                                p.addName(name)
                            elif tag == 'SEX':
                                gender = line_arguments[2]
                                p = findPerson(currentId, list_of_people)
                                p.addGender(gender)
                            elif tag == 'BIRT':
                                birth = True
                                continue;
                            elif tag == 'DEAT':
                                death = True
                                continue;
                        elif currentTag == 'FAM':
                            if married == True and tag == 'DATE':
                                fam = findFam(currentId, list_of_fams)
                                marriedDate = line_arguments[4] + '-' + convertMonth(line_arguments[3]) + '-'+ line_arguments[2]
                                fam.addMarried(marriedDate)
                                married = False
                            elif divorced == True and tag == 'DATE':
                                fam = findFam(currentId, list_of_fams)
                                divDate = line_arguments[4] + '-' + convertMonth(line_arguments[3]) + '-'+ line_arguments[2]
                                fam.addDivorced(divDate)
                                divorced = False
                            elif tag == 'MARR':
                                married = True
                                continue;
                            elif tag == 'DIV':
                                divorced = True
                                continue;
                            elif tag == 'HUSB':
                                husbandId = line_arguments[2].strip('@')
                                fam = findFam(currentId, list_of_fams)
                                husband = findPerson(husbandId, list_of_people)
                                fam.addHusband(husbandId, husband.name)
                            elif tag == 'WIFE':
                                wifeId = line_arguments[2].strip('@')
                                fam = findFam(currentId, list_of_fams)
                                wife = findPerson(wifeId, list_of_people)
                                fam.addWife(wifeId, wife.name)
                            elif tag == 'CHIL':
                                childId = line_arguments[2].strip('@')
                                fam = findFam(currentId, list_of_fams)
                                fam.addChildren(childId)
                    else :
                        valid_tags = 'N'
                else:
                    valid_tags ='N'
                    level, tag, argument =line_arguments
        
                #print("<--{}|{}|{}|{}".format(level,tag,valid_tags,argument))
            for fam in list_of_fams:
                if fam.husbandId != 'NA':
                    husband = findPerson(fam.husbandId, list_of_people)
                    if fam.wifeId != 'NA':
                        husband.addSpouse(fam.wifeId)
                    if len(fam.children) > 0:
                        husband.addChildren(fam.children)
                if fam.wifeId != 'NA':
                    wife = findPerson(fam.wifeId, list_of_people)
                    if fam.husbandId != 'NA':
                        wife.addSpouse(fam.husbandId)
                    if len(fam.children) > 0:
                        wife.addChildren(fam.children)
            
            prettyOutput(list_of_people,list_of_fams)
    except:
        print("Can't open file")


