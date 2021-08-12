import dataclasses

from .board import Base

@dataclasses.dataclass
class NeoPixel:
    board: Base
    lights_count: int