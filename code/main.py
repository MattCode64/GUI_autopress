# from figaro.figaro import figaro
from lacroix.lacroix import lacroix
from liberation.liberation import liberation


def main():
    print("\033[93m" + "START" + "\033[0m")
    lacroix()
    liberation()
    # figaro()
    print("\033[93m" + "END" + "\033[0m")


if __name__ == '__main__':
    main()
