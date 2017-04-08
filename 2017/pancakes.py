
if __name__ == "__main__":
  # read input
  t = int(raw_input())
  for i in xrange(1, t + 1):
    pancakes, flipper = raw_input().split(" ")
    flipper = int(flipper)
    print "Case #{}: {} {}".format(i, pancakes, flipper)
