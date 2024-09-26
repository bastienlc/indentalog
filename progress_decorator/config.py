from dataclasses import dataclass


@dataclass
class MonitorConfig:
    """Configuration class for the Monitor. Mainly handle visual settings."""

    spinner_type: str = "dots"
    end_color: str = "green"
    end_symbol: str = "✔"
    context_manager_name: str = "Context manager"
