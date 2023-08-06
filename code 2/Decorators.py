def dec_1 (func_1) :
    def nowexec () :
        print("executing now ...")
        func_1()
        print("executed")
    return nowexec

@dec_1
def abc () :
    print("anas")
#abc = dec_1(abc)
abc()