import datetime
from enum import Enum


class TimestampStyle(Enum):
    time_short = "t"
    time_long = "T"
    date_short = "d"
    date_long = "D"
    datetime_short = "f"
    datetime_long = "F"
    relative = "R"


def get_markdown_timestamp(timestamp: datetime.datetime, style: TimestampStyle = TimestampStyle.datetime_short):
    timestamp = timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
    return f"<t:{timestamp:.0f}:{style.value}>"
