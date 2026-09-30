def isHappy(n):
    seen = set()

    while n not in seen and n != 1:
        seen.add(n)

        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10

        n = total

    if n == 1:
        return True

    return False

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")