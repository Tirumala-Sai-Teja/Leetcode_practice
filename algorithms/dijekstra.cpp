
/*from this we get minimum distance from the given source vertex to remaining all other nodes*/
#include <iostream>
using namespace std;
#define PII pair<int , int>

int main() {
    int n,m;
    cin>>n>>m;
    vector<PII>adjList[n+1];
    for(int i = 0 ; i<m ; i++){
        int a, b , w;
        cin>>a>>b>>w;
        adjList[a].push_back(make_pair(b,w));
        adjList[b].push_back(make_pair(a,w));
    }
    
    /* dist[i] stores the minimum distance from source to i after completion of algorithm */
    int dist[n+1];
    for(int i = 0 ; i<=n ; i++)     
        dist[i] = INT_MAX;
        
        
    priority_queue<PII , vector<PII> , greater<PII>> PQ;
    
    int source = 1;
    dist[source] = 0;
    PQ.push(make_pair(dist[source] , source))
    
    while(!PQ.empty()){
        
        PII P = PQ.top();
        PQ.pop();
        int node = P.second , weight = P.first;
        
        for(PII Q : adjList[node]){
            int nextNode = Q.second , edgeWeight = Q.first;
            
            if(weight+edgeWeight < dist[nextNode]){
                dist[nextNode] = weight+edgeWeight;
                PQ.push(make_pair(dist[nextNode] ,nextNode));
            }
        }
    }
    
}
