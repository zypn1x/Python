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
    id = False


class Exit(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")
        self.id = check(self.buffer, Exit.num_ars, "exit")
        if not self.id:
            print("incorrect command. May be you wanted to print 'exit'?")

    def execute(self):
        if not self.id:
            return False
        return True


class Mkdir(Function):
    num_ars = 2

    def __init__(self, command):
        self.buffer = command.split(" ")
        self.id = check(self.buffer, Mkdir.num_ars, "mkdir")
        if not self.id:
            print("incorrect command. May be you wanted to print 'mkdir <dir.name>'?")

    def execute(self):
        if self.id:
            os.mkdir(self.buffer[1])
            print("dir", self.buffer[1], "created")


class Ls(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")
        self.id = check(self.buffer, Ls.num_ars, "ls")
        if not self.id:
            print("incorrect command. May be you wanted to print 'ls'?")

    def execute(self):
        if self.id:
            dirs = os.listdir(os.getcwd())
            for i in dirs:
                print(i)


class Pwd(Function):
    num_ars = 1

    def __init__(self, command):
        self.buffer = command.split(" ")
        self.id = check(self.buffer, Pwd.num_ars, "pwd")
        if not self.id:
            print("incorrect command. May be you wanted to print 'pwd'?")

    def execute(self):
        if self.id:
            print(os.getcwd())


class Cd(Function):
    def __init__(self, command):
        self.buffer = command.split(" ")
        if len(self.buffer) == 1:
            if self.buffer[0] == "cd":
                self.id = True
                self.num_ars = 1
            else:
                self.id = False
                print("incorrect command. May be you wanted to print 'cd'?")
        elif len(self.buffer) == 2:
            if self.buffer[0] == "cd":
                self.id = True
                self.num_ars = 2
            else:
                self.id = False
                print("incorrect command. May be you wanted to print 'cd <path/dirname>'?")
        else:
            self.id = False
            print("incorrect command. May be you wanted to print 'cd <path/dirname>'?")

    def execute(self):
        if self.id:
            if self.num_ars == 1:
                os.chdir("")
            else:
                os.chdir(self.buffer[1])


class RmDir(Function):
    num_ars = 2

    def __init__(self, command):
        self.buffer = command.split(" ")
        self.id = check(self.buffer, RmDir.num_ars, "rmdir")
        if not id:
            print("incorrect command. May be you wanted to print 'rmdir <dirname>'?")
        else:
            exist = False
            for i in os.listdir(os.getcwd()):
                if i == self.buffer[1]:
                    exist = True
            if not exist:
                print('No such directory')
            self.id = exist

    def execute(self):
        if self.id:
            os.rmdir(self.buffer[1])


class Cp(Function):
    num_args = 3
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split(" ")
        self.id = check(self.buffer, Cp.num_args, "cp")
        if check(self.buffer, Cp.num_args, "cp"):
            for i in os.listdir(os.getcwd()):
                if i == self.buffer[1]:
                    self.id = True
                    break
            if not self.id:
                print('No such file')
        else:
            print("incorrect command. May be you wanted to print 'cp <copy file name> <new file name>'?")

    def execute(self):
        if id:
            os.system(self.fun_name)


class Mv(Function):
    num_ars = 3
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split(" ")
        if check(self.buffer, Mv.num_ars, "mv"):
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
                self.id = True
            if not f_id:
                print('No such file or directory')
            if not s_id:
                print('No such directory')
        else:
            print("incorrect command. May be you wanted to print 'Mv <moving file or dir name> <path/dir>'?")

    def execute(self):
        if self.id:
            os.system(self.fun_name)


class Rm(Function):
    def __init__(self, command):
        self.buffer = command.split(" ")
        if len(self.buffer) > 2:
            print("incorrect command. May be you wanted to print 'Rm <removing  file name>'?")
            return
        if self.buffer[0] != "rm":
            print("no such command")
            return
        for i in os.listdir(os.getcwd()):
            if i == self.buffer[1]:
                self.id = True
                return
        print('No such file')

    def execute(self):
        if id:
            os.remove(self.buffer[1])
