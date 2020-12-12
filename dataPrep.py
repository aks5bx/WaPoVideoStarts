#%%
## Importing useful libraries and data file
import pandas as pd 
import numpy as np
pd.options.display.float_format = '{:.2f}'.format
wapoData = pd.ExcelFile('wapoData.xlsx')




#%% 
#######################
### READING IN DATA ###
#######################

## Overall Web Traffic
webTraffic = pd.read_excel(wapoData, 'Traffic to Washington Post', header =  2, index_col = 0).reset_index(drop = True)
webTraffic

## Overall Video Starts
videoStarts = pd.read_excel(wapoData, 'TWP Video Starts', header =  2, index_col = 0).reset_index(drop = True)
videoStarts = videoStarts.fillna(0.0)
videoStarts['Total Across All Platforms'] = videoStarts['Total'] + videoStarts['Facebook'] + videoStarts['YouTube'] + videoStarts['Apple News'] + videoStarts['AOL Video'] + videoStarts['MSN Video']
videoStarts

## Video Starts By Site Area
videoStartsSiteArea = pd.read_excel(wapoData, 'Video Starts by Site Area', header =  1, index_col = 0).reset_index(drop = True)
videoStartsSiteArea

## Video Starts by Hour (Mobile and Desktop)
mobileStartsHourly = pd.read_excel(wapoData, 'Video Starts by Hour', header =  2, index_col = 0, usecols = 'A:L').reset_index(drop = True).rename(columns = {'Hour' : 'Month'})

mobileStartsHourly = mobileStartsHourly.transpose()
new_header = mobileStartsHourly.iloc[0]
mobileStartsHourly = mobileStartsHourly[1:]
mobileStartsHourly.columns = new_header
mobileStartsHourly['Month'] = mobileStartsHourly.index
mobileStartsHourly = mobileStartsHourly[['Month', '12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM','12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM']]
mobileStartsHourly = mobileStartsHourly.rename_axis(None, axis=1).rename_axis('ind', axis=0).reset_index(drop = True)

desktopStartsHourly = pd.read_excel(wapoData, 'Video Starts by Hour', header =  2, index_col = 0, usecols = 'M:X').reset_index(drop = True).rename(columns = {'Hour' : 'Month'})
desktopStartsHourly.columns = desktopStartsHourly.columns.str.rstrip('.1')
desktopStartsHourly = desktopStartsHourly.transpose()
new_header = desktopStartsHourly.iloc[0]
desktopStartsHourly = desktopStartsHourly[1:]
desktopStartsHourly.columns = new_header
desktopStartsHourly['Month'] = desktopStartsHourly.index
desktopStartsHourly = desktopStartsHourly[['Month', '12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM','12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM']]
desktopStartsHourly = desktopStartsHourly.rename_axis(None, axis=1).rename_axis('ind', axis=0).reset_index(drop = True)

## Video Starts by Site Section
videoStartsSiteSection = pd.read_excel(wapoData, 'Video Starts by Site Section', header =  2, index_col = 0).reset_index(drop = True).rename(columns = {'Site Section' : 'Month'})
videoStartsSiteSection = videoStartsSiteSection.T
videoStartsSiteSection
new_header = videoStartsSiteSection.iloc[0]
videoStartsSiteSection = videoStartsSiteSection[1:]
videoStartsSiteSection.columns = new_header
videoStartsSiteSection['Month'] = videoStartsSiteSection.index
videoStartsSiteSection = videoStartsSiteSection[['Month', 'wp - posttv', 'wp - politics', 'wp - local', 'wp - national',
       'wp - opinions', 'wp - lifestyle', 'wp - world', 'wp - homepage',
       'wp - powerpost', 'wp - business', 'wp - sports', 'wp - entertainment',
       'Others', 'Total']]
videoStartsSiteSection = videoStartsSiteSection.rename_axis(None, axis=1).rename_axis('ind', axis=0).reset_index(drop = True)
videoStartsSiteSection
#%%
## Top 1000 videos of 2017 
top1000Videos = pd.read_excel(wapoData, 'Top 1000 Videos in 2017', header =  1, index_col = 0).reset_index(drop = True)
top1000Videos
#%%
## Videos Product Testing
videoTesting = pd.read_excel(wapoData, 'Videos Product Testing', header =  1, index_col = 0).reset_index(drop = True)
videoTesting

