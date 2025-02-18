def palindrome_check(chk_str):
    return chk_str == chk_str[::-1]

def main():
    chk_str = input()
    print(palindrome_check(chk_str))

if __name__ == "__main__":
    main()
