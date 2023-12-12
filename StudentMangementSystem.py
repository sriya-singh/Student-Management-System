import pandas as pd                
import csv
import os.path

#CREATING CSV FILES

if os.path.exists('PROJECT_PATH\\Academic_Record.csv')==0:
    f=open('Academic_Record.csv','w', newline='') 
    writerobj=csv.writer(f) 
    writerobj.writerow(['','Adm_No','Name','Class','Section','Physics','Chemistry','Maths','English','CS','Total','Percentage','Grade','Remarks'])
    f.close()

if os.path.exists('PROJECT_PATH\\Student_Details.csv')==0:
    f=open('Student_Details.csv','w', newline='') 
    writerobj=csv.writer(f) 
    writerobj.writerow(['','Adm_No','Name','Class','Section','DOB','Address','Phone','Mother_Name','Father_Name'])
    f.close()

#ACADEMIC RECORD

def addrec_academic():
    df=pd.read_csv('PROJECT_PATH\\Academic_Record.csv', index_col=0)
    Adm_No = int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print("Duplicate Adm_No",Adm_No)
    else:
        name=input("Enter Name:")           
        Class=input("Enter Class:")
        sec=input("Enter Section:")
        physics=int(input("Enter Physics Score(out of 100 ):"))
        chemistry=int(input("Enter Chemistry Score(out of 100 ):"))
        maths=int(input("Enter Maths Score(out of 100 ):"))
        english=int(input("Enter English Score(out of 100 ):"))
        cs=int(input("Enter Computer Science Score(out of 100 ):"))
        remarks=input("Enter Remarks")

        total=physics+chemistry+maths+english+cs
        percentage=(total/500)*100

        if 90<=percentage<=100:
            grade="A"
        elif 80<=percentage<=89:
            grade="B"
        elif 70<=percentage<=79:
            grade="C"
        elif 60<=percentage<=69:
            grade="D"
        elif 0<=percentage<=59:
            grade="F"

        df.loc[Adm_No]=[Adm_No,name,Class,sec,physics,chemistry,maths,english,cs,total,percentage,grade,remarks]
        df.to_csv("Academic_Record.csv",mode="w")
        print('Record Added')

