# importing all tkinter files
from tkinter import *
# create instance of tkinter
root = Tk()
# setting geometry of tkinter window
root.geometry("550x550")
# setting title of tkinter window
root.title("CORONAVIRUS (COVID-1")

# defining the function to fetch the data from covid library and to show it.
def covid_data():
    # importing matplotlib which will be used to show data graphically
    from matplotlib import pyplot as plt
    # to scale the data we are importing patches
    import matplotlib.patches as mpatches
    # importing covid library
    from covid import Covid
    # initializing covid library
    covid = Covid()
    # this declares empty lists to store different data sets
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
       # using Exception Handling to handle the exceptions.
    try:
        # updating root(tkinter window)
        root.update()
        # getting countries names entered by the user using get() method.
        countries = data.get()
        # removing white spaces from the start and end of the string
        country_names = countries.strip()
        # replacing white spaces with commas inside the string
        country_names = country_names.replace(" ", ",")
        # splitting the string to store names of countries
        # as a list
        country_names = country_names.split(",")
        # for loop to get all countries data
        for x in country_names:
            # appending countries data one-by-one in cases list
            # here, the data will be stored as a dictionary
            # for one country i.e. for each country
            # there will be one dictionary in the list
            # which will contain the whole information
            # of that country
            cases.append(covid.get_status_by_country_name(x))
            # updating the root
            root.update()
        # for loop to get one country data stored as dict in list cases
        for y in cases:
            # storing every Country's confirmed cases in the confirmed list
            confirmed.append(y["confirmed"])
            # storing every Country's active cases in the active list
            active.append(y["active"])
            # storing every Country's deaths cases in the deaths list
            deaths.append(y["deaths"])
            # storing every Country's recovered cases in the recovered list
            recovered.append(y["recovered"])
        # marking the color information on scaleusing patches
        confirmed_patch = mpatches.Patch(color='blue', label='Confirmed')
        recovered_patch = mpatches.Patch(color='green', label='Recovered')
        active_patch = mpatches.Patch(color='red', label='Active')
        deaths_patch = mpatches.Patch(color='black', label='Deaths')
        # plotting the scale on graph using legend()
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
        # showing the data using graphs
        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='blue')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], active[x], color='red')
            else:
                plt.bar(country_names[x], active[x], color='red')
                plt.bar(country_names[x], recovered[x], color='green')
            plt.bar(country_names[x], deaths[x], color='black')
        # setting the title of the graph
        plt.title('CURRENT COVID CASES')
        # giving label to x direction of graph
        plt.xlabel('COUNTRY NAME')
        # giving label to y direction of graph
        plt.ylabel('CASES(in millions)')
        # showing the full graph
        plt.show()
    except Exception as e:
        # the user must enter the correct details during entering the country names
        # otherwise, they will enter into this section
        # so ask them to diffrentiate the names using comma or space but not both.

        data.set("Enter the correct details please:")


Label(root, text="COVID-19 UPDATES\nEnter the countries names\nfor whom you want to get the\ncovid-19 data", font="LUCIDA 15 bold").pack()
Label(root, text="Enter the Country Names", font="bold").pack()
data = StringVar() #creating instance of StringVar()
#setting the text that will be displayed by default on GUI application.
data.set("Seperate Country Names using comma or space(not both)")
#Entry widget is used to accepts the string text from the user.
entry = Entry(root, textvariable=data, width=50).pack()
#here Button widget is used to create a button that will call the function "covid_data"
#created above when any on-CLICK event will occur.
Button(root, text="Get Data", command=covid_data).pack()
#this helps to run the mainloop
root.mainloop()
