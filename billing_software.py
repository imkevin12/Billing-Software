from future.moves.tkinter import *
import random, os
from tkinter import messagebox


class Bill:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")

        # Title
        bg_color = '#074463'
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE,
                      font=("times new roman", 30, "bold"), pady=2, bg=bg_color, fg="white")
        title.pack(fill=X)

        # *************** All Variables *************** #
        # Customer Variables
        self.cnameVar = StringVar()
        self.cphoneVar = StringVar()
        self.search_billVar = StringVar()       # To search the already existing bills in the records

        self.bill_noVar = StringVar()           # To show the current customer bill
        x = random.randint(1000, 9999)          # Random Bill Number
        self.bill_noVar.set(str(x))

        # Cosmetics
        self.bath_soapVar = IntVar()
        self.face_creamVar = IntVar()
        self.face_washVar = IntVar()
        self.hair_sprayVar = IntVar()
        self.hair_gelVar = IntVar()
        self.body_lotionVar = IntVar()

        # Grocery
        self.riceVar = IntVar()
        self.food_oilVar = IntVar()
        self.daalVar = IntVar()
        self.wheatVar = IntVar()
        self.sugarVar = IntVar()
        self.teaVar = IntVar()

        # Cold Drinks
        self.maazaVar = IntVar()
        self.coca_colaVar = IntVar()
        self.frootiVar = IntVar()
        self.thumbs_upVar = IntVar()
        self.limcaVar = IntVar()
        self.spriteVar = IntVar()

        # Price Variables
        self.cosmetic_priceVar = StringVar()
        self.grocery_priceVar = StringVar()
        self.cold_drink_priceVar = StringVar()

        # Tax Variables
        self.cosmetic_taxVar = StringVar()
        self.grocery_taxVar = StringVar()
        self.cold_drink_taxVar = StringVar()

        # *************** Customer Details Frame*************** #
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, pady=5, padx=20, sticky="w")
        cname_entry = Entry(F1, width=15, textvariable=self.cnameVar, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, pady=5, padx=20, sticky="w")
        cphone_entry = Entry(F1, width=15, textvariable=self.cphoneVar, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, pady=5, padx=20, sticky="w")
        bill_entry = Entry(F1, width=15, textvariable=self.search_billVar, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        search_btn = Button(F1, text="Search", command=self.find, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=40, pady=10)

        # *************** Cosmetics Frame *************** #
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        soap_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        soap_entry = Entry(F2, width=10, textvariable=self.bath_soapVar, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_entry = Entry(F2, width=10, textvariable=self.face_creamVar, font=("times new roman", 16, "bold"),
                               bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_wash_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_wash_entry = Entry(F2, width=10, textvariable=self.face_washVar, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hair_spray_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_spray_entry = Entry(F2, width=10, textvariable=self.hair_sprayVar, font=("times new roman", 16, "bold"),
                               bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hair_gel_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_entry = Entry(F2, width=10, textvariable=self.hair_gelVar, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lotion_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_lotion_entry = Entry(F2, width=10, textvariable=self.body_lotionVar, font=("times new roman", 16, "bold"),
                                bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # *************** Grocery Frame *************** #
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=330, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_entry = Entry(F3, width=10, textvariable=self.riceVar, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        food_oil_entry = Entry(F3, width=10, textvariable=self.food_oilVar, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_entry = Entry(F3, width=10, textvariable=self.daalVar, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_entry = Entry(F3, width=10, textvariable=self.wheatVar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        sugar_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sugar_entry = Entry(F3, width=10, textvariable=self.sugarVar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        tea_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tea_entry = Entry(F3, width=10, textvariable=self.teaVar, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # *************** Cold Drinks Frame *************** #
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=655, y=180, width=325, height=380)

        maaza_lbl = Label(F4, text="Maaza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        maaza_entry = Entry(F4, width=10, textvariable=self.maazaVar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        coca_cola_lbl = Label(F4, text="Coca-Cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        coca_cola_entry = Entry(F4, width=10, textvariable=self.coca_colaVar, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        frooti_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_wash_entry = Entry(F4, width=10, textvariable=self.frootiVar, font=("times new roman", 16, "bold"), bd=5,
                                relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        thumbs_up_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumbs_up_entry = Entry(F4, width=10, textvariable=self.thumbs_upVar, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_entry = Entry(F4, width=10, textvariable=self.limcaVar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        sprite_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_entry = Entry(F4, width=10, textvariable=self.spriteVar, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # *************** Bill Area Frame *************** #
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=980, y=180, width=370, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # Scroll Bar in Y direction
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # *************** Bill Menu Frame *************** #
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        # Total
        tcp_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        tcp_entry = Entry(F6, width=18, textvariable=self.cosmetic_priceVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        tgp_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        tgp_entry = Entry(F6, width=18, textvariable=self.grocery_priceVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        tcdp_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        tcdp_entry = Entry(F6, width=18, textvariable=self.cold_drink_priceVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        # Taxes
        ct_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        ct_entry = Entry(F6, width=18, textvariable=self.cosmetic_taxVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        gt_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        gt_entry = Entry(F6, width=18, textvariable=self.grocery_taxVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        cdt_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        cdt_entry = Entry(F6, width=18, textvariable=self.cold_drink_taxVar, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        # *************** Button Frame *************** #
        btn_frame = Frame(F6, bd=7, relief=GROOVE)
        btn_frame.place(x=750, width=580, height=102)

        total_btn = Button(btn_frame, command=self.total, text="Total", bg="cadetblue", fg="white", pady=15, bd=2,
                           width=10, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        generate_bill_btn = Button(btn_frame, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",
                            pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_frame, text="Clear", command=self.clear, bg="cadetblue", fg="white", pady=15, bd=2,
                           width=10, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_frame, text="Exit", command=self.exit, bg="cadetblue", fg="white", pady=15, bd=2,
                          width=10, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

        self.welcome()  # To show welcome message each time when constructor get called

    def total(self):
        self.cost_bath_soapVar = self.bath_soapVar.get() * 40
        self.cost_face_creamVar = self.face_creamVar.get() * 120
        self.cost_face_washVar = self.face_washVar.get() * 80
        self.cost_hair_sprayVar = self.hair_sprayVar.get() * 150
        self.cost_hair_gelVar = self.hair_gelVar.get() * 80
        self.cost_body_lotionVar = self.body_lotionVar.get() * 130
        self.total_cosmetic_price = float(
            self.cost_bath_soapVar +
            self.cost_face_creamVar +
            self.cost_face_washVar +
            self.cost_hair_sprayVar +
            self.cost_hair_gelVar +
            self.cost_body_lotionVar
        )
        self.cosmetic_priceVar.set("Rs. " + str(self.total_cosmetic_price))
        # Tax on Cosmetic products is 10%
        self.total_cosmetic_tax = round((self.total_cosmetic_price * 0.1), 2)
        self.cosmetic_taxVar.set("Rs. " + str(self.total_cosmetic_tax))

        self.cost_riceVar = self.riceVar.get() * 125
        self.cost_food_oilVar = self.food_oilVar.get() * 130
        self.cost_daalVar = self.daalVar.get() * 150
        self.cost_wheatVar = self.wheatVar.get() * 40
        self.cost_sugarVar = self.sugarVar.get() * 45
        self.cost_teaVar = self.teaVar.get() * 180
        self.total_grocery_price = float(
            self.cost_riceVar +
            self.cost_food_oilVar +
            self.cost_daalVar +
            self.cost_wheatVar +
            self.cost_sugarVar +
            self.cost_teaVar
        )
        self.grocery_priceVar.set("Rs. " + str(self.total_grocery_price))
        # Tax on Grocery products is 5%
        self.total_grocery_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_taxVar.set("Rs. " + str(self.total_grocery_tax))

        self.cost_maazaVar = self.maazaVar.get() * 65
        self.cost_coca_colaVar = self.coca_colaVar.get() * 90
        self.cost_frootiVar = self.frootiVar.get() * 70
        self.cost_thumbs_upVar = self.thumbs_upVar.get() * 120
        self.cost_limcaVar = self.limcaVar.get() * 40
        self.cost_spriteVar = self.spriteVar.get() * 55
        self.total_cold_drink_price = float(
            self.cost_maazaVar +
            self.cost_coca_colaVar +
            self.cost_frootiVar +
            self.cost_thumbs_upVar +
            self.cost_limcaVar +
            self.cost_spriteVar
        )
        self.cold_drink_priceVar.set("Rs. " + str(self.total_cold_drink_price))
        # Tax on Cold Drinks is 8%
        self.total_cold_drink_tax = round((self.total_cold_drink_price * 0.08), 2)
        self.cold_drink_taxVar.set("Rs. " + str(self.total_cold_drink_tax))

        self.final_bill = "Rs. " + str(float(self.total_cosmetic_price + self.total_cosmetic_tax +
                                             self.total_grocery_price + self.total_cosmetic_tax +
                                             self.total_cold_drink_price + self.total_cold_drink_tax
                                             ))

    def welcome(self):
        self.textarea.delete('1.0', END)  # To delete the previous data
        self.textarea.insert(END, "\tWelcome to KEVIN.in !\n")
        self.textarea.insert(END, f"\n Bill Number: {self.bill_noVar.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.cnameVar.get()}")
        self.textarea.insert(END, f"\n Phone Number: {self.cphoneVar.get()}")
        self.textarea.insert(END, f"\n =======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\tCOST")
        self.textarea.insert(END, f"\n =======================================")

    def bill_area(self):
        if self.cnameVar.get() == "" or self.cphoneVar.get() == "":
            messagebox.showerror("Error", "Customer details are must !")
        elif self.cosmetic_priceVar.get() == "Rs. 0.0" and self.grocery_priceVar.get() == "Rs. 0.0" and self.cold_drink_priceVar.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased !")
        else:
            self.welcome()

            # Cosmetics
            if self.bath_soapVar.get() != 0:
                self.textarea.insert(END, f"\n Bath Soap\t\t{self.bath_soapVar.get()}\t{self.cost_bath_soapVar}")
            if self.face_creamVar.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.face_creamVar.get()}\t{self.cost_face_creamVar}")
            if self.face_washVar.get() != 0:
                self.textarea.insert(END, f"\n Face Wash\t\t{self.face_washVar.get()}\t{self.cost_face_washVar}")
            if self.hair_sprayVar.get() != 0:
                self.textarea.insert(END, f"\n Hair Spray\t\t{self.hair_sprayVar.get()}\t{self.cost_hair_sprayVar}")
            if self.hair_gelVar.get() != 0:
                self.textarea.insert(END, f"\n Hair Gel\t\t{self.hair_gelVar.get()}\t{self.cost_hair_gelVar}")
            if self.body_lotionVar.get() != 0:
                self.textarea.insert(END, f"\n Body Lotion\t\t{self.body_lotionVar.get()}\t{self.cost_body_lotionVar}")

            # Grocery
            if self.riceVar.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t{self.riceVar.get()}\t{self.cost_riceVar}")
            if self.food_oilVar.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t{self.food_oilVar.get()}\t{self.cost_food_oilVar}")
            if self.daalVar.get() != 0:
                self.textarea.insert(END, f"\n Daal\t\t{self.daalVar.get()}\t{self.cost_daalVar}")
            if self.wheatVar.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t{self.wheatVar.get()}\t{self.cost_wheatVar}")
            if self.teaVar.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t{self.teaVar.get()}\t{self.cost_teaVar}")
            if self.sugarVar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t{self.sugarVar.get()}\t{self.cost_sugarVar}")

            # Cold Drinks
            if self.maazaVar.get() != 0:
                self.textarea.insert(END, f"\n Maaza\t\t{self.maazaVar.get()}\t{self.cost_maazaVar}")
            if self.coca_colaVar.get() != 0:
                self.textarea.insert(END, f"\n Coca-Cola\t\t{self.coca_colaVar.get()}\t{self.cost_coca_colaVar}")
            if self.frootiVar.get() != 0:
                self.textarea.insert(END, f"\n Frooti\t\t{self.frootiVar.get()}\t{self.cost_frootiVar}")
            if self.thumbs_upVar.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t{self.thumbs_upVar.get()}\t{self.cost_thumbs_upVar}")
            if self.limcaVar.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t{self.limcaVar.get()}\t{self.cost_limcaVar}")
            if self.spriteVar.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t{self.spriteVar.get()}\t{self.cost_sugarVar}")

            self.textarea.insert(END, f"\n ---------------------------------------")

            if self.cosmetic_taxVar.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_taxVar.get()}")
            if self.grocery_taxVar.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_taxVar.get()}")
            if self.cold_drink_taxVar.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drink_taxVar.get()}")
            self.textarea.insert(END, f"\n\n Total Bill\t\t\t{self.final_bill}")

            self.textarea.insert(END, f"\n ---------------------------------------")
            self.save()

    def save(self):
        option = messagebox.askyesno("Save Bill", "Do you want to save bill?")
        if option > 0:
            self.bill_data = self.textarea.get('1.0', END)
            file = open("E:/dell/Python/Temp/bills/" + str(self.bill_noVar.get()) + ".txt", "w")
            file.write(self.bill_data)
            file.close()
            messagebox.showinfo("Saved", f"Bill No. {self.bill_noVar.get()} saved Successfully")
        else:
            return

    def find(self):
        present = "no"
        for i in os.listdir("E:/dell/Python/Temp/bills/"):
            if i.split('.')[0] == self.search_billVar.get():
                file = open(f"E:/dell/Python/Temp/bills/{i}", "r")
                self.textarea.delete('1.0', END)
                for j in file:
                    self.textarea.insert(END, j)
                file.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear(self):
        option = messagebox.askyesno("Clear!", "Do you want to clear?")
        if option > 0:
            # Customer Variables
            self.cnameVar.set("")
            self.cphoneVar.set("")
            self.search_billVar.set("")

            self.bill_noVar.set("")
            x = random.randint(1000, 9999)
            self.bill_noVar.set(str(x))

            # Cosmetics
            self.bath_soapVar.set(0)
            self.face_creamVar.set(0)
            self.face_washVar.set(0)
            self.hair_sprayVar.set(0)
            self.hair_gelVar.set(0)
            self.body_lotionVar.set(0)

            # Grocery
            self.riceVar.set(0)
            self.food_oilVar.set(0)
            self.daalVar.set(0)
            self.wheatVar.set(0)
            self.sugarVar.set(0)
            self.teaVar.set(0)

            # Cold Drinks
            self.maazaVar.set(0)
            self.coca_colaVar.set(0)
            self.frootiVar.set(0)
            self.thumbs_upVar.set(0)
            self.limcaVar.set(0)
            self.spriteVar.set(0)

            # Total Products Price & Tax Variables
            # Price
            self.cosmetic_priceVar.set("")
            self.grocery_priceVar.set("")
            self.cold_drink_priceVar.set("")
            # Tax
            self.cosmetic_taxVar.set("")
            self.grocery_taxVar.set("")
            self.cold_drink_taxVar.set("")

            self.welcome()

    def exit(self):
        option = messagebox.askyesno("Exit!", "Do you want to exit?")
        if option > 0:
            self.root.destroy()


root = Tk()
bill = Bill(root)
root.mainloop()
