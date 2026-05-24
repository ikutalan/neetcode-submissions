class TimeMap:

    def __init__(self):
        self.stores = defaultdict(list)
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stores[key].append((timestamp,value))
        #{key:[(1, happy), (3, sad)]}
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stores:
            return ""

        values = self.stores[key]
        l = 0
        r = len(values)
        while l < r:
            mid = (l+r) // 2
            if timestamp < values[mid][0]:
                r = mid
            else:
                l = mid + 1
        if l == 0:
            return ""
        return values[l - 1][1]