from dataclasses import dataclass


@dataclass
class SPINNER_TYPES:
    DOTS: str = "dots"


@dataclass
class SYMBOLS:
    TICK_BOX: str = "🗹"
    TICK: str = "✓"


@dataclass
class COLORS:
    GREEN = "green"


@dataclass
class MonitorConfig:
    """Configuration class for the Monitor. Mainly handle visual settings."""

    spinner_type: str = SPINNER_TYPES.DOTS
    end_color: str = COLORS.GREEN
    context_manager_name: str = "Context manager"
    end_symbol: str = SYMBOLS.TICK_BOX
    offset: int = 1
