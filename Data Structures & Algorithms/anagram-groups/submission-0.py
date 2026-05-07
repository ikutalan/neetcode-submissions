class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for s in strs: # N
            sortedS = ''.join(sorted(s)) # mlogm
            res[sortedS].append(s) # act -> act, cat, pots-> pots, tops, stop....
        return list(res.values())