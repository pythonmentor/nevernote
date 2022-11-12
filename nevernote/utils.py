from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import config


def timezone_now():
    """Retourne la dateet l'heure UTC actuelle."""
    return datetime.now(tz=timezone.utc)


def localtime(value=None, timezone=None):
    """Retourne la date et l'heure locale."""
    if value is None:
        value = now()
    if timezone is None:
        timezone = ZoneInfo(config.TIME_ZONE)

    return value.astimezone(tz=timezone)
