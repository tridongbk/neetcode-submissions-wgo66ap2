class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. impossible case
        if len(s1) > len(s2):
            return False

        # 2. build two count arrays
        s1Count = [0] * 26
        s2Count = [0] * 26

        # 3. fill first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # 4. compare first windowpp
        if s1Count == s2Count:
            return True

        # 5. slide window across s2
        for i in range(len(s1), len(s2)):
            # add new char
            s2Count[ord(s2[i]) - ord('a')] += 1

            # remove old char
            s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # compare
            if s1Count == s2Count:
                return True

        return False