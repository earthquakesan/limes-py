import subprocess

import limespy.conf

class LimesRunner(object):
    def __init__(self):
        pass

    def run(self):
        pass

    def runTest(self):
        command = "java -jar %s %s" % (limespy.conf.limesPath, limespy.conf.testConfPath)
        command = command.split()
        out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
        print out


if __name__ == "__main__":
    limesRunner = LimesRunner()
    limesRunner.runTest()
