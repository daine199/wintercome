from django.db import models
from django.db.utils import IntegrityError

# Create your models here.
import base64
import time
import subprocess
import shlex
import sys
from .lib.logging import (trace_app_log, app_logging,
                          cmd_logging, logging_time,
                          str_to_bytes, cmd_error_logging)
from .lib import MACRO, common


# Owner Daine.H
# Modify 2016-01-04


class CmdTask(models.Model):
    title = models.CharField(max_length=32)
    ownerid = models.CharField(max_length=32)
    cmd = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    run_level = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

    @trace_app_log
    def task_allocate(self, userid = 1):
        if self.ownerid == userid:
            return self.base_call()
        else:
            if WinterUser.objects.get(id=userid).runLevel >= self.run_level:
                return self.base_call()
            else:
                cmd_error_logging(MACRO.RUNLEVELTOOLOW)

    @trace_app_log
    def base_call(self):
        # 运行命令行,记录运行结果到log文件,返回状态码
        log_print = "\nRun cmd {0} at {1} . \n".format(self.title, logging_time())
        cmd_logging(str_to_bytes(log_print))
        res = subprocess.Popen(shlex.split(self.cmd),
                               stdout=subprocess.PIPE)
        res_print = res.stdout.read()
        cmd_logging(res_print)
        cmd_logging(str_to_bytes('Return {0}\n'.format(res.poll())))
        return {'return_code': res.poll(), 'return_print': common.bytesToStr(res_print).split("\n")}

    @trace_app_log
    def quick_call(self):
        # 快速运行程序
        return subprocess.call(shlex.split(self.cmd))


class RunLevel(models.Model):
    title = models.CharField(max_length=32)
    level = models.IntegerField(default=MACRO.VIEWER)

    def __str__(self):
        return self.title


class WinterUser(models.Model):
    userid = models.CharField(max_length=32,
                              db_index=True,
                              unique=True)
    passwd = models.CharField(max_length=32)
    run_level = models.IntegerField(blank=True, db_index=True)

    def set_passwd(self, ori_pwd):
        pwd_byte = bytes(ori_pwd, encoding='utf-8')
        self.passwd = base64.encodebytes(pwd_byte)
        self.save()
        return self.passwd

    def get_passwd(self):
        try:
            byte_pwd = base64.decodebytes(self.passwd)
            ori_pwd = str(byte_pwd, encoding='utf-8')
        except TypeError:
            ori_pwd = ""
        return ori_pwd

    def __str__(self):
        return self.userid

    @trace_app_log
    def create_cmd(self, cmdline=None):
        if cmdline is None:
            print("ERROR CMD input!\ncmdline input is none.\n")
            app_logging('ERROR CMD input!\ncmdline input is none.\n')
        else:
            task = CmdTask(title=cmdline['title'],
                           ownerid=self.id,
                           cmd=cmdline['cmd'],
                           run_level=self.run_level)
            task.save()
            log_print = "Create Task id:" + \
                        str(task.id) + \
                        " successful .\nCMD = [" + \
                        cmdline['cmd'] + \
                        "] .\n"
            print(log_print)
            app_logging(log_print)


