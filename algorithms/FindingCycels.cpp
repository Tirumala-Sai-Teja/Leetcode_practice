/*Finding cycles in undirected graph in a function*/
bool isCycle(int node,int parent){
  if(visited[node]==true)
    return true;
  visited[node]=true;
  bool flag=false;
  for(int v: adjList[u]{
    if(v==parent)
      continue;
    flag=flag||isCycle(v,u);
  }
      return flag;
      }
