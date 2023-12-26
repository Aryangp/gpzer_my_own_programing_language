import basic
from termcolor import colored

if __name__=="__main__":
    while True:
        text=input("gpzer > ")
        result,error=basic.run("test.gp",text)
        if error:
            print(colored(error.as_string(),"red"))
        elif result:
            print(result)