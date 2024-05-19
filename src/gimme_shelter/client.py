"""Handle requests to the AA API."""

from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum
from typing import Self

from aleph_alpha_client import Client, CompletionRequest, Prompt

from gimme_shelter.interfaces import GenAIClient


class ModelNotFoundError(ValueError):
    """ModelNotFoundError is an exception that is raised when a model is not found."""


class TokenNotFoundError(ValueError):
    """TokenNotFoundError is an exception that is raised when a token is not found."""


@dataclass
class ModelInfo:
    """ModelInfo is a dataclass that stores information about a model.

    Args:
    ----
        id_name (str): The name of the model.
        display_name (str): The display name of the model.
        provider (str): The provider of the model.ß

    """

    id_name: str
    display_name: str
    provider: str


class AvailableModels(Enum):
    """AvailableModels is an enumeration that represents the available models."""

    LUMINOUS_BASE = ModelInfo(
        id_name="luminous-base",
        display_name="Luminous Base",
        provider="AlephAlpha",
    )
    LUMINOUS_BASE_CONTROL = ModelInfo(
        id_name="luminous-base-control",
        display_name="Luminous Base Control",
        provider="AlephAlpha",
    )
    LUMINOUS_EXTENDED = ModelInfo(
        id_name="luminous-extended",
        display_name="Luminous Extended",
        provider="AlephAlpha",
    )
    LUMINOUS_EXTENDED_CONTROL = ModelInfo(
        id_name="luminous-extended-control",
        display_name="Luminous Extended Control",
        provider="AlephAlpha",
    )
    LUMINOUS_SUPREME = ModelInfo(
        id_name="luminous-supreme",
        display_name="Luminous Supreme",
        provider="AlephAlpha",
    )
    LUMINOUS_SUPREME_CONTROL = ModelInfo(
        id_name="luminous-supreme-control",
        display_name="Luminous Supreme Control",
        provider="AlephAlpha",
    )


def produce_client(
    model: AvailableModels,
    secrets: Mapping[str, str] | None = None,
) -> GenAIClient:
    """Select the correct model from an input selection string."""
    match model.value:
        case ModelInfo(
            id_name=str(),
            display_name=str(),
            provider=str() as provider,
        ) if provider == "AlephAlpha":
            return AAClient(model=model.value, token=secrets["AA_TOKEN"])

        case _:
            raise ModelNotFoundError


class AAClient:
    """AAClient is a class that handles requests to the AA API.

    Args:
    ----
        model (ModelInfo, optional): The model to use for the request. Defaults to ModelInfo.LUMINOUS_BASE.
        max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 100.

    Attributes:
    ----------
        _client (Client): The client used to communicate with the AA API.
        _model (ModelInfo): The model used for the request.
        _max_tokens (int): The maximum number of tokens in the response.
        response (str | None): The response received from the AA API.


    """

    def __init__(
        self: Self,
        model: ModelInfo,
        token: str,
        max_tokens: int = 100,
    ) -> None:
        """Initialize a new instance of the AAClient class.

        Args:
        ----
            model (ModelInfo, optional): The model to use for the request. Defaults to ModelInfo.LUMINOUS_BASE.
            token (str): The API token for authentication.
            max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 100.

        """
        self._client = Client(token=token)
        self.model = model
        self._max_tokens = max_tokens
        self.response: str | None = None

    def request(self: Self, prompt: str) -> None:
        """Send a request to the AA API and get the response.

        Args:
        ----
            prompt (str): The input text for the request.

        """
        request = CompletionRequest(
            prompt=Prompt.from_text(prompt),
            maximum_tokens=self._max_tokens,
        )
        response = self._client.complete(request=request, model=self.model.id_name)
        self.response = response.completions[0].completion
