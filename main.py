
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from datetime import date
from datetime import datetime
from prettytable import from_csv
import random
import csv


class window1(Screen):
    pass

class Product_main(Screen):
    pass


class Product_info(Screen):

    l=ObjectProperty(None)
    l1=ObjectProperty(None)



    def display_from_file(self):
        with open("Product.csv") as f:
          #  s=from_csv(f)

            s=""
            csvreader = csv.reader(f)
            i = 0
            for rows in csvreader:
                for col in rows:
                    s = s + col
                    if i % 4 == 0:
                        s = s + str(" " * (10 - len(col)))
                    if i % 4 == 1:
                        s = s + str(" " * (20 - len(col)))
                    if i%4==2:
                        s=s+str(" "*(20-len(col)))
                    i+=1

                s = s + "\n"  


        self.l.text=str(s)




class Add_Product(Screen):
    p_id=ObjectProperty(None)
    qty=ObjectProperty(None)
    p_name=ObjectProperty(None)
    p_rate=ObjectProperty(None)
    def add(self):

        p=[self.p_id.text,self.p_name.text,self.qty.text,self.p_rate.text]
        if self.p_id.text=="" or self.p_name.text=="" or self.qty.text=="" or self.p_rate.text=="":
            show_popup8()

        elif int(self.qty.text)<=0 or int(self.p_rate<0):
            show_popup7()
        else :
            f=1
            with open("Product.csv","r") as f:
                csvreader=csv.reader(f)
                i=0
                for rows in csvreader:
                    for col in rows:
                        if col==p[0] and i%4==0:
                            f=0
                        i=i+1
            if f==0:
                show_popup9()
            else:
                with open("Product.csv","a+",newline="") as f:
                    csvwriters=csv.writer(f)
                    csvwriters.writerow(p)
        show_popup2()
        self.p_id.text=""
        self.p_name.text=""
        self.qty.text=""
        self.p_rate.text=""


class Product:
    count=0
    def __int__(self):
        self.Pid=0
        self.qty=0;
        self.name=""

class Customer_main(Screen):
    pass


