from args_parsing import args

def main_func():
    print("main funtion starts")
    print(args.name)
    print(args.id)
    print("main function ends")

main_func()

# c:\> python .\main.py --name Girwar --id 78
# main funtion starts
# Girwar
# 78
# main function ends