import logging

from datetime import datetime

from typing import Optional
from typing import Union
from typing import List

logger = logging.getLogger(__name__)


def safe_datetime_to_iso(d: str, input_format: Union[List[str], str]) -> Optional[str]:
    """
    Given an input datetime representation `d`
    parses and returns the isoformat representation

    `input_format` can be a `format` or a `[format]`; in the later
    case we try every one and return the first matching
    """

    if isinstance(input_format, str):
        input_format = [input_format]

    timestamp = None
    for format in input_format:
        try:
            timestamp = datetime.strptime(d, format).isoformat()
            logger.debug(f"datetime '{d}' has format '{format}'")
            break
        except Exception as e:
            timestamp = None

    return timestamp

