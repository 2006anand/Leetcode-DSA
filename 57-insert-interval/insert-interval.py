class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for start, end in intervals:
            if end < newInterval[0]:
                result.append([start, end])
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        result.append(newInterval)
        return result