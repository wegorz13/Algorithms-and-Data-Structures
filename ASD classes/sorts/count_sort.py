def count_sort(T):
  n = len(T)
  count = [0] * (n + 1)
  output = [(0,0)] * n

  for i in range(n):
    count[T[i][0]] += 1

  for i in range(1, n+1):
    count[i] += count[i - 1]

  for i in range(n-1,-1,-1):
    output[count[T[i][0]] - 1] = T[i]
    count[T[i][0]] -= 1

  return output
