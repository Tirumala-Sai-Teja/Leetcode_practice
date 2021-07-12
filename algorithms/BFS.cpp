/* for undirected graph if we want for directed graph we will just add that edge not both.
here we are calling dfs in a for loop because in competitive coding they will give two separated graphs as a single graph in such case we need for loop,
otherwise we dont need to call dfs in a separate for loop*/

#define MAXN 100005
bool visited[MAXN];
vector<int> adjList[MAXN];
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
  for(int i=1;i<=n;i++)
  {
    if(visited[i]==true)
        continue;
    else
        root=i;
    queue<int>Q;
    Q.push(root);
    visited[root]=true;
    while(!Q.empty())
    {
      int u=Q.front();
      Q.pop();
      for(int v: adjList[u])
      {
        if(visited[v]==false)
        {
          Q.push(v);
          visited[v]=true;
        }
      }
      cout<<u<<" ";
    }
  }
}
