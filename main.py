# import basic
import original
from termcolor import colored

if __name__=="__main__":
    while True:
        text=input("gpzer > ")
        if text.strip()=="":continue
        result,error=original.run("test.gp",text)
        if error:
            print(colored(error.as_string(),"red"))
        elif result:
            if len(result.elements)==1:
                print(repr(result.elements[0]))
            else:   
                print(repr(result))