compass = {'N': 0, 'NE': 45,
           'E': 90, 'SE': 135,
           'S': 180, 'SW': 225,
           'W': 270, 'NW': 315, }
compass_negative = {'N': 0, 'NE': -315,
           'E': -270, 'SE': -225,
           'S': -180, 'SW': -135,
           'W': -90, 'NW': -45, }


def direction(facing, turn):
    if turn > 0:
        new_turn = (compass.get(facing) + turn)
        while new_turn >= 360:
            new_turn -= 360
        for facing_in_compass, turn_in_compass in compass.items():
            if turn_in_compass == new_turn:
                return facing_in_compass
    else:
        if compass.get(facing) + turn > 0:
            new_turn = (compass.get(facing) + turn)
            for facing_in_compass, turn_in_compass in compass.items():
                if turn_in_compass == new_turn:
                    return facing_in_compass
        else:
            while turn <= -360:
                turn += 360
            if turn == 0:
                return facing
            if compass.get(facing) + turn > 0:
                new_turn = (compass.get(facing) + turn)
                for facing_in_compass, turn_in_compass in compass.items():
                    if turn_in_compass == new_turn:
                        return facing_in_compass
            new_turn = (compass.get(facing) + turn)
            for facing_in_compass, turn_in_compass in compass_negative.items():
                if turn_in_compass == new_turn:
                    return facing_in_compass
