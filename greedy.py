
import heapq
<<<<<<< HEAD

def Greedy(map, start, goal):
    visited = set()
    parent = {}
    gn {start : 0}

    pq = []

    heapq.heappush(pq, (gn[start], start))
=======
def greedy(map, start, goal):
    visited = set() #mark visited city
    parent = {}     #mark the source to reach a city
    gn = {start:0}

    pq = [] #list pq

    heapq.heappush(pq ,(gn[start], start)) #get to priorityqueue
    cnt = 1 #initialitation for order of step
    while pq:
        current = heapq.heappop(pq)[1] #psuh city to priorityqueue
        print()
        print(">>>>>STEP {}<<<<<<<".format(cnt))
        cnt+=1
        print("Now at {}".format(current)) #print current city

        if current == goal:
            print("Reach Location")
            print()
            path = [] #save the right path
            while current in parent:
                path.append(current) #push current to path
                current = parent[current]
            return path[::-1]   #reserved

        visited.add(current) #mark current city as visited
        for c_name in map[current]: #iterate to all neighbor
            if c_name in visited:   #city had been visited before
                continue

            gn_temp = map[current][c_name]
            print('now cek at {:5}\tg(n) = {} Kilo\t'.format(c_name, gn_temp))
            if c_name in gn and gn_temp < gn[c_name] or c_name not in gn:
                if c_name not in gn:
                    heapq.heappush(pq, (gn_temp, c_name)) #when push ti priorytyque
					print('Masukkan {} Ke Priorty Queue'.format(c_name))
				parent[c_name] = current #set source to reach city
				gn[c_name] = gn_temp		#update or set g(n)

	return None
>>>>>>> cabf92b6303eb00fcbad1c88a1368b45eb06a7a4
