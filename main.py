
# Hanoi disc problem


def move(f,t):
    # Use a breakpoint in the code line below to debug your script.
    print("Move disc from {}  to {}!".format(f,t))  # Press ⌘F8 to toggle the breakpoint.


# n is no. of disks, f from position, h is helper function, t target position.
def hanoi(n,f,h,t):
    if n == 0 :
        pass
    else :
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)


# Main
if __name__ == '__main__':
    hanoi(10,"A","B","C")

