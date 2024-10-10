#!/usr/bin/python3
"""
This module contains the canUnlockAll function that checks
if all boxes can be unlocked given a list of keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.
    
    Parameters:
    boxes (list of lists): List where each sublist contains keys to other boxes.
    
    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the first box's key
    
    while keys:
        current_key = keys.pop(0)
        
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)
