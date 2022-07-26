import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

#도시의 개수 N, 통로의 개수 M, 메세지를 보내고자 하는 도시 C 입력받기
n,m,c=map(int,input().split())
start=c

#그래프 초기화
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(1,m+1):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

#다익스트라
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        #현재 가장 작은 거리를 가진 노드
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=i[1]
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

result=0
time=0
for value in distance:
    if value!=INF:
        result+=1
        time=max(time,value)

print(result-1,time)
