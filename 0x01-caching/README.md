# 0x01. Caching
### backend || python
A caching system is like a temporary storage space that keeps copies of frequently accessed data. It stores this data in a way that makes it quicker to retrieve when needed again.

FIFO (First In, First Out) means that the first data stored in the cache will be the first to be removed when the cache is full. It works like a queue; the oldest data goes out first.

LIFO (Last In, First Out) means that the most recently added data will be the first to be removed from the cache. It's like a stack; the last item added is the first to go out.

LRU (Least Recently Used) means that the data that hasn't been accessed for the longest time will be the first to be removed. It prioritizes keeping the most recently used data.

MRU (Most Recently Used) means that the data accessed most recently will be the last to be removed. It prioritizes keeping the most recently used data.

LFU (Least Frequently Used) means that the data that has been accessed the least number of times will be the first to be removed. It prioritizes keeping the least used data.

The purpose of a caching system is to speed up access to data by storing copies of frequently accessed data closer to where it's needed. This reduces the time needed to fetch the data from its original source, like a database or a server.

However, caching systems have limits. They can only store a certain amount of data, and if the cache is full, it needs to decide which data to remove to make space for new data. Also, if the data in the cache becomes outdated or irrelevant, it might not reflect the most current information.