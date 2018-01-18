
# coding: utf-8

# In[1]:


# Import Numpy for calculations and matplotlib for charting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv


# In[2]:


# Save path to data set in a variable
city_data_file = "Resources/city_data.csv"
ride_data_file = "Resources/ride_data.csv"


# In[3]:


# Use Pandas to read data
city_data_pd = pd.read_csv(city_data_file)
ride_data_pd = pd.read_csv(ride_data_file)


# In[4]:


city_data_pd.head()


# In[5]:


ride_data_pd.head()


# In[6]:


#merged_city_data_pd = pd.merge (ride_data_pd, city_data_pd, on = "city")
#merged_city_data_pd.head()


# In[7]:


#grouped_fare
grouped_fare =  ride_data_pd.groupby("city",  as_index= False)["fare"]

#Average Fare ($) Per City
avg_fare_per_city = grouped_fare.mean()
#type(avg_fare_per_city)
avg_fare_per_city.head()


# In[8]:


#grouped_rides
grouped_rides = ride_data_pd.groupby("city",  as_index= False)["ride_id"]
#Total Number of Rides Per City
total_rides_per_city = grouped_rides.count()
total_rides_per_city.head()


# In[9]:


#grouped_drivers
grouped_drivers = city_data_pd.groupby("city",  as_index= False)["driver_count"]

#Total Number of Drivers Per City
total_drivers_per_city = grouped_drivers.sum()
total_drivers_per_city.head()


# In[10]:


#City Type (Urban, Suburban, Rural)
city_type= city_data_pd[["city", "type"]]
type(city_type)


# In[11]:


avg_fare_per_city_with_citytype = pd.merge(avg_fare_per_city, city_type, on = "city")
avg_fare_per_city_with_citytype.head()

fare_Urban = avg_fare_per_city_with_citytype.loc[avg_fare_per_city_with_citytype["type"]=="Urban"].copy()
fare_Urban
fare_Suburban = avg_fare_per_city_with_citytype.loc[avg_fare_per_city_with_citytype["type"]=="Suburban"].copy()
fare_Suburban
fare_Rural = avg_fare_per_city_with_citytype.loc[avg_fare_per_city_with_citytype["type"]=="Rural"].copy()
fare_Rural


# In[12]:


total_rides_per_city_with_citytype = pd.merge(total_rides_per_city, city_type, on = "city")
total_rides_per_city_with_citytype.head()

rides_Urban = total_rides_per_city_with_citytype.loc[total_rides_per_city_with_citytype["type"]=="Urban"].copy()
rides_Urban
rides_Suburban = total_rides_per_city_with_citytype.loc[total_rides_per_city_with_citytype["type"]=="Suburban"].copy()
rides_Suburban
rides_Rural = total_rides_per_city_with_citytype.loc[total_rides_per_city_with_citytype["type"]=="Rural"].copy()
rides_Rural


# In[13]:


total_drivers_per_city_with_citytype = pd.merge(total_drivers_per_city, city_type, on = "city")
total_drivers_per_city_with_citytype.head()

drivers_Urban = total_drivers_per_city_with_citytype.loc[total_drivers_per_city_with_citytype["type"]=="Urban"].copy()
drivers_Urban
drivers_Suburban = total_drivers_per_city_with_citytype.loc[total_drivers_per_city_with_citytype["type"]=="Suburban"].copy()
drivers_Suburban
drivers_Rural = total_drivers_per_city_with_citytype.loc[total_drivers_per_city_with_citytype["type"]=="Rural"].copy()
drivers_Rural


# In[14]:


#plotting urban
plt.scatter(rides_Urban["ride_id"], fare_Urban["fare"], s = 5*drivers_Urban["driver_count"], label = "Urban", color = "lightskyblue", linewidth = 2, alpha = .5, edgecolor = "black")


# In[15]:


#plotting Suburban
plt.scatter(rides_Suburban["ride_id"], fare_Suburban["fare"], s = 5*drivers_Suburban["driver_count"], label = "Suburban", color = "lightcoral", linewidth = 2, alpha = .5, edgecolor = "black")


