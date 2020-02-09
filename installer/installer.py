import os
import platform
import subprocess
import time


class Installer:
    wheel = ['|', '/', '-', '\\']

    def __init__(self, root: bool = False):
        if platform.system() != 'Linux':
            print('This only works on Linux')
            raise SystemExit(1)

        if root and os.geteuid() != 0:
            print('This script must be run as root')
            raise SystemExit(1)

    def run(self, message: str, command: str, die: bool = True) -> bool:
        temp = '\r [%s] ' + message
        idx = 0

        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            executable='/bin/bash')

        while proc.poll() is None:
            if idx < len(self.wheel) - 1:
                idx += 1
            else:
                idx = 0

            print(temp % self.wheel[idx], end='')
            time.sleep(0.1)

        if proc.returncode == 0:
            print(temp % '+')
            return True

        print(temp % 'x', end=': ')
        print(proc.stderr.read().decode('utf-8'), end='')

        if die:
            raise SystemExit(proc.returncode)

        return False