def updaterec_academic():
    df=pd.read_csv("Academic_Record.csv",index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        
        n=int(input('''which field do you want to update?
1.Name        6.Maths
2.Class       7.English
3.Section     8.CS
4.Physics     9.Remarks
5.Chemistry
'''))
        x=list(df.loc[Adm_No])
        
        if n==1:
            name=input("Enter new Name:")
            x[n]=name
        elif n==2:
            Class=input("Enter new Class:")
            x[n]=Class
        elif n==3:
            sec=input("Enter new Section:")
            x[n]=sec
        elif n==4:
            physics=int(input("Enter new Physics Score(out of 100 ):"))
            x[n]=physics
        elif n==5:
            chemistry=int(input("Enter new Chemistry Score(out of 100 ):"))
            x[n]=chemistry
        elif n==6:
            maths=int(input("Enter new Maths Score(out of 100 ):"))
            x[n]=maths
        elif n==7:
            english=int(input("Enter new English Score(out of 100 ):"))
            x[n]=english
        elif n==8:
            cs=int(input("Enter new CS Score(out of 100 ):"))
            x[n]=cs
        elif n==9:
            remarks=input("Enter new Remarks:")
            x[12]=remarks

        total=x[4]+x[5]+x[6]+x[7]+x[8]
        x[9]=total
        percentage=(total/500)*100
        x[10]=percentage

        if 90<=percentage<=100:
            x[11]="A"
        elif 80<=percentage<=89:
            x[11]="B"
        elif 70<=percentage<=79:
            x[11]="C"
        elif 60<=percentage<=69:
            x[11]="D"
        elif 0<=percentage<=59:
            x[11]="F"
        
        df.loc[Adm_No]=x
        
        df.to_csv("Academic_Record.csv",mode="w")
        print('Record Updated')
    else:
        print("Invalid Adm_No")

def search_academic():
    df=pd.read_csv('Academic_Record.csv',index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print(df.loc[Adm_No])
    else:
        print('Not Found')

def delrec_academic():
    df=pd.read_csv('Academic_Record.csv',index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        df.drop(Adm_No,inplace=True)
        df.to_csv('Academic_Record.csv',mode='w')
        print("Record Deleted")
    else:
        print('Invalid Adm_No',Adm_No)

def display_academic():
    df=pd.read_csv('PROJECT_PATH\\Academic_Record.csv', index_col=0)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)

def report():
    n=input('Enter Adm_No:')
    fc=open('Academic_Record.csv','r',newline='')
    csvobj=csv.reader(fc)
    x=['Adm_No','Name','Class','Section','Physics','Chemistry','Maths','English','CS','Total','Percentage','Grade','Remarks']
    for i in csvobj:
        if i[0]==n:
            fr=open(n+'.txt', 'w')
            fr.write('ABC School\n')
            for j in range(len(x)):
                fr.write(x[j]+' : '+i[j+1]+'\n')
            fr.close()
    fr=open(n+'.txt', 'r')
    a=fr.read()
    print(a)
    fr.close()
    fc.close()

def reportall():
    fc=open('Academic_Record.csv','r',newline='')
    csvobj=csv.reader(fc)
    x=['Adm_No','Name','Class','Section','Physics','Chemistry','Maths','English','CS','Total','Percentage','Grade','Remarks']
    c=0
    for i in csvobj:
        c+=1
        if c>1:
            fr=open(i[0]+'.txt', 'w')
            fr.write('ABC School\n')
            for j in range(len(x)):
                fr.write(x[j]+' : '+i[j+1]+'\n')
            fr.close()
    fc.close()
    print('Report Cards generated')

def display_fields():
    x=['Adm_No','Name','Class','Section','Physics','Chemistry','Maths','English','CS','Total','Percentage','Grade','Remarks']
    n=eval(input('''select the fields you want to be displayed
1.Adm_No      8.English
2.Name        9.CS 
3.Class       10.Total
4.Section     11.Percentage
5.Physics     12.Grade
6.Chemistry   13.Remarks
7.Maths
'''))
    l=[]
    for i in n:
        l.append(x[i-1])
    df=pd.read_csv('Academic_Record.csv',usecols=l)
    print(df)


def display_cond():
    df=pd.read_csv('Academic_Record.csv',index_col=0)
    x=['Adm_No','Name','Class','Section','Physics','Chemistry','Maths','English','CS','Total','Percentage','Grade','Remarks']
    a=int(input('''select the field on which condition is to be applied
1.Adm_No      8.English
2.Name        9.CS 
3.Class       10.Total
4.Section     11.Percentage
5.Physics     12.Grade
6.Chemistry   13.Remarks
7.Maths
'''))
    b=int(input('choose operator    1.=  2.<  3.>\n'))
    if b==1:
        if x[a-1] in ['Adm_No','Class','Physics','Chemistry','Maths','English','CS','Total','Percentage']:
            c=int(input('enter constraint'))
            new_df=df[df[x[a-1]]==c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)
        else:
            c=input('enter constraint')
            new_df=df[df[x[a-1]]==c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)
    if b==2:
        if x[a-1] in ['Adm_No','Class','Physics','Chemistry','Maths','English','CS','Total','Percentage']:
            c=int(input('enter constraint'))
            new_df=df[df[x[a-1]]<c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)
        else:
            c=input('Enter constraint')
            new_df=df[df[x[a-1]]<c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)
    if b==3:
        if x[a-1] in ['Adm_No','Class','Physics','Chemistry','Maths','English','CS','Total','Percentage']:
            c=int(input('enter constraint'))
            new_df=df[df[x[a-1]]>c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)
        else:
            c=input('enter constraint')
            new_df=df[df[x[a-1]]>c]
            pd.set_option('display.max_columns',None)
            pd.set_option('display.expand_frame_repr', False)
            print(new_df)

def pie():
    from matplotlib import pyplot as plt
    n=input('Enter Adm_No:')
    csvfile=open(r'C:\Users\Sriya & Shaurya\Desktop\cs project\Academic_Record.csv','r',newline='')
    csvobj=csv.reader(csvfile)
    for i in csvobj:
        if i[0]==n:
            x=i
            break
    csvfile.close()
    values=[]
    for j in (5,6,7,8,9):
        values.append(x[j])
    values.append(str(500-int(x[10])))
    labels=['Physics','Chemistry','Maths','English','CS','Marks lost']
    plt.style.use('fivethirtyeight')
    plt.pie(values,labels=labels,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'},shadow=True)
    plt.title('Name:{}  Adm_no:{}'.format(x[2],n))
    plt.tight_layout()
    plt.show()


#FEE RECORD
    
def addrec_fee():
    df=pd.read_csv(fname,index_col=0)   
    Adm_No = int(input("Enter Adm_No:"))           
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print("Duplicate Adm_No.",Adm_No)
    else:
        name=input("Enter Name")
        Class=input("Enter Class:")
        sec=input("Enter Section:")
        fees=int(input("Enter Fees,i.e Total fees to be paid"))
        paid=int(input("Enter Paid, i.e, Amount of fees paid"))
        due=fees-paid                                               
        dop=input("Enter Date of Payment (DD.MM.YYYY)")
        df.loc[Adm_No]=[Adm_No,name,Class,sec,fees,paid,due,dop]
        df.to_csv(fname,mode="w")
        print("Record Added")

def updaterec_fee():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        
        n=int(input('''which field do you want to update?
1.Name         4.Total fees to be paid
2.Class        5.Amount of fees paid
3.Section      6.Date of Payment
'''))
        x=list(df.loc[Adm_No])
        
        if n==1:
            name=input("Enter new Name:")
            x[n]=name
        elif n==2:
            Class=input("Enter new Class:")
            x[n]=Class
        elif n==3:
            sec=input("Enter new Section:")
            x[n]=sec
        elif n==4:
            fees=int(input("Enter Fees,i.e Total fees to be paid:"))
            x[n]=fees
        elif n==5:
            paid=int(input("Enter Paid, i.e, Amount of fees paid:"))
            x[n]=paid
        elif n==6:
            dop=input("Enter Date of Payment (DD.MM.YYYY):")
            x[7]=dop

        x[6]=x[4]-x[5]
        df.loc[Adm_No]=x

        df.to_csv(fname,mode="w")
        print('Record Updated')
    else:
        print("Invalid Adm_No")


def search_fee():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print(df.loc[Adm_No])
    else:
        print('Not Found')

def delrec_fee():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        df.drop(Adm_No,inplace=True)
        df.to_csv(fname,mode='w')
        print('Record Deleted')
    else:
        print('Invalid Adm_No',Adm_No)

def display_fee():
    df=pd.read_csv(fname, index_col=0)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)



#ATTENDANCE RECORD

def addrec_attendance():
    df=pd.read_csv(fname,index_col=0)
    Adm_No = int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print("Duplicate Adm_No.",Adm_No)
    else:
        name=input("Enter Name:")
        Class=input("Enter Class:")
        sec=input("Enter Section:")
        total=int(input("Enter total number of Days:"))
        absent=int(input("Enter No. of absent days:"))
        present=total-absent                                
        percentage= (present/total)*100
            
        df.loc[Adm_No]=[Adm_No,name,Class,sec,total,present,absent,percentage]
        df.to_csv(fname,mode="w")
        print('Record Added')
           

def updaterec_attendance():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        
        n=int(input('''which field do you want to update?
1.Name
2.Class
3.Section
4.Total number of Days
5.No. of absent days
'''))
        x=list(df.loc[Adm_No])
        
        if n==1:
            name=input("Enter new Name:")
            x[n]=name
        elif n==2:
            Class=input("Enter new Class:")
            x[n]=Class
        elif n==3:
            sec=input("Enter new Section:")
            x[n]=sec
        elif n==4:
            total=int(input("Enter total number of Days:"))
            x[n]=total
        elif n==5:
            absent=int(input("Enter No. of absent days:"))
            x[6]=absent
        
        x[5]=x[4]-x[6]
        x[7]= (x[5]/x[4])*100
        df.loc[Adm_No]=x

        df.to_csv(fname,mode="w")
        print('Record Updated')
    else:
        print("Invalid Adm_No")

def search_attendance():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print(df.loc[Adm_No])
    else:
        print('Not Found')

def delrec_attendance():
    df=pd.read_csv(fname,index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        df.drop(Adm_No,inplace=True)
        df.to_csv(fname,mode='w')
        print('Record Deleted')
    else:
        print('Invalid Adm_No',Adm_No)

def display_attendance():
    df=pd.read_csv(fname, index_col=0)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)


#STUDENT DETAILS

def addrec_details():
    df=pd.read_csv("Student_Details.csv",index_col=0)
    Adm_No = int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print("Duplicate Adm_No.",Adm_No)
    else:
        name=input("Enter Name:")
        Class=input("Enter Class:")
        sec=input("Enter Section:")
        dob=input("Enter Date Of Birth(DD.MM.YYYY):")
        add =input("Enter Address:")
        ph=input("Enter Phone Number:")
        while ph.isdigit()==False or len(ph)!=10:
            print("Invalid phone number")
            ph=input("Enter Phone Number:")
        nom=input("Enter mother's name:")
        nof=input("Enter father's name:")

        df.loc[Adm_No]=[Adm_No,name,Class,sec,dob,add,ph,nom,nof]
        df.to_csv("Student_Details.csv",mode="w")
        print('Record Added')
           
def updaterec_details():
    df=pd.read_csv("Student_Details.csv",index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    
    if len(df.loc[df['Adm_No']==Adm_No])>0:

        n=int(input('''which field do you want to update?
1.Name             5.Address
2.Class            6.Phone Number
3.Section          7.Mother's Name
4.Date Of Birth    8.Father's Name
'''))
        x=list(df.loc[Adm_No])
         
        if n==1:
            name=input("Enter new Name:")
            x[n]=name
        elif n==2:
            Class=input("Enter new Class:")
            x[n]=Class
        elif n==3:
            sec=input("Enter new Section:")
            x[n]=sec
        elif n==4:
            dob=input("Enter new Date Of Birth(DD.MM.YYYY):")
            x[n]=dob
        elif n==5:
            add =input("Enter new Address:")
            x[n]=add
        elif n==6:
            ph=input("Enter new Phone Number:")
            while ph.isdigit()==False or len(ph)!=10:
                print("Invalid phone number")
                ph=input("Enter new Phone Number:")
            x[n]=ph
        elif n==7:
            nom=input("Enter new mother's name:")
            x[n]=nom
        elif n==8:
            nof=input("Enter new father's name:")
            x[n]=nof
            
        df.loc[Adm_No]=x
        df.to_csv("Student_Details.csv",mode="w")
        print('Record Updated')
    else:
        print("Invalid Adm_No")

def search_details():
    df=pd.read_csv("Student_Details.csv",index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        print(df.loc[Adm_No])
    else:
        print('Not Found')

def delrec_details():
    df=pd.read_csv("Student_Details.csv",index_col=0)
    Adm_No=int(input("Enter Adm_No:"))
    if len(df.loc[df['Adm_No']==Adm_No])>0:
        df.drop(Adm_No,inplace=True)
        df.to_csv("Student_Details.csv",mode='w')
        print('Record Deleted')
    else:
        print('Invalid Adm_No',Adm_No)

def display_details():
    df=pd.read_csv("Student_Details.csv", index_col=0)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)

def display_fields_det():
    x=['Adm_No','Name','Class','Section','DOB','Address','Phone','Mother_Name','Father_Name']
    n=eval(input('''select the fields you want to be displayed
1.Adm_No     6.Address
2.Name       7.Phone
3.Class      8.Mother_Name
4.Section    9.Father_Name
5.DOB
'''))
    l=[]
    for i in n:
        l.append(x[i-1])
    df=pd.read_csv('Student_Details.csv',usecols=l)
    print(df)


#MAIN
    
n='y'

while n=='y':
    print('-'*70)
    print('\t\t STUDENT MANAGEMENT SYSTEM')
    print('-'*70)
    print('\t\tPress 1 - Student Details')
    print('\t\tPress 2 - Academic Record')
    print('\t\tPress 3 - Attendance Record')
    print('\t\tPress 4 - Fee Record')
    print('\t\tPress 5 - Exit')
    choice=int(input())

    if choice==1:
        x='y'
        while x=='y':
            print('-'*70)
            print('\t\t STUDENT DETAILS')
            print('-'*70)
            print('\t\tPress 1 - Display Record')
            print('\t\tPress 2 - Display all Records with selected fields')
            print('\t\tPress 3 - Add Record')
            print('\t\tPress 4 - Update Record')
            print('\t\tPress 5 - Search Record')
            print('\t\tPress 6 - Delete Record')
            c=int(input())

            if c==1:
                display_details()
            elif c==2:
                display_fields_det()
            elif c==3:
                addrec_details()
            elif c==4:
                updaterec_details()
            elif c==5:
                search_details()
            elif c==6:
                delrec_details()

            x=input('\nDo you want to continue with Student Details? (y/n)')
            if x!='y':
                break

    elif choice==2:
        x='y'
        while x=='y':
            print('-'*70)
            print('\t\t ACADEMIC RECORD')
            print('-'*70)
            print('\t\tPress 1 - Display all Records with all fields')
            print('\t\tPress 2 - Display all Records with selected fields')
            print('\t\tPress 3 - Display Records based on condition')
            print('\t\tPress 4 - Add Record')
            print('\t\tPress 5 - Update Record')
            print('\t\tPress 6 - Search Record')
            print('\t\tPress 7 - Delete Record')
            print('\t\tPress 8 - Show marks scored using pie chart')
            print('\t\tPress 9 - Generate Report Card for all')
            print('\t\tPress 10 - Generate Report Card for specific student')
            c=int(input())

            if c==1:
                display_academic()
            elif c==2:
                display_fields()
            elif c==3:
                display_cond()
            elif c==4:
                addrec_academic()
            elif c==5:
                updaterec_academic()
            elif c==6:
                search_academic()
            elif c==7:
                delrec_academic()
            elif c==8:
                pie()
            elif c==9:
                reportall()
            elif c==10:
                report()

            x=input('\nDo you want to continue with Academic record? (y/n)')
            if x!='y':
                break
            

    elif choice==3:
        x='y'
        month=input('Enter Month:')
        year=input('Enter Year:')
        fname='Attendance_Record_{}_{}.csv'.format(month,year)
        if os.path.exists('PROJECT_PATH\\{}'.format(fname))==0:
            f=open(fname,'w', newline='') 
            writerobj=csv.writer(f) 
            writerobj.writerow(['','Adm_No','Name','Class','Section','Total','Present_Days','Absent_Days','Percentage_Present'])
            f.close()

        while x=='y':
            print('-'*70)
            print('\t\t ATTENDANCE RECORD {} {}'.format(month,year))
            print('-'*70)
            print('\t\tPress 1 - Display Record')
            print('\t\tPress 2 - Add Record')
            print('\t\tPress 3 - Update Record')
            print('\t\tPress 4 - Search Record')
            print('\t\tPress 5 - Delete Record')
            c=int(input())

            if c==1:
                display_attendance()
            elif c==2:
                addrec_attendance()
            elif c==3:
                updaterec_attendance()
            elif c==4:
                search_attendance()
            elif c==5:
                delrec_attendance()

            x=input('\nDo you want to continue with Attendance Record {} {}? (y/n)'.format(month,year))
            if x!='y':
                break


    elif choice==4:
        x='y'
        month=input('Enter Month:')
        year=input('Enter Year:')
        fname='Fee_Record_{}_{}.csv'.format(month,year)
        if os.path.exists('PROJECT_PATH\\{}'.format(fname))==0:
            f=open(fname,'w', newline='') 
            writerobj=csv.writer(f) 
            writerobj.writerow(['','Adm_No','Name','Class','Section','Fees','Paid','Due','Date_of_Payment'])
            f.close()
            
        while x=='y':
            print('-'*70)
            print('\t\t FEE RECORD {} {}'.format(month,year))
            print('-'*70)
            print('\t\tPress 1 - Display Record')
            print('\t\tPress 2 - Add Record')
            print('\t\tPress 3 - Update Record')
            print('\t\tPress 4 - Search Record')
            print('\t\tPress 5 - Delete Record')
            c=int(input())

            if c==1:
                display_fee()
            elif c==2:
                addrec_fee()
            elif c==3:
                updaterec_fee()
            elif c==4:
                search_fee()
            elif c==5:
                delrec_fee()

            x=input('\nDo you want to continue with Fee Record {} {}? (y/n)'.format(month,year))
            if x!='y':
                break

    elif choice==5:
        print('THANK YOU')
        break


