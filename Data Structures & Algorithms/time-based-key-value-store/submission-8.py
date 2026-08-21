class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, [""] * (timestamp-1))
        length = len(self.timeMap[key])
        if length < timestamp:
            for i in range(timestamp - length-1):
                self.timeMap[key].append(self.timeMap[key][length-1])
        self.timeMap[key].append(value)


    def get(self, key: str, timestamp: int) -> str:
        
        
        
        if not key in self.timeMap:
            return ""
        elif timestamp == 0:
            return self.timeMap[key][timestamp]
        length = len(self.timeMap[key])
        if length < timestamp:
            for i in range(timestamp - length):
                self.timeMap[key].append(self.timeMap[key][length-1])
        return self.timeMap[key][timestamp-1]
        

        
