def check_str(check_str):
    prev_parity = int(check_str[0]) % 2
    for i in range(1, len(check_str)):
        current_parity = int(check_str[i]) % 2
        if prev_parity == current_parity:
            return False
        prev_parity = current_parity
    return True

def longest_substring(input_str):
    longest_str = input_str[0]
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)):
            if check_str(input_str[i:j+1]) == True and len(longest_str) < len(input_str[i:j+1]):
                longest_str = input_str[i:j+1]
    return longest_str                

def main():
    print("main function")
    input_str = "225424272163254474441338664823"
    print(longest_substring("225424272163254474441338664823"))

if __name__ == "__main__":
    main()
