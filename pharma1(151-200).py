        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt = Entry(DataFrameLeft,font = ("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)

        #=================== Images ===============
        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text = "Stay Home Stay Safe:",padx=2,pady=6,bg="white",fg="blue",width=37)
        lblhome.place(x=415,y=140)

        img2=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2);
        b1 = Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=770,y=330)

        img3=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=330)
        
        img4=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=475,y=330)


        #================== dataframeRight =========================

        DataFramerRight = LabelFrame(DataFrame,bd=10,relief=Ridge,padx=20,text="Medicine Add Department",
                        fg="darkgreen",font=("arial",12,"bold"))
        DataFramerRight.place(x=910,y=5,width=540,height=350)


        img5=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img5=img5.resize((150,135),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)               

        img6=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img6=img6.resize((150,135),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=960,y=160)

        img7=Image.open("G:/Pharmacy Management System Project/tab.jpg")
        img7=img7.resize((150,135),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=960,y=160)