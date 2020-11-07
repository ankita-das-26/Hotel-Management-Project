from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel mgmt systems")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        MainFrame=Frame(self.root)
        MainFrame.grid()

        TopFrame=Frame(MainFrame,bd=14,width=1350,height=550,padx=20,relief=RIDGE,bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame=Frame(TopFrame,bd=10,width=450,height=550,padx=2,relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame=Frame(TopFrame,bd=10,width=820,height=550,padx=2,relief=RIDGE,bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame=Frame(MainFrame,bd=10,width=1350,height=150,padx=20,relief=RIDGE,bg="powder blue" )
        BottomFrame.pack(side=BOTTOM)

        def iExit():
            iExit=tkinter.messagebox.askyesno("hotel mgmt systems","confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def Receipt():
            self.txtReceipt.insert(END,CustomerRef.get()+ '\t' + FirstName.get()+ "\t" + Surname.get()+
            "\t"+Address.get()+ "\t" + PostCode.get()+"\t" + Mobile.get()+"\t" + Nationality.get()+
            "\t"+ CheckInDate.get()+ "\t" +  CheckOutDate.get()+ "\t" +  PaidTax.get()+"\t" + SubTotal.get()+
            "\t"+ TotalCost.get()+"\n")
        def Reset():
            CustomerRef.set("")
            FirstName.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            self.txtReceipt.delete("1.0",END)

    
        def TotalCostandDate():
            InDate=CheckInDate.get()
            OutDate=CheckOutDate.get()
            InDate=datetime.strptime(InDate,"%d/%m/%Y")
            OutDate=datetime.strptime(OutDate,"%d/%m/%Y")
            TotalDays.set(abs((OutDate-InDate).days))
            
            if(Meal.get()=="Breakfast" and RoomType.get()=="Single"):
             q1=float(17)
             q2=float(34)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Breakfast" and RoomType.get()=="Double"):
             q1=float(35)
             q2=float(43)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Breakfast" and RoomType.get()=="Family"):
             q1=float(43)
             q2=float(63)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)

            elif(Meal.get()=="Lunch" and RoomType.get()=="Single"):
             q1=float(29)
             q2=float(37)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Lunch" and RoomType.get()=="Double"):
             q1=float(37)
             q2=float(43)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Lunch" and RoomType.get()=="Family"):
             q1=float(46)
             q2=float(63)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Dinner" and RoomType.get()=="Single"):
             q1=float(28)
             q2=float(37)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Dinner" and RoomType.get()=="Double"):
             q1=float(30)
             q2=float(43)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="Dinner" and RoomType.get()=="Family"):
             q1=float(43)
             q2=float(63)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="All" and RoomType.get()=="Single"):
             q1=float(30)
             q2=float(37)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.05))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.05)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="All" and RoomType.get()=="Double"):
             q1=float(36)
             q2=float(48)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.08))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.08)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
            elif(Meal.get()=="All" and RoomType.get()=="Family"):
             q1=float(40)
             q2=float(60)
             q3=float(TotalDays.get())
             q4=float(q1+q2)
             q5=float(q3*q4)
             Tax="Rs"+str('%.2f'%((q5)*0.09))
             ST="Rs"+str('%.2f'%((q5)))
             TT="Rs"+str('%.2f'%(q5+((q5)*0.09)))
             PaidTax.set((Tax))
             SubTotal.set(ST)
             TotalCost.set(TT)
           
             
             
        CustomerRef=StringVar()
        FirstName=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB=StringVar()
        IDType=StringVar()
        Gender=StringVar()
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()
       
        

        self.lblCustomer_Ref=Label(LeftFrame,font=('arial',12,'bold'),text="Customer Ref:",padx=2,bg="powder blue")
        self.lblCustomer_Ref.grid(row=0,column=0,sticky=W)
        self.txtCustomer_Ref=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CustomerRef,width=20)
        self.txtCustomer_Ref.grid(row=0,column=1,pady=3,padx=20)

        
        self.lblFirstName=Label(LeftFrame,font=('arial',12,'bold'),text="FirstName:",padx=2,bg="powder blue")
        self.lblFirstName.grid(row=1,column=0,sticky=W)
        self.txtFirstName=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=FirstName,width=20)
        self.txtFirstName.grid(row=1,column=1,pady=3,padx=20)



        self.lblSurname=Label(LeftFrame,font=('arial',12,'bold'),text="Surname",padx=2,bg="powder blue")
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Surname,width=20)
        self.txtSurname.grid(row=2,column=1,pady=3,padx=20)

        
        self.lblAddress=Label(LeftFrame,font=('arial',12,'bold'),text="Address",padx=2,bg="powder blue")
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Address,width=20)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        

        self.lblPostCode=Label(LeftFrame,font=('arial',12,'bold'),text="PostCode",padx=2,bg="powder blue")
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=PostCode,width=20)
        self.txtPostCode.grid(row=4,column=1,pady=3,padx=20)


                

        self.lblMobile=Label(LeftFrame,font=('arial',12,'bold'),text="Mobile",padx=2,bg="powder blue")
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Mobile,width=20)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)


        self.lblEmail=Label(LeftFrame,font=('arial',12,'bold'),text="Email",padx=2,bg="powder blue")
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=Email,width=20)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        

        self.lblNationality=Label(LeftFrame,font=('arial',12,'bold'),text="Nationality",padx=2,bg="powder blue")
        self.lblNationality.grid(row=7,column=0,sticky=W)
        self.cboNationality=ttk.Combobox(LeftFrame,textvariable=Nationality,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboNationality['value']=('','India','USA','China','UK','Australia','Bhutan')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7,column=1,pady=3,padx=20)



        self.lblDOB=Label(LeftFrame,font=('arial',12,'bold'),text="DOB",padx=2,bg="powder blue")
        self.lblDOB.grid(row=8,column=0,sticky=W)
        self.txtDOB=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=DOB,width=20)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20) 



        self.lblIDType=Label(LeftFrame,font=('arial',12,'bold'),text="IDType",padx=2,bg="powder blue")
        self.lblIDType.grid(row=9,column=0,sticky=W)
        self.cboIDType=ttk.Combobox(LeftFrame,textvariable=IDType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboIDType['value']=('','Pilot Licence','Driving Licence','StudentID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)        



        self.lblGender=Label(LeftFrame,font=('arial',12,'bold'),text="Gender",padx=2,bg="powder blue")
        self.lblGender.grid(row=10,column=0,sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame,textvariable=Gender,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)

        
        self.lblCheck_In_Date=Label(LeftFrame,font=('arial',12,'bold'),text="Check_In_Date",padx=2,bg="powder blue")
        self.lblCheck_In_Date.grid(row=11,column=0,sticky=W)
        self.txtCheck_In_Date=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CheckInDate,width=20)
        self.txtCheck_In_Date.grid(row=11,column=1,pady=3,padx=20)

        self.lblCheck_Out_Date=Label(LeftFrame,font=('arial',12,'bold'),text="Check_Out_Date",padx=2,bg="powder blue")
        self.lblCheck_Out_Date.grid(row=12,column=0,sticky=W)
        self.txtCheck_Out_Date=Entry(LeftFrame,font=('arial',12,'bold'),textvariable=CheckOutDate,width=20)
        self.txtCheck_Out_Date.grid(row=12,column=1,pady=3,padx=20)

        
        self.lblMeal=Label(LeftFrame,font=('arial',12,'bold'),text="Meal",padx=2,bg="powder blue")
        self.lblMeal.grid(row=13,column=0,sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame,textvariable=Meal,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner','All')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=4,padx=20)


        
        self.lblRoomType=Label(LeftFrame,font=('arial',12,'bold'),text="RoomType",padx=2,bg="powder blue")
        self.lblRoomType.grid(row=14,column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomType['value']=('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)


        
        self.lblRoomNo=Label(LeftFrame,font=('arial',12,'bold'),text="RoomNo",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=15,column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame,textvariable=RoomNo,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value']=('','001','002','003','004','005','006')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15,column=1,pady=3,padx=20)

                
        self.lblRoomExtNo=Label(LeftFrame,font=('arial',12,'bold'),text="RoomExtNo",padx=2,bg="powder blue")
        self.lblRoomExtNo.grid(row=16,column=0,sticky=W)
        self.cboRoomExtNo=ttk.Combobox(LeftFrame,textvariable=RoomExtNo,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomExtNo['value']=('','101','102','103','104','105','106')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16,column=1,pady=3,padx=20)

        self.lblLabel=Label(RightFrame,font=('arial',10,'bold'),pady=10,bg="cadet blue",
                            text="Customer Ref\tFirstname\tSurname\tAddress\tPostCode\tMobile\tNationality\tCheckInDate\tCheckOutDate")
        self.lblLabel.grid(row=0,column=0,columnspan=17)

        self.txtReceipt=Text(RightFrame,height=15,width=108,bd=10,font=('arial',11,'bold'))
        self.txtReceipt.grid(row=1,column=0,columnspan=2,padx=2,pady=5)


        self.lblDays=Label(RightFrame,font=('arial',14,'bold'),text="No of days",bd=7,bg="cadet blue",fg="black",)
        self.lblDays.grid(row=2,column=0,sticky=W)
        self.txtDays=Entry(RightFrame,font=('arial',14,'bold'),textvariable=TotalDays,bd=7,bg="white",width=67,justify=LEFT)
        self.txtDays.grid(row=2,column=1)

        self.lblPaidTax=Label(RightFrame,font=('arial',14,'bold'),text="Paid Tax",bd=7,bg="cadet blue",fg="black",)
        self.lblPaidTax.grid(row=3,column=0,sticky=W)
        self.txtPaidTax=Entry(RightFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7,bg="white",width=67,justify=LEFT)
        self.txtPaidTax.grid(row=3,column=1)

        
        self.lblSubTotal=Label(RightFrame,font=('arial',14,'bold'),text="SubTotal",bd=7,bg="cadet blue",fg="black",)
        self.lblSubTotal.grid(row=4,column=0,sticky=W)
        self.txtSubTotal=Entry(RightFrame,font=('arial',14,'bold'),textvariable=SubTotal,bd=7,bg="white",width=67,justify=LEFT)
        self.txtSubTotal.grid(row=4,column=1)

                
        self.lblTotalCost=Label(RightFrame,font=('arial',14,'bold'),text="TotalCost",bd=7,bg="cadet blue",fg="black",)
        self.lblTotalCost.grid(row=5,column=0,sticky=W)
        self.txtTotalCost=Entry(RightFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7,bg="white",width=67,justify=LEFT)
        self.txtTotalCost.grid(row=5,column=1)

        self.btnTotal=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),
                             width=21,height=2,bg="powder blue",text="Total",command=TotalCostandDate).grid(row=0,column=4,padx=4)        

        self.btnReceipt=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),
                             width=21,height=2,bg="powder blue",text="Receipt",command=Receipt).grid(row=0,column=5,padx=5)

        self.btnReset=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),
                             width=21,height=2,bg="powder blue",text="Reset",command=Reset).grid(row=0,column=6,padx=5) 

        self.btnExit=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),
                             width=21,height=2,bg="powder blue",text="Exit",command=iExit).grid(row=0,column=7,padx=5) 

if __name__=='__main__':
    root=Tk()
    application=Hotel(root)
    root.mainloop()
