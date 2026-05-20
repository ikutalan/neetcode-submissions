class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - position) / speed = time
        # 时间大 = 花的时间多 = 慢
        # 时间小 = 花的时间少 = 快
        cars = sorted(zip(position, speed))
        fleet = 0
        curr_max = 0
        for pos, spd in reversed(cars):
            time = (target - pos) / spd
            if time > curr_max: # merge
                fleet += 1
                curr_max = time
        return fleet
