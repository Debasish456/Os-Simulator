from re import A
from django.shortcuts import render
arrival=list()
i=1


def index(request):
    return render(request,'PS/ps.html')

def add(request):  
    global arrival,i
    ps=0
    if request.method=='POST':
        a1=int(request.POST['newat'])
        a2=int(request.POST['newbt'])
        ps=int(request.POST['a3'] )
        arrival.append([a1,a2,i,False])
        i+=1

    else:
        arrival=[]
        i=1
    
    if ps==1:
        return render(request, 'PS/pscheduling/fcfs.html', {'arrival':arrival})
    elif ps==2:
        return render(request, 'PS/pscheduling/sjf.html', {'arrival':arrival})
    elif ps==3:
        return render(request, 'PS/pscheduling/rr.html', {'arrival':arrival})
    elif ps==4:
        return render(request, 'PS/pscheduling/srtf.html', {'arrival':arrival})
    elif ps==5:
        return render(request, 'PS/pscheduling/priority.html', {'arrival':arrival})
    else:
        return render(request, 'PS/pscheduling/fcfs.html', {'arrival':arrival})

def clear(request):
    global arrival,i
    ps=0
    
    if request.method=="POST":
        arrival=[]
        i=1
        ps=int(request.POST['clearv'])

    if ps==1:
        return render(request, 'PS/pscheduling/fcfs.html', {'arrival':arrival})
    elif ps==2:
        return render(request, 'PS/pscheduling/sjf.html', {'arrival':arrival})
    elif ps==3:
        return render(request, 'PS/pscheduling/rr.html', {'arrival':arrival})
    elif ps==4:
        return render(request, 'PS/pscheduling/srtf.html', {'arrival':arrival})
    elif ps==5:
        return render(request, 'PS/pscheduling/priority.html', {'arrival':arrival})
    else:
        return render(request, 'PS/pscheduling/fcfs.html', {'arrival':arrival})

def edit(request,p):
    pass

def fcfs(request):
    global arrival,i
    sorted_Arrival=[]
    if request.method=="POST":
        sorted_Arrival=sorted(arrival,key=lambda m:m[0])
        for i in range(len(sorted_Arrival)):
            if i==0:
                ct=sorted_Arrival[i][0]+sorted_Arrival[i][1]
                wt=0
            else:
                ct=max(sorted_Arrival[i-1][4],sorted_Arrival[i][0])+sorted_Arrival[i][1]
                wt=max(0,sorted_Arrival[i-1][4]-sorted_Arrival[i][0])
            tat=ct-sorted_Arrival[i][0]
            sorted_Arrival[i].append(ct)
            sorted_Arrival[i].append(wt)
            sorted_Arrival[i].append(tat)
    else:
        arrival=[]
        i=1

    return render(request, 'PS/pscheduling/fcfs.html',{'arrival':arrival,"sorted":sorted_Arrival})


def sjf(request):
    global arrival,i
    ans=[]
    
    
    if request.method=='POST':
        sorted_Arrival=sorted(arrival, key=lambda x: (x[0],x[1]))
        j=0
        while j<len(sorted_Arrival):
            if not ans:
                sorted_Arrival[0][3]=True
                ans.append(sorted_Arrival[0])
                ans[0].append(ans[0][0]+ans[0][1])
                ans[0].append(0)
                ans[0].append(ans[0][4]-ans[0][0])
                completion=ans[0][4]
            else:
                m=1e9
                samp=-1
                for i in range(len(sorted_Arrival)):
                    if not sorted_Arrival[i][3] and sorted_Arrival[i][0]<=completion:
                        if sorted_Arrival[i][1]<m:
                            m=sorted_Arrival[i][1]
                            samp=i
                if samp!=-1:
                    sorted_Arrival[samp][3]=True
                    ans.append(sorted_Arrival[samp])
                    ans[j].append(ans[j-1][4]+ans[j][1])
                    ans[j].append(ans[j-1][4]-ans[j][0])
                    ans[j].append(ans[j][4]-ans[j][0])
                    completion=ans[j][4]
                else:
                    for i in range(len(sorted_Arrival)):
                        if not sorted_Arrival[i][3]:
                            sorted_Arrival[i][3]=True
                            ans.append(sorted_Arrival[i])
                            ans[j].append(ans[j][0]+ans[j][1])
                            ans[j].append(0)
                            ans[j].append(ans[j][4]-ans[j][0])
                            completion=ans[j][4]
                            break

            j+=1
    
    else:
        arrival=[]
        i=1
        
    return render(request, 'PS/pscheduling/sjf.html',{'arrival':arrival,'sorted':ans})

def srtf(request):
    return render(request, "PS/pscheduling/srtf.html")

def priority(request):
    return render(request, "PS/pscheduling/priority.html")

def rr(request):
    return render(request,'PS/pscheduling/rr.html')