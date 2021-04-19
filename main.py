from tkinter import *
import covid
from matplotlib import pyplot as plt
from covid import Covid
from PIL import ImageTk, Image
#import patches to scale the data
import matplotlib.patches as mpatches


#initializing covid library
covid = Covid()

pathoftheimage = 'C:/Users/kurtk/OneDrive/Desktop/DontOpen/Python/Projects/Covid19Update/covback.jpg'

#initializing tkinter
window = Tk()
window.geometry("350x450")
window.config(bg="#416C7B")
window.title("Covid-19 Update Based on Countries")
icon = PhotoImage(file='C:/Users/kurtk/OneDrive/Desktop/DontOpen/Python/Projects/Covid19Update/image.png')
window.iconphoto(True,icon)

img = ImageTk.PhotoImage(Image.open(pathoftheimage))
panel = Label(window, image=img)
panel.pack()

#get covid data and display it
def getCovidData():
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []


    #using try and except to run program without errors
    try:
        #updating window
        window.update()
        #getting countries names entered by the user
        countries = data.get()
        #removing white spaces from the start and the end of the string
        country_names = countries.strip()
        #replacing white spaces with commas inside the string
        country_names = country_names.replace(" ", ",")
        #spliting the string to store names of countries as a list
        country_names = country_names.split(",")

        #for loop to get all countries data
        for i in country_names:
            # appending countries data one by one
            cases.append(covid.get_status_by_country_name(i))
            #updating the window
            window.update()

        #getting country data stored as a dictionary in the list cases
        for x in cases:
            #storing data
            confirmed.append(x["confirmed"])
            active.append(x["active"])
            deaths.append(x["deaths"])
            recovered.append(x["recovered"])

        #making the color information on scaleusing patches
        confirmed_patch = mpatches.Patch(color='green', label='confirmed')
        recovered_patch = mpatches.Patch(color='red', label='recovered')
        active_patch = mpatches.Patch(color='blue', label='active')
        deaths_patch = mpatches.Patch(color='black', label='deaths')

        #ploting the scale on graph using legend()
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        #showing the data using graphs
        for i in range(len(country_names)):
            plt.bar(country_names[i], confirmed[i], color='green')
            if recovered[i] > active[i]:
                plt.bar(country_names[i], recovered[i], color='red')
                plt.bar(country_names[i], active[i], color='blue')
            else:
                plt.bar(country_names[i], active[i], color='blue')
                plt.bar(country_names[i], recovered[i], color='red')
            plt.bar(country_names[i], deaths[i], color='black')

        #the graph
        plt.title('Current Covid Cases')
        plt.xlabel('Contry Name')
        plt.ylabel('Cases(in millions)')
        plt.show()
    except Exception as e:
        #this will run when the user enters incorrect details
        data.set("Invalid entry! Please enter correct details")

Label(window, text="Enter all countries names\nfor whom you want to get\ncovid-19 data", font=('Comic Sans MS', 15, "bold" ),fg="white", bg="#416C7B").pack()
space = Label(window,text="",font=('Comic Sans MS', 15, "bold" ),bg="#416C7B").pack()

Label(window, text="Seperate country names using comma or space(not both)", font=('Comic Sans MS',9, "bold"), fg="white", bg="#416C7B").pack()
Label(window, text="Enter country name:",font=('Comic Sans MS',8, "bold"),fg="white", bg="#416C7B").pack()

data = StringVar()
data.set("")

entryField = Entry(window, textvariable=data, width=50).pack()
Button(window, text="Get Data", cursor="hand2",bg="blue", fg="white",  command=getCovidData).pack()
    

window.mainloop()