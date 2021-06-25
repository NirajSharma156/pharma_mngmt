            conn.close()
            messagebox.showinfo("Success","data has been inserted")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row=content["values"]


        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])            
     
