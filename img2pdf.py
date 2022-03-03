import os 
from tkinter import Tk, Canvas, Label, Button, filedialog, messagebox
from PIL import Image


root= Tk()
root.title('Image 2 PDF')

font = ('helvetica', 12, 'bold')
canvas = Canvas(root, width = 300, height = 300, relief = 'raised')
canvas.pack()

label = Label(root, text='Image 2 PDF')
label.config(font=('helvetica', 20))
canvas.create_window(150, 30, window=label)

def getFile():
    global listOfFiles
    import_folder_path = filedialog.askdirectory()
    listOfFiles = list()
    img_exts = [".jpg", '.JPG','.jpeg', '.JPEG','.png','.PNG', '.svg','.SVG', '.gif','.GIF']
    for (dirpath, dirnames, filenames) in os.walk(import_folder_path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            if os.path.splitext(full_path)[1] in img_exts:
                listOfFiles.append(full_path)


browseButton = Button(text="Select Folder Path", command=getFile, font=font)
canvas.create_window(150, 100, window=browseButton)

def convertToPdf():
    global img
    for i in listOfFiles:
        image = Image.open(i)
        img = image.convert('RGB')
        img.save(os.path.splitext(i)[0]+".pdf")

convertButton = Button(text='Convert to PDF', command=convertToPdf, font=font)
canvas.create_window(150, 150, window=convertButton)

def deleteImg():
    MsgBox = messagebox.askquestion('Delete Images','Are you sure you want to delete all the images within this folder?', icon = 'warning')
    if MsgBox == 'yes':
        for i in listOfFiles:
            os.remove(i)

deleteButton = Button(text='Delete Image Files', command=deleteImg, font=font)
canvas.create_window(150, 200, window=deleteButton)

def exitApplication():
    root.destroy()
exitButton = Button(root, text='Exit Application',command=exitApplication, font=font)
canvas.create_window(150, 250, window=exitButton)

root.mainloop()