spell = "Wingardium Leviosa"

def my_func():
    s = input()
    if s in spell:
        print(spell.find(s))
    else:
        print(-1)

my_func()
