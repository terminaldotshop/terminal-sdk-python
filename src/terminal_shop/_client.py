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
from .resources import app, card, cart, view, email, order, token, address, product, profile, subscription
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
    "dev": "https://api.dev.terminal.shop/",
}


class Terminal(SyncAPIClient):
    product: product.ProductResource
    profile: profile.ProfileResource
    address: address.AddressResource
    card: card.CardResource
    cart: cart.CartResource
    order: order.OrderResource
    subscription: subscription.SubscriptionResource
    token: token.TokenResource
    app: app.AppResource
    email: email.EmailResource
    view: view.ViewResource
    with_raw_response: TerminalWithRawResponse
    with_streaming_response: TerminalWithStreamedResponse

    # client options
    bearer_token: str
    app_id: str | None

    _environment: Literal["production", "dev"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | NotGiven = NOT_GIVEN,
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
        """Construct a new synchronous Terminal client instance.

        This automatically infers the `bearer_token` argument from the `TERMINAL_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TERMINAL_BEARER_TOKEN")
        if bearer_token is None:
            raise TerminalError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TERMINAL_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self.app_id = app_id

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

        self.product = product.ProductResource(self)
        self.profile = profile.ProfileResource(self)
        self.address = address.AddressResource(self)
        self.card = card.CardResource(self)
        self.cart = cart.CartResource(self)
        self.order = order.OrderResource(self)
        self.subscription = subscription.SubscriptionResource(self)
        self.token = token.TokenResource(self)
        self.app = app.AppResource(self)
        self.email = email.EmailResource(self)
        self.view = view.ViewResource(self)
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
            "x-terminal-app-id": self.app_id if self.app_id is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | None = None,
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
            app_id=app_id or self.app_id,
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
    product: product.AsyncProductResource
    profile: profile.AsyncProfileResource
    address: address.AsyncAddressResource
    card: card.AsyncCardResource
    cart: cart.AsyncCartResource
    order: order.AsyncOrderResource
    subscription: subscription.AsyncSubscriptionResource
    token: token.AsyncTokenResource
    app: app.AsyncAppResource
    email: email.AsyncEmailResource
    view: view.AsyncViewResource
    with_raw_response: AsyncTerminalWithRawResponse
    with_streaming_response: AsyncTerminalWithStreamedResponse

    # client options
    bearer_token: str
    app_id: str | None

    _environment: Literal["production", "dev"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | NotGiven = NOT_GIVEN,
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
        """Construct a new async AsyncTerminal client instance.

        This automatically infers the `bearer_token` argument from the `TERMINAL_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TERMINAL_BEARER_TOKEN")
        if bearer_token is None:
            raise TerminalError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TERMINAL_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self.app_id = app_id

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

        self.product = product.AsyncProductResource(self)
        self.profile = profile.AsyncProfileResource(self)
        self.address = address.AsyncAddressResource(self)
        self.card = card.AsyncCardResource(self)
        self.cart = cart.AsyncCartResource(self)
        self.order = order.AsyncOrderResource(self)
        self.subscription = subscription.AsyncSubscriptionResource(self)
        self.token = token.AsyncTokenResource(self)
        self.app = app.AsyncAppResource(self)
        self.email = email.AsyncEmailResource(self)
        self.view = view.AsyncViewResource(self)
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
            "x-terminal-app-id": self.app_id if self.app_id is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | None = None,
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
            app_id=app_id or self.app_id,
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
        self.product = product.ProductResourceWithRawResponse(client.product)
        self.profile = profile.ProfileResourceWithRawResponse(client.profile)
        self.address = address.AddressResourceWithRawResponse(client.address)
        self.card = card.CardResourceWithRawResponse(client.card)
        self.cart = cart.CartResourceWithRawResponse(client.cart)
        self.order = order.OrderResourceWithRawResponse(client.order)
        self.subscription = subscription.SubscriptionResourceWithRawResponse(client.subscription)
        self.token = token.TokenResourceWithRawResponse(client.token)
        self.app = app.AppResourceWithRawResponse(client.app)
        self.email = email.EmailResourceWithRawResponse(client.email)
        self.view = view.ViewResourceWithRawResponse(client.view)


class AsyncTerminalWithRawResponse:
    def __init__(self, client: AsyncTerminal) -> None:
        self.product = product.AsyncProductResourceWithRawResponse(client.product)
        self.profile = profile.AsyncProfileResourceWithRawResponse(client.profile)
        self.address = address.AsyncAddressResourceWithRawResponse(client.address)
        self.card = card.AsyncCardResourceWithRawResponse(client.card)
        self.cart = cart.AsyncCartResourceWithRawResponse(client.cart)
        self.order = order.AsyncOrderResourceWithRawResponse(client.order)
        self.subscription = subscription.AsyncSubscriptionResourceWithRawResponse(client.subscription)
        self.token = token.AsyncTokenResourceWithRawResponse(client.token)
        self.app = app.AsyncAppResourceWithRawResponse(client.app)
        self.email = email.AsyncEmailResourceWithRawResponse(client.email)
        self.view = view.AsyncViewResourceWithRawResponse(client.view)


class TerminalWithStreamedResponse:
    def __init__(self, client: Terminal) -> None:
        self.product = product.ProductResourceWithStreamingResponse(client.product)
        self.profile = profile.ProfileResourceWithStreamingResponse(client.profile)
        self.address = address.AddressResourceWithStreamingResponse(client.address)
        self.card = card.CardResourceWithStreamingResponse(client.card)
        self.cart = cart.CartResourceWithStreamingResponse(client.cart)
        self.order = order.OrderResourceWithStreamingResponse(client.order)
        self.subscription = subscription.SubscriptionResourceWithStreamingResponse(client.subscription)
        self.token = token.TokenResourceWithStreamingResponse(client.token)
        self.app = app.AppResourceWithStreamingResponse(client.app)
        self.email = email.EmailResourceWithStreamingResponse(client.email)
        self.view = view.ViewResourceWithStreamingResponse(client.view)


class AsyncTerminalWithStreamedResponse:
    def __init__(self, client: AsyncTerminal) -> None:
        self.product = product.AsyncProductResourceWithStreamingResponse(client.product)
        self.profile = profile.AsyncProfileResourceWithStreamingResponse(client.profile)
        self.address = address.AsyncAddressResourceWithStreamingResponse(client.address)
        self.card = card.AsyncCardResourceWithStreamingResponse(client.card)
        self.cart = cart.AsyncCartResourceWithStreamingResponse(client.cart)
        self.order = order.AsyncOrderResourceWithStreamingResponse(client.order)
        self.subscription = subscription.AsyncSubscriptionResourceWithStreamingResponse(client.subscription)
        self.token = token.AsyncTokenResourceWithStreamingResponse(client.token)
        self.app = app.AsyncAppResourceWithStreamingResponse(client.app)
        self.email = email.AsyncEmailResourceWithStreamingResponse(client.email)
        self.view = view.AsyncViewResourceWithStreamingResponse(client.view)


Client = Terminal

AsyncClient = AsyncTerminal
