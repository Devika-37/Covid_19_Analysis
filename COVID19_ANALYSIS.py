
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set visualization style
sns.set_style('darkgrid')
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (17, 5)
plt.rcParams['figure.facecolor'] = '#00000000'

# Read the dataset
df = pd.read_csv('sample_covid.csv')

# Select relevant columns
rnr = df[['continent', 'location', 'total_cases', 'total_deaths', 'people_vaccinated', 'total_boosters']]

# Group by location and get the max value for each metric
dfe = rnr.groupby('location', as_index=False).max()

# Remove specific rows by index (if they exist)
invalid_indices = [1, 12, 70, 71, 96]
sm = dfe.drop(index=[i for i in invalid_indices if i in dfe.index])

# Reset index and sort by total cases
sn = sm.reset_index(drop=True).sort_values('total_cases', ascending=False).reset_index(drop=True)

# Extract and plot Top 20 Countries by Total Cases
top20_ca = sn.head(20)

# Plot with explicit label color
plt.figure(figsize=(17, 8))
sns.barplot(x='total_cases', y='location', data=top20_ca, palette='viridis')

# plotting
plt.title('Top 20 Countries in Asia by Total Cases', color='white', fontsize=18)
plt.xlabel('Total Cases', color='white')
plt.ylabel('Country', color='white')
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')

# Display the plot
plt.show()


# Extract and plot Top 20 Countries by Total Deaths
top20_de = sn.sort_values('total_deaths', ascending=False).head(20)
top20_deaths = top20_de[['location', 'total_deaths']].reset_index(drop=True)

plt.figure(figsize=(17, 8))
sns.barplot(x='total_deaths', y='location', data=top20_deaths, palette='plasma')

# plotting
plt.title('Top 20 Countries in Asia by Total Deaths', color='white', fontsize=18)
plt.xlabel('Total Deaths', color='white')
plt.ylabel('Country', color='white')
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')
plt.show()

# Extract and plot Top 20 Countries by People Vaccinated
top20_vac = sn.sort_values('people_vaccinated', ascending=False).head(20)
top20_vaccinated = top20_vac[['location', 'people_vaccinated']].reset_index(drop=True)

plt.figure(figsize=(17, 8))
sns.barplot(x='people_vaccinated', y='location', data=top20_vaccinated, palette='coolwarm')

# Plotting
plt.title('Top 20 Countries in Asia by People Vaccinated', color='white', fontsize=18)
plt.xlabel('People Vaccinated', color='white')
plt.ylabel('Country', color='white')
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')
plt.show()

# Extract and plot Top 20 Countries by Total Boosters
top20_boos = sn.sort_values('total_boosters', ascending=False).head(20)
top20_boosters = top20_boos[['location', 'total_boosters']].reset_index(drop=True)

plt.figure(figsize=(17, 8))
sns.barplot(x='total_boosters', y='location', data=top20_boosters, palette='copper')

# Plotting
plt.title('Top 20 Countries in Asia by Total Boosters', color='white', fontsize=18)
plt.xlabel('Total Boosters', color='white')
plt.ylabel('Country', color='white')
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')
plt.show()


