def findDivisors(num, divisor=1, divisors=None):
    if divisors is None:
        divisors = set()

    if divisor * divisor > num:
        return sorted(divisors)

    if num % divisor == 0:
        divisors.add(divisor)
        divisors.add(num // divisor)

    return findDivisors(num, divisor + 1, divisors)

num = 15
divisors = findDivisors(num)
print("Divisors of", num, "are:", divisors)