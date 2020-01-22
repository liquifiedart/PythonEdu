class Exercises:

    # Find n number of primes, starting at 2
    # A prime number is only divisible by itself and 1
    def find_n_primes(self, n):
        result = list()
        testing_value = 2

        # Loop until we find N primes
        # Each iteration should take a value i and try to divide i, i-1 times
        # If any is 0 it is not a prime, move onto next number
        while len(result) < n:
            is_prime = True

            # is testing_value prime?
            for j in range(2, testing_value):
                if testing_value % j == 0:
                    is_prime = False
                    break

            if is_prime:
                result.append(testing_value)
            testing_value += 1

        return result

    # Get's the nth value of the fibonacci sequence
    # 1, 1, 2, 3
    def fibonacci(self, nth):
        prev1 = 0
        prev2 = 1
        result = prev2
        print(prev2.__str__() + ", ", end="")
        for i in range(nth - 1):
            result = prev1 + prev2
            print(result.__str__() + ", ", end="")
            prev1 = prev2
            prev2 = result
        print("")
        return result

    # Given a string find the biggest palindrome substring
    # example: AABCDCBA output should be ABCDCBA
    # A palindrone reads the same frontwards / backwards
    def find_largest_palindrone(self, value):

        max_palindrone_substring = ("", 0)

        for i in range(len(value)):
            substring = value[i: i + len(value)]
            result = self.get_max_palindrone_len(substring)

            if max_palindrone_substring[1] < result[1]:
                max_palindrone_substring = result

        return max_palindrone_substring[0]

    def get_max_palindrone_len(self, substring):

        sub_palindrone = ""
        palindrone_len = 1
        single_char_ct = 0
        dict_counts = {}
        sslen = len(substring)
        for i in range(sslen):

            # if it doesnt exist
            if not substring[i] in dict_counts:
                dict_counts[substring[i]] = 1
                single_char_ct += 1
            else:
                if dict_counts[substring[i]] == 1:
                    single_char_ct -= 1
                dict_counts[substring[i]] = dict_counts[substring[i]] + 1

            # ODD or EVEN length with correct single character count
            if i > 0 and single_char_ct <= 1:
                if palindrone_len < i + 1:
                    palindrone_len = i + 1
                    sub_palindrone = substring[0:(i + 1)]

            # if the len of the current iteration > the len of the remaining values
            # and the single char ct is greater than 1
            currlen = (i+1)
            remainingchars = (sslen - currlen)
            if currlen > remainingchars and single_char_ct > remainingchars:
                break

        if single_char_ct <= 1:
            palindrone_len = len(substring)
            sub_palindrone = substring

        if palindrone_len > 1:
            print(sub_palindrone)
        return (sub_palindrone, len(sub_palindrone))

    # Given an array Find K most frequent elements
    # Example: [1, 2, 3, 2, 4, 6, 6, 2]
    # If K is 2, return should be [6, 2] or [2, 6] based on how you sort results
    # 0(v + kn)
    def get_common_elements(self, k, values):
        counts = dict()
        high_values = [None for x in range( k )]

        # store frequencies in a dictionary
        for value in values:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        for key in counts.keys():
            self.fill_high_values_N(key, counts, high_values, False)

        return high_values



    def fill_high_values_N(self, value, counts, high_values, ascending):
        is_value_set = False
        rollover = None

        # Traverse backwards through our high values array and roll-over the value once a higher was replaced
        if ascending:
            range_direction = range(len(high_values))
        else:
            range_direction = range(len(high_values) - 1, -1, -1)

        for high_value_idx in range_direction:

            # if we have a matching value in our high value store and we haven't set a roll over value, exit
            if high_values[high_value_idx] == value and rollover is None:
                break

            # Higher Value: Do we have a higher number of counts? Rollover must not be used yet
            # Remember starting at the right of the array, which hold's highest
            if rollover is None and high_values[high_value_idx] in counts and counts[high_values[high_value_idx]] < counts[value]:
                rollover = high_values[high_value_idx]
                high_values[high_value_idx] = value
                is_value_set = True

            # roll-over: higher value as we traverse backwards through high value store
            # don't roll-over a value
            elif rollover is not None:
                tmp = high_values[high_value_idx]
                high_values[high_value_idx] = rollover
                rollover = tmp

            # Empty-HighValues: if no value is in our high value array put a value in it,
            # unless we have already placed our value at a higher point in the array
            elif high_values[high_value_idx] is None and is_value_set is False:
                high_values[high_value_idx] = value
                break


    # Given an array Find K most frequent elements
    # Example: [1, 2, 3, 2, 4, 6, 6, 2]
    # If K is 2, return should be [6, 2] or [2, 6] based on how you sort results
    # 0(v + k + n)
    def get_common_elements_v2(self, k, values):
        counts = dict()
        frequencies = [list() for x in range(len(values) + 1)]
        high_values = list()

        # store frequencies in a dictionary
        for value in values:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        # add values to each frequency bucket
        for key in counts.keys():
            frequencies[counts[key]].append(key)

        # traverse backwards through buckets and add first K items,
        # including each item in a bucket if there are more than 1
        for bucketidx in range(len(frequencies) - 1, -1, -1):
            for freq in frequencies[bucketidx]:
                if k == 0:
                    break
                high_values.append(freq);
                k -= 1

        # result will have high values at [0]
        return high_values


    def ricky_find_max_elements_v2(self, list_of_numbers):
        '''Function that finds the most frequently appearing values in a list'''
        max_count = 0

        if len(list_of_numbers) == 0:
            return "Please enter a list with values in it"

        v = set(list_of_numbers)
        for i in set(list_of_numbers):
            count = list_of_numbers.count(i)
            max_count = count if count > max_count else max_count

        max_value_list = [x for x in list_of_numbers if list_of_numbers.count(x) >= max_count]
        return set(max_value_list)
