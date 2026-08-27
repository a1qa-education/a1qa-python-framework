from enum import Enum


class MainPageNavigation(Enum):
    """Sections available in the main navigation menu of timeanddate.com."""
    NEWS = "News"
    WORLD_CLOCK = "World Clock"
    TIME_ZONES = "Time Zones"
    CALENDAR = "Calendar"
    WEATHER = "Weather"
    SUN_MOON_SPACE = "Sun, Moon & Space"
    TIMERS = "Timers"
    CALCULATORS = "Calculators"

    @classmethod
    def from_label(cls, label: str) -> "MainPageNavigation":
        """
        Resolve an enum member by its visible label.

        :param label: Text of the navigation link as rendered on the page.
        :return: Matching enum member.
        """
        for section in cls:
            if section.value == label:
                return section
        raise ValueError(f"Unknown main page navigation section: '{label}'")
