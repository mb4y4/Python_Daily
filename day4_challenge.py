#prime numbers

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(start, end):
    prime_numbers = []
    for num in range(max(start, 2), end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def main():
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    
    prime_numbers = generate_primes(start, end)
    
    print(f"Prime numbers between {start} and {end}:")
    for prime in prime_numbers:
        print(prime)

if __name__ == "__main__":
    main()