## Video Starts by Referrer Type
videoStartsReferrer = pd.read_excel(wapoData, 'Video Starts by Referrer Type', header =  2, index_col = 0).reset_index(drop = True)
videoStartsReferrer

## Video Starts - Facebook and Google
videoStartsSocialMedia = pd.read_excel(wapoData, 'Video Starts from FB & Google', header =  3, index_col = 0).reset_index(drop = True)
videoStartsSocialMedia

## Videos Produced
videosProduced = pd.read_excel(wapoData, 'Videos Produced', header =  1, index_col = 0).reset_index(drop = True)
videosProduced

## Pre Roll Ads on Videos
videosPreProll = pd.read_excel(wapoData, 'Pre-roll Ads on Videos', header =  1, index_col = 0).reset_index(drop = True)
videosPreProll





# %%
###########################
### HIGH LEVEL ANALYSIS ###
###########################
## Overall website traffic

## By looking at the table generally we can see that there is no significant increase or decrease in unique visitors, visits, or pageviews for the month of October versus the preceding months 
## We can confirm this by seeing that the values for October are all within the standard deviation for both the previous month's number and the 2017 Jan - Sep average numbers

webTrafficPre = webTraffic[webTraffic.Month < '2017-10-01']
webTrafficPre.loc['stdev'] = webTrafficPre.std()
webTrafficPre.loc['avg'] = webTrafficPre.mean()

webTrafficL3M = webTrafficPre[webTrafficPre.Month > '2017-07-01']
webTrafficL3M.loc['stdev'] = webTrafficL3M.std()
webTrafficL3M.loc['avg'] = webTrafficL3M.mean()

webTrafficOct = webTraffic[webTraffic.Month >= '2017-10-01']

for col in webTrafficPre.columns: 
    if col == 'Month':
        continue 

    pre_std = webTrafficPre[webTrafficPre.index == 'stdev'][col].values[0]
    l3m_std = webTrafficL3M[webTrafficL3M.index == 'stdev'][col].values[0]


    pre_avg = webTrafficPre[webTrafficPre.index == 'avg'][col].values[0]
    l3m_avg = webTrafficL3M[webTrafficL3M.index == 'avg'][col].values[0]

    october = webTrafficOct[col].values[0]

    if (l3m_avg - october) > (l3m_std * 0.25): 
        print('Last 3 Month: Significant Dip ', col, ' ', october)

    if (pre_avg - october) > (pre_std * 0.25): 
        print('2017: Significant Dip ', col, ' ', october)





#%%
## Overall Video Starts

## At first glance, it appears that the YouTube numbers are abnormally low, which close to a 9 million video start deficit from the month prior. Additionally, the wapo.com numbers look low for a similar reason. 
## However, after further analysis, we see that the fluctuation exhibited by the YouTube numbers are actually well within range of the fluctuation we see historically and specifically during 2017. By doing this analysis, we instead uncover wapo.com being abnormally low and MSN Video being abnormally low. 
## We also find that video starts are really only down in total from the July - Sep upswing; the total starts metric from the data available 

videoStartsPre = videoStarts[videoStarts.Month < '2017-10-01']
videoStarts2017Pre = videoStartsPre[videoStartsPre.Month > '2016-12-01']
videoStartsJulyPlus = videoStartsPre[videoStartsPre.Month > '2017-07-01']

videoStartsPre = videoStartsPre.replace(0, np.NaN)
videoStarts2017Pre = videoStarts2017Pre.replace(0, np.NaN)
videoStartsJulyPlus = videoStartsJulyPlus.replace(0, np.NaN)

videoStartsPre.loc['stdev'] = videoStartsPre.std()
videoStartsPre.loc['avg'] = videoStartsPre.mean()

videoStarts2017Pre.loc['stdev'] = videoStarts2017Pre.std()
videoStarts2017Pre.loc['avg'] = videoStarts2017Pre.mean()

videoStartsJulyPlus.loc['stdev'] = videoStartsJulyPlus.std()
videoStartsJulyPlus.loc['avg'] = videoStartsJulyPlus.mean()

videoStartsOct =  videoStarts[videoStarts.Month >= '2017-10-01']

