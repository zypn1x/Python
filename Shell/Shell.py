import os
print('Terminal V 1.0')
print(os.name, ':: hellow,', os.getlogin(),  ', waiting your command...')
while True:
    cmd = input()
    if cmd == "exit":
        break
    elif cmd[0:5] == "mkdir":
        name = cmd[6:]
        os.mkdir(name)
        print("dir", name, "created")
    elif cmd == "ls":
        buffer = os.listdir(os.getcwd())
        for i in buffer:
            print(i)
    elif cmd == "pwd":
        print(os.getcwd())
    elif cmd[0:2] == "cd":
        name = cmd[3:]
        os.chdir(name)
    elif cmd[0:5] == "rmdir":
        name = cmd[6:]
        ID = True
        for i in os.listdir(os.getcwd()):
            if i == name:
                ID = True
                break
        if ID:
            os.rmdir(name)
        else:
            print('No such directory')
    elif cmd[0:2] == "cp" and cmd[2] == " ":
        file_names = cmd.split(" ")
        ID = False
        for i in os.listdir(os.getcwd()):
            if i == file_names[1]:
                ID = True
                break
        if ID:
            os.system(cmd)
        else:
            print('No such file')
    elif cmd[0:2] == "mv":
        name = cmd.split(" ")
        f_ID = False
        s_ID = False
        for i in os.listdir(os.getcwd()):
            if i == name[1]:
                f_ID = True
            if i == name[2]:
                s_ID = True
            if f_ID and s_ID:
                break
        if f_ID and s_ID:
            os.system(cmd)
        if not f_ID:
            print('No such file or directory')
        if not s_ID:
            print('No such directory')
    elif cmd[0:2] == "rm" and cmd[2] == " ":
        name = cmd[3:]
        ID = False
        for i in os.listdir(os.getcwd()):
            if i == name:
                ID = True
                break
        if ID:
            os.remove(name)
        else:
            print('No such file')

print('end.')
