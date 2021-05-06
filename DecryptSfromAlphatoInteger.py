class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i',
                    '10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q',
                    '18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x',
                     '25':'y','26':'z'}      
        l=s.split('#')
        
        res=''
        s4=''
        for k,i in enumerate(l):
            c=len(i)
            s1=''
            s2=''
            s3=''
            if s[-1]=='#' or k!=len(l)-1:
                if c>2 :
                    s1=d[i[-2::1]]
                   
                    for j in range(c-2):
                        s2=s2+d[i[j]]
                    s3=s2+s1
                    
                if c==2:
                    s3=d[i]
                    
                
            else:
                for j in i:
                        s4=s4+d[j]
                    
                s3=s4 
            
            res=res+s3 
        return res
