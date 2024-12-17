# Product

Types:

```python
from terminal_sdk.types import Product, ProductVariant, ProductListResponse
```

Methods:

- <code title="get /product">client.product.<a href="./src/terminal_sdk/resources/product.py">list</a>() -> <a href="./src/terminal_sdk/types/product_list_response.py">ProductListResponse</a></code>

# Profile

Types:

```python
from terminal_sdk.types import Profile, ProfileUpdateResponse, ProfileMeResponse
```

Methods:

- <code title="put /profile">client.profile.<a href="./src/terminal_sdk/resources/profile.py">update</a>(\*\*<a href="src/terminal_sdk/types/profile_update_params.py">params</a>) -> <a href="./src/terminal_sdk/types/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /profile">client.profile.<a href="./src/terminal_sdk/resources/profile.py">me</a>() -> <a href="./src/terminal_sdk/types/profile_me_response.py">ProfileMeResponse</a></code>

# Address

Types:

```python
from terminal_sdk.types import (
    Address,
    AddressCreateResponse,
    AddressListResponse,
    AddressDeleteResponse,
)
```

Methods:

- <code title="post /address">client.address.<a href="./src/terminal_sdk/resources/address.py">create</a>(\*\*<a href="src/terminal_sdk/types/address_create_params.py">params</a>) -> <a href="./src/terminal_sdk/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /address">client.address.<a href="./src/terminal_sdk/resources/address.py">list</a>() -> <a href="./src/terminal_sdk/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /address/{id}">client.address.<a href="./src/terminal_sdk/resources/address.py">delete</a>(id) -> <a href="./src/terminal_sdk/types/address_delete_response.py">AddressDeleteResponse</a></code>

# Card

Types:

```python
from terminal_sdk.types import Card, CardCreateResponse, CardListResponse, CardDeleteResponse
```

Methods:

- <code title="post /card">client.card.<a href="./src/terminal_sdk/resources/card.py">create</a>(\*\*<a href="src/terminal_sdk/types/card_create_params.py">params</a>) -> <a href="./src/terminal_sdk/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /card">client.card.<a href="./src/terminal_sdk/resources/card.py">list</a>() -> <a href="./src/terminal_sdk/types/card_list_response.py">CardListResponse</a></code>
- <code title="delete /card/{id}">client.card.<a href="./src/terminal_sdk/resources/card.py">delete</a>(id) -> <a href="./src/terminal_sdk/types/card_delete_response.py">CardDeleteResponse</a></code>

# Cart

Types:

```python
from terminal_sdk.types import (
    Cart,
    CartConvertResponse,
    CartGetResponse,
    CartSetAddressResponse,
    CartSetCardResponse,
    CartSetItemResponse,
)
```

Methods:

- <code title="post /cart/convert">client.cart.<a href="./src/terminal_sdk/resources/cart.py">convert</a>() -> <a href="./src/terminal_sdk/types/cart_convert_response.py">CartConvertResponse</a></code>
- <code title="get /cart">client.cart.<a href="./src/terminal_sdk/resources/cart.py">get</a>() -> <a href="./src/terminal_sdk/types/cart_get_response.py">CartGetResponse</a></code>
- <code title="put /cart/address">client.cart.<a href="./src/terminal_sdk/resources/cart.py">set_address</a>(\*\*<a href="src/terminal_sdk/types/cart_set_address_params.py">params</a>) -> <a href="./src/terminal_sdk/types/cart_set_address_response.py">CartSetAddressResponse</a></code>
- <code title="put /cart/card">client.cart.<a href="./src/terminal_sdk/resources/cart.py">set_card</a>(\*\*<a href="src/terminal_sdk/types/cart_set_card_params.py">params</a>) -> <a href="./src/terminal_sdk/types/cart_set_card_response.py">CartSetCardResponse</a></code>
- <code title="put /cart/item">client.cart.<a href="./src/terminal_sdk/resources/cart.py">set_item</a>(\*\*<a href="src/terminal_sdk/types/cart_set_item_params.py">params</a>) -> <a href="./src/terminal_sdk/types/cart_set_item_response.py">CartSetItemResponse</a></code>

# Order

Types:

```python
from terminal_sdk.types import Order, OrderListResponse, OrderGetResponse
```

Methods:

- <code title="get /order">client.order.<a href="./src/terminal_sdk/resources/order.py">list</a>() -> <a href="./src/terminal_sdk/types/order_list_response.py">OrderListResponse</a></code>
- <code title="get /order/{id}">client.order.<a href="./src/terminal_sdk/resources/order.py">get</a>(id) -> <a href="./src/terminal_sdk/types/order_get_response.py">OrderGetResponse</a></code>

# Subscription

Types:

```python
from terminal_sdk.types import (
    Subscription,
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="put /subscription">client.subscription.<a href="./src/terminal_sdk/resources/subscription.py">create</a>(\*\*<a href="src/terminal_sdk/types/subscription_create_params.py">params</a>) -> <a href="./src/terminal_sdk/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscription">client.subscription.<a href="./src/terminal_sdk/resources/subscription.py">list</a>() -> <a href="./src/terminal_sdk/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /subscription/{id}">client.subscription.<a href="./src/terminal_sdk/resources/subscription.py">delete</a>(id) -> <a href="./src/terminal_sdk/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Token

Types:

```python
from terminal_sdk.types import Token, TokenListResponse, TokenDeleteResponse, TokenGetResponse
```

Methods:

- <code title="get /token">client.token.<a href="./src/terminal_sdk/resources/token.py">list</a>() -> <a href="./src/terminal_sdk/types/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /token/{id}">client.token.<a href="./src/terminal_sdk/resources/token.py">delete</a>(id) -> <a href="./src/terminal_sdk/types/token_delete_response.py">TokenDeleteResponse</a></code>
- <code title="get /token/{id}">client.token.<a href="./src/terminal_sdk/resources/token.py">get</a>(id) -> <a href="./src/terminal_sdk/types/token_get_response.py">TokenGetResponse</a></code>

# App

Types:

```python
from terminal_sdk.types import App, AppListResponse, AppDeleteResponse, AppGetResponse
```

Methods:

- <code title="get /app">client.app.<a href="./src/terminal_sdk/resources/app.py">list</a>() -> <a href="./src/terminal_sdk/types/app_list_response.py">AppListResponse</a></code>
- <code title="delete /app/{id}">client.app.<a href="./src/terminal_sdk/resources/app.py">delete</a>(id) -> <a href="./src/terminal_sdk/types/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="get /app/{id}">client.app.<a href="./src/terminal_sdk/resources/app.py">get</a>(id) -> <a href="./src/terminal_sdk/types/app_get_response.py">AppGetResponse</a></code>

# Email

Types:

```python
from terminal_sdk.types import EmailCreateResponse
```

Methods:

- <code title="post /email">client.email.<a href="./src/terminal_sdk/resources/email.py">create</a>(\*\*<a href="src/terminal_sdk/types/email_create_params.py">params</a>) -> <a href="./src/terminal_sdk/types/email_create_response.py">EmailCreateResponse</a></code>

# View

Types:

```python
from terminal_sdk.types import ViewInitResponse
```

Methods:

- <code title="get /view/init">client.view.<a href="./src/terminal_sdk/resources/view.py">init</a>() -> <a href="./src/terminal_sdk/types/view_init_response.py">ViewInitResponse</a></code>
