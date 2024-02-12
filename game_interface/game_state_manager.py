class GameStateManager:
    """
    This class handles the current state of the game.

    Attributes
    ----------
    current_state (str): string that contains the current state of the game
    """

    def __init__(self, current_state):
        """
        Initializes the GameSateManager class.

        Parameters
        ----------
        current_state (str): string that contains the current state of the game.
        """
        self.current_state = current_state

    def get_state(self):
        """
        Retrieves the current state the game is in.
        """
        return self.current_state

    def set_state(self, state):
        """
        Sets the game state to the string given in the 'state' parameter.
        """
        self.current_state = state
