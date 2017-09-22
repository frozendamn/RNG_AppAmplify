# !/bin/python3


class BlankValue(Exception):
    pass


class MultipleValues(Exception):
    pass


class InvalidNumber(Exception):
    pass


class GenerateRandomNumber:
    global_var = dict()  # temporarily holding all input values to improve performance

    def __init__(self, num_given):

        if num_given in self.global_var.keys():
            pass
        else:  # initializing required attributes
            self.high = self.gen_list(num_given, "high")
            self.low = self.gen_list(num_given, "low")
            self.high_out = 0
            self.low_out = 0
            self.global_var[num_given] = {'high': self.high, 'low': self.low,
                                          'high_out': self.high_out, 'low_out': self.low_out}

    def custom_rand(self, num_given, list_type):  # gets a random element from a list of integers
        if not self.global_var[num_given][list_type]:
            self.global_var[num_given][list_type] = self.gen_list(num_given, list_type)
        else:
            pass
        list_len = len(self.global_var[num_given][list_type])
        index = id(num_given) + id(list_len)
        index = abs(list_len - (index % list_len)) - 1
        return self.global_var[num_given][list_type].pop(index)

    def gen_list(self, num_given, list_type):
        mid = num_given // 2  # generating two distinct list with high and low values
        if list_type == "high":
            result = [i for i in range(mid + 1, num_given + 1)]
        else:
            result = [i for i in range(1, mid + 1)]

        return result

    def get_number(self, num_given):
        h = self.global_var[num_given]["high_out"]
        l = self.global_var[num_given]["low_out"]
        if h == 0:
            self.global_var[num_given]["high_out"] += 1
            list_type = "high"
        elif l == 0:
            self.global_var[num_given]["low_out"] += 1
            list_type = "low"
        else:
            a = (h + 1) / (h + l + 1)
            b = h / (h + l + 1)  # biasing the output in order to have 73% high numbers

            p1 = abs(0.73 - a)
            p2 = abs(0.73 - b)

            if p1 > p2:
                self.global_var[num_given]["low_out"] += 1
                list_type = "low"
            else:
                self.global_var[num_given]["high_out"] += 1
                list_type = "high"

        result = self.custom_rand(num_given, list_type)
        return result


if __name__ == "__main__":

    flag = True

    while flag:
        try:
            number = input("Please provide a single integer in range 2 to 1000000\n").strip().split()
            if number:
                pass
            else:
                raise BlankValue("Blank Value is provided")

            if len(number) > 1:
                raise MultipleValues("Multiple Values is provided")

            elif number[0].isdigit():
                number = int(number[0])
                if number > 1:
                    obj = GenerateRandomNumber(number)
                    random_number = obj.get_number(number)
                    print("Your number is {0}\n".format(random_number))
                    exit_code = input("Would you like to continue ? [Y]/[N]\n")
                    if exit_code:
                        pass
                    else:
                        raise BlankValue("Blank Value is provided")
                else:
                    raise InvalidNumber("Value provided is not in given range")
            else:
                raise InvalidNumber("Value provided is not in given range")

        except (BlankValue, MultipleValues, InvalidNumber) as e:
            print(str(e) + ", Exiting Program...")
            break

        if exit_code[0].upper() == 'Y':
            pass
        elif exit_code[0].upper() == 'N':
            print("Program is exiting... Thanks !!!")
            flag = False
        else:
            print("Inappropriate input provided, program exiting...")
            flag = False

# Test case 1 before running it, kindly unset the flag
'''
number = 124
obj = GenerateRandomNumber(number)
high_count = 0
low_count = 0

for _ in range(100):
    res = obj.get_number(number)
    print(res)
    if res > number//2:
        high_count += 1
    else:
        low_count += 1

print("high count is {0}, and low count is {1}".format(high_count, low_count))
'''
