import os


def read_file(savedir="./"):
    with open("test.txt", encoding="utf-8") as target_file:
        if savedir != "./" and savedir[-1] != "/":
            savedir = savedir + "/"

        # created the directory if not present
        if not os.path.exists(os.path.dirname(savedir)):
            print(
                "[ + ] "
                + os.path.dirname(savedir)
                + " directory does not exist, creating it."
            )
            os.makedirs(os.path.dirname(savedir))

        content = target_file.read()

    return content


def process_report(savedir="./"):
    content = read_file()
    with open(
        f"{savedir}redacted_{os.path.basename('test.txt')}",
        "w",
        encoding="utf-8",
    ) as result:
        for line in content:
            print(line)


process_report()
