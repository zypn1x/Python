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
    f_name = "exit"

    @staticmethod
    def execute():
        if not check(Exit.fun_name, Exit.num_ars, "exit"):
            print("no such command")
            return False
        return True


class Mkdir(Function):
    num_ars = 2
    f_name = "mkdir"

    @staticmethod
    def execute():
        if not check(Mkdir.fun_name, Mkdir.num_ars, "mkdir"):
            print("no such command")
            return
        buffer = Mkdir.fun_name.split(" ")
        os.mkdir(buffer[1])
        print("dir", buffer[1], "created")


class Ls(Function):
    num_ars = 1
    f_name = "ls"

    @staticmethod
    def execute():
        if not check(Ls.fun_name, Ls.num_ars, "ls"):
            print("no such command")
            return
        dirs = os.listdir(os.getcwd())
        for i in dirs:
            print(i)


class Pwd(Function):
    num_ars = 1
    f_name = "pwd"

    @staticmethod
    def execute():
        if not check(Pwd.fun_name, Pwd.num_ars, "pwd"):
            print("no such command")
            return
    print(os.getcwd())


class Cd(Function):
    f_name = "cd"

    @staticmethod
    def execute():
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
    f_name = "rmdir"

    @staticmethod
    def execute():
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
    f_name = "cp"

    @staticmethod
    def execute():
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
    f_name = "mv"

    @staticmethod
    def execute():
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
    f_name = "rm"

    @staticmethod
    def execute():
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


class Shell:
    commands = [Cd, Ls, Mkdir, Pwd, Exit, RmDir, Cp, Mv, Rm]

    def shell(self):
        print('Terminal V 1.0')
        while True:
            cmd = input()
            word = cmd.split()
            id = False
            if word[0] == Exit.f_name:
                break
            for i in self.commands:
                if word[0] == i.f_name:
                    i.fun_name = cmd
                    i.execute()
                    id = True
            if not id:
                print("no such command")
        print('end.')


sh = Shell
sh.shell(sh)
