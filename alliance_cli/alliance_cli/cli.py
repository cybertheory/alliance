from argparse import ArgumentParser
import os

def main():
    parser = ArgumentParser(prog='alliance', description='helps manage alliance router\'s APIKEYS')
    parser.add_argument('command', choices=['list','configure'], help="List all stored APIKEYS or Configure APIKEYs.")
    args = parser.parse_args()
    match args.command:
        case "list":
                with open(os.getcwd()+"/_keys.txt", "r") as f:
                    contents = f.readlines()
                    print("key_openai", contents[0].strip() if len(contents)>0 else "empty")
                    print("key_huggingface", contents[1] if len(contents)>1 else "empty")
        case "configure":
                if not os.environ.get("key_openai"):
                    openai = input("key_openai (set to env variable if needed): ")
                if not os.environ.get("key_huggingface"):
                    huggingface = input("key_huggingface (set to env variable if needed): ")
                with open(os.getcwd()+"/_keys.txt", "w") as f:
                    f.write(openai+"\n"+huggingface)
                lines = set()
                lineslist = []
                with open(os.getcwd()+"/.gitignore", "r") as f:
                    lineslist = f.readlines()
                    lines = set(lineslist)
                with open(os.getcwd()+"/.gitignore", "a") as f:
                    if "_keys.txt" not in lines:
                        if len(lines) > 0 and lineslist[len(lines)-1][-1] != "\n":
                            f.write("\n")
                        f.write("_keys.txt")


if __name__ == '__main__':
    main()
