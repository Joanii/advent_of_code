def get_numbers_from_lines():
    calibration_value = 0
    for line in lines:
        line.strip()
        digits = []
        for character in line:
            if character.isdigit():
                digits.append(character)
        number = int(f'{digits[0]}{digits[-1]}')
        print(number)
        calibration_value += number
    print(calibration_value)


def get_written_and_numerical_digits_from_lines(lines):
    calibration_value = 0
    unique_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in lines:
        line = line.strip()
        written_digits = [digit for digit in unique_digits if digit in line]
        indexes = [line.index(digit) for digit in written_digits]
        digits = []
        for digit in written_digits:
            index = [i for i in range(len(line)) if line.startswith(digit, i)]
            for _ in range(len(index)):
                digits.append(unique_digits.index(digit) + 1)
        for idx, character in enumerate(line):
            if character.isdigit():
                digits.append(int(character))
                indexes.append(idx)
        indexes, digits = zip(*sorted(zip(indexes, digits)))
        number = int(f'{digits[0]}{digits[-1]}')
        calibration_value += number
    print(calibration_value)


if __name__ == '__main__':
    with open('day01_input.txt') as f:
        lines = f.readlines()
    # Task 1
    get_numbers_from_lines(lines)
    # Task 2
    get_written_and_numerical_digits_from_lines(lines)
