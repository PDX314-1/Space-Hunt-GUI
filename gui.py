import tkinter

click_ctr=0
def click_up():
   global click_ctr
   click_ctr=click_ctr+1
   lbl_header_3 = tkinter.Label(text="CTR: "+str(click_ctr))
   lbl_header_3.pack()
   return



main_window = tkinter.Tk()
main_window.title("G.S.S. Old Spice")
main_window.geometry("600x600")

lbl_header_1 = tkinter.Label(text="G.S.S. Old Spice Bridge Display", font=("Arial",12,"bold"))

lbl_header_2 = tkinter.Label(text="Distance")
distance_input = tkinter.Text(height=1,width=5)
lbl_header_3 = tkinter.Label(text="Direction")
direction_input = tkinter.Text(height=1,width=5)

btn_proceed = tkinter.Button(main_window, text="Proceed", command=click_up)

lbl_header_1.place(relx=0.0,rely=0.0, anchor='nw')
lbl_header_2.place(relx=0.0,rely=0.05, anchor='nw')
distance_input.place(relx=0.1,rely=0.05, anchor='nw')
lbl_header_3.place(relx=0.0,rely=0.1, anchor='nw')
direction_input.place(relx=0.1,rely=0.1, anchor='nw')
btn_proceed.place(relx=0.1,rely=0.2, anchor='nw')


main_window.mainloop()