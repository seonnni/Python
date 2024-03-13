N = int(input())
for i in range(N*2):
    if N == 1:
        print("*")
        break
    else:
        if N % 2 != 0:
            if i % 2 == 0:
                print("* "*int((N+1)/2))
            else:
                print(" *"*int(N/2))
        else:
            if i % 2 == 0:
                print("* "*int(N/2))
            else:
                print(" *"*int(N/2))