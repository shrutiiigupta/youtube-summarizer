import tkinter as tk
import vid_to_text as v


# Top level window
root = tk.Tk()
root.title("TextBox Input")
root.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget


def printInput():
    input_link = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Provided Input: "+input_link)
    link_show()
    v.vid_to_text(input_link)
 

# TextBox Creation
inputtxt = tk.Text(root, height=2, width=50)

inputtxt.pack()

# Button Creation
printButton = tk.Button(root, text="Get Transcript", command=printInput)
printButton.pack()

lbl = tk.Label(root, text="")

def link_show():
    # Label Creation
    lbl.pack()

root.mainloop()


