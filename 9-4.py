INF=int(1e9)

#전체 회사의 개수 N과 경로의 개수 M 입력받기
n,m=map(int,input().split())

#2차원 그래프 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#연결된 경로 입력받기
for i in range(1,m+1):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#목적지 번호 입력받기
x,k=map(int,input().split())

#자기 자신에게 가는 경로는 0으로 처리
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
            graph[j][i]=0

#플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=graph[1][k]+graph[k][x]

if result>=INF:
    print('-1')
else:
    print(result)
