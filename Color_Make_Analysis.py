
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Plot Style Sheet
from matplotlib import style
style.use('seaborn-white')

# Files to Load 
Traffic_Data_File = "Resources/Traffic_Violations_Final.csv"
color_popularity_File = "Resources/DuPont _Car_color_popularity.csv"

#Output file variables
output_Color_PNG = "output_data/Color.png"
output_Color_Speeding_PNG = "output_data/Color_Speeding.png"
Make_PNG = "output_data/Make_Speeding.png"

#Read CSV files
Traffic_Data = pd.read_csv(Traffic_Data_File)
color_popularity= pd.read_csv(color_popularity_File)

Traffic_Data.head()


# In[2]:


#Clean general population color data to match formatting of traffic data
color_popularity["Color"].replace(['White'], 'WHITE', inplace=True)
color_popularity["Color"].replace(['Silver'], 'SILVER', inplace=True)
color_popularity["Color"].replace(['Red'], 'RED', inplace=True)
color_popularity["Color"].replace(['Others'], 'OTHER', inplace=True)
color_popularity["Color"].replace(['Grey'], 'GRAY', inplace=True)
color_popularity["Color"].replace(['Green'], 'GREEN', inplace=True)
color_popularity["Color"].replace(['Brown'], 'BROWN', inplace=True)
color_popularity["Color"].replace(['Blue'], 'BLUE', inplace=True)
color_popularity["Color"].replace(['Black'], 'BLACK', inplace=True)

color_popularity


# In[3]:


#Clean up colors to match color popularity table
Traffic_Data['Vehicle Color'].replace(['ORANGE', 'YELLOW', 'PURPLE', 'PINK', 'MULTICOLOR'], 'OTHER', inplace=True)
Traffic_Data['Vehicle Color'].replace(['GOLD', 'TAN'], 'BROWN', inplace=True)
Traffic_Data['Vehicle Color'].unique()


# In[4]:


#Create dataframe to hold color count of all violations and calulate the percentage for each color
#Group by Color count 
Data_by_Color = Traffic_Data.groupby(['Vehicle Color']).count()
Data_by_Color = pd.DataFrame(Data_by_Color['Charge'])

#Calculate color percent of total pulled over
Data_by_Color['Percent_PulledOver'] = (Data_by_Color['Charge']/Data_by_Color['Charge'].sum())*100

#Change the column name on the popularity file so it can be merged
color_popularity.rename(index=str, columns={'Color': 'Vehicle Color'}, inplace=True)

#Add population distrubution data from color_popularity file
Data_by_Color = pd.merge(Data_by_Color, color_popularity, on="Vehicle Color", how="left")

#organize the data from largest to smallest 
Data_by_Color = Data_by_Color.sort_values(by='Charge', ascending=False)

Data_by_Color


# In[5]:


#Create dataframe to hold color count of all speeding only violations and calulate the percentage for each color
#filter by only speeding violations
Data_by_Color_Speeding = Traffic_Data.loc[Traffic_Data["Description"] == "EXCEEDING THE POSTED SPEED LIMIT", :]

#Group by Color count 
Data_by_Color_Speeding = Data_by_Color_Speeding.groupby(['Vehicle Color']).count()
Data_by_Color_Speeding = pd.DataFrame(Data_by_Color_Speeding['Charge'])

#Calculate color percent of total pulled over
Data_by_Color_Speeding['Percent_Speeding'] = (Data_by_Color_Speeding['Charge']/Data_by_Color_Speeding['Charge'].sum())*100

#Add population distrubution data from color_popularity file
Data_by_Color_Speeding = pd.merge(Data_by_Color_Speeding, color_popularity, on="Vehicle Color", how="left")

#organize the data from largest to smallest 
Data_by_Color_Speeding = Data_by_Color_Speeding.sort_values(by='Charge', ascending=False)

Data_by_Color_Speeding


# In[6]:


Data_by_Color['Vehicle Color'].unique()


# In[10]:


#Plot Color analysis for total cars pulled over 

#Assign variable for number of groups
n_groups = 9

#Assign 2 vairables for Y axis values
y_value = Data_by_Color["Percent_PulledOver"].tolist()
y_value_Compare = Data_by_Color["Population_Distribution"].tolist()

#Assign variable to color list 
Color_List1 = ['Black', 'Silver', 'White', 'Gray', 'Blue', 'Red', 'saddlebrown', 'Green', 'violet']

#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(10,6)
rects1 = plt.bar(index, y_value, bar_width,
                 alpha= 1,
                 color= Color_List1,
                 edgecolor='black',
                 label='% of Total Vehicles Pulled Over')

rects2 = plt.bar(index + bar_width, y_value_Compare, bar_width,
                 alpha= .7,
                 color='lightblue',
                 edgecolor='black',
                 hatch = '///',
                 label='% of Vehicle Color Popularity')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Vehicle Color', fontsize = 14)
