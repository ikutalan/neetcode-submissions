class Twitter:

    def __init__(self):
        self.timer = 0
        self.user_tweets = defaultdict(list)
        self.user_followee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followee[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most recent  
        max_heap = []
        res = []
        users = self.user_followee[userId] | {userId} # followee + self
        # seed
        for user in users: #关注的人
            if self.user_tweets[user]:
                idx = len(self.user_tweets[user]) - 1
                ts,tid = self.user_tweets[user][idx]
                heapq.heappush(max_heap, (-ts,tid,user, idx))
        while max_heap and len(res) < 10:
            neg_ts, tid, user, idx = heapq.heappop(max_heap)
            res.append(tid)
            if idx > 0:
                ts, tid = self.user_tweets[user][idx-1]
                heapq.heappush(max_heap, (-ts, tid, user, idx-1))
        return res