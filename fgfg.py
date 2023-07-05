self.detector = cv2.CascadeClassifier(self.harcascadePath)
        ft = open("ld.txt", "r")
        a,b=ft.read().split(",")
        ft.close()
        nam=""
        self.Id =a
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
            my_c = con.cursor()
            my_c.execute("select * from login where Username=%s Type=%s",(a,b))
            data = my_c.fetchone()
            fn=data[3]
            ln=data[4]
            nam=fn+" "+ln

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.window)


        self.name =nam