from argparse import ArgumentParser
import os

FILENAME = "_keys.txt"
def main():
    parser = ArgumentParser(prog='alliance', description='helps manage alliance router\'s APIKEYS')
    parser.add_argument('command', choices=['list','configure'], help="List all stored APIKEYS or Configure APIKEYs.")
    parser.add_argument('--nogitignore', '--nogi', '-n', action="store_true" ,help=f"Choose to ignore {FILENAME} or not. Default is True.")
    args = parser.parse_args()
    match args.command:
        case "list":
                with open(os.getcwd()+f"/{FILENAME}", "r") as f:
                    contents = f.readlines()
                    print("key_openai", contents[0].strip() if len(contents)>0 else "empty")
                    print("key_huggingface", contents[1] if len(contents)>1 else "empty")
        case "configure":
                if not os.environ.get("key_openai"):
                    openai = input("key_openai (set to env variable if needed): ")
                if not os.environ.get("key_huggingface"):
                    huggingface = input("key_huggingface (set to env variable if needed): ")
                with open(os.getcwd()+f"/{FILENAME}", "w") as f:
                    f.write(openai+"\n"+huggingface)
                lines = set()
                lineslist = []
              
                if not args.nogitignore:
                   
                    with open(os.getcwd()+"/.gitignore", "r") as f:
                        lineslist = f.readlines()
                        lines = set(lineslist)
                    with open(os.getcwd()+"/.gitignore", "a") as f:
                        if FILENAME not in lines:
                            if len(lines) > 0 and lineslist[len(lines)-1][-1] != "\n":
                                f.write("\n")
                            f.write(FILENAME)
                else:
                    with open(os.getcwd()+"/.gitignore", "r") as f:
                        lineslist = f.readlines()
                        lines = set(lineslist)
                    if FILENAME in lines:
                        lines= lines.remove(FILENAME)
                        if lines:
                            lineslist = list(lines)
                        else:
                            lineslist = []
                    with open(os.getcwd()+"/.gitignore", "w") as f:
                        f.writelines(lineslist)

if __name__ == '__main__':
    main()
