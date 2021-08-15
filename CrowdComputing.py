from statistics import mean
from  scipy import stats
Estimates = []
#To calculate trim mean so sort the above list, sort func sorts the data in ascending order
Estimates.sort()
m=stats.trim_meam(Estimates,0.1)
print(m)
# for i in range(len(Estimates)):
#     print(Estimates[i])
#Ten % mean
tv=int(0.1*len(Estimates)) #0.1*75 = 7.5 => 7
#Delete tha smalles 10% values
Estimates = Estimates[tv:]
#Remove the largest 10% values
Estimates = Estimates[:len(Estimates)-tv]

#Calculate the mean
print(mean(Estimates))

