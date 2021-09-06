# Import the datetime class from the datetime module.
import datetime

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)
#print ("Hello World")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
 #   print(county_dict)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
'''for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")'''

counties = ['Arapahoe', 'Denver', 'Jefferson']


counties_tuple = ("Arapahoe","Denver","Jefferson")

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
#print(counties_dict.get("Denver"))#this returns value
voting_data  =[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
