# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import (
    CardGetResponse,
    CardListResponse,
    CardCreateResponse,
    CardDeleteResponse,
    CardCollectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Terminal) -> None:
        card = client.card.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Terminal) -> None:
        response = client.card.with_raw_response.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Terminal) -> None:
        with client.card.with_streaming_response.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardCreateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Terminal) -> None:
        card = client.card.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Terminal) -> None:
        response = client.card.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Terminal) -> None:
        with client.card.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Terminal) -> None:
        card = client.card.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CardDeleteResponse, card, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Terminal) -> None:
        response = client.card.with_raw_response.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDeleteResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Terminal) -> None:
        with client.card.with_streaming_response.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDeleteResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.card.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_collect(self, client: Terminal) -> None:
        card = client.card.collect()
        assert_matches_type(CardCollectResponse, card, path=["response"])

    @parametrize
    def test_raw_response_collect(self, client: Terminal) -> None:
        response = client.card.with_raw_response.collect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardCollectResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_collect(self, client: Terminal) -> None:
        with client.card.with_streaming_response.collect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardCollectResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Terminal) -> None:
        card = client.card.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CardGetResponse, card, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Terminal) -> None:
        response = client.card.with_raw_response.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardGetResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Terminal) -> None:
        with client.card.with_streaming_response.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardGetResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.card.with_raw_response.get(
                "",
            )


class TestAsyncCard:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTerminal) -> None:
        card = await async_client.card.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        )
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTerminal) -> None:
        response = await async_client.card.with_raw_response.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardCreateResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTerminal) -> None:
        async with async_client.card.with_streaming_response.create(
            token="tok_1N3T00LkdIwHu7ixt44h1F8k",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardCreateResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTerminal) -> None:
        card = await async_client.card.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTerminal) -> None:
        response = await async_client.card.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTerminal) -> None:
        async with async_client.card.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTerminal) -> None:
        card = await async_client.card.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CardDeleteResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTerminal) -> None:
        response = await async_client.card.with_raw_response.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDeleteResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTerminal) -> None:
        async with async_client.card.with_streaming_response.delete(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDeleteResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.card.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_collect(self, async_client: AsyncTerminal) -> None:
        card = await async_client.card.collect()
        assert_matches_type(CardCollectResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_collect(self, async_client: AsyncTerminal) -> None:
        response = await async_client.card.with_raw_response.collect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardCollectResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_collect(self, async_client: AsyncTerminal) -> None:
        async with async_client.card.with_streaming_response.collect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardCollectResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncTerminal) -> None:
        card = await async_client.card.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CardGetResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTerminal) -> None:
        response = await async_client.card.with_raw_response.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardGetResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTerminal) -> None:
        async with async_client.card.with_streaming_response.get(
            "crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardGetResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.card.with_raw_response.get(
                "",
            )
