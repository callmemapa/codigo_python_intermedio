def run():
    # Fun
    my_list = [1,2,3,4,5]

    # squares = [i**2 for i in range(1, len(my_list)+1)]
    squares = list(map(lambda x: x**2, my_list))

    print(squares)


if __name__ == '__main__':
    run()