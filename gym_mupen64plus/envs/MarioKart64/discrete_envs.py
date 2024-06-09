import abc
from gym_mupen64plus.envs.MarioKart64.mario_kart_env import MarioKartEnv
from gym import spaces

class DiscreteActions:
    ACTION_MAP = [
        ("NO_OP", [0, 0, 0, 0, 0, 0, 0]),
        ("ITEMS", [0, 0, 1, 0, 0, 0, 1]),
        ("REVERSE", [0, -80, 0, 1, 0, 0, 0]),
        ("STRAIGHT", [0, 0, 1, 0, 0, 0, 0]),
    ]

    for i in range(79):
        ACTION_MAP.append(("r " + str(i), [i+1, 0, 1, 0, 0, 0, 0]));
        ACTION_MAP.append(("l " + str(i), [-i-1, 0, 1, 0, 0, 0, 0]));
        if i > 20:
            ACTION_MAP.append(("rd " + str(i), [i+1, 0, 1, 0, 1, 0, 0]));
            ACTION_MAP.append(("ld " + str(i), [-i-1, 0, 1, 0, 1, 0, 0]));




    @staticmethod
    def get_action_space():
        return spaces.Discrete(len(DiscreteActions.ACTION_MAP))

    @staticmethod
    def get_controls_from_action(action):
        return DiscreteActions.ACTION_MAP[action][1]


class MarioKartDiscreteEnv(MarioKartEnv):

    ENABLE_CHECKPOINTS = True

    def __init__(self, character='mario', course='LuigiRaceway'):
        super(MarioKartDiscreteEnv, self).__init__(character=character, course=course)

        # This needs to happen after the parent class init to effectively override the action space
        self.action_space = DiscreteActions.get_action_space()

    def _step(self, action):
        # Interpret the action choice and get the actual controller state for this step
        controls = DiscreteActions.get_controls_from_action(action)

        return super(MarioKartDiscreteEnv, self)._step(controls)
