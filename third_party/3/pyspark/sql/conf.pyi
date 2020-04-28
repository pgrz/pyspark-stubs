# Stubs for pyspark.sql.conf (Python 3.5)
#

from typing import Any, Optional
from py4j.java_gateway import JavaObject  # type: ignore[import]

class RuntimeConfig:
    def __init__(self, jconf: JavaObject) -> None: ...
    def set(self, key: str, value: str) -> str: ...
    def get(self, key: str, default: Optional[str] = ...) -> str: ...
    def unset(self, key: str) -> None: ...
    def isModifiable(self, key: str) -> bool: ...
