import hashlib

def mine_adventcoin(secret_key, leading_zeroes):
    n = 1
    target_prefix = '0' * leading_zeroes
    while True:
        input_str = secret_key + str(n)
        hash_result = hashlib.md5(input_str.encode()).hexdigest()
        if hash_result[:leading_zeroes] == target_prefix:
            return n
        n += 1

secret_key = "ckczppom"

result_5_zeroes = mine_adventcoin(secret_key, 5)
result_6_zeroes = mine_adventcoin(secret_key, 6)

print("The lowest number with 5 leading zeroes is:", result_5_zeroes)
print("The lowest number with 6 leading zeroes is:", result_6_zeroes)

