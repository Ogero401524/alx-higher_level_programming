#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, name, value):
        """
        Prevents creation of any attribute other than 'first_name'.
        Raises AttributeError if an attempt is made to set an attribute 
        with a name other than 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)
