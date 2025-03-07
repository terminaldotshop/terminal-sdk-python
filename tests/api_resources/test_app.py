# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import AppGetResponse, AppListResponse, AppCreateResponse, AppDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Terminal) -> None:
        app = client.app.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Terminal) -> None:
        response = client.app.with_raw_response.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Terminal) -> None:
        with client.app.with_streaming_response.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Terminal) -> None:
        app = client.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Terminal) -> None:
        response = client.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Terminal) -> None:
        with client.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Terminal) -> None:
        app = client.app.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Terminal) -> None:
        response = client.app.with_raw_response.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Terminal) -> None:
        with client.app.with_streaming_response.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.app.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Terminal) -> None:
        app = client.app.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Terminal) -> None:
        response = client.app.with_raw_response.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Terminal) -> None:
        with client.app.with_streaming_response.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.app.with_raw_response.get(
                "",
            )


class TestAsyncApp:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTerminal) -> None:
        app = await async_client.app.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTerminal) -> None:
        response = await async_client.app.with_raw_response.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTerminal) -> None:
        async with async_client.app.with_streaming_response.create(
            name="Example App",
            redirect_uri="https://example.com/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTerminal) -> None:
        app = await async_client.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTerminal) -> None:
        response = await async_client.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTerminal) -> None:
        async with async_client.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTerminal) -> None:
        app = await async_client.app.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTerminal) -> None:
        response = await async_client.app.with_raw_response.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTerminal) -> None:
        async with async_client.app.with_streaming_response.delete(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.app.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncTerminal) -> None:
        app = await async_client.app.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTerminal) -> None:
        response = await async_client.app.with_raw_response.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTerminal) -> None:
        async with async_client.app.with_streaming_response.get(
            "cli_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.app.with_raw_response.get(
                "",
            )
