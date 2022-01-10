from typing import List


def unique_candidates(c: List[int], t: int):

    rv = []
    size = len(c)

    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            rv.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, size):
            # add the number into the combination
            comb.append(c[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - c[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(t, [], 0)

    return rv

def combinationSum2(c, t):
    result = []
    size = len(c)
    
    def dfs(l, start):
        if sum(l) == t:
            result.append(l[:])
            return
        
        if sum(l) > t:
            return
        
        for i in range(start, size):
            l.append(c[i])
            dfs(l, i)
            l.pop()

    dfs([], 0)
    return result

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    subsets = []
    candidates.sort()
    for idx, candidate in enumerate(candidates):
        left = target - candidate
        if left == 0:
            subsets.append([candidate])
        elif left > 0:
            for subset in self.combinationSum(candidates[idx:], left):
                subsets.append([candidate] + subset)
        else:
            break
    
    return subsets

print(combinationSum([2,3,6,7], 7))

print(combinationSum([2,3,5], 8))

print(combinationSum([2], 1))