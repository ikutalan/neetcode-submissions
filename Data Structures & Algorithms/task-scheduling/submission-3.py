class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        all_tasks = [-c for c in Counter(tasks).values()]
        heapq.heapify(all_tasks) # max heap based on the task count
        queue = deque() # (剩余次数，可用时间)tasks in the first avaiable time order
        time = 0 # curr time

        while all_tasks or queue: #说明还有没有处理完的requst
            time += 1
            if all_tasks:
                cnt = heapq.heappop(all_tasks) + 1
                if cnt != 0:
                    queue.append((cnt, time + n)) # put it into CD
            if queue and queue[0][1] == time:
                heapq.heappush(all_tasks, queue.popleft()[0])
        return time