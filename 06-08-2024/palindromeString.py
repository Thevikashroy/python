


def isPalindromeRecurison(_Str):
    if len(_Str) <=1:
        return True
    
    if _Str[0] != _Str[-1]:
        return False
    
    SubString = _Str[1:len(_Str)-1]
    return isPalindromeRecurison(SubString)





def main():
    _Str = "malayalam"
    print(isPalindromeRecurison(_Str))
main()