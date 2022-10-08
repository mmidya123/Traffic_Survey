#python3 file
# @author: Mrityunjay Midya @NIT ROURKELA 
import pandas as pd
import csv
import sys

def csvdata():
    data=pd.read_csv('Traffic_Survey.csv')
    print(data.head(8))
    
def summery(x):
    t= float(input("Enter Survey Time in Min(Add prev. session if considered)\n"))
    print('______________Total Counts Summery_____________')
    print("TOTAL NO OF ENTRY IN THIS RUN= ",x)
    csvdata()
    
    #As per IRC:106-1990- PCU counting standard considering >10% (page-10)
    PHT= int(((c1*0.5+c2*.75+c3*2+c4+(c5+c6)*3.7+c7*2)*60)/t)
    print("Total Correct Vehicle Entry Counts=",(c1+c2+c3+c4+c5+c6+c7))
    print("Predicted Average Hourly Traffic in Equivalent PCU = ", PHT)
    print("....To restart the programm please run the proggramme again.......")
    print("THANK YOU FOR USING THIS PROGRAMME IN YOUR GREAT WORK !!!")

def plots() :
    df = pd.DataFrame({
    	'Vehicle': ['ByCycle', 'Bike', "Auto Riksaw", "Four Wheeler",'Bus' , 'Truck', 'Others', "Wrong Entry"],
    	'Counts': [c1, c2, c3, c4, c5, c6, c7, c8]
    	})

    df.plot(x="Vehicle", y=["Counts"], kind="bar")
    
def give():
    print("Please choose from the below options")
    print("1.ByCycle ")
    print("2.Bike")
    print("3.Auto Riksaw")
    print("4.Four Wheeler")
    print("5.Bus")
    print("6.Truck")
    print("7.Others")
    print("\'EXIT\' -TO EXIT PROGRAMME WITHOUT SAVING DATA")
    s=input("Enter 0(zero) to exit entry and to show the Results\n")
    return s

def storedata():
    filename = "Traffic_Survey.csv"
    fields = ['Vehicles', 'Counts']
    rows = [ ['ByCycle', c1],
             ['Bike', c2],
             ["Auto Riksaw", c3],
             ["Four Wheeler", c4],
             ['Bus' , c5],
             ['Truck', c6] ,
             ['Others', c7],
             ["Wrong Entry", c8]]

    with open(filename, 'w') as csvfile:
    	csvwriter = csv.writer(csvfile)
    	csvwriter.writerow(fields)
    	csvwriter.writerows(rows)


              
print(".........Welcome to road vehicle traffic counting system- ..........." )
print("---Existing Data--- \n ")
csvdata()
k=input("\n \nDo you want to resume your count? [Y / N / EXIT ] \n")
k=k.upper()
    
if k== 'EXIT':
    sys.exit("Programm Terminated As you  Requested\n")
    
elif k== 'N' :
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
 
else :
    data=pd.read_csv('Traffic_Survey.csv')
    c1=data.iloc[0,1]
    c2=data.iloc[1,1]
    c3=data.iloc[2,1]
    c4=data.iloc[3,1]
    c5=data.iloc[4,1]
    c6=data.iloc[5,1]
    c7=data.iloc[6,1]
    c8=data.iloc[7,1]  
    print("Value of Previous Total Correct Vehicles Entries=", (c1+c2+c3+c4+c5+c6+c7))
    print('Previous Wrong Entries=', c8)



i=0
cnt= 10000      
while i<= cnt :
    i= i+ 1
    num1= give()
    if num1.isnumeric()== True :
        num=int(num1)
        if num==0:
            summery(i)
            plots()
            storedata()
            break
        
        elif num== 1:
            c1= c1+1        
        elif num== 2:
             c2= c2+1         
        elif num== 3:
             c3= c3+1           
        elif num== 4:
             c4= c4+1             
        elif num== 5:
             c5= c5+1             
        elif num== 6:
             c6= c6+1             
        elif num== 7:
            c7= c7+1        
        else:
            c8=c8+1
            print("Thats a wrong entry!" ,'\n', "Please Enter a Valid Vehicle category")
    elif num1.upper()== 'EXIT':
        sys.exit("Programm Terminated As you  Requested\n")

    else:
        c8=c8+1
        print("Thats a wrong entry!" ,'\n',"Please Enter a Valid Vehicle category")

    


   
    
    
    
    