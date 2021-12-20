
class student:      #defining a class
 
    def name(self,f_name,l_name):       # class method for getting and storing name of student
        self.f_name = f_name
        self.l_name = l_name
        with open("psim.txt","a") as f:
             f.write("\nstudent name:" +a+" "+b)

    def address(self,home,dist,stat,country):       #class method for getting and storing address of student
        self.home = home
        self.dist = dist
        self.stat = stat
        self.country = country
        with open("psim.txt","a") as f:
             f.write("\nhome town:"+self.home+"\ndistrict:"+self.dist+"\nstate:"+self.stat+"\ncountry:"+self.country)
    
    def contact(self,m_number_1,m_number_2):        #class method for getting and storing contact details of student 
        self.m_number_1 = m_number_1
        if m_number_2== None:           #checking if alternative contact details are filled or not
            m_number_2="not filled"
        else:
            self.m_number_2 = m_number_2
        with open("psim.txt","a") as f:
            f.write("\ncontact no. :"+self.m_number_1+"\nalternate contact no. :"+self.m_number_2)

    def parent(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name
        with open("psim.txt",'a') as f:
            f.write("\nfather name:"+self.father_name+"\nmother name:"+self.mother_name)
            f.write("\n---------------------")
    
print("welcome to student info management")

flag = 1

while flag == 1 :
    obj = student()         #creating an instance/object of main class
    a = input("enter your first name:")         #storing values in variable for each data item
    b = input("enter your last name:")

    c = input("home town:")
    d = input("district:")
    e = input("state:")
    f = input("country:")

    g = input("enter your contact no here:")
    h = input("enter your another contact no here:")
    if not h:
        h ="not entered"

    i = input("enter father name:")
    j = input("enter mother name:")

    print("do you want to save this info in system:")       #asking user for, want to save data or not 
    s_opt = int(input("for yes enter 1,for no enter 0:"))
    if s_opt == 1:
        obj.name(a,b)
        obj.address(c,d,e,f)
        obj.contact(g,h)
        obj.parent(i,j) 
        print("your data is successfully saved")
    elif s_opt ==0:
        print("your data is not saved into file system")
    flag = int(input("do you want to enter more data:(1 for yes/0 for no)"))
    print("\n \n \n")


