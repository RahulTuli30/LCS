import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) in [0,1]:
            return s
        x = self.modify(s)
        #print("Modified String : {}".format(x))
        P = self.get_ps_lengths(x)

        # for c, l in zip(x, P):
            #print("character : {} Length of Palindromic Substring with this "
             #     "center : {}".format(c, l))

        center = np.argmax(P)
        l = P[center]

        return s[(center - l)//2 : (center + l) //2]

    def modify(self, s):
        unk_character = '#'

        new = []

        for i, c in enumerate(s):
            if i == 0:
                new.append(unk_character)

            new.append(c)
            new.append(unk_character)

        return ''.join(new)

    def get_ps_lengths(self, s):
        P = [0] * len(s)
        c, r = 0, 0
        #print("Recieved String : {}".format(s))

        for i in range(1, len(s)):
            mirror_location = 2 * c - i

            if i < r:
                P[i] = min(r - i, P[mirror_location])

            while i - (1 + P[i]) >= 0 and i + (1 + P[i]) < len(s) \
                    and s[i + (1 + P[i])] == s[i - (1 + P[i])]:
                P[i] += 1

            if i + P[i] > r:
                c = i
                r = i + P[i]

        return P
