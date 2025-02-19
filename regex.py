import re

# Meta characters
# . ^ $ * + ? { } [ ] \ | ( )


"""

\d
Matches any decimal digit; this is equivalent to the class [0-9].

\D
Matches any non-digit character; this is equivalent to the class [^0-9].

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

"""

def main():
    print("main")
    print(re.ASCII)

if __name__ == "__main__":
    main()
