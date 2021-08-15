import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
#automatically generates x vlues if u dnt pass any
plt.plot([1,2,3,4],[1,4,9.6]) #(x,y)
plt.ylabel("ylabel ","x label") #labeling thr graph
plt.plot([1,2,3,4],[1,4,9.6],'ro')
#ro :red dot
#r-- :red dashes
#bs :blue square
#g^ :green triangle


import matplotlib.pyplot as plt
Estimates=[]
#constnt values for y
y=[]
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates, y, 'r--')


