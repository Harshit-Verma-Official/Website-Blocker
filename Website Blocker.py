import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def block(url):
    file = open("C://Windows//System32//drivers//etc//hosts", 'a+')
    file.seek(0)
    content = file.read()
    if url in content:
        print(url + " is already blocked.")
    else:
        if "www" in url:
            domain = url.replace("www.", "")
            file.write("127.0.0.1 " + domain + "\n")
            file.write("127.0.0.1 " + url + "\n")
            file.close()
            print(url + " is Blocked.")
        else:
            file.write("127.0.0.1 " + url + "\n")
            file.write("127.0.0.1 www." + url + "\n")
            file.close()
            print(url + " is Blocked")


def unblock(url):
    file = open("C://Windows//System32//drivers//etc//hosts", 'r+')
    content = file.read()
    file.close()
    new_host = []
    if url in content:
        old = content.split('\n')
        for line in old:
            if not url in line:
                new_host.append(line)
        final_content = "\n".join(new_host)
        file = open("C://Windows//System32//drivers//etc//hosts", 'w+')
        file.write(final_content)
        file.close()
        print(url + " unblocked")
    else:
        print(url + " is not in the blocked list.")


if is_admin():
    print("1. Block Website\n2. Unblock Website\n")
    inp = int(input())
    if inp == 1:
        website = input()
        while True:
            if website.strip() != '':
                block(website)
                break
            else:
                print("Empty String. Enter again : ")
                website = input()
    elif inp == 2:
        website = input()
        while True:
            if website.strip() != '':
                unblock(website)
                break
            else:
                print("Empty String. Enter again : ")
                website = input()
    else:
        print("Bad Choice\n")
    while True:
        pass

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
