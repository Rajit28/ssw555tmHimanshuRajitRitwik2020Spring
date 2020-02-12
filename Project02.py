level=tag=argument = "Not Available"
set_of_valid_tags = { '0' :['HEAD','NOTE','TRLR'], '1':['BIRT','CHIL','DIV','HUSB','WIFE','MARR','NAME','SEX','DEAT','FAMC','FAMS'], '2' :['DATE']}
try:
    with open('ssw555tmHimanshuRajitRitwik2020Spring.ged') as file_variable:
        for line in file_variable:
            line=line.strip()
            print("-->{}".format(line))
            line_arguments = line.split(" ")
            length_of_line_arguments = len(line_arguments)
            if length_of_line_arguments == 3 and line_arguments[0] == '0' and line_arguments[2] in {'INDI','FAM'}:
                level, tag, argument = line_arguments
                valid_tags = 'Y'
            elif length_of_line_arguments >= 2:
                level, tag = line_arguments[0],line_arguments[1]
                argument = " ".join(line_arguments[2:])
                if level in set_of_valid_tags and tag in set_of_valid_tags[level]:
                    valid_tags ='Y'
                else :
                    valid_tags = 'N'
            else:
                valid_tags ='N'
                level, tag, argument =line_arguments
    
            print("<--{}|{}|{}|{}".format(level,tag,valid_tags,argument))
except :
    print("Can't open file")



