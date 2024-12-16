# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import cart, cards, users, emails, orders, products, addresses, subscriptions
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import TerminalError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Terminal",
    "AsyncTerminal",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.terminal.shop/",
    "sandbox": "https://sandbox.terminal.shop/",
}


class Terminal(SyncAPIClient):
    products: products.ProductsResource
    users: users.UsersResource
    addresses: addresses.AddressesResource
    cards: cards.CardsResource
    cart: cart.CartResource
    orders: orders.OrdersResource
    subscriptions: subscriptions.SubscriptionsResource
    emails: emails.EmailsResource
    with_raw_response: TerminalWithRawResponse
    with_streaming_response: TerminalWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous terminal client instance.

        This automatically infers the `bearer_token` argument from the `TERMINAL_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TERMINAL_BEARER_TOKEN")
        if bearer_token is None:
            raise TerminalError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TERMINAL_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TERMINAL_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TERMINAL_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.products = products.ProductsResource(self)
        self.users = users.UsersResource(self)
        self.addresses = addresses.AddressesResource(self)
        self.cards = cards.CardsResource(self)
        self.cart = cart.CartResource(self)
        self.orders = orders.OrdersResource(self)
        self.subscriptions = subscriptions.SubscriptionsResource(self)
        self.emails = emails.EmailsResource(self)
        self.with_raw_response = TerminalWithRawResponse(self)
        self.with_streaming_response = TerminalWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTerminal(AsyncAPIClient):
    products: products.AsyncProductsResource
    users: users.AsyncUsersResource
    addresses: addresses.AsyncAddressesResource
    cards: cards.AsyncCardsResource
    cart: cart.AsyncCartResource
    orders: orders.AsyncOrdersResource
    subscriptions: subscriptions.AsyncSubscriptionsResource
    emails: emails.AsyncEmailsResource
    with_raw_response: AsyncTerminalWithRawResponse
    with_streaming_response: AsyncTerminalWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async terminal client instance.

        This automatically infers the `bearer_token` argument from the `TERMINAL_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TERMINAL_BEARER_TOKEN")
        if bearer_token is None:
            raise TerminalError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TERMINAL_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TERMINAL_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TERMINAL_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.products = products.AsyncProductsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.addresses = addresses.AsyncAddressesResource(self)
        self.cards = cards.AsyncCardsResource(self)
        self.cart = cart.AsyncCartResource(self)
        self.orders = orders.AsyncOrdersResource(self)
        self.subscriptions = subscriptions.AsyncSubscriptionsResource(self)
        self.emails = emails.AsyncEmailsResource(self)
        self.with_raw_response = AsyncTerminalWithRawResponse(self)
        self.with_streaming_response = AsyncTerminalWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TerminalWithRawResponse:
    def __init__(self, client: Terminal) -> None:
        self.products = products.ProductsResourceWithRawResponse(client.products)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.addresses = addresses.AddressesResourceWithRawResponse(client.addresses)
        self.cards = cards.CardsResourceWithRawResponse(client.cards)
        self.cart = cart.CartResourceWithRawResponse(client.cart)
        self.orders = orders.OrdersResourceWithRawResponse(client.orders)
        self.subscriptions = subscriptions.SubscriptionsResourceWithRawResponse(client.subscriptions)
        self.emails = emails.EmailsResourceWithRawResponse(client.emails)


class AsyncTerminalWithRawResponse:
    def __init__(self, client: AsyncTerminal) -> None:
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.addresses = addresses.AsyncAddressesResourceWithRawResponse(client.addresses)
        self.cards = cards.AsyncCardsResourceWithRawResponse(client.cards)
        self.cart = cart.AsyncCartResourceWithRawResponse(client.cart)
        self.orders = orders.AsyncOrdersResourceWithRawResponse(client.orders)
        self.subscriptions = subscriptions.AsyncSubscriptionsResourceWithRawResponse(client.subscriptions)
        self.emails = emails.AsyncEmailsResourceWithRawResponse(client.emails)


class TerminalWithStreamedResponse:
    def __init__(self, client: Terminal) -> None:
        self.products = products.ProductsResourceWithStreamingResponse(client.products)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.addresses = addresses.AddressesResourceWithStreamingResponse(client.addresses)
        self.cards = cards.CardsResourceWithStreamingResponse(client.cards)
        self.cart = cart.CartResourceWithStreamingResponse(client.cart)
        self.orders = orders.OrdersResourceWithStreamingResponse(client.orders)
        self.subscriptions = subscriptions.SubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.emails = emails.EmailsResourceWithStreamingResponse(client.emails)


class AsyncTerminalWithStreamedResponse:
    def __init__(self, client: AsyncTerminal) -> None:
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.addresses = addresses.AsyncAddressesResourceWithStreamingResponse(client.addresses)
        self.cards = cards.AsyncCardsResourceWithStreamingResponse(client.cards)
        self.cart = cart.AsyncCartResourceWithStreamingResponse(client.cart)
        self.orders = orders.AsyncOrdersResourceWithStreamingResponse(client.orders)
        self.subscriptions = subscriptions.AsyncSubscriptionsResourceWithStreamingResponse(client.subscriptions)
        self.emails = emails.AsyncEmailsResourceWithStreamingResponse(client.emails)


Client = Terminal

AsyncClient = AsyncTerminal
