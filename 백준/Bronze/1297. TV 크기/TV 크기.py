# 1297
D, H, W = map(int, input().split())
r = D/(H**2 + W**2)**0.5
a = H*r
b = W*r
print(int(a),int(b))