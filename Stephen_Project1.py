
# coding: utf-8

# # Project 1 - Stephen's code
# ----
# 
# ### Question 5 and 6 Analysis
# * Due to the recent advancment and use of mobile phones while driving, we we wanted to specifically test to see if Men or Women comitted this offense more than the other gender. Mobile phone use can consist of talking or texting. Many states have recently inacted laws prohibiting the use of mobile phones while driving. From the data collected, the data shows Men were caught using their mobile phones while driving more often than Women by almost 6000 more occurences.
# * We also wanted to investigate out of all the violations comitted during this time frame of our data, whether Men or Women were more prone to comitting certain types of violations over the other gender. Our hypothesis for this gender analysis was that both Men and Women comitted violations of each type equally. But the data shows otherwise. Of all the violations, Women only comitted one violation more often than Men, and that was "Failure to Secure Child in Safety Seat", but just by a very slight margin. Of the top 10 most comitted violations, you can see from the graph that Men, and by a wide margin on most violation types, comitted these violations more times than Women. From this analysis, my hypothesis as to why there is such disparity is that Men are typically thrill seekers when it comes to cars and generally don't think of the consequences of related actions. 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Plot Style Sheet
from matplotlib import style
style.use('seaborn-white')

# Files to Load 
Traffic_Data_File = "Traffic_Violations_Final.csv"


#Read CSV files
Traffic_Data = pd.read_csv(Traffic_Data_File)


#Display dataframe
Traffic_Data.head()


# In[2]:


#list column headers
list(Traffic_Data)


# In[3]:


#find unique values for Description column
Traffic_Data["Description"].unique()


# In[4]:


#Count total violations recorded by each gender
#notice how there are some unknown genders
Traffic_Data.Gender.value_counts()


# In[5]:


#group by description
Traffic_Data_by_Description = Traffic_Data.groupby(["Description"]).count()
Traffic_Data_by_Description


# In[6]:


#filter data to show violations for each gender
Male_Traffic_Data_df = Traffic_Data.loc[Traffic_Data["Gender"] == "MALE", :]
Female_Traffic_Data_df = Traffic_Data.loc[Traffic_Data["Gender"] == "FEMALE", :]
Male_Traffic_Data_df.head()


# In[8]:


#Creating series in order to create a new dataframes that we will use as basis for our analysis
#do value counts for each gender to see how many times each gender comitted each violation description
#we will use these series to create new columns in a new dataframe we will create to compare male vs female violations
Description_Male_Counts = Male_Traffic_Data_df["Description"].value_counts()

Description_Female_Counts = Female_Traffic_Data_df["Description"].value_counts()

#Adding of each gender counts to get sum totals so we can find out top 10 most committed violations
Sum_of_Male_Female_Counts = Description_Male_Counts + Description_Female_Counts


# In[12]:


#create new dataframe with the series we found above to compare male vs female violation descriptions comitted
Description_Analysis_by_gender_df = pd.DataFrame({"Male description counts": Description_Male_Counts,
                                                  "Female description counts": Description_Female_Counts,
                                                 "Sum of counts": Sum_of_Male_Female_Counts})

#fill in NA values with zero since some violation descriptions were not comitted by any females
#for example no females comitted Driving motor vehicle when not qualified to do so
Description_Analysis_by_gender_df["Female description counts"].fillna(value=0, inplace=True)

#create new dataframe that is sorted by Sum of counts so we can use as basis for top10 analysis
#sort the dataframe descending on Sum of gender description counts column so we can find the top 10 most comitted violation descriptions
Description_Analysis_top10 = Description_Analysis_by_gender_df.sort_values(by=["Sum of counts"], ascending=False)

Description_Analysis_top10


# In[14]:


#Creating of dataframes for each graph we will make in order to show gender comparissons of violations descriptions 
#Create dataframe to use for graph to compare men vs women comitting violation description of using
#mobile while while driving
mobile_phone_analysis = Description_Analysis_by_gender_df.loc["DRIVER USING MOBILE PHONE WHILE OPERATING VEHICLE", :]

