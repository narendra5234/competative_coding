[Math For Coding](https://www.geeksforgeeks.org/math-in-competitive-programming/)
1. **Big Integer**: Avoid Big Integer Limitation: for numbers greater than long long int by storing large number using module 10(%10) in list / vectors.

    **Eg**: [factorial of a large number.](https://www.geeksforgeeks.org/factorial-large-number/)

2. **GCD**: GCD of two numbers is the largest number that divides both of them. A simple way to find GCD is to factorize both numbers and multiply common factors.

    **Euclidean Algo**

    ~~~
   def gcd(a, b): 
    if a == 0 :
        return b
    return gcd(b%a, a)
   ~~~
   **Extended Euclidean Algo**:

   ax + by = gcd(a, b)

   ~~~
   def gcdExtended(a, b):  
    if a == 0 :   
        return b, 0, 1
             
    gcd, x1, y1 = gcdExtended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1 
    return gcd, x, y 
   ~~~
   ***NOTE***:  a%b=a-(a//b)*b


3. **LCM**:
    lcm(a, b) = a * b / gcd(a, b)
4. [**Prime Numbers**](https://www.geeksforgeeks.org/prime-numbers/):
Primes are numbers that can only be divided by themselves and 1.

    **Note**:
   1. [Wilson’s Theorem:](https://www.geeksforgeeks.org/wilsons-theorem/)
     prime iff (p-1)!%p==(p-1)
   2. [Fermats Little Therorem:](https://en.wikipedia.org/wiki/Fermat's_little_theorem)
        prime iff (a^p)%p== p.
   3. Prime number therorem...

   ***All primes less than N***:

   1.Naive Method:
   ~~~
    def get_primes(n: int):
        if n == 1:
            return
        primes = []
        for num in range(2, n+1):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        return primes
   ~~~

   2.Sieve of Eratosthenes and Segmented Sieve

   [Sieve of Eratosthenes]((https://www.geeksforgeeks.org/sieve-of-eratosthenes/)):
   ~~~
       def sieve_of_eratosthenes(n):
        number_wise_is_prime_dict = {num: True for num in range(2, n + 1)}
        num = 2
        while num * num <= n:
            if number_wise_is_prime_dict[num]:
                for i in range(num * num, n + 1, num):
                    number_wise_is_prime_dict[i] = False
            num += 1

        return list(map(lambda x: x[0], filter(lambda x: x[1], number_wise_is_prime_dict.items())))
   ~~~
    time: O(N*Log(LogN))
    NOTE: when N is large it is inefficient, use segmented seive

   [Segmented Sieve](https://www.geeksforgeeks.org/segmented-sieve/):

5. **Modular Arithmetic**:
       a%b gives remainder when a is divided by b(remainder when a//b.)
       Use Modular properties to avoid overflow.

      Fast Modulo Exponentiation:
      ~~~
      ll expo(ll a, ll b, ll m) 
        { 
            if (b == 0) 
                return 1; 
            ll p = expo(a, b / 2, m) % m; 
            p = (p * p) % m; 
          
            return (b % 2 == 0) ? p : (a * p) % m; 
        }   
      ~~~

      [Inverse Modulo](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/):

      ~~~
         def modInverse(a, m) : 
            a = a % m; 
            for x in range(1, m) : 
                if ((a * x) % m == 1) : 
                    return x 
            return 1
      ~~~

6. Chinese Remainder Theorem and etc..

7. Series and Sequences:
    site: <https://oeis.org/A001597>
8. Catalan Numbers:
    site: <https://www.geeksforgeeks.org/program-nth-catalan-number/>
9. Combinations and Permutations.