preOct = []
preOct2017 = []
JulytoSep = []
for col in videoStarts2017Pre.columns: 
    if col == 'Month' or col == 'Total':
        continue

    pre_std = videoStartsPre[videoStartsPre.index == 'stdev'][col].values[0]
    pre2017_std = videoStarts2017Pre[videoStarts2017Pre.index == 'stdev'][col].values[0]
    julyPlus_std = videoStartsJulyPlus[videoStartsJulyPlus.index == 'stdev'][col].values[0]


    pre_avg = videoStartsPre[videoStartsPre.index == 'avg'][col].values[0]
    pre2017_avg = videoStarts2017Pre[videoStarts2017Pre.index == 'avg'][col].values[0]
    julyPlus_avg = videoStartsJulyPlus[videoStartsJulyPlus.index == 'avg'][col].values[0]


    october = videoStartsOct[col].values[0]

    if (pre_avg - october) > pre_std * (0.25):
        preOct.append((col, october))

    if (pre2017_avg - october) > pre2017_std * 0.25:
        preOct2017.append((col, october))

    if (julyPlus_avg - october) > pre2017_std * 0.25:
        JulytoSep.append((col, october))


print('Pre October Issues')
for each in preOct:
    print(each)

print('Pre Oct 2017 Issues')
for each in preOct:
    print(each)

print('July to Sep 2017 Issues')
for each in preOct:
    print(each)




# %%
## Video Starts by Site Area
VSSApre = videoStartsSiteArea[videoStartsSiteArea.Month < '2017-10-01']
VSSApre.loc['stdev'] = VSSApre.std()
VSSApre.loc['avg'] = VSSApre.mean()

VSSA_l3m = VSSApre[VSSApre.Month > '2017-07-01']
VSSA_l3m.loc['stdev'] = VSSA_l3m.std()
VSSA_l3m.loc['avg'] = VSSA_l3m.mean()

VSSA_october = videoStartsSiteArea[videoStartsSiteArea.Month >= '2017-10-01']

for col in VSSA_october.columns: 
    if col == 'Month' or col == 'Video - Start':
        continue 

    pre_std = VSSApre[VSSApre.index == 'stdev'][col].values[0]
    l3m_std = VSSA_l3m[VSSA_l3m.index == 'stdev'][col].values[0]


    pre_avg = VSSApre[VSSApre.index == 'avg'][col].values[0]
    l3m_avg = VSSA_l3m[VSSA_l3m.index == 'avg'][col].values[0]

    october = VSSA_october[col].values[0]

    if (l3m_avg - october) > (l3m_std * 0.25): 
        print('Last 3 Month: Significant Dip ', col, ' ', october)

    if (pre_avg - october) > (pre_std * 0.25): 
        print('2017: Significant Dip ', col, ' ', october)





# %%
## Video Starts by Site Section

VSSSpre = videoStartsSiteSection[videoStartsSiteSection.Month < '2017-10-01']
VSSSpre.loc['stdev'] = VSSSpre.std()
VSSSpre.loc['avg'] = VSSSpre.mean()

VSSS_l3m = VSSSpre[VSSSpre.Month > '2017-07-01']
VSSS_l3m.loc['stdev'] = VSSS_l3m.std()
VSSS_l3m.loc['avg'] = VSSS_l3m.mean()

VSSS_october = videoStartsSiteSection[videoStartsSiteSection.Month >= '2017-10-01']

for col in VSSS_october.columns: 
    if col == 'Month' or col == 'Video - Start':
        continue 

    pre_std = VSSSpre[VSSSpre.index == 'stdev'][col].values[0]
    l3m_std = VSSS_l3m[VSSS_l3m.index == 'stdev'][col].values[0]

    pre_avg = VSSSpre[VSSSpre.index == 'avg'][col].values[0]
    l3m_avg = VSSS_l3m[VSSS_l3m.index == 'avg'][col].values[0]

    october = VSSS_october[col].values[0]

    if (l3m_avg - october) > (l3m_std * 0.5): 
        print('Last 3 Month: Significant Dip ', col, ' ', october)

    if (pre_avg - october) > (pre_std * 0.5): 
        print('2017: Significant Dip ', col, ' ', october)





# %%
## Hourly Video Starts
import statistics

mobileHSpre = mobileStartsHourly[mobileStartsHourly.Month < '2017-10-01']
mobileHSpre.loc['stdev'] = mobileHSpre.std()
mobileHSpre.loc['avg'] = mobileHSpre.mean()

