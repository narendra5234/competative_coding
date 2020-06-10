class Prime:
    @staticmethod
    def check_primes(num: int):
        if num == 1:
            return False
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        return is_prime

    @staticmethod
    def get_primes_1(n: int):
        if n == 1:
            return
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime is True:
                primes.append(num)
        return primes

    # using for-else
    @staticmethod
    def get_primes_2(n: int):
        if n == 1:
            return
        primes = []
        for num in range(2, n + 1):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)

        return primes

    # Sieve Of Eratosthenes
    @staticmethod
    def get_primes_3(n):
        number_wise_is_prime_dict = {num: True for num in range(2, n + 1)}
        num = 2
        while num * num <= n:
            if number_wise_is_prime_dict[num]:
                for i in range(num * num, n + 1, num):
                    number_wise_is_prime_dict[i] = False
            num += 1

        return list(map(lambda x: x[0], filter(lambda x: x[1], number_wise_is_prime_dict.items())))


# print(Prime().check_primes(2))
# print(Prime().get_primes_1(13))
print(Prime().get_primes_2(13))
# print(Prime().get_primes_3(13))
