from constants.const import (
    HEADER_MAIN,
    OPCAO_HEADER
)

def main():
    print(HEADER_MAIN)
    print(OPCAO_HEADER)

    while True:
        opcao = int(input())

        if opcao == 6:
            break


if __name__ == '__main__':
    main()
