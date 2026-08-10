class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chunks = []
        l = 0
        for space in spaces:
            chunks.append(s[l:space])
            l = space
        chunks.append(s[l:])
        return " ".join(chunks)