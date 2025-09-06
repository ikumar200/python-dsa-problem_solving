# sumof didigts
n=8
# ----------------------------------------------------
# def sumD(n):
#     if n==0:
#         return 0

#     return n%10 +sumD(n//10)

# print(sumD(n))

# -----------------------------------------------------
# reverse digit
# s=str(n)
# print(id(s))
# s=s[::-1]
# print(id(s))
# print(int(s))

# -------------------------------------------------------
# prime testing
# def isPrime(n):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             return False
#             break
#     return True

# print(isPrime(n))

# --------------------------------------------------
# check power
# def isPower(x,y):
#     pow=x
#     if x==1:
#         return y==1
#     if y==1:
#         return 1
    
#     while pow<=y:
#         pow*=x
#         if pow==y:
#             return True
#     return False


# print(isPower(3,27))

# --------------------------------------------------
# factorial of n
# def factorial(n):
#     if n==1:
#         return 1
    
#     return n*factorial(n-1)
# print(factorial(4))

# ----------------------------------------------------
# LCM anf HCF
# def lcm_hcf(n,m):
#     # lcm
#     for i in range(min(n,m),m*n+1):
#         if i%n==0 and i%m==0:
#             print(i)
#             break
    
#     # hcf
#     x=1
#     for i in range(1,min(n,m)+1):
#         if m%i==0 and n%i==0:
#             x=i
#     print(x)

# lcm_hcf(2,3)