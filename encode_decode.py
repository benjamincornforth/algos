from typing import List, Dict, Optional

class Solution:
    def encode(self, strs: List[str]) -> str:
        
        return ''.join([f'{len(s)}#{s}' for s in strs])

    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        n=len(s)
        while i<n:
            if s[i]=='#':
                step_size=int(s[i-1])
                print(f'at position:{i+1}, skip:{step_size},for str:{s[i+1:i+1+step_size]}')
                output.append(s[i+1:i+1+step_size])
                i+=step_size
            i+=1

        return output

s=Solution()
en_res=s.encode([''])
print(f'encoded:{en_res}')
de_res=s.decode(en_res)
print(f'decoded:{de_res}')

en_res=s.encode(["neet","code","love","you"])
print(f'encoded:{en_res}')
de_res=s.decode(en_res)
print(f'decoded:{de_res}')

#dec_res=s.decode(en_res)
#print(f'decoded:{dec_res}')

