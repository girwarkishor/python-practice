import argparse

parse = argparse.ArgumentParser();

parse.add_argument("-n", "--name", type=str, help="Its takes username as the input string")
parse.add_argument('--id', type=str, help="Its takes id as the input string")

args = parse.parse_args();
# this code is not executed on the main.py
if __name__ == "__main__":
    print("args file print element")
    print(args.name)
    print(args.id)
    print("args file print element end")

# When you run this code then only above print will execute
# c:\> python .\args_parsing.py --name Girwar id 123
# args file print element
# Girwar
# 78
# args file print element end

# Without if __name__ == "__main__": statement output will be for main.py
# c:\> python .\main.py --name Girwar --id 78
# args file print element
# Girwar
# 78
# args file print element end
# main funtion starts
# Girwar
# 78
# main function ends
# (venv) PS F:\Python Automation Learning\args_class>
