def main():
    while True:
        data = input()
        if 'exit' == data:
            break

        soma = 0
        flag = False
        num = ''
        for i in range(len(data)):
            if data[i:i + 3] == 'off':
                flag = False

            elif data[i:i + 2] == 'on':
                flag = True

            elif data[i] == '=':
                if num:
                    soma += int(num)
                print(soma)
                soma = 0
                num = ''

            elif flag:
                if data[i].isdigit():
                    num += data[i]
                else:
                    if num:
                        soma += int(num)
                    num = ''

        if num:                            
            soma += int(num)


if __name__ == "__main__":
    main()