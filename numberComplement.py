class Solution {
public:
    int findComplement(int n) {
        int i,j,a=0,d;
        long int b=1;
        while(n>0)
        {
            if(n%2==0)
                    d=1;
            else
                d=0;
            a=a+d*b;
            b=b*2;
            n=n/2;
            
        }
        return a;
        }
        
};
