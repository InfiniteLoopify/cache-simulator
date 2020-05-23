import tkinter as tk
# import os


class Gui:
    answer = []

    def guiCreate(self):

        window = tk.Tk()

        # label = tk.Label(window, text='File Name')
        # label.place(x=65, y=50)

        # entry = tk.Entry(window)
        # entry.insert(-1, 'input10.txt')
        # entry.grid(row=0, column=1)
        # entry.place(x=140, y=50)

        # files = os.listdir("files/")
        # files.sort()
        # fileDrop = tk.StringVar(window)
        # fileDrop.set(files[0])
        # drop1 = tk.OptionMenu(window, fileDrop, *files)
        # drop1.place(x=140, y=45)
        SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

        label1 = tk.Label(window, text='Memory Size')
        label1.place(x=85, y=75)
        opt1 = [["2"+("%d" % i).translate(SUP), 2**i]
                for i in range(10, 16)]
        varDrop1 = tk.StringVar(window)
        varDrop1.set(opt1[0])
        drop1 = tk.OptionMenu(window, varDrop1, *opt1)
        drop1.place(x=180, y=70)
        drop1.config(width=10)

        label2 = tk.Label(window, text='Cache Size')
        label2.place(x=98, y=105)
        opt2 = [["2"+("%d" % i).translate(SUP), 2**i]
                for i in range(3, 16)]
        varDrop2 = tk.StringVar(window)
        varDrop2.set(opt2[0])
        drop2 = tk.OptionMenu(window, varDrop2, *opt2)
        drop2.place(x=180, y=100)
        drop2.config(width=10)

        label = tk.Label(window, text='Block Size      = \t8')
        label.place(x=85, y=138)
        label = tk.Label(window, text='Hit Time         = \t1 ms')
        label.place(x=85, y=158)
        label = tk.Label(window, text='Miss Penalty  = \t20 ms')
        label.place(x=85, y=178)

        # varEdge = tk.IntVar()
        # varWeight = tk.IntVar()
        # edge = tk.Checkbutton(window, text="Show All Edges", variable=varEdge)
        # weight = tk.Checkbutton(
        #     window, text="Show Edge Weights", variable=varWeight)
        # edge.place(x=100, y=140)
        # weight.place(x=100, y=160)

        def getGuiInput():
            temp1 = varDrop1.get()
            temp2 = varDrop2.get()
            temp1 = temp1.split(',')
            temp2 = temp2.split(',')
            self.answer = [int(temp1[1].replace(')', '')),
                           min(int(temp1[1].replace(')', '')),
                               int(temp2[1].replace(')', ''))
                               )]
            window.destroy()
            # temp = varDrop.get()
            # for i in range(len(opt)):
            #     if opt[i] == temp:
            #         self.guiArray = [
            #             entry.get(), i, varEdge.get(), varWeight.get()]
            #         window.destroy()

        button = tk.Button(window, text='Calculate',
                           width=25, command=getGuiInput)
        button.place(x=80, y=200)

        window.title('Graph')
        window.geometry("400x300+10+10")
        window.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.guiCreate()
