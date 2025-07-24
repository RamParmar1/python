class Solution:
  def maxScoreSightseeingPair(self, values) :
    ans = 0
    bestPrv = 0

    for value in values:
      ans = max(ans, value + bestPrv)
      bestPrv = max(bestPrv, value) - 1

    return ans
