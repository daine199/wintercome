# Owner Daine.H
# Modify 2016-01-05
# logging 装饰器

from wintercome.lib import MACRO, common
import time
import os

def init_log_path():
    if not os.path.exists(MACRO.APPLOGPATH):
        pass



def trace_app_log(func):
    """

    :param func:    trace_log(func)
    :return:        logging(*args,**kwargs)
    :action:        print log in stdout
    """
    if MACRO.LOGGINGSWITCH == 1:

        def logging(*args,**kwargs):
            logfile = time.strftime(MACRO.APPLOGFILETIME,
                                time.localtime(time.time()))
            with open(os.path.join(MACRO.APPLOGPATH,
                                   logfile), 'a') as log:
                logtime = time.strftime(MACRO.APPLOGTIME,
                                        time.localtime(time.time()))
                print(logtime, ":Start {0}:({1},{2})..".format(func.__name__,
                                                               args, kwargs))
                log.write("\n\n{0}: Start {1}:({2},{3})..\n".format(logtime,
                                                                    func.__name__,
                                                                    args, kwargs))
            return func(*args, **kwargs)
        return logging
    else:
        def logging(*args,**kwargs):
            return func(*args, **kwargs)
        return logging


def app_logging(raw_input):
    if MACRO.LOGGINGSWITCH == 1:
        logfile = time.strftime(MACRO.APPLOGFILETIME,
                                time.localtime(time.time()))
        with open(os.path.join(MACRO.APPLOGPATH,
                               logfile), 'a') as log:
            log.write(raw_input)
    else:
        pass


def str_to_bytes(raw_input):
    return bytes(raw_input, encoding='utf-8')


def cmd_logging(raw_input):
    if MACRO.LOGGINGSWITCH == 1:
        logfile = time.strftime(MACRO.CMDLOGFILETIME,
                                time.localtime(time.time()))
        with open(os.path.join(MACRO.CMDLOGPATH,
                               logfile), 'ab') as log:
            print(common.bytesToStr(raw_input))
            log.write(raw_input)
    else:
        pass


def cmd_error_logging(error_type=MACRO.RUNLEVELTOOLOW):
    if MACRO.LOGGINGSWITCH == 1:
        logfile = time.strftime(MACRO.CMDLOGFILETIME,
                                time.localtime(time.time()))
        with open(os.path.join(MACRO.CMDLOGPATH,
                               logfile), 'a') as log:
            print(error_type)
            log.write(error_type)
    else:
        pass


def logging_time(time_format=MACRO.APPLOGTIME):
    retime = time.strftime(time_format, time.localtime(time.time()))
    return retime










@trace_app_log
def logtests():
    print("I'm the tests one")

@trace_app_log
def logtests2(a = None):
    print("I'm the tests two with paramete {0}".format(a))

@trace_app_log
def logtests3(a = None, b = None, c = None):
    print("I'm the tests two with paramete {0},{1},{2}".format(a,b,c))

if __name__ == '__main__':
    logtests()

    logtests2("Big improve!")

    logtests3(a = "I've no idea.",b = 54, c = [123,231])