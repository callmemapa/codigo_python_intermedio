def run():
    palindrome = lambda string: string == string[::1]

    print(palindrome('reconocer'))


if __name__ == '__main__':
    run()