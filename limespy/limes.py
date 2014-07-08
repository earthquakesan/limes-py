import subprocess

import limespy.conf

class LimesRunner(object):
    def __init__(self):
        self.limesPath = limespy.conf.limesPath
        pass

    def run(self, confPath):
        command = self.makeLimesCommand(confPath)
        stdout = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
        return stdout

    def makeLimesCommand(self, confPath):
        command = "java -jar %s %s" % (self.limesPath, confPath)
        return command.split()

    def runTest(self):
        print self.run(limespy.conf.testConfPath)

if __name__ == "__main__":
    limesRunner = LimesRunner()
    print limesRunner.runTest()
