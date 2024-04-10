# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    '''For each character in the input string:
    Form a simpler string by removing the character from the input string
    Generate all permutations of the simpler string recursively (i.e. call the
    perm_gen_lex function with the simpler string)
    Add the removed character to the front of each permutation of the simpler string, and
    add the resulting permutation to the list '''
    if not str_in:
        return []

    if len(str_in) == 1:
        return [str_in]

    lst = []
    for i in range(0, len(str_in)):
        first = str_in[i]
        for perm in perm_gen_lex(str_in[:i] + str_in[i + 1:]):
            lst.append(first + perm)

    return lst
