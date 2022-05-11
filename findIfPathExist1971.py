from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        edge=defaultdict(list)
        for a,b in edges:
            edge[a].append(b)
            edge[b].append(a)
            
        visited,stack=set(),[source]
        
        while(stack):
            val=stack.pop()
            for i in edge[val]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)
                    if i==destination:
                        return True
        return False
      
      
      
# from collections import defaultdict
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         edge=defaultdict(list)
#         for i in edges:
#             a,b=i
#             if(edge.get(a,-1)==-1):
#                 edge[a]=[b]
#             else:
#                 edge[a].append(b)
#             if(edge.get(b,-1)==-1):
#                 edge[b]=[a]
#             else:
#                 edge[b].append(a)
        
#         visited=[False]*n      
#         dfs_ar=[] 
#         self.dfs(source,edge,visited,dfs_ar)
#         return visited[destination]
                

#     def dfs(self,src,edge,visited,dfs_ar):
#         if(visited[src]==True):
#             return
#         visited[src]=True
#         dfs_ar.append(src)
#         for i in edge[src]:
#             if visited[i]==False:
#                 self.dfs(i,edge,visited,dfs_ar)