plt.ylabel('Percent of Vehicles', fontsize = 14)
plt.title('Vehicle Color Analysis', fontweight="bold", fontsize = 18)
plt.xticks(index + bar_width / 2, ('BLACK', 'SILVER', 'WHITE', 'GRAY', 'BLUE', 'RED', 'BROWN', 'GREEN', 'OTHER'), fontsize = 13)
plt.yticks(fontsize = 13)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig(output_Color_PNG, bbox_inches="tight")

plt.show()


# In[11]:


Data_by_Color_Speeding['Vehicle Color'].unique()


# In[17]:


#Plot Color analysis for cars pulled over for speeding
#Assign variable for number of groups
n_groups2 = 9

#Assign 2 vairables for Y axis values
y_value2 = Data_by_Color_Speeding["Percent_Speeding"].tolist()
y_value_Compare2 = Data_by_Color_Speeding["Population_Distribution"].tolist()

#Assign variable to color list 
Color_List2 = ['Black', 'Silver', 'White', 'Gray', 'Blue', 'Red', 'saddlebrown', 'Green', 'violet']

#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index2 = np.arange(n_groups2)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(10,6)
rects1 = plt.bar(index2, y_value2, bar_width,
                 alpha= 1,
                 color= Color_List2,
                 edgecolor='black',
                 label='% of Total Cars Pulled Over for Speeding')

rects2 = plt.bar(index2 + bar_width, y_value_Compare2, bar_width,
                 alpha= .7,
                 color='lightsteelblue',
                 edgecolor='black',
                 hatch = '///',
                 label='% of Car Color Popularity')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Vehicle Color', fontsize = 14)
plt.ylabel('Percent of Cars Speeding', fontsize = 14)
plt.title('Car Color Speeding Analysis', fontweight="bold", fontsize = 18)
plt.xticks(index2 + bar_width / 2, ('BLACK', 'SILVER', 'WHITE', 'GRAY', 'BLUE', 'RED', 'BROWN', 'GREEN', 'OTHER'), fontsize = 13)
plt.yticks(fontsize = 13)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig(output_Color_Speeding_PNG, bbox_inches="tight")

plt.show()


# In[13]:


#Create a Dataframe to store the count of the Make of cars pulled over for speeding and split between Cited and Warning 
#Filter for Speeding violations
Speeding = Traffic_Data.loc[Traffic_Data["Description"] == "EXCEEDING THE POSTED SPEED LIMIT", :]

#create DF for Violation Type - Vehicles cited and let off with warning
Speeding = pd.DataFrame(Speeding[['Vehicle Make', 'Violation Type']])
Citation = Speeding.loc[Speeding['Violation Type'] == 'Citation', :]

#Use groupby to count the number of rows per make in each category
Citation_Count = Citation.groupby(['Vehicle Make'], as_index=False).count()
Total_Speeding = Speeding.groupby(['Vehicle Make'], as_index=False).count()


#Sort total Speeding from largest number to smallest
Total_Speeding = Total_Speeding.sort_values(by='Violation Type', ascending=False)
Total_Speeding = Total_Speeding.loc[Total_Speeding['Violation Type'] > 1100]

#Merge number cited with total speeding DF
Speeding_df = pd.merge(Total_Speeding , Citation_Count, on="Vehicle Make", how="left")

#Rename Columns 
Speeding_df.rename(index=str, columns={'Violation Type_x': 'Total_Speeding'}, inplace=True)
Speeding_df.rename(index=str, columns={'Violation Type_y': 'Citation'}, inplace=True)

Speeding_df


# In[16]:


#Create bar graph to show the top vehicle makes and the amount cited vs total speeding 
make = Speeding_df['Vehicle Make'].tolist()
Cited_Speeding = Speeding_df.Citation.tolist()
All_Speeding = Speeding_df.Total_Speeding.tolist()

#Create plot
plt.barh(make, All_Speeding, color='skyblue', alpha=1, align="center", edgecolor='black', label="Total Vehicles Pulled Over")
plt.barh(make, Cited_Speeding, color='r', alpha=1, align="center", edgecolor='black', label="Vehicles That Received a Citation")

#Labels, Size and Legend
plt.rcParams["figure.figsize"] = (10,8)
plt.xlabel('Number of Vehicles Pulled Over for Speeding', fontsize = 14)
plt.title('Speeding by Vehicle Make', fontweight="bold", fontsize = 18)
plt.yticks(fontsize = 12)
plt.xticks(fontsize = 12)
plt.grid(True)
plt.legend(fontsize = 14, frameon=True)

#save figure 
plt.tight_layout()
plt.savefig(Make_PNG, bbox_inches="tight")

plt.show()

