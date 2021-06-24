        #========== side frame ===============
        side_frame = Frame(DataFramerRight,bd = 4,relief = RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height = 160)
        
        sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=x)
        sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=y)

        self.medicine_table = ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)


        #====================== Medicine Add  Buttons=========================
        down_frame = Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=135,height=160)

        btnAddmed = Button(down_frame,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed = Button(down_frame,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)


        btnDeletemed = Button(down_frame,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)


        btnClearmed = Button(down_frame,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)


        #========================= Frame Details =================================
        Framedeatils=Frame(self.root,,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1530,height=210)

