#!/usr/bin/python

import time


def CheckTask(Task):
    taskTime=Task['StartTime']
    current=time.time()  
    if abs(current-taskTime)<2:
        return True
    else:
        return False

def Tick():
    # Sleep for a while
    time.sleep(1)

def Init():
    print('init')
    taskList=[]
    taskList.append({'StartTime':time.time()+10})
    return taskList


if __name__=='__main__':
    taskList=Init()
    while True:
        for task in taskList:
            if CheckTask(task):
                print("ringringring")
        Tick()

