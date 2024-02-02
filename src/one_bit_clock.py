from semantics import Semantics


class OneBitClock(Semantics):
    def initial(self):
        return [0, 1]

    def actions(self, configuration):
        action = []
        if configuration == 1:
            action.append(lambda x: [0])
        elif configuration == 0:
            action.append(lambda x: [1])
        return action

    def execute(self, action, configuration):
        return action(configuration)
