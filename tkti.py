import argparse
from math import isqrt
from typing import List

def print_intro() -> None:
    print("Hello, world!")
    print("Ini untuk issue tkti-17 revisi")
    print("tes worklflow ketiga")


def generate_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for number in range(2, isqrt(limit) + 1):
        if sieve[number]:
            step = number
            start = number * number
            sieve[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and summarize prime numbers.")
    parser.add_argument(
        "limit",
        type=int,
        nargs="?",
        default=100,
        help="Upper bound (inclusive) when searching for prime numbers.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress the introductory messages.",
    )
    args = parser.parse_args()

    if not args.quiet:
        print_intro()

    primes = generate_primes(args.limit)
    if not primes:
        print(f"Tidak ada bilangan prima ditemukan hingga {args.limit}.")
        return

    print(f"Ditemukan {len(primes)} bilangan prima hingga {args.limit}.")
    print(f"Bilangan prima terbesar: {primes[-1]}")
    print(f"Jumlah total bilangan prima: {sum(primes)}")


if __name__ == "__main__":
    main()