class update_Customer(Screen):

    c_id = ObjectProperty(None)
    c_name = ObjectProperty(None)
    c_address = ObjectProperty(None)
    c_email = ObjectProperty(None)
    c_contact = ObjectProperty(None)
    c_out_amt = ObjectProperty(None)

    def custupdate(self):
        U = []
        flag = 1
        with open("Customer_data2.csv") as f:
            csvreader = csv.reader(f)

            for rows in csvreader:
                U.append(rows)

        for list in U:
            for i in range(len(list) - 5):
                if list[i] == self.c_id.text:
                    list[i + 1] = self.c_name.text
                    list[i + 2] = self.c_contact.text
                    list[i + 3] = self.c_address.text
                    list[i + 4] = self.c_email.text
                    list[i + 5] = self.c_out_amt.text
                    flag = 0
                    break


        if flag==1:
            show_popup13()

        print(U)
        if flag==0:
            if self.c_id.text == "" or self.c_name.text == "" or self.c_contact.text == "" or self.c_address.text == "" or self.c_email.text == "" or self.c_out_amt.text == "":
                show_popup8()

            else:

                with open("Customer_data1.csv") as f:
                    U1 = []
                    csvreader = csv.reader(f)

                    for rows in csvreader:
                        U1.append(rows)

                for list in U1:
                    for i in range(len(list) - 1):
                        if list[i] == self.c_id.text:
                            list[i + 1] = self.c_name.text

                with open("Customer_data1.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    print("Hello")
                    for list in U1:
                        writer.writerow(list)

                with open("Customer_data2.csv","w",newline="") as f:
                    writer=csv.writer(f)
                    print("Hello")
                    for list in U:
                        writer.writerow(list)

        self.c_id.text=""
        self.c_name.text=""
        self.c_contact.text=""
        self.c_address.text=""
        self.c_email.text=""
        self.c_out_amt.text=""





class Customer_info2(Screen):

    v=ObjectProperty(None)
    cid = ObjectProperty(None)


    def view(self):
        s=""
        with open("Customer_data2.csv") as f:
            flag=1
            U=[]
            reader=csv.reader(f)
            for rows in reader:
                U.append(rows)
            for list in U:
                if len(list)!=0:
                    if list[0]==self.cid.text:
                        s=   "cid                 :"+list[0]+"\n"
                        s=s+ "Name                :" +list[1]+"\n"
                        s=s+ "Number              :"+list[2]+"\n"
                        s=s+ "Area                :"+list[3]+"\n"
                        s=s+ "Email ID            :"+list[4]+"\n"
                        s=s+ "Outstanding amount  :"+list[5]+"\n"
                        flag=0
            if flag==0:
                f_name=str(self.cid.text) +"order.csv"
                try:
                    o=[]
                    with open(f_name) as f1:
                        reader=csv.reader(f1)
                        for list in reader:
                            o=list
                        if len(o)!=0:
                            s=s+"Last Ordered Date:" +o[len(o)-3]
                        else:
                            s = s + "Last Ordered Date:" + "Not Ordered Anything Yet"

                except IOError:
                    s = s + "Last Ordered Date:" + "Not Ordered Anything Yet"

                finally:
                    self.v.text=s
            if flag==1:
                show_popup13()


    def cid_store(self):
        with open("cid.txt","w") as f:
            f.write(self.cid.text)


class Add_Customer(Screen):

    c_name=ObjectProperty(None)
    c_id=ObjectProperty(None)
    c_num=ObjectProperty(None)
    c_area=ObjectProperty(None)
    c_email=ObjectProperty(None)

    l=["T.Nagar","Anna Nagar","Mylapore","K.K Nagar","Kodambakkam","Tambaram","Alwarpet","Besant Nagar"]

    def add(self):

        if self.c_id.text=="" or self.c_name.text=="" or self.c_num.text=="" or self.c_area.text=="" or self.c_email.text=="" :
            show_popup8()

        elif self.c_area.text not in Add_Customer.l :
            show_popup10()


        else:
            f=1
            with open("Customer_data1.csv") as f:
                reader=csv.reader(f)
                for rows in reader:
                    for col in rows:
                        if col==self.c_id.text:
                            f=0
                            break

            if f==0:
                show_popup12()
            else:

                with open("Customer_data1.csv","a+",newline="") as f:
                    csvwriter=csv.writer(f)
                    p=[self.c_id.text,self.c_name.text]
                    csvwriter.writerow(p)
                with open("Customer_data2.csv", "a+",newline="") as f:
                    csvwriter = csv.writer(f)
                    p = [self.c_id.text, self.c_name.text,self.c_num.text,self.c_area.text,self.c_email.text,"0"]
                    csvwriter.writerow(p)
                    show_popup3()
        self.c_id.text=""
        self.c_name.text=""
        self.c_email.text=""
        self.c_num.text=""
        self.c_area.text=""



class Customer_info(Screen):

    l=ObjectProperty(None)
    def display_from_file(self):
        s =""
        with open("Customer_data1.csv") as f:
            csvreader=csv.reader(f)
            for rows in csvreader:
                for col in rows:
                    s=s+ "      " + col
                s=s+"\n"
        self.l.text=s


class Customer(Customer_info):
    def __init__(self, **kwargs):
        super(Customer_info, self).__init__(**kwargs)
        self.outstanding_amt=0
        self.order=[]


class Order1(Screen):
    oid=ObjectProperty(None)
    qty=ObjectProperty(None)
    pid=ObjectProperty(None)
    date_=ObjectProperty(None)
    final=[]
    r=0
    def add(self):
        if self.oid.text=="":
            show_popup16()
        else:
            with open("Product.csv") as f:
                p=[]
                i=0
                flag=1
                qty_p=0
                reader=csv.reader(f)
                for list in reader:
                    for col in list:
                        if col==self.pid.text and i%4==0:
                            p=list
                            qty_p=int(list[2])
                            flag=0
                        i+=1
                if flag==1:
                    show_popup13()

                else:

                    print(qty_p,self.qty.text)
                    if qty_p<int(self.qty.text):
                        show_popup20()

                    else :
                        Order1.final=Order1.final+p
                        Order1.r=Order1.r+int(p[2])*int(p[3])
                        with open("Product.csv") as file:
                            p1=[]
                            reader=csv.reader(file)
                            for rows in reader:
                                p1.append(rows)
                            for rows in p1:
                                if rows[0]==self.pid.text:
                                    rows[2]=str(int(rows[2])-int(self.qty.text))
                        with open("Product.csv","w",newline="") as file:
                            writer =csv.writer(file)
                            for rows in p1:
                                writer.writerow(rows)


        self.pid.text=""
        self.qty.text=""


    def paynow(self):

                today_date=date.today()
                d1 = today_date.strftime("%d/%m/%Y")
                today=datetime.strptime(d1,"%d/%m/%Y")
                d = self.date_.text
                print(d)
                my_date = datetime.strptime(d, "%d/%m/%Y")
                if int(my_date.day)<int(today.day) or (int(my_date.month)<today.month and int(my_date.month)>12) or int(my_date.year)!=today.year:
                    show_popup14()

                else:

                    with open("cid.txt") as f:
                        cid=f.read()
                    Order1.final.append("@")
                    Order1.final.append(Order1.r)
                    Order1.final.append(self.date_.text)
                    Order1.final.append("Paid")
                    Order1.final.append(self.oid.text)
                    f_name=str(cid)+"order.csv"
                    print(Order1.final)
                    with open(f_name,"a",newline="") as f:
                        writer=csv.writer(f)
                        writer.writerow(Order1.final)
                    show_popup15()
                    with open("oid.text","w") as f:
                        f.write(self.oid.text)
                        self.oid.text=""
                    sm.current="Order2"

    def paylater(self):

                today_date=date.today()
                d1 = today_date.strftime("%d/%m/%Y")
                today=datetime.strptime(d1,"%d/%m/%Y")
                d = self.date_.text
                print(d)
                my_date = datetime.strptime(d, "%d/%m/%Y")
                if int(my_date.day)<int(today.day) or (int(my_date.month)<today.month and int(my_date.month)>12) or int(my_date.year)!=today.year:
                    show_popup14()

                else:
                    with open("cid.txt") as f:
                        cid=f.read()
                    Order1.final.append("@")
                    Order1.final.append(Order1.r)
                    Order1.final.append(self.date_.text)
                    Order1.final.append("Not Paid")
                    Order1.final.append(self.oid.text)
                    U = []

                    with open("Customer_data2.csv") as f:
                        csvreader = csv.reader(f)

                        for rows in csvreader:
                            U.append(rows)

                    for list in U:
                        for i in range(len(list) - 5):
                            if list[i] == cid:
                                list[i + 5] = str(int(list[i + 5])+int(Order1.r))
                                break

                    with open("Customer_data2.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        for list in U:
                            writer.writerow(list)
                    f_name=str(cid)+"order.csv"
                    with open(f_name,"a",newline="") as f:
                        writer=csv.writer(f)
                        writer.writerow(Order1.final)
                    show_popup15()
                    with open("oid.text","w") as f:
                        f.write(self.oid.text)
                        self.oid.text = ""
                    sm.current="Order2"

    def order_id(self):

        while 1:
            with open("cid.txt") as f:
                cid = f.read()
            n=random.randint(1,100000)
            oid=cid+"O"+str(n)
            flag=1
            f_name=cid+"order.csv"
            with open(f_name) as f:
                reader=csv.reader(f)
                for list in reader:
                    for col in list:
                        if col==oid:
                            flag=0
                if flag==1:
                    return oid

                if flag==0:
                    flag1=1
                    oid=cid+"o"+str(n)
                    for list in reader:
                        for col in list:
                            if col == oid:
                                flag1 = 0
                    if flag1==1:
                        return oid





    def set_date(self):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        return d1

class update_order(Screen):

    oid=ObjectProperty(None)
    status=ObjectProperty(None)
    def update_order(self):
        with open("cid.txt") as f:
            cid=f.read()
        flag = 1
        u1=[]
        f_name = str(cid) + "order.csv"
        if self.oid.text == "" or self.status.text == "":
            show_popup8()
        else:
            with open(f_name) as f:
                reader = csv.reader(f)
                for list in reader:
                    u1.append(list)
                for o in u1:
                    if o[len(o) - 1] == self.oid.text:
                        flag = 0
                        if o[len(o) - 2] == "Not Paid" and self.status.text == "Paid":
                            o[len(o) - 2] = "Paid"
                            amt = o[len(o) - 4]
                            with open("Customer_data2.csv") as f1:
                                reader1 = csv.reader(f1)
                                u = []
                                for list in reader1:
                                    u.append(list)

                                for rows in u:
                                    i = 0
                                    for col in rows:
                                        i = i + 1
                                        if col == cid and i == 1:
                                            rows[5] = str(int(rows[5]) - int(amt))
                                            if int(rows[5]) < 0:
                                                rows[5] = 0
                            with open("Customer_data2.csv", "w", newline="") as f1:
                                writer1 = csv.writer(f1)

                                for rows in u:
                                    writer1.writerow(rows)
                                show_popup19()

                        elif o[len(o) - 2] == 'Paid':
                            show_popup18()

            if flag==0:

                with open(f_name,"w",newline="") as f:
                    writer = csv.writer(f)
                    for list in u1:
                        writer.writerow(list)



            if flag == 1:
                show_popup17()
        self.oid.text=""
        self.status.text=""


class view_order(Screen):
    l=ObjectProperty(None)

    def view(self):
        with open("cid.txt") as f:
            cid=f.read()
        f_name=str(cid)+"order.csv"
        with open(f_name) as f:
            reader =csv.reader(f)
            u=[]
            for list in reader:
                u.append(list)
            s="Order Id             Order Date              Payment         Status\n"
            for list in u:
                s=s+ list[len(list)-1] +"           "+list[len(list)-3]+"           "+list[len(list)-4]+"           "+list[len(list)-2] +"\n"

        self.l.text=s



class view_order2(Screen):
    l=ObjectProperty(None)
    oid=ObjectProperty(None)
    def view(self):
        with open("cid.txt") as f:
            cid=f.read()
        f_name=str(cid)+"order.csv"
        s="Pid            Product name          Qty           rate/product\n"
        u=[]
        with open(f_name) as f:
            reader=csv.reader(f)
            for list in reader:
                u.append(list)
            i=0
            for row in u:
                if row[-1]==self.oid.text:
                    for col in row:
                        if col=="@":
                            break
                        else:
                            s=s+col+"               "
                            i = i + 1
                            if i%4==0:
                                s=s+"\n"
                    s=s+"\n"
                    s=s+"           Date   :" +row[-3]+"\n"
                    s=s+"           Status :" +row[-2]+"\n"
        self.l.text=s



class Order2(Screen):
    l=ObjectProperty(None)

    def show(self):
        with open("cid.txt") as f:
            cid=f.read()
        f_name=cid+"order.csv"
        with open("oid.text") as f:
            oid=f.read()
        with open(f_name) as file:
            s = "                                        BILL INVOICE                                                        \n"
            s = s + "------------------------------------------------------------------------------------------------------------------------\n"
            s = s + "   product id         product name             quantity                 rate/piece                total     \n"
            s = s + "-------------------------------------------------------------------------------------------------------------------------\n"
            U = []
            reader = csv.reader(file)
            for list in reader:
                U.append(list)
                i = 0
                for row in U:
                    if row[-1] == oid:
                        for col in row:
                            if col == "@":
                                break
                            else:
                                s = s + col + "                 "
                                i = i + 1
                                if i % 4 == 0:
                                    s = s + "         " + str(int(list[i - 1]) * int(list[i - 2]))
                                    s = s + "\n"

                        s=s+"\n\n\n"
                        s = s + "         Order ID      :" + row[-1] + "\n"
                        s = s + "         Date          :" + row[-3] + "\n"
                        s = s + "         Bill amount   :" + row[-4] + "\n"
                        s = s + "         Payment status:" + row[-2] + "\n"
        self.l.text=s
        print(s)

class update_Product(Screen):
    p_id=ObjectProperty(None)
    qty=ObjectProperty(None)
    p_name=ObjectProperty(None)
    p_rate=ObjectProperty(None)
    def update(self):
        c=[]
        f=1
        p=[self.p_id.text,self.p_name.text,self.qty.text,self.p_rate.text]

        if self.p_id.text=="" or self.p_name.text=="" or self.qty.text=="" or self.p_rate.text:
            show_popup8()

        elif int(self.qty.text)<=0 or int(self.p_rate.text) <0:
            show_popup7()

        else:
            with open("Product.csv") as f:
                csvreader=csv.reader(f)
                for rows in csvreader:
                        c.append(rows)
            print(c)
            for list in c:
                for i in range(len(list)-3):
                    if list[i]==self.p_id.text:
                        list[i+1]=self.p_name.text
                        list[i+2]=self.qty.text
                        list[i+3]=self.p_rate.text
                        f=0
                        break
            print(c)
            if f==1:
                show_popup5()
            else:
                show_popup6()
                with open("Product.csv","w",newline="") as f:
                    csvwriter=csv.writer(f)
                    for list in c:
                        csvwriter.writerow(list)



        self.p_id.text = ""
        self.p_name.text = ""
        self.qty.text = ""
        self.p_rate.text=""



class MainWindow(ScreenManager):
    pass

class login(Screen):
    username=ObjectProperty(None)
    password=ObjectProperty(None)

    def submit(self):
        if self.username.text=="20pt" and self.password.text=="Psg":
            sm.current="second"
        else:
            self.username.text=""
            self.password.text=""
            show_popup()

sm=MainWindow()

kv=Builder.load_file("login.kv")

screens = [login(name="login"),window1(name="second"),Product_main(name="Product_main"),Product_info(name="Product_information"),Add_Product(name="Add_Product"),Customer_main(name="Customer_main"),Customer_info(name="Customer_information"),Add_Customer(name="Add_Customer"),Customer_info2(name="Customer_info2"),Order1(name="Order1"),Order2(name="Order2"),update_Product(name="update_product"),update_Customer(name="update_customer"),update_order(name="update_order"),view_order(name="view_order"),view_order2(name="view_order2")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

def show_popup():
    popupWindow = Popup(title="login error", content=Label(text="Access Denied"), size_hint=(None,None),size=(300,100))
    popupWindow.open()

def show_popup2():
    popupWindow = Popup(title="Information", content=Label(text="Item Added Successfully"), size_hint=(None,None),size=(300,100))
    popupWindow.open()

def show_popup3():
    popupWindow = Popup(title="Information", content=Label(text="New Customer Added Successfully"), size_hint=(None,None),size=(300,100))
    popupWindow.open()

def show_popup4():
    popupWindow = Popup(title="Error", content=Label(text="No such Product Id Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup5():
    popupWindow = Popup(title="Error", content=Label(text="Product Id Does Not Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup6():
    popupWindow = Popup(title="Information", content=Label(text="Product Updated Successfully"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup7():
    popupWindow = Popup(title="Error", content=Label(text="Product Quantity and rate Cannot be Negative or Zero"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup8():
    popupWindow = Popup(title="Error", content=Label(text="Mandatory fields cannot be left blank"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup9():
    popupWindow = Popup(title="Error", content=Label(text="Product Id Already Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup10():
    popupWindow = Popup(title="Warning", content=Label(text="Enter A valid Area"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup11():
    popupWindow = Popup(title="Warning", content=Label(text="Enter A valid Email-Id"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup12():
    popupWindow = Popup(title="Error", content=Label(text="Customer Id Already Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup13():
    popupWindow = Popup(title="Error", content=Label(text="Customer Id Dosent Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup14():
    popupWindow = Popup(title="Error", content=Label(text="Incorrect Date"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup15():
    popupWindow = Popup(title="Information", content=Label(text="Order Successfully Taken"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup16():
    popupWindow = Popup(title="Error", content=Label(text="Order ID Not Given"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup17():
    popupWindow = Popup(title="Error", content=Label(text="Order ID Does Not Exist"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup18():
    popupWindow = Popup(title="Error", content=Label(text="Status-\'paid\' cannot be updated"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup19():
    popupWindow = Popup(title="Information", content=Label(text="Updated Successfully"), size_hint=(None,None),size=(500,100))
    popupWindow.open()

def show_popup20():
    popupWindow = Popup(title="Error", content=Label(text="Given Number Of Stock Not Available\nPlease Try Entering Different quantity"), size_hint=(None,None),size=(500,200))
    popupWindow.open()


class loginApp(App):

    def build(self):
        return sm
if __name__=="__main__":
    loginApp().run()

