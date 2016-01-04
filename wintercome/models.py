from django.db import models

# Create your models here.
import base64, time, os, subprocess, shlex
from wintercome import MACRO

# Owner Daine.H
# Modify 2016-01-04




class cmdTask(models.Model):
    title = models.CharField(max_length=32)
    ownerid = models.IntegerField(default=1)
    cmd = models.CharField(max_length=500)
    runlevel =  models.IntegerField(blank=True)# groupLevel id
    def __str__(self):
        return self.title
    def taskAllocate(self,userid = 1):
        # 1.需要比对owner是否是执行的用户
        pass
    def baseCall(self):
        # 运行命令行,记录运行结果到log文件,返回状态码
        logfile = time.strftime(MACRO.CMDLOGTIME,time.localtime(time.time()))
        with open(os.path.join('wintercome/log/cmdlog/',logfile), 'ab') as log:
            res = subprocess.Popen(shlex.split(self.cmd),stdout = subprocess.PIPE)
            log.write(bytes('\nRun cmd [' + self.title + ']\nat: ' +
                            time.strftime('%H:%M:%S',time.localtime(time.time())) + "\n\n",
                            encoding='utf-8'))
            log.write(res.stdout.read())
            return res.poll()
    def quickcall(self):
        # 快速运行程序
        return subprocess.call(shlex.split(self.cmd))





class groupLevel(models.Model):
    title = models.CharField(max_length=32)
    level = models.IntegerField(default= MACRO.VIEWER)
    def __str__(self):
        return self.title


class winterUser(models.Model):
    userid = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    group = models.IntegerField(blank=True)
    def setPasswd(self, ori_pwd):
        pwd_byte = bytes(ori_pwd,encoding = 'utf-8')
        self.passwd = base64.encodebytes(pwd_byte)
        return self.passwd
    def getPasswd(self):
        try:
            byte_pwd = base64.decodebytes(self.passwd)
            ori_pwd = str(byte_pwd,encoding = 'utf-8')
        except:
            ori_pwd = ""
        return ori_pwd
    def __str__(self):
        return self.userid
    def createCmd(self,cmdline = None):
        logfile = time.strftime(MACRO.APPLOGTIME,time.localtime(time.time()))
        with open(os.path.join('wintercome/log/applog/',logfile), 'ab') as log:
            if cmdline == None:
                print("\nERROR CMD input!")
                log.write(b'cmdline input is none.')
                break
            else:
                cmdTask()

