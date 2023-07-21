from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
from mysql.connector import errorcode
import re

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x720+0+0")
        
        title = Label(self.root, text="Student Management System",bd=10,relief=GROOVE, font=("Arial Rounded MT Bold",35, "bold"), bg="light grey", fg="black")
        title.pack(side=TOP,fill=X)
        
      #---------Variables-----------
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.em_var=StringVar()
        self.ph_var=StringVar()
        self.gen_var=StringVar()
        self.dep_var=StringVar()
        self.ht_var=StringVar()
        self.cg_var=StringVar()
        
        self.search=StringVar()
        self.search_txt=StringVar()
      
      #----------Manage----------------
        
        Manage_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#0DBBB7")
        Manage_Frame.place(x=25,y=90,width=460,height=600)
        
        mtitle = Label(Manage_Frame, text="Student Management",font=("Arial Rounded MT Bold",20), bg="#D6D4D4", fg="black")
        mtitle.grid(row=0,columnspan=2,pady=6,padx=85)
        
        roll=Label(Manage_Frame, text="Roll No.",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        roll.grid(row=1,column =0, pady=7,padx=12,sticky="w")
        
        txt_roll=Entry(Manage_Frame,textvariable=self.roll_var,bd=5,relief=GROOVE, font=("Candara",14,"bold"), bg="white", fg="black")
        txt_roll.grid(row=1,column =1, pady=7,padx=12,sticky="w")
        
        name=Label(Manage_Frame, text="Name",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        name.grid(row=2,column =0,  pady=12,padx=12,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,bd=5,relief=GROOVE,font=("Candara",14,"bold"), bg="white", fg="black")
        txt_name.grid(row=2,column =1,  pady=12,padx=12,sticky="w")
        
        em=Label(Manage_Frame, text="Email",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        em.grid(row=3,column =0,  pady=12,padx=12,sticky="w")
        
        txt_em=Entry(Manage_Frame,textvariable=self.em_var,bd=5,relief=GROOVE,font=("Candara",14,"bold"), bg="white", fg="black")
        txt_em.grid(row=3,column =1,  pady=12,padx=12,sticky="w")
        
        ph=Label(Manage_Frame, text="Phone No.",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        ph.grid(row=4,column =0,  pady=12,padx=12,sticky="w")
        
        txt_ph=Entry(Manage_Frame,textvariable=self.ph_var,bd=5,relief=GROOVE,font=("Candara",14,"bold"), bg="white", fg="black")
        txt_ph.grid(row=4,column =1,  pady=12,padx=12,sticky="w")
        
        gen=Label(Manage_Frame, text="Gender",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        gen.grid(row=5,column =0,  pady=12,padx=12,sticky="w")
        
        gen_comb=ttk.Combobox(Manage_Frame,textvariable=self.gen_var, font=("Candara",13,"bold"),state='readonly')
        gen_comb['values']=["MALE","FEMALE","OTHERS"]
        gen_comb.grid(row=5,column =1,  pady=12,padx=12,sticky="w")
        
        dp=Label(Manage_Frame, text="Department",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        dp.grid(row=6,column =0,  pady=12,padx=12,sticky="w")
        
        dep_comb=ttk.Combobox(Manage_Frame,textvariable=self.dep_var,font=("Candara",13,"bold"),state='readonly')
        dep_comb['values']=["CSE","IT","ECE","EEE","MECH","CHEM","PROD","CIV","BIO"]
        dep_comb.grid(row=6,column =1,  pady=12,padx=12,sticky="w")
        
        ht=Label(Manage_Frame, text="Hostel No.",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        ht.grid(row=7,column =0,  pady=12,padx=12,sticky="w")
        
        txt_ht=Entry(Manage_Frame,textvariable=self.ht_var,bd=5,relief=GROOVE,font=("Candara",14,"bold"), bg="white", fg="black")
        txt_ht.grid(row=7,column =1,  pady=12,padx=12,sticky="w")
        
        cg=Label(Manage_Frame, text="CGPA",font=("Arial Rounded MT Bold",14), bg="#0DBBB7", fg="black")
        cg.grid(row=8,column =0,  pady=12,padx=12,sticky="w")
        
        txt_cg=Entry(Manage_Frame,textvariable=self.cg_var,bd=5,relief=GROOVE,font=("Candara",14,"bold"), bg="white", fg="black")
        txt_cg.grid(row=8,column =1,  pady=12,padx=12,sticky="w")
        
        
     #--------------Buttons-----------
        
        But_Frame=Frame(Manage_Frame,bd=3,relief=RIDGE,bg="#0DBBB7")
        But_Frame.place(x=12,y=510,width=425)   
        
        AddB=Button(But_Frame,command=self.add_data,text="Add",font=("Arial Rounded MT Bold",11),width=8,activebackground="#A0D565").grid(row=0,column=0,padx=9,pady=10)
        DeleteB=Button(But_Frame,command=self.delete,text="Delete",font=("Arial Rounded MT Bold",11),width=9,activebackground="#A0D565").grid(row=0,column=1,padx=9,pady=10)
        UpdateB=Button(But_Frame,command=self.update,text="Update",font=("Arial Rounded MT Bold",11),width=9,activebackground="#A0D565").grid(row=0,column=2,padx=9,pady=10)
        ClearB=Button(But_Frame,command=self.clear,text="Clear",font=("Arial Rounded MT Bold",11),width=8,activebackground="#A0D565").grid(row=0,column=3,padx=9,pady=10)
      
        
      #---------------Details----------
        
        Det_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#0DBBB7")
        Det_Frame.place(x=500,y=90,width=840,height=600)
        
        lb_sch=Label(Det_Frame, text="Search By",font=("Arial Rounded MT Bold",18), bg="#0DBBB7", fg="black")
        lb_sch.grid(row=0,column =0,  pady=10,padx=20,sticky="w")
        
        sch_comb=ttk.Combobox(Det_Frame,width=10,textvariable=self.search, font=("Candara",14,"bold"),state='readonly')
        sch_comb['values']=["Roll No.","Name","Gender","Department","Hostel","CGPA"]
        sch_comb.grid(row=0,column =1,  pady=12,padx=8,sticky="w")
        
        txt_sch=Entry(Det_Frame,textvariable=self.search_txt,bd=5,width = 18,relief=GROOVE, font=("Candara",14,"bold"), bg="white", fg="black")
        txt_sch.grid(row=0,column =2,  pady=12,padx=12,sticky="w")
        
        sch_but=Button(Det_Frame,command=self.searchdata,text="Search",font=("Arial Rounded MT Bold",11),bd=5,relief=GROOVE,width=10,activebackground="#A0D565").grid(row=0,column=3,padx=10,pady=10)
        rst_but=Button(Det_Frame,command=self.fetch_data,text="Reset",font=("Arial Rounded MT Bold",11),bd=5,relief=GROOVE,width=10,activebackground="red").grid(row=0,column=4,padx=10,pady=10)
        
        #--------------Table----------------
        
        Tbl_Frame=Frame(Det_Frame,bd=5,relief=RIDGE,bg="#0DBBB7")
        Tbl_Frame.place(x=10,y=70,width=760,height=500)
      
        s_x=Scrollbar(Tbl_Frame,orient=HORIZONTAL)
        s_y=Scrollbar(Tbl_Frame,orient=VERTICAL)
        
        self.St_Table=ttk.Treeview(Tbl_Frame,columns=("Roll No.","Name","Email","Phone No.","Gender","Department","Hostel No.","CGPA"),xscrollcommand=s_x.set,yscrollcommand=s_y.set)
        
        s_x.pack(side=BOTTOM,fill=X)
        s_y.pack(side=RIGHT,fill=Y)
        s_x.config(command=self.St_Table.xview)
        s_y.config(command=self.St_Table.yview)        
        self.St_Table.heading("Roll No.",text="Roll No.")
        self.St_Table.heading("Name",text="Name")
        self.St_Table.heading("Email",text="Email")
        self.St_Table.heading("Phone No.",text="Phone No.")
        self.St_Table.heading("Gender",text="Gender")
        self.St_Table.heading("Department",text="Department")
        self.St_Table.heading("Hostel No.",text="Hostel No.")
        self.St_Table.heading("CGPA",text="CGPA")
        self.St_Table['show']='headings'
        self.St_Table.pack(fill=BOTH,expand=1) 
        self.St_Table.bind("<ButtonRelease>",self.cursor)
        self.fetch_data() 
        
    def  add_data(self):
      if (self.roll_var.get()=="" or self.name_var.get()=="" or self.em_var.get()=="" or self.ph_var.get()=="" or self.gen_var.get()=="" or self.dep_var.get()=="" or self.ht_var.get()=="" or self.cg_var.get()==""):
         messagebox.showerror("ERROR","All Fields Must Be Filled")
      else:
         try:
          conn=mysql.connector.connect(host="localhost",username="root",password="Rishav@14",database="std")
          curs=conn.cursor()
          curs.execute("insert into stdata values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.roll_var.get(),
                                                                               self.name_var.get(),
                                                                               self.em_var.get(),
                                                                               self.ph_var.get(),
                                                                               self.gen_var.get(),
                                                                               self.dep_var.get(),
                                                                               self.ht_var.get(),
                                                                               self.cg_var.get()))
        
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("SUCCESS","Data Has Been Added",parent=self.root)
         except Exception as es:
           messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
    
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Rishav@14",database="std")
      curs=conn.cursor()
      curs.execute("select * from stdata")
      rows=curs.fetchall()
      if len(rows)!=0:
        self.St_Table.delete(*self.St_Table.get_children())
        for i in rows:
          self.St_Table.insert('',END,values=i)
        conn.commit()
      conn.close()
    
    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.em_var.set("")
        self.ph_var.set("")
        self.gen_var.set("")
        self.dep_var.set("")
        self.ht_var.set("")
        self.cg_var.set("")
        
    def cursor(self,event=""):
       row_cursor=self.St_Table.focus()
       content=self.St_Table.item(row_cursor)
       data=content["values"]
       self.roll_var.set(data[0])
       self.name_var.set(data[1])
       self.em_var.set(data[2])
       self.ph_var.set(data[3])
       self.gen_var.set(data[4])
       self.dep_var.set(data[5])
       self.ht_var.set(data[6])
       self.cg_var.set(data[7])   
       
    def update(self):
       if (self.roll_var.get()=="" or self.name_var.get()=="" or self.em_var.get()=="" or self.ph_var.get()=="" or self.gen_var.get()=="" or self.dep_var.get()=="" or self.ht_var.get()=="" or self.cg_var.get()==""):
         messagebox.showerror("ERROR","All Fields Must Be Filled")
       else:
        update=messagebox.askyesno("UPDATE","Are You Sure You Want To Update The Student Data",parent=self.root)
        try:
          if update>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rishav@14",database="std")
            curs=conn.cursor()
            curs.execute("update stdata set name=%s,email=%s,phone=%s,gender=%s,department=%s,hostel=%s,cgpa=%s where roll_no=%s",(self.name_var.get(),
                                                                               self.em_var.get(),
                                                                               self.ph_var.get(),
                                                                               self.gen_var.get(),
                                                                               self.dep_var.get(),
                                                                               self.ht_var.get(),
                                                                               self.cg_var.get(),
                                                                               self.roll_var.get()))
          else:
           if not update:
             return
                       
        
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("SUCCESS","Data Has Been Updated",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
            
    def delete(self):
      delete=messagebox.askyesno("DELETE","Are You Sure You Want To Delete The Student Data",parent=self.root)
      
      if delete>0:
        conn=mysql.connector.connect(host="localhost",username="root",password="Rishav@14",database="std")
        curs=conn.cursor()
        curs.execute("delete from stdata where roll_no=%s",(self.roll_var.get(),))
      else:
        if not delete:
          return
            
      conn.commit()
      conn.close()
      self.fetch_data()
      self.clear()
      
    def searchdata(self):
      if (self.search.get()=="" or self.search_txt.get()==""):
        messagebox.showerror("ERROR","Make A Selection")    
      else:
         conn=mysql.connector.connect(host="localhost",username="root",password="Rishav@14",database="std")
         curs=conn.cursor()
         if (self.search.get()=="Roll No."):
           curs.execute("select * from stdata where roll_no LIKE '%"+str(self.search_txt.get())+"%'")
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         if (self.search.get()=="CGPA"):
           query = "SELECT * FROM stdata WHERE cgpa >= %s"
           cgpa_filter = float(self.search_txt.get())  
           values = (cgpa_filter,)
           curs.execute(query, values)
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         if (self.search.get()=="Name"):
           curs.execute("select * from stdata where name LIKE '%"+str(self.search_txt.get())+"%'")
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         if (self.search.get()=="Gender"):
           query = "SELECT * FROM stdata WHERE gender REGEXP %s"
           pattern = r"\b" + re.escape(self.search_txt.get()) + r"\b"
           values = [pattern]
           curs.execute(query, values)
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         if (self.search.get()=="Department"):
           curs.execute("select * from stdata where department LIKE '%"+str(self.search_txt.get())+"%'")
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         if (self.search.get()=="Hostel"):
           curs.execute("select * from stdata where hostel LIKE '%"+str(self.search_txt.get())+"%'")
           rows=curs.fetchall()
           if len(rows)!=0:
            self.St_Table.delete(*self.St_Table.get_children())
            for i in rows:
              self.St_Table.insert('',END,values=i)
              conn.commit()
           conn.close()
         
 
              
        
        
        
root = Tk()
ob = Student(root)
root.mainloop()
