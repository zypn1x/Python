import os


def check(args, args_needed, f_name):
    if len(args) != args_needed:
        return False
    if args[0] != f_name:
        return False
    return True


class Function:
    num_ars = 0
    buffer = []


class Exit(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Exit.num_ars, "exit"):
            print("no such command")
            return False
        return True


class Mkdir(Function):
    num_ars = 2

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Mkdir.num_ars, "mkdir"):
            print("no such command")
            return
        os.mkdir(self.buffer[1])
        print("dir", self.buffer[1], "created")


class Ls(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Ls.num_ars, "ls"):
            print("no such command")
            return
        dirs = os.listdir(os.getcwd())
        for i in dirs:
            print(i)


class Pwd(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Pwd.num_ars, "pwd"):
            print("no such command")
            return
        print(os.getcwd())


class Cd(Function):

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if len(self.buffer) == 1:
            if self.buffer[0] == "cd":
                os.chdir("")
            else:
                print("no such command")
        elif len(self.buffer) == 2:
            if self.buffer[0] == "cd":
                os.chdir(self.buffer[1])
            else:
                print("no such command")
        else:
            print("no such command")


class RmDir(Function):
    num_ars = 2

    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, RmDir.num_ars, "rmdir"):
            print("no such command")
            return
        name = self.buffer[1]
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
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Cp.num_args, "cp"):
            print("no such command")
            return
        id = False
        for i in os.listdir(os.getcwd()):
            if i == self.buffer[1]:
                id = True
                break
        if id:
            os.system(self.fun_name)
        else:
            print('No such file')


class Mv(Function):
    num_ars = 3
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split(" ")

    def execute(self):
        if not check(self.buffer, Mv.num_ars, "mv"):
            print("no such command")
            return
        f_id = False
        s_id = False
        for i in os.listdir(os.getcwd()):
            if i == self.buffer[1]:
                f_id = True
            if i == self.buffer[2]:
                s_id = True
            if f_id and s_id:
                break
        if f_id and s_id:
            os.system(self.fun_name)
        if not f_id:
            print('No such file or directory')
        if not s_id:
            print('No such directory')


class Rm(Function):
    def __init__(self, command):
        self.buffer = command.split(" ")

    def execute(self):
        if len(self.buffer) > 2:
            print("no directory or file")
            return
        if self.buffer[0] != "rm":
            print("no such command")
            return
        name = self.buffer[1]
        id = False
        for i in os.listdir(os.getcwd()):
            if i == name:
                id = True
                break
        if id:
            os.remove(name)
        else:
            print('No such file')
