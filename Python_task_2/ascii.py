def generate_ascii_hash(char1, char2, char3):
    ascii1 = ord(char1)
    ascii2 = ord(char2)
    ascii3 = ord(char3)

    return ascii1 * ascii2 * ascii3


def check_strength_level(hash_value):
    if hash_value >= 500000:
        return "Strong"
    else:
        return "Weak"


def main():
    char1 = input("Enter character 1: ")
    char2 = input("Enter character 2: ")
    char3 = input("Enter character 3: ")

    hash_value = generate_ascii_hash(char1, char2, char3)
    strength = check_strength_level(hash_value)

    print("\n--- Security Readout ---")
    print("Characters:", char1, char2, char3)
    print("ASCII values:", ord(char1), ord(char2), ord(char3))
    print("Hash value:", hash_value)
    print("Hash strength:", strength)


if __name__ == "__main__":
    main()
