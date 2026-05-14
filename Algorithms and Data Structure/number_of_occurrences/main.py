class Solution(object):

    def areOccurrencesEqual(self, s):

        freq = {}

        for char in s:

            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
                
        values = list(freq.values())
        
        first = values[0]

        for count in values:
            if count != first:
                return False

        return True


test = Solution()

print(test.areOccurrencesEqual("tete"))