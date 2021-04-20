#intializing 
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

#importing numpy, os, sys
import numpy as np 
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Storing information about the experimental sessions
psychopyVersion = '2020.2.10'
expName = 'posner v1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# Putting ExperimentHandler
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\warda\\Downloads\\posner-master\\posner-master\\posner v1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# saving a log file for detail info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame


# Setup the Window

win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initializing components for "instructions"
instructsClock = core.Clock()
instructText = visual.TextStim(win=win, name='instructText',
    text='Welcome to the experiment.\nA red colored target will appear on the left or the right side of the screen brfore you, followed by a cue. \n\nPress the "left" key when the target appears to the left of the screen, and the "right" key when the target appears to the right. Try to do this as fast as possible. \nPress any key to start the experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyToStart = keyboard.Keyboard()
mouseStart = event.Mouse(win=win)
x, y = [None, None]
mouseStart.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cue = visual.ImageStim(
    win=win,
    name='cue', units='height', 
    image='images/arrow-left.png', mask=None,
    ori=1.0, pos=(0, 0), size=(.20, .20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
target = visual.ImageStim(
    win=win,
    name='target', units='height', 
    image='images/circle_red.png', mask=None,
    ori=0, pos=[0,0], size=(.20, .20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
keyPress = keyboard.Keyboard()

# Initialize components for Routine "BlankScreen5"
BlankScreen5Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
finishMsg = visual.TextStim(win=win, name='finishMsg',
    text="Thanks for taking part in the experiment.\n\nWe'll just go and save that data for you!",
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#Prepare to start Routine "instructs"
continueRoutine = True
# update component parameters for each repeat
keyToStart.keys = []
keyToStart.rt = []
_keyToStart_allKeys = []
# setup some python lists for storing info about the mouseStart
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructsComponents = [instructText, keyToStart, mouseStart]
for thisComponent in instructsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# Run Routine "instruction"
while continueRoutine:
    # get current time
    t = instructsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Text* updates
    if instructText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructText.frameNStart = frameN  # exact frame index
        instructText.tStart = t  # local t and not account for scr refresh
        instructText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructText, 'tStartRefresh')  # time at next scr refresh
        instructText.setAutoDraw(True)
    
    # *keyToStart* updates
    waitOnFlip = False
    if keyToStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyToStart.frameNStart = frameN  # exact frame index
        keyToStart.tStart = t  # local t and not account for scr refresh
        keyToStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyToStart, 'tStartRefresh')  # time at next scr refresh
        keyToStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyToStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyToStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyToStart.status == STARTED and not waitOnFlip:
        theseKeys = keyToStart.getKeys(keyList=None, waitRelease=False)
        _keyToStart_allKeys.extend(theseKeys)
        if len(_keyToStart_allKeys):
            keyToStart.keys = _keyToStart_allKeys[-1].name  # just the last key pressed
            keyToStart.rt = _keyToStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouseStart* updates
    if mouseStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouseStart.frameNStart = frameN  # exact frame index
        mouseStart.tStart = t  # local t and not account for scr refresh
        mouseStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouseStart, 'tStartRefresh')  # time at next scr refresh
        mouseStart.status = STARTED
        mouseStart.mouseClock.reset()
        prevButtonState = mouseStart.getPressed()  # if button is down already this ISN'T a new click
    if mouseStart.status == STARTED:  # only update if started and not finished!
        buttons = mouseStart.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
 # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# Ending Routine "instructions"
for thisComponent in instructsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructText.started', instructText.tStartRefresh)
thisExp.addData('instructText.stopped', instructText.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouseStart.started', mouseStart.tStart)
thisExp.addData('mouseStart.stopped', mouseStart.tStop)
thisExp.nextEntry()
# the Routine "instructs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # Prepare to start Routine "trial"
    continueRoutine = True
    routineTimer.add(2.200000)
    # update component parameters for each repeat
    cue.setOri(cueOri)
    target.setPos([targetX, 0])
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    keyPress.keys = []
    keyPress.rt = []
    _keyPress_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, cue, target, mouse, keyPress]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1



