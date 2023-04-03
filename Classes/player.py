from dataclasses import dataclass
from Mixins.GetChoiceMixin import GetChoiceMixin

@dataclass(order=True)
class Player(GetChoiceMixin):
    _wins: int 
    _current_choice: str

    @property
    def wins(self) -> int:
        return self._wins

    @wins.setter
    def wins(self, v: int) -> None:
        self._wins = v

    
    @property
    def current_choice(self) -> str:
        return self._current_choice

    @current_choice.setter
    def wins(self, v: str) -> None:
        self._current_choice = v