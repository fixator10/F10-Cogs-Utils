import datetime
from enum import Enum


class TimestampStyle(Enum):
    time_short = "t"  # 16:20
    time_long = "T"  # 16:20:30
    date_short = "d"  # 20/04/2021
    date_long = "D"  # 20 April 2021
    datetime_short = "f"  # 20 April 2021 16:20 :: default
    datetime_long = "F"  # Tuesday, 20 April 2021 16:20
    relative = "R"  # 2 months ago


def get_markdown_timestamp(timestamp: datetime.datetime, style: TimestampStyle = None) -> str:
    timestamp = timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
    return f"<t:{timestamp:.0f}:{style.value}>" if style else f"<t:{timestamp:.0f}>"
