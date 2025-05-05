# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="white")
# %%

# Defining the file path for the Excel file
EXfp = 'EValuateNY.xlsx'

# Opening the Excel file and going to the correct sheet and skipping the first two rows while indexing on "Row Labels"
df = pd.read_excel(EXfp, sheet_name='Pivot Table', skiprows=2, index_col='Row Labels', dtype=str)

# Show the first few rows to confirm everything is going correctly
print(df.head())
# %%
# Making sure that the specificed columns are numeric so that calculations will go over smoothly 
df['BEVs on the Road'] = pd.to_numeric(df['BEVs on the Road'])
df['PHEVs on the Road'] = pd.to_numeric(df['PHEVs on the Road'])
df['EVs on the Road'] = pd.to_numeric(df['EVs on the Road'])
df['DCFC Ports'] = pd.to_numeric(df['DCFC Ports'])
df['Level 2 Ports'] = pd.to_numeric(df['Level 2 Ports'])

# Rounding the three columns ('BEVs on the Road', 'PHEVs on the Road', 'EVs on the Road') to whole numbers
df['BEVs on the Road'] = df['BEVs on the Road'].round(0)
df['PHEVs on the Road'] = df['PHEVs on the Road'].round(0)
df['EVs on the Road'] = df['EVs on the Road'].round(0)
print(df.head())

# %%
#Cleaning the data of unnecessary rows
df_clean = df[df.index.isin(['(blank)', 'Out of State', 'Unknown', 'Grand Total'])==False]
# %%

# Sort the DataFrame by the relevant columns and get the top 15 counties
df_sorted_bevs = df_clean.sort_values('BEVs on the Road', ascending=False)
df_sorted_phevs = df_clean.sort_values('PHEVs on the Road', ascending=False)
df_sorted_evs = df_clean.sort_values('EVs on the Road', ascending=False)

# %%
#Creating Bar Charts for the 3 "...on the Road" columns
# Setting up figure and axis for the BEVs graph
fig, ax1 = plt.subplots()
# Plotting the data on ax1 using sns.barplot
sns.barplot(x=df_sorted_bevs.head, y=df_sorted_bevs['BEVs on the Road'], ax=ax1)
# Adding titles and labels
ax1.set_title("Top 15 Counties for BEVs on the Road")
ax1.set_xlabel('County')
ax1.set_ylabel('Number of BEVs on the Road')
# Rotate x-axis labels for readability
ax1.set_xticklabels(df_sorted_bevs.index, rotation=90)
# Adjust layout
fig.tight_layout()
# Showing the plot 
plt.show()
# Saving the figure
fig.savefig('T_15_BEVs_OTR.png')
# %%

# Setting up figure and axis for the PHEVs graph
fig, ax1 = plt.subplots()
# Plotting the data on ax1 using sns.barplot
sns.barplot(x=df_sorted_phevs.index, y=df_sorted_phevs['PHEVs on the Road'], ax=ax1)
# Adding titles and labels
ax1.set_title("Top 15 Counties for PHEVs on the Road")
ax1.set_xlabel('County')
ax1.set_ylabel('Number of PHEVs on the Road')
# Rotate x-axis labels for readability
ax1.set_xticklabels(df_sorted_phevs.index, rotation=90)
# Adjust layout
fig.tight_layout()
# Showing the plot
plt.show()
# Saving the figure
fig.savefig('T_15_PHEVs_OTR.png')
# %%

# Setting up figure and axis for the EVs graph
fig, ax1 = plt.subplots()
# Plotting the data on ax1 using sns.barplot
sns.barplot(x=df_sorted_evs.index, y=df_sorted_evs['EVs on the Road'], ax=ax1)
# Adding titles and labels
ax1.set_title("Top 15 Counties for EVs on the Road")
ax1.set_xlabel('County')
ax1.set_ylabel('Number of EVs on the Road')
# Rotate x-axis labels for readability
ax1.set_xticklabels(df_sorted_evs.index, rotation=90)
# Adjust layout
fig.tight_layout()
# Showing the plot
plt.show()
# Saving the figure
fig.savefig('T_15_EVs_OTR.png')
# %%

#Creating a new column that tells shows the total amount of chargers available in each county and then calculating the # of ports per EV

df_sorted_DCFC = df_clean.sort_values('DCFC Ports', ascending=False).head(15)
df_sorted_L2 = df_clean.sort_values('Level 2 Ports', ascending=False).head(15)
# %%

# Setting up figure and axis for the DCFCs graph
fig, ax1 = plt.subplots()
# Plotting the data on ax1 using sns.barplot
sns.barplot(x=df_sorted_DCFC.index, y=df_sorted_DCFC['DCFC Ports'], ax=ax1)
# Adding titles and labels
ax1.set_title("Top 15 Counties for DCFC Ports")
ax1.set_xlabel('County')
ax1.set_ylabel('Number of DCFC Ports')
# Rotate x-axis labels for readability
ax1.set_xticklabels(df_sorted_DCFC.index, rotation=90)
# Adjust layout
fig.tight_layout()
# Showing the plot
plt.show()
# Saving the figure
fig.savefig('T_15_DCFC_Ports.png')
# %%

# Setting up figure and axis for the EVs graph
fig, ax1 = plt.subplots()
# Plotting the data on ax1 using sns.barplot
sns.barplot(x=df_sorted_L2.index, y=df_sorted_L2['Level 2 Ports'], ax=ax1)
# Adding titles and labels
ax1.set_title("Top 15 Counties for Level 2 Ports")
ax1.set_xlabel('County')
ax1.set_ylabel('Number of Level 2 Ports')
# Rotate x-axis labels for readability
ax1.set_xticklabels(df_sorted_L2.index, rotation=90)
# Adjust layout
fig.tight_layout()
# Saving the figure
fig.savefig('T_15_L2_Ports.png')
# Showing the plot
plt.show()



