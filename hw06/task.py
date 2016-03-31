UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS="abcdefghijklmnopqrstuvwxyz"
NUMBERS="1234567890"
SYMBOLS=".?!&#,;:-_*"

pw = raw_input("Password: ")

#Task the First
def isValid(pw):
    if [1 for x in pw if x in UC_LETTERS]:
        if [1 for x in pw if x in LC_LETTERS]:
            if [1 for x in pw if x in NUMBERS]:
                print [1 for x in pw if x in NUMBERS]
                print "Valid password"
                return True 
    print "Nope."
    return False

#Task the Second
def strength(pw):
    strength = 0
    if len(pw) <= 6:
        strength = len(pw) - 2
        if [1 for x in pw if x in SYMBOLS]:
            strength += 1
        print "Password Strength: " + str(strength)
        return
    else:
        n = [1 if x in UC_LETTERS else 0 for x in pw]
        m = n[0]
        for i in n[1:]:
            if m != i:
                strength += 1
            m = i
        n = [1 if x in LC_LETTERS else 0 for x in pw]
        m = n[0]
        for i in n[1:]:
            if m != i:
                strength += 1
            m = i
        n = [1 if x in NUMBERS else 0 for x in pw]
        m = n[0]
        for i in n[1:]:
            if m != i:
                strength += 1
            m = i
        n = [1 if x in SYMBOLS else 0 for x in pw]
        m = n[0]
        for i in n[1:]:
            if m != i:
                strength += 1
            m = i
        if strength > 10:
            strength = 10
        print "Password Strength: " + str(strength)
        return

if (isValid(pw)):
    strength(pw)


