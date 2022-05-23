from src.commands import Ls, Cd, Mkdir, Pwd, Exit, RmDir, Cp, Mv, Rm


class Shell:
    commands = \
        {'cd': Cd, 'ls': Ls, 'mkdir': Mkdir, 'pwd': Pwd, 'exit': Exit, 'rmdir': RmDir, 'cp': Cp, 'mv': Mv, 'rm': Rm}

    def run(self):
        print('Terminal V 3.2')
        while True:
            cmd = input()
            word = cmd.split()
            if len(word) == 0:
                print("no such command")
            elif len(word) == 1 and word[0] == Exit.__name__.lower():
                break
            else:
                if word[0] in self.commands.keys():
                    command = self.commands[word[0]](cmd)
                    command.execute()
                else:
                    print("no such command")
        print('end.')