# In[16]:


#plotting Rural
plt.scatter(rides_Rural["ride_id"], fare_Rural["fare"], s = 5*drivers_Rural["driver_count"], label = "Rural", color = "gold", linewidth = 2, alpha = .5, edgecolor = "black")


# In[17]:


# Adds a legend and sets its location to the lower right
plt.legend(fontsize = "small", loc="best")


# In[18]:


plt.title("Pyber Ride sharing data")
plt.xlabel("total_rides_per_city")
plt.ylabel("avg_fare_per_city")
plt.xlim(0, 40)
plt.ylim(15, 45)
plt.grid()


# In[19]:


plt.savefig("PyBubble.png")
plt.show()


# In[20]:


#% of Total Fares by City Type
merged_df_city = pd.merge(city_data_pd, ride_data_pd, on='city')
fare = merged_df_city.groupby("type")["fare"].sum()
#print(fare)
total = merged_df_city["fare"].sum()
#print(total)
percent_fare_per_city_type = (fare*100)/total
percent_fare_per_city_type


# In[21]:


#% of Total Rides by City Type
rides= merged_df_city.groupby("type")["ride_id"].count()
#print(rides)
total_rides= merged_df_city["ride_id"].count()
#print(total_rides)
percent_rides_per_city_type = (rides*100)/total_rides
percent_rides_per_city_type


# In[22]:


#% of Total Drivers by City Type
drivers= city_data_pd.groupby("type")["driver_count"].sum()
#print(drivers)
total_drivers= city_data_pd["driver_count"].sum()
#print(total_drivers)
percent_drivers_per_city_type = (drivers*100)/total_drivers
percent_drivers_per_city_type


# In[23]:


explode = (0, 0.1, 0)


# In[24]:


#creating a pie chart -- % of Total Fares by City Type
percent_fare_per_city_type
colors = ["coral", "lightskyblue", "gold"]
labels = ["Rural in Coral", "Suburban in LightBlue", "Urban in Gold"]
plt.pie(percent_fare_per_city_type, labels = labels, shadow = True, startangle = 90 , explode=explode, colors = colors, autopct='%1.2f%%')
plt.title("% Total fare per city type")


# In[25]:


# Saves an image of our chart so that we can view it in a folder
plt.savefig("PercentageTotalFare_PerCityType.png")
plt.show()


# In[26]:


percent_rides_per_city_type


# In[27]:


#creating a pie chart= % of Total Rides by City Type
percent_rides_per_city_type
colors = ["coral", "lightskyblue", "gold"]
labels = ["Rural in Coral", "Suburban in LightBlue", "Urban in Gold"]
plt.pie(percent_rides_per_city_type, labels = labels, shadow = True, startangle = 90, explode=explode, colors = colors, autopct='%1.2f%%')
plt.title("% Total rides per city type")


# In[28]:


# Saves an image of our chart so that we can view it in a folder
plt.savefig("PercentageTotalRides_PerCityType.png")
plt.show()


# In[29]:


percent_drivers_per_city_type


# In[30]:


#creating a pie chart= % of Total Drivers by City Type
percent_drivers_per_city_type
colors = ["coral", "lightskyblue", "gold"]
labels = ["Rural in Coral", "Suburban in LightBlue", "Urban in Gold"]
plt.pie(percent_drivers_per_city_type, labels = labels, shadow = True, startangle = 90, explode=explode, colors = colors, autopct='%1.2f%%')
plt.title("% Total Drivers per city type")


# In[31]:


# Saves an image of our chart so that we can view it in a folder
plt.savefig("PercentageTotalDrivers_PerCityType.png")
plt.show()


# In[ ]:


#Conclusions
#There are more # of rides and more # of drivers in Urban areas but cost seems relatively less compare to suburban and rural areas. 
#A possible explanation for this trend could be people take short distance rides in the city, going to nearby point of interests and a lot more often.
#Also, it is more likely that suburban areas and rural areas are more spread out. Hence, fare is more and likely, drivers available are fewer.

