class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        frequencies = {}
        used_frequencies = set()
        
        for char in s:
            if char not in frequencies:
                frequencies[char] = 0
            frequencies[char] += 1
		
        for freq in frequencies.values():
            temp_freq = freq
            while temp_freq in used_frequencies:
                deletions += 1
                temp_freq -= 1
                          
            if temp_freq != 0:
                used_frequencies.add(temp_freq)
        return(deletions)    
                
        
    
        