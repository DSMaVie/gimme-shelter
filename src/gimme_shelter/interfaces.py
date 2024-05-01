"""A collection of interfaces for Structural Subtyping to be used in the server func."""

from collections.abc import Collection
from typing import Protocol, Self


class PromptSetting[T](Protocol):
    """Interface that defines how settings are handled."""

    @property
    def description(self: Self) -> str:
        """A Description for the GenAI model to use."""

    @property
    def selection_values(self: Self) -> Collection[T]:
        """The list of possible values."""

    def parse_selection(self: Self, selection: T) -> str:
        """Parse a selection so that the model understands it."""


class GenAIClient(Protocol):
    """Handles the request to a GenAIModel to generate."""

    def request(self: Self, prompt: str) -> str:
        """Send the prompot to the Model and extract string answer."""
