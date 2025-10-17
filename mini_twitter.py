    # Rules:
    # Each tweet has a unique TweetID and a timestamp
    # A user's news feed should be sorted by most recent first
    # A user’s news feed should show up to 10 most recent tweets from themselves + all users they follow.
    # Each user can follow/unfollow others, but cannot unfollow themselves.

from collections import defaultdict
import heapq

class MiniTwitter:

    def __init__(self):
        self.userFollow = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.userTweets[userId].append((-self.counter, tweetId))


    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        min_heap = []

        users = {userId} | self.userFollow[userId]

        for uid in users:
            for tweet in self.userTweets[uid][-10:]:
                heapq.heappush(min_heap, tweet)
            
            for _ in range(min(10, len(min_heap))):
                time, tweetId = heapq.heappop(min_heap)
                feed.append(tweetId)

        return feed[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.userFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollow[followerId]:
            self.userFollow[followerId].remove(followeeId)

twitter = MiniTwitter()
twitter.postTweet(1, 101)
twitter.postTweet(1, 102)
twitter.postTweet(2, 201)

twitter.follow(1, 2)
print(twitter.getNewsFeed(1))

twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
