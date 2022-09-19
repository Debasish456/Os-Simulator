from django.test import TestCase

# Create your tests here.

# global arrival,ans
#     sorted_Arrival=[]
#     if request.method=="POST":
#         sorted_Arrival=sorted(arrival,key=lambda x: (x[0],x[1]))
#         ans.append(sorted_Arrival[0])
#         for i in range(len(sorted_Arrival)):
#             if i==0:
#                 ct=sorted_Arrival[i][0]+sorted_Arrival[i][1]
#                 wt=0
#                 tat=ct-sorted_Arrival[i][0]
#                 sorted_Arrival[i][3]=True
#                 ans[i][3]=True 
#                 ans[i].append(ct)
#                 ans[i].append(0)
#                 ans[i].append(tat)
#                 completion=ct
#             else:
#                 j=0
#                 queue=[]
                
#                 while j<len(sorted_Arrival) and sorted_Arrival[j][0]<=completion and not sorted_Arrival[j][3]:
#                     sorted_Arrival[j][3]=True
#                     queue.append(sorted_Arrival[j])
#                     j+=1
#                 sorted_queue=sorted(queue,key=lambda x: (x[1],x[0]))
#                 for k in range(len(sorted_queue)):
#                     if k==0:
#                         ct=sorted_queue[k][0]+sorted_queue[k][1]
#                         wt=0
#                     else:
#                         ct=max(sorted_Arrival[k-1][4],sorted_Arrival[k][0])+sorted_Arrival[k][1]
#                         wt=max(0,sorted_Arrival[k-1][4]-sorted_Arrival[k][0])
#                     completion=max(completion,ct)

#                     tat=ct-sorted_queue[k][0]
#                     sorted_queue[k].append(ct)
#                     sorted_queue[k].append(wt)
#                     sorted_queue[k].append(tat)
#                 for i in range(len(sorted_queue)):
#                     ans.append(sorted_queue[i])
#     else:
#         arrival=[]
#         ans=[]