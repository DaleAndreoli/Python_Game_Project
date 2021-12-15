#
# Description:
#   The parent class from which game events inherit. 
#   Establishes the execute method.
#
# OOP Principles Used:
#   Polymorphism
#
# Reasoning:
#   Polymorphism is used by the events that make up the game loop. 
#       They each implement different versions of the same .execute() method.
# 

class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")