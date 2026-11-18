
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            lineLength = 0

            # Step 1: Greedily select words
            while j < n and lineLength + len(words[j]) + (j - i) <= maxWidth:
                lineLength += len(words[j])
                j += 1

            numWords = j - i
            totalSpaces = maxWidth - lineLength

            # Step 2: Last line or single word
            if j == n or numWords == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                # Step 3: Distribute spaces evenly
                gaps = numWords - 1
                spaces = totalSpaces // gaps
                extra = totalSpaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces + (1 if k - i < extra else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result
