# Given a string, find the length of the longest substring, which has no repeating characters.

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".


def non_repeat_substring(my_string):
    # store last_letter, length_longest (output), curr_length
    # for char in my_string
    # compare to last_letter. if same, don't change last_letter or length_longest, but reset curr_length to 0
                            # else, change last_letter, curr_length, and, if relevant, length_longest
    last_letter = ''
    longest_nonrepeater = 0
    curr_length = 0

    for char in my_string:
        if char==last_letter:
            curr_length = 1
        else:
            last_letter = char
            curr_length += 1
            if curr_length > longest_nonrepeater:
                longest_nonrepeater += 1

    return longest_nonrepeater

print(non_repeat_substring("aabccbb")) #abc, 3
print(non_repeat_substring("abbbb")) #ab, 2
print(non_repeat_substring("abccde")) #abc or cde, 3

