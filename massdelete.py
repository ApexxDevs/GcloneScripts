import subprocess
import re
 
print('Warning! Check The Files You are Deleting')
 
class multidelete():        
    def delFiles(self):
        with open('delinks.txt') as f:
            fin = f.readlines()

            for line in fin:
                self.links = re.search(r'([\w-]){33}|([\w-]){19}', line).group()
                command = 'gclone --config=rclone.conf deletefile GC:{' + self.links + '}-vP --stats-one-line --stats=15s --fast-list'
                process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
                print(process.stdout)
                print('============================\n'+
                        'Link has been Deleted :)\n'+
                        '============================')
            print('All Links has been Deleted! :)')

    def runScript(self):
        self.delFiles()

multidelete().runScript()
input()
