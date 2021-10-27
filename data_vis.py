import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

path = 'sat_data.csv'

sat = pd.read_csv(path)

path = 'un_enrollment_data.csv'

un = pd.read_csv(path)

#Preparing the data for enrollment

enrollment_by_year = pd.DataFrame(columns=['year','USA','Czech_Rep','Italy','total'])


for year in range(1999,2014):
    USA = un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'Female') & (un['Reference Area'] == 'United States of America')].sum() / un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'United States of America')].sum() 
    Czech_Rep = un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'Female') & (un['Reference Area'] == 'Czech Republic')].sum() / un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'Czech Republic')].sum()
    Italy = un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'Female') & (un['Reference Area'] == 'Italy')].sum() / un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'Italy')].sum()
    

    
    total = un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'United States of America')].sum() + un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'Czech Republic')].sum() + un['Observation Value'].loc[(un['Time Period'] == year) & (un['Sex'] == 'All genders') & (un['Reference Area'] == 'Italy')].sum()
    
    temp = {'year':year,'USA':USA,'Czech_Rep':Czech_Rep,'Italy':Italy, 'total':total}
    
    enrollment_by_year = enrollment_by_year.append(temp, ignore_index=True)
    
    
#Preparing the data for SAT    
    
step = 50

sat_results = pd.DataFrame(columns=['range','maths','reading','writing'])

for bin in range(4,16):
    
    if bin == 4:
        res_range = str(step*bin) + ' - ' + str(step*(bin+1))
    else:
        res_range = str(step*bin + 1) + ' - ' + str(step*(bin+1))
        
        
    maths = len(sat.loc[(sat['Mathematics Mean'] > (step*bin)) & (sat['Mathematics Mean'] < (step*(bin+1)+1))])
    reading = len(sat.loc[(sat['Critical Reading Mean'] > (step*bin)) & (sat['Critical Reading Mean'] < (step*(bin+1)+1))])
    writing = len(sat.loc[(sat['Writing Mean'] > (step*bin)) & (sat['Writing Mean'] < (step*(bin+1)+1))])
    
    temp = {'range':res_range,'maths':maths,'reading':reading,'writing':writing}
    
    sat_results = sat_results.append(temp, ignore_index = True)
    
    
plt.figure(1)

plot1 = sat_results.plot(kind='bar', x = 'range', xlabel = 'Mean Range', ylabel = 'Number of schools')

plot1.legend(labels=['Mean in Mathematics', 'Mean in Critical Reading', 'Mean in Writing'])

plt.savefig('SAT_figure.png')

plt.figure(2)


plot2 = enrollment_by_year.plot(kind = 'line', x = 'year', y = ['USA', 'Czech_Rep', 'Italy'], xlabel = 'Year', ylabel = 'Percentage of female in Grade 5')

plot2.legend(labels=['USA', 'Czech Republic', 'Italy'])
plt.xticks(range(1999, 2014, 1))
plt.xticks(rotation=90)

plot2.yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
    
plt.savefig('Enrollment_figure.png')

    

    
    
    

    
    