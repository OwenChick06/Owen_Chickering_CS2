import csv

fhand = open('student_data_cs2.txt','r') #Opens file as fhand
with open('new_data_file.csv', 'w', newline='') as file: #Opens file to write
    for line in fhand: #For every line in the file
        '''
        The following lines define which vertical slices of the txt file represent what data
        '''
        Id = line[0:4].strip() 
        Name = line[4:15].strip()
        LastName = line[21:30].strip()
        Grade = line[36:42].strip()
        gpa = line[42:46].strip()
        BirthDate = line[48:58].strip()
        Gender = line[60:66].strip()
        ClassRank = line[67:76].strip()
        AttendPCT = line[76:80].strip()
        Honors = line[86:93].strip()
        Sports = line[93:102].strip()
        ClubCount = line[102:111].strip()
        file.write(Id + ',' + Name + ',' + LastName + ',' + Grade + ',' + gpa + ',' + BirthDate + ',' + Gender + ',' + ClassRank + ',' + AttendPCT + ',' + Honors + ',' + Sports + ',' + ClubCount+'\n')
        #Writes the data to a new file