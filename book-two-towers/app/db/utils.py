from typing import Any


def convert_str_to_int(value: Any) -> int | None:
    match value:
        case str():
            try:
                return int(value)
            except Exception:
                return None
        case _:
            return None
