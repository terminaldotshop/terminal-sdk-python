# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import ProfileMeResponse, ProfileUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Terminal) -> None:
        profile = client.profile.update(
            email="john@example.com",
            name="John Doe",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Terminal) -> None:
        response = client.profile.with_raw_response.update(
            email="john@example.com",
            name="John Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Terminal) -> None:
        with client.profile.with_streaming_response.update(
            email="john@example.com",
            name="John Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_me(self, client: Terminal) -> None:
        profile = client.profile.me()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_me(self, client: Terminal) -> None:
        response = client.profile.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_me(self, client: Terminal) -> None:
        with client.profile.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileMeResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncTerminal) -> None:
        profile = await async_client.profile.update(
            email="john@example.com",
            name="John Doe",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTerminal) -> None:
        response = await async_client.profile.with_raw_response.update(
            email="john@example.com",
            name="John Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTerminal) -> None:
        async with async_client.profile.with_streaming_response.update(
            email="john@example.com",
            name="John Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_me(self, async_client: AsyncTerminal) -> None:
        profile = await async_client.profile.me()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_me(self, async_client: AsyncTerminal) -> None:
        response = await async_client.profile.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncTerminal) -> None:
        async with async_client.profile.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileMeResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
