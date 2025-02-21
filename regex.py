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

"""

"""

def main():
    print("main")
    print(re.ASCII)
    print(re.DOTALL)

    re.compile("ab*")

    p = re.compile('[a-z]+')
    print(p)

    m = p.match('tempo')
    print(m.group())
    print(m.start())
    print(m.end())

    print(m.span())

    print(re.findall(r"\d+", "12312 1231231 abcdfwfwe aa 12312"))
    print(re.finditer(r"\d+", "12312 1231231 abcdfwfwe aa 12312"))

    p = re.compile('(a(b)c)d')
    m = p.match('abcd')
    print(m.group(2))

    p = re.compile(r'\b(\w+)\s+\1\b')
    print(p.search('Paris in the the spring').group())

    m = re.match("([abc])+", "abc")
    print(m.groups())

    m = re.match("(?:[abc])+", "abc")
    print(m.groups())

    p = re.compile(r'(?P<word>\b\w+\b)')
    m = p.search( '(((( Lots of punctuation )))' )
    print(m.group('word'))

    m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
    print(m.groupdict())

if __name__ == "__main__":
    main()