mobileHSl3m = mobileHSpre[mobileHSpre.Month > '2017-07-01']
mobileHSl3m.loc['stdev'] = mobileHSl3m.std()
mobileHSl3m.loc['avg'] = mobileHSl3m.mean()

mobileHSOctober = mobileStartsHourly[mobileStartsHourly.Month >= '2017-10-01']
mtotal = []
mtotalL3M = []

for col in mobileHSOctober.columns: 
    if col == 'Month' or col == 'Video - Start':
        continue 

    pre_std = mobileHSpre[mobileHSpre.index == 'stdev'][col].values[0]
    l3m_std = mobileHSl3m[mobileHSl3m.index == 'stdev'][col].values[0]

    pre_avg = mobileHSpre[mobileHSpre.index == 'avg'][col].values[0]
    l3m_avg = mobileHSl3m[mobileHSl3m.index == 'avg'][col].values[0]

    october = mobileHSOctober[col].values[0]

    if (l3m_avg - october) > (l3m_std * 0.25): 
        print('Last 3 Month: Significant Dip ', col, ' ', october)
        print(l3m_avg - october)
        mtotalL3M.append(l3m_avg - october)

    if (pre_avg - october) > (pre_std * 0.25): 
        print('2017: Significant Dip ', col, ' ', october)
        print(pre_avg - october)
        mtotal.append(pre_avg - october)



# %%
## Desktop Video Starts
## Hourly Video Starts

desktopHSpre = desktopStartsHourly[desktopStartsHourly.Month < '2017-10-01']
desktopHSpre.loc['stdev'] = desktopHSpre.std()
desktopHSpre.loc['avg'] = desktopHSpre.mean()

desktopHSl3m = desktopHSpre[desktopHSpre.Month > '2017-07-01']
desktopHSl3m.loc['stdev'] = desktopHSl3m.std()
desktopHSl3m.loc['avg'] = desktopHSl3m.mean()

desktopHSOctober = desktopStartsHourly[desktopStartsHourly.Month >= '2017-10-01']
dtotal = []
dtotalL3M = []

for col in desktopHSOctober.columns: 
    if col == 'Month' or col == 'Video - Start':
        continue 

    pre_std = desktopHSpre[desktopHSpre.index == 'stdev'][col].values[0]
    l3m_std = desktopHSl3m[desktopHSl3m.index == 'stdev'][col].values[0]

    pre_avg = desktopHSpre[desktopHSpre.index == 'avg'][col].values[0]
    l3m_avg = desktopHSl3m[desktopHSl3m.index == 'avg'][col].values[0]

    october = desktopHSOctober[col].values[0]


    if (l3m_avg - october) > (l3m_std * 0.25): 
        print('Last 3 Month: Significant Dip ', col, ' ', october)
        print(l3m_avg - october)
        dtotalL3M.append(l3m_avg - october)

    if (pre_avg - october) > (pre_std * 0.25): 
        print('2017: Significant Dip ', col, ' ', october)
        print(pre_avg - october)
        dtotal.append(pre_avg - october)


# %%
## Top 1000 Videos

def trySplit(text):
    try:
        val = text.split('-')[1]
    except:
        val = None
    return val

def getMonth(date):
    month = date.split('/')[0]
    return month

def getYear(date):
    try:
        month = date.split('/')[2]
    except: 
        month = 123

    return month

top1000Videos['Date'] = top1000Videos['Video Name'].apply(lambda x : trySplit(x))
top1000Videos = top1000Videos.dropna()
top1000Videos['Month'] = top1000Videos['Date'].apply(lambda x : getMonth(x))
top1000Videos['Year'] = top1000Videos['Date'].apply(lambda x : getYear(x))


top1000Videos = top1000Videos[top1000Videos.Year == '2017 ']
top1000Videos = top1000Videos[top1000Videos['Month'].isin([' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',' 12'])]
top1000Videos['Month'] = top1000Videos['Month'].astype('int')
t1000gb = top1000Videos.groupby('Month')['Video Starts'].sum().reset_index().sort_values(by = 'Month')
t1000gb = t1000gb[t1000gb.Month < 11]
t1000gb.loc['Average'] = t1000gb.mean()


# %%
