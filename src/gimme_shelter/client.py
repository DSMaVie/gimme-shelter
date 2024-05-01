"""Handle requests to the AA API."""

import os
from enum import StrEnum
from typing import Self

from aleph_alpha_client import Client, CompletionRequest, Prompt

from gimme_shelter.interfaces import GenAIClient


def produce_client(selection: str) -> GenAIClient:
    """Select the correct model from an input selection string."""
    raise NotImplementedError


class AAModel(StrEnum):
    """Enumeration of AA models."""

    BASE = "luminous-base"


class AARequester:
    """AARequester is a class that handles requests to the AA API.

    Args:
    ----
        model (AAModel, optional): The model to use for the request. Defaults to AAModel.BASE.
        max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 100.

    Attributes:
    ----------
        _client (Client): The client used to communicate with the AA API.
        _model (AAModel): The model used for the request.
        _max_tokens (int): The maximum number of tokens in the response.
        response (str | None): The response received from the AA API.


    """

    def __init__(
        self: Self,
        model: AAModel = AAModel.BASE,
        max_tokens: int = 100,
    ) -> None:
        """Initialize a new instance of the AARequester class.

        Args:
        ----
            model (AAModel, optional): The model to use for the request. Defaults to AAModel.BASE.
            max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 100.

        """
        self._client = Client(token=os.getenv("AA_TOKEN"))
        self._model = model
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
            maximum_tokens=self.max_tokens,
        )
        response = self._client.complete(request=request, model=self._model)

        self.response = response.completions[0].completion
