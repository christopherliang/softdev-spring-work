def make_counter():
    # private "instance" data
    # python scoping rules necessitate list
    count = [0]

    # public methods
    def inc():
        count[0] = count[0] + 1
    def dec():
        count[0] = count[0] - 1
    def reset():
        count[0] = 0
    def get():
        return count[0]

    # return dictionary to allow access to all methods
    return { 'inc' : inc, 'dec' : dec, 'reset': reset, 'get' : get }

c1 = make_counter()
c2 = make_counter()

c1['inc']()
c1['inc']()
c1['inc']()
print c1['get']()

c2['inc']()

