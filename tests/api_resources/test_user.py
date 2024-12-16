# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from terminal import Terminal, AsyncTerminal
from tests.utils import assert_matches_type
from terminal.types import UserMeResponse, UserInitResponse, UserUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Terminal) -> None:
        user = client.user.update()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Terminal) -> None:
        user = client.user.update(
            email="john@example.com",
            name="John Doe",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Terminal) -> None:
        response = client.user.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Terminal) -> None:
        with client.user.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_init(self, client: Terminal) -> None:
        user = client.user.init()
        assert_matches_type(UserInitResponse, user, path=["response"])

    @parametrize
    def test_raw_response_init(self, client: Terminal) -> None:
        response = client.user.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserInitResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_init(self, client: Terminal) -> None:
        with client.user.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserInitResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_me(self, client: Terminal) -> None:
        user = client.user.me()
        assert_matches_type(UserMeResponse, user, path=["response"])

    @parametrize
    def test_raw_response_me(self, client: Terminal) -> None:
        response = client.user.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserMeResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_me(self, client: Terminal) -> None:
        with client.user.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserMeResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncTerminal) -> None:
        user = await async_client.user.update()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTerminal) -> None:
        user = await async_client.user.update(
            email="john@example.com",
            name="John Doe",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTerminal) -> None:
        response = await async_client.user.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTerminal) -> None:
        async with async_client.user.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_init(self, async_client: AsyncTerminal) -> None:
        user = await async_client.user.init()
        assert_matches_type(UserInitResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_init(self, async_client: AsyncTerminal) -> None:
        response = await async_client.user.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserInitResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncTerminal) -> None:
        async with async_client.user.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserInitResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_me(self, async_client: AsyncTerminal) -> None:
        user = await async_client.user.me()
        assert_matches_type(UserMeResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_me(self, async_client: AsyncTerminal) -> None:
        response = await async_client.user.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserMeResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncTerminal) -> None:
        async with async_client.user.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserMeResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True