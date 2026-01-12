from typing import List

# =====================
# Version information
# =====================
__version__ = "0.1.0"
__author__ = "Calculator Microservice Team"

# =====================
# Public imports
# =====================
from .calculator import add, subtract, multiply, divide
from .logger import get_logger

# =====================
# Public API
# =====================
__all__: List[str] = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "get_logger",
    "__version__",
]

def get_version() -> str:
    """
    Return the package version.

    :return: The package version string.
    :rtype: str
    """
    return __version__


# =====================
# Package initialization log
# =====================
_logger = get_logger("calculator_service")
_logger.info("Calculator Microservice v%s initialized", __version__)
