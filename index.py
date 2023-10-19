from tkinter import *
from compress_module import compress_file
from tkinter import filedialog
import os


def open_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a file to compress")
    directory, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    new_file_path = f"{directory}/compressed-{name}{extension}"

    msg = compress_file(file_path,new_file_path)
    message.configure(text=msg)
    print(msg)

root = Tk()
root.geometry("1200x200")
root.title("File compresser and de-compressor")

explore_files = Button(text="Compress File", command=open_file)
explore_files.pack()
message = Label(text="")
message.pack()

# # Input UI
# input_label = Label(text="Input filename")
# input_file = Entry(root)

# input_label.grid(row=0, column=0)
# input_file.grid(row=0, column=1)

# # Output UI
# output_label = Label(text="Output file name")
# output_file = Entry(root)

# output_label.grid(row=1, column=0)
# output_file.grid(row=1, column=1)

# # button
# compress_btn = Button(text="Compress", command=lambda:compress_file(input_file.get(), output_file.get()))
# compress_btn.grid(row="2", column="1")

root.mainloop()