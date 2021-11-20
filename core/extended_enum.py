from __future__ import annotations # allows self-reference in class
from enum import Enum
from typing import Tuple


class ExtendedEnum(Enum):

	@classmethod
	def list(cls) -> list[Tuple[any, any]]:
		# the cls provides the members to map
		return list(map(lambda c: (c, c.value), cls))