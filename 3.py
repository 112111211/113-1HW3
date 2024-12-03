def josephus_iterative(n, k):
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result + 1

# 測試
n = 5  # 朋友數量
k = 2  # 數到第 k 個人

result = josephus_iterative(n, k)
print(f"最後剩下的人的編號是: {result}")
