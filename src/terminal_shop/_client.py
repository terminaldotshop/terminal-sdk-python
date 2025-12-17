# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import TerminalError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import app, card, cart, view, email, order, token, address, product, profile, subscription
    from .resources.app import AppResource, AsyncAppResource
    from .resources.card import CardResource, AsyncCardResource
    from .resources.cart import CartResource, AsyncCartResource
    from .resources.view import ViewResource, AsyncViewResource
    from .resources.email import EmailResource, AsyncEmailResource
    from .resources.order import OrderResource, AsyncOrderResource
    from .resources.token import TokenResource, AsyncTokenResource
    from .resources.address import AddressResource, AsyncAddressResource
    from .resources.product import ProductResource, AsyncProductResource
    from .resources.profile import ProfileResource, AsyncProfileResource
    from .resources.subscription import SubscriptionResource, AsyncSubscriptionResource

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
    "production": "https://api.terminal.shop",
    "dev": "https://api.dev.terminal.shop",
}


class Terminal(SyncAPIClient):
    # client options
    bearer_token: str
    app_id: str | None

    _environment: Literal["production", "dev"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def product(self) -> ProductResource:
        from .resources.product import ProductResource

        return ProductResource(self)

    @cached_property
    def profile(self) -> ProfileResource:
        from .resources.profile import ProfileResource

        return ProfileResource(self)

    @cached_property
    def address(self) -> AddressResource:
        from .resources.address import AddressResource

        return AddressResource(self)

    @cached_property
    def card(self) -> CardResource:
        from .resources.card import CardResource

        return CardResource(self)

    @cached_property
    def cart(self) -> CartResource:
        from .resources.cart import CartResource

        return CartResource(self)

    @cached_property
    def order(self) -> OrderResource:
        from .resources.order import OrderResource

        return OrderResource(self)

    @cached_property
    def subscription(self) -> SubscriptionResource:
        from .resources.subscription import SubscriptionResource

        return SubscriptionResource(self)

    @cached_property
    def token(self) -> TokenResource:
        from .resources.token import TokenResource

        return TokenResource(self)

    @cached_property
    def app(self) -> AppResource:
        from .resources.app import AppResource

        return AppResource(self)

    @cached_property
    def email(self) -> EmailResource:
        from .resources.email import EmailResource

        return EmailResource(self)

    @cached_property
    def view(self) -> ViewResource:
        from .resources.view import ViewResource

        return ViewResource(self)

    @cached_property
    def with_raw_response(self) -> TerminalWithRawResponse:
        return TerminalWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TerminalWithStreamedResponse:
        return TerminalWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    bearer_token: str
    app_id: str | None

    _environment: Literal["production", "dev"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        app_id: str | None = None,
        environment: Literal["production", "dev"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def product(self) -> AsyncProductResource:
        from .resources.product import AsyncProductResource

        return AsyncProductResource(self)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        from .resources.profile import AsyncProfileResource

        return AsyncProfileResource(self)

    @cached_property
    def address(self) -> AsyncAddressResource:
        from .resources.address import AsyncAddressResource

        return AsyncAddressResource(self)

    @cached_property
    def card(self) -> AsyncCardResource:
        from .resources.card import AsyncCardResource

        return AsyncCardResource(self)

    @cached_property
    def cart(self) -> AsyncCartResource:
        from .resources.cart import AsyncCartResource

        return AsyncCartResource(self)

    @cached_property
    def order(self) -> AsyncOrderResource:
        from .resources.order import AsyncOrderResource

        return AsyncOrderResource(self)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        from .resources.subscription import AsyncSubscriptionResource

        return AsyncSubscriptionResource(self)

    @cached_property
    def token(self) -> AsyncTokenResource:
        from .resources.token import AsyncTokenResource

        return AsyncTokenResource(self)

    @cached_property
    def app(self) -> AsyncAppResource:
        from .resources.app import AsyncAppResource

        return AsyncAppResource(self)

    @cached_property
    def email(self) -> AsyncEmailResource:
        from .resources.email import AsyncEmailResource

        return AsyncEmailResource(self)

    @cached_property
    def view(self) -> AsyncViewResource:
        from .resources.view import AsyncViewResource

        return AsyncViewResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTerminalWithRawResponse:
        return AsyncTerminalWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTerminalWithStreamedResponse:
        return AsyncTerminalWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Terminal

    def __init__(self, client: Terminal) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.ProductResourceWithRawResponse:
        from .resources.product import ProductResourceWithRawResponse

        return ProductResourceWithRawResponse(self._client.product)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithRawResponse:
        from .resources.profile import ProfileResourceWithRawResponse

        return ProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def address(self) -> address.AddressResourceWithRawResponse:
        from .resources.address import AddressResourceWithRawResponse

        return AddressResourceWithRawResponse(self._client.address)

    @cached_property
    def card(self) -> card.CardResourceWithRawResponse:
        from .resources.card import CardResourceWithRawResponse

        return CardResourceWithRawResponse(self._client.card)

    @cached_property
    def cart(self) -> cart.CartResourceWithRawResponse:
        from .resources.cart import CartResourceWithRawResponse

        return CartResourceWithRawResponse(self._client.cart)

    @cached_property
    def order(self) -> order.OrderResourceWithRawResponse:
        from .resources.order import OrderResourceWithRawResponse

        return OrderResourceWithRawResponse(self._client.order)

    @cached_property
    def subscription(self) -> subscription.SubscriptionResourceWithRawResponse:
        from .resources.subscription import SubscriptionResourceWithRawResponse

        return SubscriptionResourceWithRawResponse(self._client.subscription)

    @cached_property
    def token(self) -> token.TokenResourceWithRawResponse:
        from .resources.token import TokenResourceWithRawResponse

        return TokenResourceWithRawResponse(self._client.token)

    @cached_property
    def app(self) -> app.AppResourceWithRawResponse:
        from .resources.app import AppResourceWithRawResponse

        return AppResourceWithRawResponse(self._client.app)

    @cached_property
    def email(self) -> email.EmailResourceWithRawResponse:
        from .resources.email import EmailResourceWithRawResponse

        return EmailResourceWithRawResponse(self._client.email)

    @cached_property
    def view(self) -> view.ViewResourceWithRawResponse:
        from .resources.view import ViewResourceWithRawResponse

        return ViewResourceWithRawResponse(self._client.view)


class AsyncTerminalWithRawResponse:
    _client: AsyncTerminal

    def __init__(self, client: AsyncTerminal) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.AsyncProductResourceWithRawResponse:
        from .resources.product import AsyncProductResourceWithRawResponse

        return AsyncProductResourceWithRawResponse(self._client.product)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithRawResponse:
        from .resources.profile import AsyncProfileResourceWithRawResponse

        return AsyncProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def address(self) -> address.AsyncAddressResourceWithRawResponse:
        from .resources.address import AsyncAddressResourceWithRawResponse

        return AsyncAddressResourceWithRawResponse(self._client.address)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithRawResponse:
        from .resources.card import AsyncCardResourceWithRawResponse

        return AsyncCardResourceWithRawResponse(self._client.card)

    @cached_property
    def cart(self) -> cart.AsyncCartResourceWithRawResponse:
        from .resources.cart import AsyncCartResourceWithRawResponse

        return AsyncCartResourceWithRawResponse(self._client.cart)

    @cached_property
    def order(self) -> order.AsyncOrderResourceWithRawResponse:
        from .resources.order import AsyncOrderResourceWithRawResponse

        return AsyncOrderResourceWithRawResponse(self._client.order)

    @cached_property
    def subscription(self) -> subscription.AsyncSubscriptionResourceWithRawResponse:
        from .resources.subscription import AsyncSubscriptionResourceWithRawResponse

        return AsyncSubscriptionResourceWithRawResponse(self._client.subscription)

    @cached_property
    def token(self) -> token.AsyncTokenResourceWithRawResponse:
        from .resources.token import AsyncTokenResourceWithRawResponse

        return AsyncTokenResourceWithRawResponse(self._client.token)

    @cached_property
    def app(self) -> app.AsyncAppResourceWithRawResponse:
        from .resources.app import AsyncAppResourceWithRawResponse

        return AsyncAppResourceWithRawResponse(self._client.app)

    @cached_property
    def email(self) -> email.AsyncEmailResourceWithRawResponse:
        from .resources.email import AsyncEmailResourceWithRawResponse

        return AsyncEmailResourceWithRawResponse(self._client.email)

    @cached_property
    def view(self) -> view.AsyncViewResourceWithRawResponse:
        from .resources.view import AsyncViewResourceWithRawResponse

        return AsyncViewResourceWithRawResponse(self._client.view)


class TerminalWithStreamedResponse:
    _client: Terminal

    def __init__(self, client: Terminal) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.ProductResourceWithStreamingResponse:
        from .resources.product import ProductResourceWithStreamingResponse

        return ProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithStreamingResponse:
        from .resources.profile import ProfileResourceWithStreamingResponse

        return ProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def address(self) -> address.AddressResourceWithStreamingResponse:
        from .resources.address import AddressResourceWithStreamingResponse

        return AddressResourceWithStreamingResponse(self._client.address)

    @cached_property
    def card(self) -> card.CardResourceWithStreamingResponse:
        from .resources.card import CardResourceWithStreamingResponse

        return CardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def cart(self) -> cart.CartResourceWithStreamingResponse:
        from .resources.cart import CartResourceWithStreamingResponse

        return CartResourceWithStreamingResponse(self._client.cart)

    @cached_property
    def order(self) -> order.OrderResourceWithStreamingResponse:
        from .resources.order import OrderResourceWithStreamingResponse

        return OrderResourceWithStreamingResponse(self._client.order)

    @cached_property
    def subscription(self) -> subscription.SubscriptionResourceWithStreamingResponse:
        from .resources.subscription import SubscriptionResourceWithStreamingResponse

        return SubscriptionResourceWithStreamingResponse(self._client.subscription)

    @cached_property
    def token(self) -> token.TokenResourceWithStreamingResponse:
        from .resources.token import TokenResourceWithStreamingResponse

        return TokenResourceWithStreamingResponse(self._client.token)

    @cached_property
    def app(self) -> app.AppResourceWithStreamingResponse:
        from .resources.app import AppResourceWithStreamingResponse

        return AppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def email(self) -> email.EmailResourceWithStreamingResponse:
        from .resources.email import EmailResourceWithStreamingResponse

        return EmailResourceWithStreamingResponse(self._client.email)

    @cached_property
    def view(self) -> view.ViewResourceWithStreamingResponse:
        from .resources.view import ViewResourceWithStreamingResponse

        return ViewResourceWithStreamingResponse(self._client.view)


class AsyncTerminalWithStreamedResponse:
    _client: AsyncTerminal

    def __init__(self, client: AsyncTerminal) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.AsyncProductResourceWithStreamingResponse:
        from .resources.product import AsyncProductResourceWithStreamingResponse

        return AsyncProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithStreamingResponse:
        from .resources.profile import AsyncProfileResourceWithStreamingResponse

        return AsyncProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def address(self) -> address.AsyncAddressResourceWithStreamingResponse:
        from .resources.address import AsyncAddressResourceWithStreamingResponse

        return AsyncAddressResourceWithStreamingResponse(self._client.address)

    @cached_property
    def card(self) -> card.AsyncCardResourceWithStreamingResponse:
        from .resources.card import AsyncCardResourceWithStreamingResponse

        return AsyncCardResourceWithStreamingResponse(self._client.card)

    @cached_property
    def cart(self) -> cart.AsyncCartResourceWithStreamingResponse:
        from .resources.cart import AsyncCartResourceWithStreamingResponse

        return AsyncCartResourceWithStreamingResponse(self._client.cart)

    @cached_property
    def order(self) -> order.AsyncOrderResourceWithStreamingResponse:
        from .resources.order import AsyncOrderResourceWithStreamingResponse

        return AsyncOrderResourceWithStreamingResponse(self._client.order)

    @cached_property
    def subscription(self) -> subscription.AsyncSubscriptionResourceWithStreamingResponse:
        from .resources.subscription import AsyncSubscriptionResourceWithStreamingResponse

        return AsyncSubscriptionResourceWithStreamingResponse(self._client.subscription)

    @cached_property
    def token(self) -> token.AsyncTokenResourceWithStreamingResponse:
        from .resources.token import AsyncTokenResourceWithStreamingResponse

        return AsyncTokenResourceWithStreamingResponse(self._client.token)

    @cached_property
    def app(self) -> app.AsyncAppResourceWithStreamingResponse:
        from .resources.app import AsyncAppResourceWithStreamingResponse

        return AsyncAppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def email(self) -> email.AsyncEmailResourceWithStreamingResponse:
        from .resources.email import AsyncEmailResourceWithStreamingResponse

        return AsyncEmailResourceWithStreamingResponse(self._client.email)

    @cached_property
    def view(self) -> view.AsyncViewResourceWithStreamingResponse:
        from .resources.view import AsyncViewResourceWithStreamingResponse

        return AsyncViewResourceWithStreamingResponse(self._client.view)


Client = Terminal

AsyncClient = AsyncTerminal
