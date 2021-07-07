/* for undirected graph*/

#define MAXN 100005
bool visited[MAXN];
vector<int> adjList[MAXN];
void dfs(int u){
  if(visited[u]==true)
    return;
  visited[u]=true;
  cout<<u<<" ";
  for(int v: adjList[u]){
    if(visited[v]==false)
      dfs(v);
  }
}
int main(){
  int n, m;
  cin>>n>>m;
  for(int i=0;i<m;i++)
  {
    int a,b;
    cin>>a>>b;
    adjList[a].push_back(b);
    adjList[b].pudh_back(a);
  }
  int root;
  for(int i=0;i,=n;i++)
    visited[i]=false;
  for(int i=1;i<=n;i++)
  {
    if(visited[i]=true)
      continue;
    else:
      root=i;
    dfs(i);
  }
}
