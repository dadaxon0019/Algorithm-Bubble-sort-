def solution(s):
    final_string = ""
    for letter in s:
        if letter.isupper():
            final_string += ' ' + letter
        else:
            final_string +=letter
    return final_string

res = solution('camelCase')
print(res)