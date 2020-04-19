import datetime
import main_parser

# US19 First Cousins shoud not marry
# first cousins should not marry one another
# Author: Himanshu Tanwar

def US19():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)
	
    individualError = []

    #check if parents of husband and spouse. If parents are siblings in each others families then first cousins. Return
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId != 'NA':
            hParents = main_parser.findParents(fam.husbandId, listFam)
            wParents = main_parser.findParents(fam.wifeId, listFam)
            if hParents and wParents:
                #check if either hParents are siblings with wParents
                siblings = main_parser.checkIfSiblings(hParents,wParents,listFam)
                if siblings == True:
                    individualError.append(fam)
    return individualError


# US20 Aunts and Uncles
# Aunts and Uncles should not marry their neices or nephews
# Author: Himanshu Tanwar

def US20():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    individualError = []
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId != 'NA':
            hParents = main_parser.findParents(fam.husbandId, listFam)
            wParents = main_parser.findParents(fam.wifeId, listFam)
            if hParents and wParents:
                hSiblings = main_parser.checkIfSiblings(hParents,fam,listFam)
                wSiblings = main_parser.checkIfSiblings(wParents,fam,listFam)
                if hSiblings == True:
                    individualError.append(fam)
                elif wSiblings == True:
                    individualError.append(fam)
    return individualError

#Author Rajit Gohel

def US21():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    Error=[]

    flag1 = False
    flag2 = False
    for fam in listFam:
        if fam.husbandId !='NA':
            husb= main_parser.findPerson(fam.husbandId, listPeople)
            if husb.gender !='M':
                flag1 = True
        if fam.wifeId !='NA':
            wife=main_parser.findPerson(fam.wifeId, listPeople)
            if wife.gender!='F':
                flag2 = True
        if flag1 or flag2:
            Error.append(fam)
            flag1 = False
            flag2 = False
    return Error

#Author Rajit Gohel
def US22():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    IndividualIdError=[]
    FamilyIDError=[]

    dictionary={}
    for person in listPeople:
        if person.id in dictionary and dictionary[person.id] != person:
            IndividualIdError.append(person.id)
        else:
            dictionary[person.id]= person
    
    dictionary={}
    for family in listFam:
        if family.id in dictionary and dictionary[family.id] != family:
            FamilyIDError.append(family.id)
        else:
            dictionary[family.id] = family
    
    return IndividualIdError,FamilyIDError


#Author Ritvik Tiwari
def US23():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)
    
    birthdayError=[]
    dictionary={}
    for person in listPeople:
        if person.name in dictionary and person.birthday == dictionary[person.name][0] and person.id != dictionary[person.name][1]:
            birthdayError.append((person.birthday,person.name))
        else:
            dictionary[person.name] = (person.birthday,person.id)

    return birthdayError

#Author Ritvik Tiwari
def US24():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = main_parser.parse(file_)

    familyError=[]
    dictionary={}
    for fam in listFam:
        if fam.husbandId != 'NA' and fam.wifeId !='NA':
            husb= main_parser.findPerson(fam.husbandId, listPeople)
            wife= main_parser.findPerson(fam.wifeId, listPeople)
            if husb.name in dictionary and dictionary[husb.name][1] == fam.married:
                familyError.append((husb.name,fam.married))
            else:
                dictionary[husb.name]=(wife.name,fam.married)
            if wife.name in dictionary and dictionary[wife.name][1] == fam.married:
                familyError.append((wife.name,fam.married))
            else:
                dictionary[wife.name]=(husb.name,fam.married)
    return familyError
