#CREDITS TO KALLAXENC. ALL CODE BELOW IS COPYRIGHT KALLAXENC. PLEASE DO NOT CLAIM CODE AS YOURS.
import webbrowser
from time import sleep
from tkinter import *
response="Nothing Yet."
#Headers and windows
mw = Tk()
mw.title("KI AI V1.0")
header1 = Label(mw, text="Hello, I am KI AI V1.0.")
header2 = Label(mw, text= "Conversation:")
#Default Text
intro = Label(mw, text= "Searching Tool:")
info1 = Label(mw, text= "Currently I can websearch what you demand.")
info2 = Label(mw, text= "Despite my limitations, updates are coming soon.")
header1.grid(column=0, row=0)
header2.grid(column=0, row=1)
intro.grid(column=1, row=2)
info1.grid(column=1, row=3)
info2.grid(column=1, row=4)

#Conversation
historyHeading = Label(mw, text="You Previously Searched:")
history = Label(mw, text=f"---> {response}")
currentfunction = Label(mw, text="I'm not currently doing anything, \n so how about me searching for \nsomething using the text box below?")
currentfunction.grid(column=1, row=6)

historyHeading.grid(column=1, row=7)
history.grid(column=1, row=8)

#Search bar
questionLabel = Label(mw, text="Input a thing you want to search -->")
searchBox = Entry(mw, width=20)


def searchFor():
    response = searchBox.get()

    history.configure(text=f"---> {response}")
    webbrowser.open(
        f"https://www.google.com/search?q={response}&rlz=1C1CHZN_enGB1034GB1040&oq=geometry+dash&aqs=chrome.0.69i59j46i67i131i433i650j46i67i433i650j0i67i131i433i650j69i60j5j69i61l2.2999j0j7&sourceid=chrome&ie=UTF-8")
    currentfunction.configure(text=f"Finished Searching for {response}")


searchButton = Button(mw, text="Enter", command=searchFor)
questionLabel.grid(column=1, row=10)
searchBox.grid(column=1, row=11)
searchButton.grid(column=1, row=12)

#Conversation function
conversationHeader = Label(mw, text="Conversation Function:")
conversationInfo1 = Label(mw, text="I have some basic buttons with questions you can ask me.")
conversationInfo2 = Label(mw, text="This feature hopefully will become proper AI at some point.")
conversationHeader.grid(column=2, row=2)
conversationInfo1.grid(column=2, row=3)
conversationInfo2.grid(column=2, row=4)
#print(f"Searching for: {ques}")
#webbrowser.open(f"https://www.google.com/search?q={ques}&rlz=1C1CHZN_enGB1034GB1040&oq=geometry+dash&aqs=chrome.0.69i59j46i67i131i433i650j46i67i433i650j0i67i131i433i650j69i60j5j69i61l2.2999j0j7&sourceid=chrome&ie=UTF-8")
mw.mainloop()