#Create a dataframe of the top 10 most comitted violation based on the Men most comitted violations
#in order to do a gender analysis 
gender_violation_analysis_top10 = Description_Analysis_top10.iloc[0:10, 0:2]

#Create 6 different dataframes to use for graphs to compare men vs women comitting
#each different violation description
gender_violation_analysis_g1 = Description_Analysis_by_gender_df.iloc[0:10, 0:2]

gender_violation_analysis_g2 = Description_Analysis_by_gender_df.iloc[10:20, 0:2]

gender_violation_analysis_g3 = Description_Analysis_by_gender_df.iloc[20:30, 0:2]

gender_violation_analysis_g4 = Description_Analysis_by_gender_df.iloc[30:40, 0:2]

gender_violation_analysis_g5 = Description_Analysis_by_gender_df.iloc[40:50, 0:2]

gender_violation_analysis_g6 = Description_Analysis_by_gender_df.iloc[50:57, 0:2]


# In[15]:


#Plot Data for analysis of using mobile phone while driving male vs female

#Assign variable for number of groups
n_groups = 1

#Assign 2 vairables for Y axis values
y_value_male = mobile_phone_analysis["Male description counts"].tolist()
y_value_female = mobile_phone_analysis["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(5,6)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Gender', fontsize = 14)
plt.ylabel('Number of Violations', fontsize = 14)
plt.title('Gender Comparisson of\nUsing Mobile Phone\nWhile Operating Vehicle', fontweight="bold", fontsize = 18)
plt.xticks(index + bar_width / 2, ['Using Mobile Phone While\nOperating Vehicle'], fontsize = 12)
plt.yticks(fontsize = 12)
plt.ylim(0, 40000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+5000,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("MaleVsFemaleUsingMobilePhone.png", bbox_inches="tight")

plt.show()


# In[16]:


#Plot Data for Top 10 Violation Descriptions

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_top10["Male description counts"].tolist()
y_value_female = gender_violation_analysis_top10["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 16)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 16)
plt.title('Gender Comparission\nof Top 10 Traffic Violations', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Driving Without Valid\nLicense or Registration', 'Failure to Obey\nTraffic Control Device', 'Exceeding Posted\nSpeed Limit', 'Driving Vehicle with\nUnathorized Equipment', 'DUI', 'Improper, Fraudulent, or\nUnathorized Use of\nVehicle Registration', 'Driver Using Mobile Phone\nWhile Operating Vehicle', 'Driving Without Lighted\nHeadlights When Required', 'Driver Or Occupant Not\nRestrained by Seatbelt', 'Reckless or\nAggressive Driving'], fontsize = 14, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 275000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+16000,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)


#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisTop10.png", bbox_inches="tight")

plt.show()


# In[17]:


#Plot Data for violations by gender group 1 of 6

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g1["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g1["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 1', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Abandoning Vehilce\nOn Public Property', 'Elude Police', 'Drifting', 'No Seat Belt', 'Failure to Curb', 'Failure to Signal', 'Following Vehicle\nToo Close', 'Spinning Wheels', 'Using Mobile Phone', 'Violation of\nRental Agreement'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 25000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+1200,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)


#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup1.png", bbox_inches="tight")

plt.show()


# In[18]:


#Plot Data for violations by gender group 2 of 6

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g2["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g2["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 2', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Driving Vehilce\nWhen Not Qualified', 'Tampering Vehicle', 'Excessive Speed', 'DUI', 'Driving Using\nHeadphones', 'Unathorized Equip.', 'No Valid Medical\nExaminers Cert.', 'Obstructed View', 'Unsafe Load', 'Driving Without Insurance'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 130000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+7500,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup2.png", bbox_inches="tight")

plt.show()


# In[19]:


#Plot Data for violations by gender group 3 of 6

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g3["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g3["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 3', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Driving Without\nHeadlights When Required', 'Driving Without Headlights\nWhile Using Wipers', 'No Valid License or Registration', 'Exceeding Allowable Weight', 'Exceeding Posted\nSpeed Limit', 'Failing to Display\nProper Vehicle ID', 'Failure to Offer Reasonable\nAssistance to Injured Person', 'No Address Change\nWithin 30 Days', 'Not Moving for\nEmergency Vehicle', 'Failure to Control\nSpeed to Avoid Collision'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 260000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+15000,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup3.png", bbox_inches="tight")

plt.show()


# In[20]:


#Plot Data for violations by gender group 4 of 6

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g4["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g4["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 4', fontweight="bold", fontsize = 18)
plt.xticks(index, ['No Decal on\nMotor Scooter', 'Failure to Drive on\nRight Side When Required', 'Failure to Furnish Written Info\non Unattended Damaged Vehicle', 'Failure to Obey\nTraffice Control Device', 'Failure to Reduce Light\nWhen Approaching Vehicle', 'Failure to Remain\nAt Scene of Accident', 'Failure to Report Accident\nor Give False Report', 'Failure to Secure\nChild in Safety Seat', 'Failure to Yield\nRight of Way', 'Unathorized Display or\nUse of Vehicle Registration'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 200000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+15000,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup4.png", bbox_inches="tight")

plt.show()


# In[21]:


#Plot Data for violations by gender group 5 of 6

#Assign variable for number of groups
n_groups = 10

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g5["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g5["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,12)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 5', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Letting Unathorized\nPerson Drive Vehicle', 'Littering', 'Misc.', 'Parking in Prohibited\nLocation or Manner', 'Participating in\nSpeed Contest', 'Pedestrian Crossing Roadway\nBetween Adjacent Intersection\nWith Traffic Control Signal', 'Pedestrian Failure to\nObey Traffic Control Signal', 'Provisional Driver\nWithout Authorized Person', 'Reckless or\nAggressive Driving', 'Stopping Vehicle Improperly'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 25000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+1500,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup5.png", bbox_inches="tight")

plt.show()


# In[22]:


#Plot Data for violations by gender group 6 of 6

#Assign variable for number of groups
n_groups = 7

#Assign 2 vairables for Y axis values
y_value_male = gender_violation_analysis_g6["Male description counts"].tolist()
y_value_female = gender_violation_analysis_g6["Female description counts"].tolist()


#Set sub plots
fig, ax = plt.subplots()

#Set index variable
index = np.arange(n_groups)

#Set bar width 
bar_width = 0.4

#create 2 different bar plots 
fig.set_size_inches(20,6)
rects1 = plt.bar(index, y_value_male, bar_width,
                 alpha= 1,
                 color= 'lightblue',
                 edgecolor='black',
                 label='Male')

rects2 = plt.bar(index + bar_width, y_value_female, bar_width,
                 alpha= .7,
                 color='pink',
                 edgecolor='black',
                 hatch = '///',
                 label='Female')

#Create Labels, Ledgend, and grid attributes 
plt.grid(True)
plt.xlabel('Violation Description', fontweight="bold", fontsize = 14)
plt.ylabel('Number of Violations', fontweight="bold", fontsize = 14)
plt.title('Traffic Violations\nby Gender Group 6', fontweight="bold", fontsize = 18)
plt.xticks(index, ['Unlawful Use of\nHistoric Vehicle', 'Unsafe Backing of Vehicle', 'Unsafe or Improper\nLane Change', 'Unsafe or Improper Passing', 'Use of Vehicle Horn When Not\nReasonably Neccessary For Safety', 'Willfully Disobeying Lawful Order\nAnd Direction of Police Officer', 'Willfully Driving Vehicle\nat Slow Speed Impeeding Normal\nand Reasonable Traffic Movement'], fontsize = 12, rotation=45)
plt.yticks(fontsize = 14)
plt.ylim(0, 20000)
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+3000,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=45)
plt.legend(fontsize = 14, frameon=True)

#Show and export PNG of graph 
plt.tight_layout()
plt.savefig("GenderViolationAnalysisGroup6.png", bbox_inches="tight")

plt.show()

