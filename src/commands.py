import os
import argparse


class Function:
    buffer = []


class Exit(Function):
    parser = argparse.ArgumentParser()

    def __init__(self, command):
        self.buffer = command.split()


class Mkdir(Function):

    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('mkdir', type=str, nargs='?', const='mkdir')
        parser.add_argument('name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            os.mkdir(self.buffer[1])
        except FileExistsError:
            print("Dir already exists!")
        except IndexError:
            print("print the name of the dir")
        except:
            print("incorrect command. May be you wanted to print 'Mkdir <dirname>'?")


class Ls(Function):

    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('ls', type=str, nargs='?', const='ls')
        try:
            parser.parse_args(self.buffer)
            dirs = os.listdir(os.getcwd())
            for i in dirs:
                print(i)
        except:
            print("incorrect command. May be you wanted to print 'ls'?")


class Pwd(Function):

    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('pwd', type=str, nargs='?', const='pwd')
        try:
            parser.parse_args(self.buffer)
            print(os.getcwd())
        except:
            print("incorrect command. May be you wanted to print 'pwd'?")


class Cd(Function):
    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('cd', type=str, nargs='?', const='cd')
        parser.add_argument('dir_name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            os.chdir(self.buffer[1])
        except FileNotFoundError:
            print("incorrect command. ", self.buffer[1], " not found")
        except NotADirectoryError:
            print("incorrect command. ", self.buffer[1], " is not directory")
        except:
            print("incorrect command. May be you wanted to print 'cd <dir_name/../space>'?")


class RmDir(Function):

    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('rmdir', type=str, nargs='?', const='rmdir')
        parser.add_argument('dir_name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            os.rmdir(self.buffer[1])
        except FileNotFoundError:
            print("incorrect command. ", self.buffer[1], " not found")
        except NotADirectoryError:
            print("incorrect command. ", self.buffer[1], " is not directory")
        except:
            print("incorrect command. May be you wanted to print 'cd <dir_name/../space>'?")


class Cp(Function):
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('cp', type=str, nargs='?', const='cp')
        parser.add_argument('copied_name', type=str, nargs=1)
        parser.add_argument('new_name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            dirs = os.listdir(os.getcwd())
            for i in dirs:
                if self.buffer[2] == i:
                    raise FileExistsError
            os.system(self.fun_name)
        except FileExistsError:
            print("incorrect command. ", self.buffer[2], " already exists")
        except FileNotFoundError:
            print("incorrect command. ", self.buffer[1], " not found")
        except:
            print("incorrect command. May be you wanted to print 'cp <copy file name> <new file name>'?")


class Mv(Function):
    num_ars = 3
    fun_name = ""

    def __init__(self, command):
        self.fun_name = command
        self.buffer = command.split()
        print("incorrect command. May be you wanted to print 'Mv <moving file or dir name> <path/dir>'?")

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('mv', type=str, nargs='?', const='mv')
        parser.add_argument('moved_name', type=str, nargs=1)
        parser.add_argument('dir_name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            os.system(self.fun_name)
        except NotADirectoryError:
            print("incorrect command. ", self.buffer[2], " not a directory")
        except FileNotFoundError:
            print("incorrect command. ", self.buffer[1], " not found")
        except:
            print("incorrect command. May be you wanted to print 'Mv <moving file or dir name> <path/dir>'?")


class Rm(Function):
    def __init__(self, command):
        self.buffer = command.split()

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('rm', type=str, nargs='?', const='rm')
        parser.add_argument('removed_name', type=str, nargs=1)
        try:
            parser.parse_args(self.buffer)
            os.remove(self.buffer[1])
        except IndexError:
            print("you should write file name")
        except FileNotFoundError:
            print("incorrect command. File not fund")
        except:
            print("incorrect command. May be you wanted to print 'Rm <removing  file name>'?")
