from study_tools.calculations import mean, clamp
from study_tools.formatting import format_result


def main():
    result = mean(10, 20, 30)
    print(format_result(result))


if __name__ == "__main__":
    main()