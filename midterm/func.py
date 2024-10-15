#!/usr/bin/env python3
"""
func.py
Author: Tandin

This module contains the function has_bad_chars, which checks if a string contains either dashes (-) or dots (.).
"""

def has_bad_chars(target: str) -> bool:
    """
    Checks if the input string contains either dashes (-) or dots (.).
    
    Args:
        target (str): The string to check.
    
    Returns:
        bool: True if the string contains either '-' or '.', otherwise False.
    """
    return '-' in target or '.' in target
