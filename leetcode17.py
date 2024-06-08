phonekeypad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

empty = ['']
a = input()
if a:
    for digit in a:
        if digit in phonekeypad:
            letters = phonekeypad[digit]
            newcombinations = []
            for letter in letters:
                for existingcombination in empty:
                    newcombinations.append(existingcombination + letter)
            empty = newcombinations

print(empty)
