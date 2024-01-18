class States:
    ACCEPT, REJECT = 201, 202
    UNDEFINED, STOP = 304, 305
    S = 101

    D, DM, DMY = 401, 402, 403
    Y, YM, YMD = 501, 502, 503


class Event:
    ACCEPT, REJECT = 'ACCEPT','REJECT'
    D, Y = 'DAY', 'YEAR'
    M, MD, MR,  = 'Month', 'MonthDigit', 'MonthRoman'


class Action:
    @staticmethod
    def reject():
        return Event.REJECT

    @staticmethod
    def end():
        return Event.END


class FSM:
    def __init__(self, *, routes=None, action=None, correct=Event.ACCEPT):
        self.routes = routes or []
        self.state = States.S
        self.action = action
        self.stop = States.STOP
        self.correct = correct
        self.counter = 0

    def run(self):
        while self.state != self.stop:
            stop = True
            event = self.action() if self.action else None
            event = self.checkEvent(event)

            for route in self.routes:
                if self.state == route['currState'] and event == route['event']:
                    stop = False
                    self.state, self.action = route['newState'], route['action']
                    break
            
            if stop:
                for route in self.routes:
                    if self.state == route['currState'] and event == None:
                        self.state, self.action = route['newState'], route['action']
                        break

    def checkEvent(self, event):
        if event not in self.correct:
            return None
        if event == Event.ACCEPT:
            self.counter += 1
        return event