# Product

Types:

```python
from terminal_shop.types import Product, ProductVariant, ProductListResponse, ProductGetResponse
```

Methods:

- <code title="get /product">client.product.<a href="./src/terminal_shop/resources/product.py">list</a>() -> <a href="./src/terminal_shop/types/product_list_response.py">ProductListResponse</a></code>
- <code title="get /product/{id}">client.product.<a href="./src/terminal_shop/resources/product.py">get</a>(id) -> <a href="./src/terminal_shop/types/product_get_response.py">ProductGetResponse</a></code>

# Profile

Types:

```python
from terminal_shop.types import Profile, ProfileUpdateResponse, ProfileMeResponse
```

Methods:

- <code title="put /profile">client.profile.<a href="./src/terminal_shop/resources/profile.py">update</a>(\*\*<a href="src/terminal_shop/types/profile_update_params.py">params</a>) -> <a href="./src/terminal_shop/types/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /profile">client.profile.<a href="./src/terminal_shop/resources/profile.py">me</a>() -> <a href="./src/terminal_shop/types/profile_me_response.py">ProfileMeResponse</a></code>

# Address

Types:

```python
from terminal_shop.types import (
    Address,
    AddressCreateResponse,
    AddressListResponse,
    AddressDeleteResponse,
    AddressGetResponse,
)
```

Methods:

