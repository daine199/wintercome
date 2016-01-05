from django.db import models

# Create your models here.
import base64, time, os, subprocess, shlex
from wintercome.lib.logging import (trace_app_log, appLogging,
                                    cmdLogging, loggingtime,
                                    strToBytes)
from wintercome.lib import MACRO


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
    @trace_app_log
    def baseCall(self):
        # 运行命令行,记录运行结果到log文件,返回状态码
        logprint = "Run cmd {0} at {1} . \n".format(self.title,loggingtime())
        cmdLogging(strToBytes(logprint))
        res = subprocess.Popen(shlex.split(self.cmd),
                               stdout = subprocess.PIPE)
        cmdLogging(res.stdout.read())
        cmdLogging(strToBytes('Return {0}\n'.format(res.poll())))
        return res.poll()

    @trace_app_log
    def quickcall(self):
        # 快速运行程序
        return subprocess.call(shlex.split(self.cmd))

class runLevel(models.Model):
    title = models.CharField(max_length=32)
    level = models.IntegerField(default= MACRO.VIEWER)
    def __str__(self):
        return self.title


class winterUser(models.Model):
    userid = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    runLevel = models.IntegerField(blank=True)
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
    @trace_app_log
    def createCmd(self,cmdline = None):
        logfile = time.strftime(MACRO.APPLOGFILETIME,
                                time.localtime(time.time()))
        logtime = time.strftime(MACRO.APPLOGTIME,
                                time.localtime(time.time()))
        if cmdline == None:
            print("ERROR CMD input!\ncmdline input is none.\n")
            appLogging('ERROR CMD input!\ncmdline input is none.\n')
        else:
            try:
                task = cmdTask(title = cmdline['title'],
                               ownerid = self.id,
                               cmd = cmdline['cmd'],
                               runlevel = self.runLevel)
                task.save()
                logprint = "Create Task id:" + \
                               str(task.id) + \
                               " successed.\nCMD = [" + \
                               cmdline['cmd'] + \
                               "] .\n"
                print(logprint)
                appLogging(logprint)
            except:
                logprint = "Create task failed." + \
                           "\nCreate " + cmdline['cmd'] + \
                           " failed.\n"
                print(logprint)
                appLogging(logprint)


