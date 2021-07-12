#include<bits/stdc++.h>
using namespace std;
vector<pair<int,int>>adj[1000001];
int main(){
    int n;
    cin>>n;
    unordered_map<int,int>mp;
    for(int i=0;i<n;++i){
        int x;
        cin>>x;
        mp[x]=INT_MAX;
    }
    int e;
    cin>>e;
    for(int i=0;i<e;++i)
    {
        int x,y,d;
        cin>>x>>y>>d;
        adj[x].push_back({y,d});
    }
    int src,dest;
    cin>>src>>dest;
    set<pair<int,int>>s;
    mp[src]=0;
    s.insert({0,src});
    while(!s.empty())
    {
        pair<int,int>tmp=*(s.begin());
        s.erase(s.begin());
        int u=tmp.second;
        for(auto i=adj[u].begin();i!=adj[u].end();++i){
            int v=(*i).first;
            int weight=(*i).second;
            if(mp[v]>mp[u]+weight){
                if(mp[v]!=INT_MAX)
                s.erase(s.find({mp[v],v}));
                mp[v]=mp[u]+weight;
                s.insert({mp[v],v});
            }
        }
    }
    if(mp[dest])
    cout<<mp[dest]<<endl;
    return 0;
}
// second method but there are some changes to do


#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,input,m,u,v,cost,start,end;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>input;
    }
    cin>>m;
    unordered_map<int,vector<pair<int,int>>>graph;
    for(int i=0;i<m;i++)
    {
        cin>>u>>v>>cost;
        graph[u].push_back({v,cost});
    }
    cin>>start;
    cin>>end;
    queue<pair<int,int>>q;
    q.push({start,0});
    pair<int,int>p;
    int result=9999;
    while(!q.empty())
    {
        p=q.front();
        q.pop();
        int node=p.first;
        int cost=p.second;
        //cout<<cost;
        if(node==end)
        {
            result=min(result,cost);
        }
        for(auto x:graph[node])
        {
            q.push({x.first,x.second+cost});
        }
    }
    cout<<result;
    return 0;
}
