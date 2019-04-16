import Tkinter, tkFileDialog
import getHold, deletePost, removeRefs, getTitles

root = Tkinter.Tk()

root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
#Ta bort bestandsposter:
#deletePost.raderaPoster(getHold.getHold(root.filename))

#Ta bort RefK-markningar:
removeRefs.removeRefs(getHold.getHold(root.filename))

