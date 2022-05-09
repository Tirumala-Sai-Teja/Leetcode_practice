from collections import deque
class graph:
    def __init__(self,n):
        # self.adj=dict[list]
        self.visited:list[bool]
        self.adj={}
        self.visited=[False]*n
    def addEdge(self,a,b):
        if(self.adj.get(a,-1)!=-1):
            self.adj[a].append(b)
        else:
            self.adj[a]=[b]
      
    def dfs(self,node):
        if(self.visited[node]==True):
            return
        self.visited[node]=True
        print(node,end=" ")
        for i in self.adj[node]:
            if(self.visited[i]==False):
                self.dfs(i)
    def bfs(self,node):
        if(self.visited[node]==True):
            return
        q=deque([node])
        while(q):
            for i in self.adj[node]:
                 if(self.visited[i]==False):
                    self.visited[i]=True 
                    q.append(i)
            print(q.popleft(),end=" ")
                 
g=graph(5)
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    g.addEdge(a,b);
    g.addEdge(b,a);
# for i in range(5):
#     if(g.visited[i]==False):
#         g.dfs(i)
for i in range(5):
    if(g.visited[i]==False):
        g.bfs(i)
        
        
output:
  5
  0 1
  0 2
  0 3
  1 2
  2 4
  
  dfs:0 1 2 4 3
  bfs:0 1 2 3 4
