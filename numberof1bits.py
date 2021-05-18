class Solution {
public:
    int hammingWeight(uint32_t n) {
        string s = bitset<32>(n).to_string();
        int i = 0;
        for(int j = s.size()-1;j >= 0;j--)
        {
            if(s[j] - '0')
                i++;
        }
        return i;
    }
};
