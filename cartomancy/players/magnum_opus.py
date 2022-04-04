"""
This file should contain the definition of class <game_name>Player
where <game_name> should be CamelCase.
"""

from cartomancy.players.base import Player
from cartomancy.games.go_fish.card import CARD_FIELD_VALUES
from cartomancy.games.core.events import ExchangeEvent, BookEvent, FailEvent, DrawEvent


class MagnumOpusPlayer(Player):
    """A magnum opus players class."""
    GAME = 'MagnumOpusPlayer'

    def __init__(self, name):
        super().__init__(name)
        self.is_out = False

    def set_alchemist(self, name):
        """set the alchemist into the alchemist zone."""
        pass
