#%%
print("The quick brown fox")
#%%
# %matplotlib inline 
import matplotlib.pyplot as mt
import pandas as  pd


#%%
spots = pd.read_csv("http://sidc.be/silso/DATA/SN_d_tot_V2.0.csv",sep=";" )
spots.columns = ["Year","Month","Day", "Fdate","Spots", "Sd","Obs" ,"Defin"]
spots.head()
#%%
## Download NOAA/AAVSO Sunspot and Plot
noaa = pd.read_csv("https://www.aavso.org/sites/default/files/solar/NOAAfiles/NOAAdaily.csv")
noaa.head()
#%%
x = spots.Fdate
y = spots.Spots
mt.figure(figsize =(12,8))
mt.plot(x,y)
mt.title("Mean Yearly Sunspots")
mt.xlabel("Year")
mt.ylabel("Mean Sunspots")
mt.grid(axis='both')
mt.show()
#%%
# Pull out data for 1955 and plot
s = spots[spots.Year==1955]
s.head()
#%%
x = s.Month
y = s.Spots
mt.figure(figsize =(12,8))
mt.bar(x,y)
mt.title("Sunspost for the Year of my Birth: 1955")
mt.xlabel("Year")
mt.ylabel("Mean Sunspots")
mt.grid(axis='y')
mt.show()
#%%
# Plot (NOAA) sunspot for year >= 2010
n = noaa[noaa.Year >=2010]
n.head()
x = n.Year
y = n.Ra
mt.figure(figsize =(12,8))
mt.bar(x,y)
mt.title("Mean Sunspots(NOAA) by Year:2010-2019")
mt.xlabel("Year")
mt.ylabel("Mean Sunspots")
mt.grid(axis='y')
mt.show()
