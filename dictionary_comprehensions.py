def run():
    # dict_list = {i: i**3 for i in range(1,101) if i % 3 != 0}
    dict_list = {i: i**(1/2) for i in range(1,1001)}
    print(dict_list)


if __name__ == '__main__':
    run()