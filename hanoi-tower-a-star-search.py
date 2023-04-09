# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:49:21 2023
comp3600/20
assignment 2
name:Reem Al Harrasi
id:126146
"""
#variables for design purposes
line='_'*40

#put our tower of hanoi space set in a dictionary
space={'LMS,0,0':[('LM,0,S',1),('LM,S,0',1)],
           'LM,0,S':[('L,M,S',2),('LM,S,0',1),('LMS,0,0',1)],
           'LM,S,0':[('L,S,M',2),('LM,0,S',1),('LMS,0,0',1)],
           'L,M,S':[('L,MS,0',1),('LS,M,0',1),('LM,0,S',2)],
           'L,S,M':[('L,0,MS',1),('LS,0,M',1),('LM,S,0',2)],
           'L,MS,0':[('0,MS,L',3),('LS,M,0',1),('L,M,S',1)],
           'LS,M,0':[('L,MS,0',1),('LS,0,M',2),('L,M,S',1)],
           'LS,0,M':[('L,0,MS',1),('LS,M,0',2),('L,S,M',1)],
           'L,0,MS':[('0,L,MS',3),('LS,0,M',1),('L,S,M',1)],
           '0,MS,L':[('S,M,L',1),('0,M,LS',1),('L,MS,0',3)],
           '0,L,MS':[('S,L,M',1),('0,LS,M',1),('L,0,MS',3)],
           'S,M,L':[('S,0,LM',2),('0,M,LS',1),('0,MS,L',1)],
           '0,M,LS':[('M,0,LS',2),('S,M,L',1),('0,MS,L',1)],
           '0,LS,M':[('M,LS,0',2),('S,L,M',1),('0,L,MS',1)],
           'S,L,M':[('S,LM,0',2),('0,LS,M',1),('0,L,MS',1)],
           'S,0,LM':[('0,0,LMS',1),('0,S,LM',1),('S,M,L',2)],
           'M,0,LS':[('M,S,L',1),('MS,0,L',1),('0,M,LS',2)],
           'M,LS,0':[('MS,L,0',1),('M,L,S',1),('0,LS,M',2)],
           'S,LM,0':[('0,LMS,0',1),('0,LM,S',1),('S,L,M',2)],
           '0,0,LMS':[('0,S,LM',1),('S,0,LM',1)],
           '0,S,LM':[('M,S,L',2),('0,0,LMS',1),('S,0,LM',1)],
           'M,S,L':[('0,S,LM',2),('MS,0,L',1),('M,0,LS',1)],
           'MS,0,L':[('M,S,L',1),('MS,L,0',3),('M,0,LS',1)],
           'MS,L,0':[('M,L,S',1),('MS,0,L',3),('M,LS,0',1)],
           'M,L,S':[('0,LM,S',2),('MS,L,0',1),('M,LS,0',1)],
           '0,LM,S':[('0,LMS,0',1),('M,L,S',2),('S,LM,0',1)],
           '0,LMS,0':[('0,LM,S',1),('S,LM,0',1)]}

#state heuristic costs for all nodes
heuristic={'LMS,0,0':40,
           'LM,0,S':35,
           'LM,S,0':41,
           'L,M,S':22,
           'L,S,M':33,
           'L,MS,0':4,
           'LS,M,0':12,
           'LS,0,M':24,
           'L,0,MS':21,
           '0,MS,L':9,
           '0,L,MS':15,
           'S,M,L':6,
           '0,M,LS':6,
           '0,LS,M':16,
           'S,L,M':13,
           'S,0,LM':7,
           'M,0,LS':6,
           'M,LS,0':19,
           'S,LM,0':18,
           '0,0,LMS':0,
           '0,S,LM':3,
           'M,S,L':7,
           'MS,0,L':5,
           'MS,L,0':9,
           'M,L,S':8,
           '0,LM,S':22,
           '0,LMS,0':14}

#compue f(x) for states to sort frontier
def f(x):
    return int(x[1])+int(x[2])

#creating a function for uniform cost algorithm 
def astar(start, goal, space,heuristic):
    
    #initialize variables
    explored = set()
    frontier = [(start,0,heuristic[start], [])]#add start to frontier with cost=0
    iteration=1
    
    #while frontier is not empty
    while frontier:
        #sort list
        frontier.sort(key=f,reverse=True)
        #print iteration's frontier and explored
        print('\niteration number: ',iteration)
        print(line,'frontier',line)
        print("%-10s%-10s"%("state","f(x)-g(x)-h(x)"))
        print("-----     --------------")
        for i in frontier:
            a='('+i[0]+')'
            print("%-10s"%(a),i[1]+i[2],'-',i[1],'-',i[2])
        print(line,'explored',line)
        if explored:
            print(explored,'\n\n')
        else:
            print('{}\n\n')
        
        #pop out the state with the least cost
        current,cost,_,path =frontier.pop()
        if current == goal:
            return path, cost #stop if current state is the goal
        
        if current not in explored: #explore current's neighbors and add it explored set if it is not there already
            explored.add(current)
            for item in space[current]: #get nighbors of the current state
                neighbor=item[0] #get neighbor
                neighborcost=item[1] #get neighbor cost
                newcost=cost + neighborcost #calculate new cumulative cost
                newpath=path + [(current, neighbor)] #path from start to neighbor
                #add to frontier the new neighbor with new cost and the path as a tuple
                flag=False
                if neighbor not in explored:#check if neighbor is not in explored
                    for index,(s,c,h,p) in enumerate(frontier):#compare
                        if s==neighbor:
                            flag=True
                            if c>newcost:#replacing tuple in case the new neibhor has less cost
                                del frontier[index]
                                frontier.append((neighbor,newcost,heuristic[neighbor],newpath))
                                break
                    if flag==False: #in not in frontier but also not in explored then append
                        frontier.append((neighbor,newcost,heuristic[neighbor],newpath))
               
                                
                                
                        
        iteration+=1
    #return none for pathand cost if the goal state is not found
    return None,None


#ask user for start and goal state
print(' '*33,'  hanoi tower puzzle')

start='LMS,0,0'
goal='0,0,LMS'
print()#skip line: for output design purposes
#call function
path,cost = astar(start, goal, space,heuristic)
#print depending on whether we got a solution or not
if path==None:
    print('\n\nsolution does not exist')
else:
    print('\n\nshortest path obtained:')
    for i in path:
        print(i[0],end='  >  ')
    print(i[1])
    print('\ncost:',cost)