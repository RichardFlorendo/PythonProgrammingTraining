class Solution:
    __privateCounter = 0

    def sum(self):
        self.__privateCounter += 1
        print(self.__privateCounter)


count = Solution()
count.sum()
count.sum()

print(count.__privateCounter)