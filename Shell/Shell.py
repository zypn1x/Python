import os


def check(args, args_needed, f_name):
    conditions = args.split(" ")
    if len(conditions) != args_needed:
        return False
    if conditions[0] != f_name:
        return False
    return True


class Function:
    num_ars = 0
    fun_name = ""


class Exit(Function):
    num_ars = 1

    @staticmethod
    def exit():
        if not check(Exit.fun_name, Exit.num_ars, "exit"):
            print("no such command")
            return False
        return True


class Mkdir(Function):
    num_ars = 2

    @staticmethod
    def mkdir():
        if not check(Mkdir.fun_name, Mkdir.num_ars, "mkdir"):
            print("no such command")
            return
        buffer = Mkdir.fun_name.split(" ")
        os.mkdir(buffer[1])
        print("dir", buffer[1], "created")


class Ls(Function):
    num_ars = 1

    @staticmethod
    def ls():
        if not check(Ls.fun_name, Ls.num_ars, "ls"):
            print("no such command")
            return
        dirs = os.listdir(os.getcwd())
        for i in dirs:
            print(i)


class Pwd(Function):
    num_ars = 1

    @staticmethod
    def pwd():
        if not check(Pwd.fun_name, Pwd.num_ars, "pwd"):
            print("no such command")
            return
    print(os.getcwd())


class Cd(Function):

    @staticmethod
    def cd():
        args = Cd.fun_name.split(" ")
        if len(args) == 1:
            if args[0] == "cd":
                os.chdir("")
            else:
                print("no such command")
        elif len(args) == 2:
            if args[0] == "cd":
                os.chdir(args[1])
            else:
                print("no such command")
        else:
            print("no such command")


class RmDir(Function):
    num_ars = 2

    @staticmethod
    def rmdir():
        if not check(RmDir.fun_name, RmDir.num_ars, "rmdir"):
            print("no such command")
            return
        args = RmDir.fun_name.split(" ")
        name = args[1]
        exist = False
        for i in os.listdir(os.getcwd()):
            if i == name:
                exist = True
                break
        if exist:
            os.rmdir(name)
        else:
            print('No such directory')


class Cp(Function):
    num_args = 3

    @staticmethod
    def cp():
        if not check(Cp.fun_name, Cp.num_ars, "cp"):
            print("no such command")
            return
        file_names = Cp.fun_name.split(" ")
        id = False
        for i in os.listdir(os.getcwd()):
            if i == file_names[1]:
                id = True
                break
        if id:
            os.system(Cp.fun_name)
        else:
            print('No such file')


class Mv(Function):
    num_ars = 3

    @staticmethod
    def mv():
        if not check(Mv.fun_name, Mv.num_ars, "mv"):
            print("no such command")
            return
        name = Mv.fun_name.split(" ")
        f_id = False
        s_id = False
        for i in os.listdir(os.getcwd()):
            if i == name[1]:
                f_id = True
            if i == name[2]:
                s_id = True
            if f_id and s_id:
                break
        if f_id and s_id:
            os.system(Mv.fun_name)
        if not f_id:
            print('No such file or directory')
        if not s_id:
            print('No such directory')


class Rm(Function):

    @staticmethod
    def rm():
        args = Rm.fun_name.split(" ")
        if len(args) > 2:
            print("no directory or file")
            return
        if args[0] != "rm":
            print("no such command")
            return
        name = args[1]
        id = False
        for i in os.listdir(os.getcwd()):
            if i == name:
                id = True
                break
        if id:
            os.remove(name)
        else:
            print('No such file')


print('Terminal V 1.0')
while True:
    cmd = input()
    if cmd[0:4] == "exit":
        command = Exit
        command.fun_name = cmd
        if command.exit():
            break
    elif cmd[0:5] == "mkdir":
        command = Mkdir
        command.fun_name = cmd
        command.mkdir()
    elif cmd[0:2] == "ls":
        command = Ls
        command.fun_name = cmd
        command.ls()
    elif cmd[0:3] == "pwd":
        command = Pwd
        command.fun_name = cmd
        command.pwd()
    elif cmd[0:2] == "cd":
        command = Cd
        command.fun_name = cmd
        command.cd()
    elif cmd[0:5] == "rmdir":
        command = RmDir
        command.fun_name = cmd
        command.rmdir()
    elif cmd[0:2] == "cp":
        command = Cp
        command.fun_name = cmd
        command.cp()
    elif cmd[0:2] == "mv":
        command = Mv
        command.fun_name = cmd
        command.mv()
    elif cmd[0:2] == "rm":
        command = Rm
        command.fun_name = cmd
        command.rm()
    else:
        print("no such command")
print('end.')
