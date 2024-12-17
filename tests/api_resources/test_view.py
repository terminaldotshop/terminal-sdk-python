# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import ViewInitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestView:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_init(self, client: Terminal) -> None:
        view = client.view.init()
        assert_matches_type(ViewInitResponse, view, path=["response"])

    @parametrize
    def test_raw_response_init(self, client: Terminal) -> None:
        response = client.view.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewInitResponse, view, path=["response"])

    @parametrize
    def test_streaming_response_init(self, client: Terminal) -> None:
        with client.view.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewInitResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncView:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_init(self, async_client: AsyncTerminal) -> None:
        view = await async_client.view.init()
        assert_matches_type(ViewInitResponse, view, path=["response"])

    @parametrize
    async def test_raw_response_init(self, async_client: AsyncTerminal) -> None:
        response = await async_client.view.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewInitResponse, view, path=["response"])

    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncTerminal) -> None:
        async with async_client.view.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewInitResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True