- <code title="post /address">client.address.<a href="./src/terminal_shop/resources/address.py">create</a>(\*\*<a href="src/terminal_shop/types/address_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /address">client.address.<a href="./src/terminal_shop/resources/address.py">list</a>() -> <a href="./src/terminal_shop/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /address/{id}">client.address.<a href="./src/terminal_shop/resources/address.py">delete</a>(id) -> <a href="./src/terminal_shop/types/address_delete_response.py">AddressDeleteResponse</a></code>
- <code title="get /address/{id}">client.address.<a href="./src/terminal_shop/resources/address.py">get</a>(id) -> <a href="./src/terminal_shop/types/address_get_response.py">AddressGetResponse</a></code>

# Card

Types:

```python
from terminal_shop.types import (
    Card,
    CardCreateResponse,
    CardListResponse,
    CardDeleteResponse,
    CardCollectResponse,
    CardGetResponse,
)
```

Methods:

- <code title="post /card">client.card.<a href="./src/terminal_shop/resources/card.py">create</a>(\*\*<a href="src/terminal_shop/types/card_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /card">client.card.<a href="./src/terminal_shop/resources/card.py">list</a>() -> <a href="./src/terminal_shop/types/card_list_response.py">CardListResponse</a></code>
- <code title="delete /card/{id}">client.card.<a href="./src/terminal_shop/resources/card.py">delete</a>(id) -> <a href="./src/terminal_shop/types/card_delete_response.py">CardDeleteResponse</a></code>
- <code title="post /card/collect">client.card.<a href="./src/terminal_shop/resources/card.py">collect</a>() -> <a href="./src/terminal_shop/types/card_collect_response.py">CardCollectResponse</a></code>
- <code title="get /card/{id}">client.card.<a href="./src/terminal_shop/resources/card.py">get</a>(id) -> <a href="./src/terminal_shop/types/card_get_response.py">CardGetResponse</a></code>

# Cart

Types:

```python
from terminal_shop.types import (
    Cart,
    CartClearResponse,
    CartConvertResponse,
    CartGetResponse,
    CartSetAddressResponse,
    CartSetCardResponse,
    CartSetItemResponse,
)
```

Methods:

- <code title="delete /cart">client.cart.<a href="./src/terminal_shop/resources/cart.py">clear</a>() -> <a href="./src/terminal_shop/types/cart_clear_response.py">CartClearResponse</a></code>
- <code title="post /cart/convert">client.cart.<a href="./src/terminal_shop/resources/cart.py">convert</a>() -> <a href="./src/terminal_shop/types/cart_convert_response.py">CartConvertResponse</a></code>
- <code title="get /cart">client.cart.<a href="./src/terminal_shop/resources/cart.py">get</a>() -> <a href="./src/terminal_shop/types/cart_get_response.py">CartGetResponse</a></code>
- <code title="put /cart/address">client.cart.<a href="./src/terminal_shop/resources/cart.py">set_address</a>(\*\*<a href="src/terminal_shop/types/cart_set_address_params.py">params</a>) -> <a href="./src/terminal_shop/types/cart_set_address_response.py">CartSetAddressResponse</a></code>
- <code title="put /cart/card">client.cart.<a href="./src/terminal_shop/resources/cart.py">set_card</a>(\*\*<a href="src/terminal_shop/types/cart_set_card_params.py">params</a>) -> <a href="./src/terminal_shop/types/cart_set_card_response.py">CartSetCardResponse</a></code>
- <code title="put /cart/item">client.cart.<a href="./src/terminal_shop/resources/cart.py">set_item</a>(\*\*<a href="src/terminal_shop/types/cart_set_item_params.py">params</a>) -> <a href="./src/terminal_shop/types/cart_set_item_response.py">CartSetItemResponse</a></code>

# Order

Types:

```python
from terminal_shop.types import Order, OrderCreateResponse, OrderListResponse, OrderGetResponse
```

Methods:

- <code title="post /order">client.order.<a href="./src/terminal_shop/resources/order.py">create</a>(\*\*<a href="src/terminal_shop/types/order_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/order_create_response.py">OrderCreateResponse</a></code>
- <code title="get /order">client.order.<a href="./src/terminal_shop/resources/order.py">list</a>() -> <a href="./src/terminal_shop/types/order_list_response.py">OrderListResponse</a></code>
- <code title="get /order/{id}">client.order.<a href="./src/terminal_shop/resources/order.py">get</a>(id) -> <a href="./src/terminal_shop/types/order_get_response.py">OrderGetResponse</a></code>

# Subscription

Types:

```python
from terminal_shop.types import (
    Subscription,
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
)
```

Methods:

- <code title="post /subscription">client.subscription.<a href="./src/terminal_shop/resources/subscription.py">create</a>(\*\*<a href="src/terminal_shop/types/subscription_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscription">client.subscription.<a href="./src/terminal_shop/resources/subscription.py">list</a>() -> <a href="./src/terminal_shop/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /subscription/{id}">client.subscription.<a href="./src/terminal_shop/resources/subscription.py">delete</a>(id) -> <a href="./src/terminal_shop/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
- <code title="get /subscription/{id}">client.subscription.<a href="./src/terminal_shop/resources/subscription.py">get</a>(id) -> <a href="./src/terminal_shop/types/subscription_get_response.py">SubscriptionGetResponse</a></code>

# Token

Types:

```python
from terminal_shop.types import (
    Token,
    TokenCreateResponse,
    TokenListResponse,
    TokenDeleteResponse,
    TokenGetResponse,
)
```

Methods:

- <code title="post /token">client.token.<a href="./src/terminal_shop/resources/token.py">create</a>() -> <a href="./src/terminal_shop/types/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /token">client.token.<a href="./src/terminal_shop/resources/token.py">list</a>() -> <a href="./src/terminal_shop/types/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /token/{id}">client.token.<a href="./src/terminal_shop/resources/token.py">delete</a>(id) -> <a href="./src/terminal_shop/types/token_delete_response.py">TokenDeleteResponse</a></code>
- <code title="get /token/{id}">client.token.<a href="./src/terminal_shop/resources/token.py">get</a>(id) -> <a href="./src/terminal_shop/types/token_get_response.py">TokenGetResponse</a></code>

# App

Types:

```python
from terminal_shop.types import (
    App,
    AppCreateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
)
```

Methods:

- <code title="post /app">client.app.<a href="./src/terminal_shop/resources/app.py">create</a>(\*\*<a href="src/terminal_shop/types/app_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/app_create_response.py">AppCreateResponse</a></code>
- <code title="get /app">client.app.<a href="./src/terminal_shop/resources/app.py">list</a>() -> <a href="./src/terminal_shop/types/app_list_response.py">AppListResponse</a></code>
- <code title="delete /app/{id}">client.app.<a href="./src/terminal_shop/resources/app.py">delete</a>(id) -> <a href="./src/terminal_shop/types/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="get /app/{id}">client.app.<a href="./src/terminal_shop/resources/app.py">get</a>(id) -> <a href="./src/terminal_shop/types/app_get_response.py">AppGetResponse</a></code>

# Email

Types:

```python
from terminal_shop.types import EmailCreateResponse
```

Methods:

- <code title="post /email">client.email.<a href="./src/terminal_shop/resources/email.py">create</a>(\*\*<a href="src/terminal_shop/types/email_create_params.py">params</a>) -> <a href="./src/terminal_shop/types/email_create_response.py">EmailCreateResponse</a></code>

# View

Types:

```python
from terminal_shop.types import Region, ViewInitResponse
```

Methods:

- <code title="get /view/init">client.view.<a href="./src/terminal_shop/resources/view.py">init</a>() -> <a href="./src/terminal_shop/types/view_init_response.py">ViewInitResponse</a></code>
