from tkinter import *
from chat import get_response, bot_name
from PIL import ImageTk, Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Combobox
from data import get_data, conn
from ttkbootstrap.tableview import Tableview
from data import header, data_list
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 15 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = ttk.Window(themename="vapor")
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550)
        self.login_window()
        
    def run(self):
        self.window.mainloop()


    def error_form(self):
        error_win = Toplevel(self.window)
        error_win.wm_title("Error")
        message_label = Label(error_win, text="Please Fill Form", font="Helvetica 14 bold")
        message_label.place(relwidth=1)
        b = Button(error_win, text="Ok",command=self.login_window, font=FONT)
        b.place(relx= 0.25, rely=0.5, relwidth=0.5)
    
    def error_pass(self):
        error_win = Toplevel(self.window)
        error_win.wm_title("Error")
        message_label = Label(error_win, text="Wrong Password", font="Helvetica 14 bold")
        message_label.place(relwidth=1)
        b = Button(error_win, text="Ok",command=self.login_window, font=FONT)
        b.place(relx= 0.25, rely=0.5, relwidth=0.5)
    
    def error_feedback(self):
        error_win = Toplevel(self.window)
        error_win.wm_title("Error")
        message_label = Label(error_win, text="Please Give Feedback", font="Helvetica 12 bold")
        message_label.place(relwidth=1)
        b = Button(error_win, text="Ok",command=self.feedback_popup, font=FONT)
        b.place(relx= 0.25, rely=0.5, relwidth=0.5)


    def feedback_popup(self):
        self.win = Toplevel(self.window)
        self.win.wm_title("Feedback")
        head_label = Label(self.window, text="Feedback", font="Helvetica 12 bold")
        head_label.place(relwidth=1)
        self.win.configure(width=200,height=200)
        l = Label(self.win, text="Are You Satisfied with UBot?")
        l.grid(row=3, column=2)
        self.feedback = Entry(self.win)
        self.feedback.bind('<Return>', self.f_submit)
        self.feedback.focus()
        self.feedback.grid(row = 3, column=3)
        
        b = Button(self.win, text="Submit",command=lambda:self.f_submit(None), font=FONT)
        b.grid(row=5, column=2)
    
    def f_submit(self, event):
        if self.feedback.get() == '':
            self.error_feedback()
        else:
            get_data(self.name,self.depart,self.feedback.get())
            self.login_window()
    
    def login_window(self):
        for i in self.window.winfo_children():
            i.destroy()
        head_label = Label(self.window, text="Login Page", font="Helvetica 20 bold")
        head_label.place(relwidth=1)
        img = Image.open('bot.png')
        img = img.resize((150, 140), Image.ANTIALIAS)
        
        self.my_img = ImageTk.PhotoImage(img)
        photo_label = Label(image=self.my_img, anchor=CENTER)
        photo_label.place(relx=0.37,rely=0.13)

        # Create a label for the form
        Name_label = Label(self.window, text="Enter Your Name:",font="Helvetica 18")
        Name_label.place(relx=0.15,rely=0.45)

        # Create a text entry widget for the form
        self.Name_entry = Entry(self.window)
        self.Name_entry.place(relx=0.63,rely=0.454)
        self.Name_entry.config(width=12, font=FONT)
        self.Name_entry.focus()
        # Create a text entry widget for the form
        dep_label = Label(self.window, text = "Select Your Department:",font="Helvetica 18")
        dep_label.place(relx=0.03,rely=0.60)
        options = ["CS", "Admin", "Outsider","Law","DVM","DPT","EE","SE"]
        self.dropdown = Combobox(self.window, values=options, state="readonly")
        self.dropdown.current(0)  # set the default value
        self.dropdown.place(relx=0.63,rely=0.60)
        self.dropdown.config(width=10, font=FONT)
        # Create a submit button for the form
        submit_button = Button(self.window, text="Submit", command=self.submit_form,font=FONT_BOLD, width= 7,height=2)
        submit_button.place(relx=0.40,rely=0.75)


    def admin_pass(self):
        form = Toplevel(self.window)
        form.title("Form")
        form.geometry("200x200")

        # Create a label for the form
        label = Label(form, text="Enter Password")
        label.pack()
        self.pass_entry = Entry(form)
        self.pass_entry.pack()
        self.pass_entry.bind('<Return>', self.feedback_table)
        self.pass_entry.focus()
        submit_button = Button(form, text="Submit", command=self.feedback_table)
        submit_button.pack()

    def feedback_table(self):
        if self.pass_entry.get() == '1234':
            for i in self.window.winfo_children():
                i.destroy()
            head_label = Label(self.window, text="Feedback Page", font=FONT_BOLD)
            head_label.place(relwidth=1)
            line = Label(self.window, width=470)
            line.place(relwidth=1, rely=0.07, relheight=0.1)

            dv = Tableview(
                master=self.window,
                coldata=header,
                rowdata=data_list,
                bootstyle=PRIMARY,
                pagesize=10,
                height=10,
                autofit=True,
                stripecolor=('green', None)
            )
            dv.place(relwidth=1, relheight= 0.70, rely= 0.13)

            btn = Button(self.window, text="Back",font=FONT_BOLD, command= self.login_window)
            btn.place(relwidth=0.25, relx= 0.6, rely = 0.9)
        else:
            self.error_pass()
    
    def submit_form(self):
        self.name = self.Name_entry.get()
        self.depart = self.dropdown.get()
        if self.depart == "Admin":
            self.admin_pass()
        else:
            if self.name == '':
                self.error_form()
            else:
                self.chat_window()



    def chat_window(self):
        for i in self.window.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.window, text="Let's Chat", font=FONT_BOLD, pady=5)
        head_label.place(relwidth=0.3)
        img = Image.open('bot.png')
        img = img.resize((30, 30), Image.ANTIALIAS)
        
        self.my_icon = ImageTk.PhotoImage(img)
        photo_label = Label(image=self.my_icon, anchor=CENTER)
        photo_label.place(relx=0.30)
        btn = Button(self.window, text="Finish",font=FONT_BOLD, command= self.feedback_popup)
        btn.place(relwidth=0.25, relx= 0.70, rely = 0.01)
        # tiny divider
        line = Label(self.window, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, font=FONT, padx=10, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=0.95, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.window)
        scrollbar.place(relheight=0.745, relx=0.964, rely=0.08)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        btn_img = Image.open('send.png')
        btn_img = btn_img.resize((30, 30), Image.ANTIALIAS)
        self.my_btn = ImageTk.PhotoImage(btn_img)
        send_button = Button(bottom_label, text="Send",image=self.my_btn, font=FONT_BOLD, width=20,compound=RIGHT,
                            command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, self.name)
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
    
        
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
    conn.close()