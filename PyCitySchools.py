#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


###Pandas Homework 4 ###

# Dependencies and Setup

import csv 
import pandas as pd
import numpy as np
import os as os


# In[2]:


# Files to Load 

school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# In[3]:


# Read School and Student CSV Files and model into Pandas

school_df = pd.read_csv(school_data_to_load)
student_df = pd.read_csv(student_data_to_load)


# In[51]:


# sanity check for school csv
school_df.tail()


# In[52]:


#sanity check for student csv
student_df.head()


# ## School Summary

# In[ ]:


# Part Two: School Summary

Create an overview table that summarizes key metrics about each school, including:
School Name
School Type
Total Students
Total School Budget
Per Student Budget
Average Math Score
Average Reading Score
get_ipython().run_line_magic('Passing', 'Math')
get_ipython().run_line_magic('Passing', 'Reading')
Overall Passing Rate (Average of the above two)
Top Performing Schools (By Passing Rate)
We will use copy_school_sum for this portion


# In[76]:


# District totals from school_df

total_schools = len(school_df)

total_students = school_df["size"].sum()

total_budget = school_df["budget"].sum()


# District totals from student_df

ave_math = round(student_df["math_score"].mean(), 1)

ave_read = round(student_df["reading_score"].mean(), 1)

student_total = len(student_df)

passed_math = (student_df["math_score"] >= 70).value_counts()[True]

percent_pass_math= round((pass_math/student_total)*100, 1)

passed_read = (student_df["reading_score"] >= 70).value_counts()[True]

percent_pass_read = round((pass_read/student_total)*100, 1)

percent_pass_overall = round((perc_pass_math + perc_pass_read)/2, 1)


# In[77]:


district_summary_df = pd.DataFrame({"Number of Schools": [total_schools],
                                    "Number of Students": [total_students],
                                    "Total Budget": [total_budget],
                                    "Average Math Score": [ave_math],
                                    "Percent Passing Math": [percent_pass_math],
                                    "Average Reading Score": [ave_read],
                                    "Percent Passing Reading": [percent_pass_read],
                                    "Overall Passing Percentage": [percent_pass_overall] },
                                   
            columns = ["Number of Schools", "Number of Students", "Total Budget", "Average Math Score", 
                       "Percent Passing Math", "Average Reading Score", "Percent Passing Reading", 
                       "Overall Passing Percentage"])
                                              
district_summary_df


# In[79]:


# create and label columns for merge

school_df = school_df.rename(columns = {"name": "school name"})

student_df = student_df.rename(columns = {"school": "school name"})


# In[81]:


#group students by school name
student_groupby_school = student_df.groupby(["school_name"])


# In[82]:


#calculate average math pass scores by school

avg_math_school = pd.DataFrame(round(student_groupby_school["math_score"].mean(), 2))
avg_math_school.columns = ["average math score"]
avg_math_school = avg_math_school.reset_index()

pass_math_school = student_df[student_df["math_score"] > 70].groupby("school_name")


pass_math_total_school = pd.DataFrame(round(pass_math_school["math_score"].count(), 1))
pass_math_total_school.columns = ["number pass math"]
pass_math_total_school = pass_math_total_school.reset_index()


# In[84]:


#calculate average reading pass scores by school
avg_read_school = pd.DataFrame(round(student_groupby_school["reading_score"].mean(), 1))
avg_read_school.columns = ["average reading score"]
avg_read_school = avg_read_school.reset_index()
pass_read_school = student_df[student_df["reading_score"] > 70].groupby("school_name")

pass_read_total_school = pd.DataFrame(pass_read_school["reading_score"].count())
pass_read_total_school.columns = ["number pass reading"]
pass_read_total_school = pass_read_total_school.reset_index()


# In[85]:


#merge school dataframe with newly made math and reading dataframes

combined_df = pd.merge(school_df, avg_math_school, on = "school_name", how = "outer")

combined_df = pd.merge(combined_df, pass_math_total_school, on = "school_name", how = "outer")

combined_df = pd.merge(combined_df, avg_read_school, on = "school_name", how = "outer")

combined_df = pd.merge(combined_df, pass_read_total_school, on= "school_name", how = "outer")

combined_df


# In[86]:


#create new column for percent passing math at each school

combined_df["% passing math"] = round((combined_df["number pass math"]/combined_df["size"])*100, 1)

#create new column for percent passing reading at each school
combined_df["% passing reading"] = round((combined_df["number pass reading"]/combined_df["size"])*100, 1)

#create new column for percent passing reading and math at each school
combined_df["% overall passing"] = round((combined_df["% passing math"] + combined_df["% passing reading"])/2, 1)

combined_df


# In[87]:



#create new column for budget per student
combined_df["budget/student"] = round(combined_df["budget"]/combined_df["size"], 2)

combined_df


# In[88]:


#school summary dataframe

school_summary = pd.DataFrame(combined_df[["school_name", "type", "size", "budget", "budget/student", 
                                                       "average math score", "% passing math", "average reading score", 
                                                       "% passing reading", "% overall passing"]])
school_summary


# In[ ]:


# Part Three: Top 5 performing schools
Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:

School Name
School Type
Total Students
Total School Budget
Per Student Budget
Average Math Score
Average Reading Score
get_ipython().run_line_magic('Passing', 'Math')
get_ipython().run_line_magic('Passing', 'Reading')
Overall Passing Rate (Average of the above two)
Top Performing Schools (By Passing Rate)


# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[10]:





# In[89]:



#Top Performing Schools (By % Overall Passing)¶
#Sort and display the top five performing schools by % overall passing.

top_performing_schools = pd.DataFrame(school_summary_unformatted.sort_values("% overall passing", ascending = False)[:5])
top_performing_schools


# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[ ]:


# Part Four: Bottom 5 performing schools
Include:

School Name
School Type
Total Students
Total School Budget
Per Student Budget
Average Math Score
Average Reading Score
get_ipython().run_line_magic('Passing', 'Math')
get_ipython().run_line_magic('Passing', 'Reading')
Overall Passing Rate (Average of the above two)


# In[11]:





# In[90]:



# Bottom Performing Schools (By % Overall Passing)¶
# Sort and display the five worst-performing schools by % overall passing.

bottom_performing_schools = pd.DataFrame(school_summary_unformatted.sort_values("% overall passing")[:5])
bottom_performing_schools


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[12]:





# In[91]:


# Part 5: Math Scores by Grade
#Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


# In[92]:



#collect data per grade

ninth = student_df.loc[student_df["grade"] == "9th"].groupby("school_name", as_index = False)                                                      
tenth = student_df.loc[student_df["grade"] == "10th"].groupby("school_name", as_index = False)
eleventh = student_df.loc[student_df["grade"] == "11th"].groupby("school_name", as_index = False)
twelfth = student_df.loc[student_df["grade"] == "12th"].groupby("school_name", as_index = False)


# In[93]:


#calculate math score averages per grade by school
ninth_math_avg_df = pd.DataFrame(round(ninth["math_score"].mean(), 1))
tenth_math_avg_df = pd.DataFrame(round(tenth["math_score"].mean(), 1))
eleventh_math_avg_df = pd.DataFrame(round(eleventh["math_score"].mean(), 1))
twelfth_math_avg_df = pd.DataFrame(round(twelfth["math_score"].mean(), 1))


# In[100]:


#Math Scores by Grade
#merge into one dataframe

avg_math_bygrade_df = pd.merge(ninth_math_avg_df, tenth_math_avg_df, on = "school_name", how = "inner")
avg_math_bygrade_df = pd.merge(avg_math_bygrade_df, eleventh_math_avg_df, on = "school_name", how = "inner")
avg_math_bygrade_df = pd.merge(avg_math_bygrade_df, twelfth_math_avg_df, on = "school_name", how = "inner")
avg_math_bygrade_df.columns = ["school name", "9th", "10th", "11th", "12th"]


avg_math_bygrade_df


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[13]:





# In[94]:


#Part 6: Reading Scores by Grade
#Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


# In[95]:



#calculate reading score averages per grade by school
ninth_read_avg_df = pd.DataFrame(round(ninth["reading_score"].mean(), 1))
tenth_read_avg_df = pd.DataFrame(round(tenth["reading_score"].mean(), 1))
eleventh_read_avg_df = pd.DataFrame(round(eleventh["reading_score"].mean(), 1))
twelfth_read_avg_df = pd.DataFrame(round(twelfth["reading_score"].mean(), 1))


# In[96]:


#Reading Scores by Grade
#merge into one dataframe
avg_read_bygrade_df = pd.merge(ninth_read_avg_df, tenth_read_avg_df, on = "school_name", how = "inner")
avg_read_bygrade_df = pd.merge(avg_read_bygrade_df, eleventh_read_avg_df, on = "school_name", how = "inner")
avg_read_bygrade_df = pd.merge(avg_read_bygrade_df, twelfth_read_avg_df, on = "school_name", how = "inner")
avg_read_bygrade_df.columns = ["school_name", "9th", "10th", "11th", "12th"]

avg_read_bygrade_df


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[18]:





# In[108]:


# #Part 7: Scores by School Spending

bins = [0, 600, 625, 650, 675]
group_names = ["< $600", "$600 - 625", "$625 - 650", "$650 - 675"]

Scores_by_School_Spending = round(school_summary[["average math score", "% passing math", 
                                                   "average reading score", "% passing reading", 
                                                   "% overall passing"]].groupby(pd.cut(school_summary_unformatted["size"],
                                                   bins = bins, labels = group_names)).mean(), 1)

Scores_by_School_Spending


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[110]:


#Scores by School Size

bins = [0, 1000, 3500, 5000]
group_names = ["Small (<1000)", "Medium (1000-3500)", "Large (3500-5000)"]

Scores_by_School_Size = round(school_summary[["average math score", "% passing math", 
                                                   "average reading score", "% passing reading", 
                                                   "% overall passing"]].groupby(pd.cut(school_summary_unformatted["size"],
                                                   bins = bins, labels = group_names)).mean(), 1)
Scores_by_School_Size


# In[ ]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[24]:





# In[111]:


#Scores by School Type

Scores_by_School_Type = round(school_summary_unformatted[["average math score", "% passing math", "average reading score",
                                                   "% passing reading", "% overall passing"]].groupby(
                                                   school_summary_unformatted["type"]).mean(), 1)

Scores_by_School_Type


# In[ ]:


# Observations##

# Smaller schools ie those with less than 1,000 students outperform larger schools with more than 3500 students.
# Charter schools outperfom District schools in both reading and math scores.
# It appears that budget per student produces no measurable affect on the increased score per student .

