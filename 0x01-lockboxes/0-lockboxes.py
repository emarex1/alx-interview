#!/usr/bin/python3
""" method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        """ outer loop """
        if not box:
            continue
        for key in box:
            """ inner loop """
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False