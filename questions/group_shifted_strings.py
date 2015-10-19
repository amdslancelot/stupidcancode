"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.
"""

class Solution(object):
    '''
    1. Use Tuple to display the distance of each char to first char
    2. map(sorted, {})
    '''
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        r = {}
        for x in strings:
            t = tuple((ord(c)-ord(x[0]))%26 for c in x)
            if t in r:
                r[t].append(x)
            else:
                r[t] = [x]
        return map(sorted, r.values())

s = Solution()
r = s.groupStrings(["az","yx"])
print "ans:", r

'''
["fpbnsbrkbcyzdmmmoisaa"
"cpjtwqcdwbldwwrryuclcngw"
"a"
"fnuqwejouqzrif"
"js"
"qcpr"
"zghmdiaqmfelr"
"iedda"
"l"
"dgwlvcyubde"
"lpt"
"qzq"
"zkddvitlk"
"xbogegswmad"
"mkndeyrh"
"llofdjckor"
"lebzshcb"
"firomjjlidqpsdeqyn"
"dclpiqbypjpfafukqmjnjg"
"lbpabjpcmkyivbtgdwhzlxa"
"wmalmuanxvjtgmerohskwil"
"yxgkdlwtkekavapflheieb"
"oraxvssurmzybmnzhw"
"ohecvkfe"
"kknecibjnq"
"wuxnoibr"
"gkxpnpbfvjm"
"lwpphufxw"
"sbs"
"txb"
"ilbqahdzgij"
"i"
"zvuur"
"yfglchzpledkq"
"eqdf"
"nw"
"aiplrzejplumda"
"d"
"huoybvhibgqibbwwdzhqhslb"
"rbnzendwnoklpyyyauemm"]
'''
