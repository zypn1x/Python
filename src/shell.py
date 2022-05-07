from src.commands import Ls, Cd, Mkdir, Pwd, Exit, RmDir, Cp, Mv, Rm


class Shell:
    commands = \
        {'cd': Cd, 'ls': Ls, 'mkdir': Mkdir, 'pwd': Pwd, 'exit': Exit, 'rmdir': RmDir, 'cp': Cp, 'mv': Mv, 'rm': Rm}

    def run(self):
        print('Terminal V 2.1')
        while True:
            cmd = input()
            word = cmd.split()
            if len(word) == 0:
                print("no such command")
            elif word[0] == Exit.__name__.lower():
                break
            else:
                id = False
                for i in self.commands.keys():
                    if word[0] == i:
                        command = self.commands[i](cmd)
                        command.execute()
                        id = True
                if not id:
                    print("no such command")
        print('end.')
