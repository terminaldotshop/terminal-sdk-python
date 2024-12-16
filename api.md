# Shared Types

```python
from terminal.types import Address, Card, Cart, Order, Product, ProductVariant, Subscription, User
```

# Product

Types:

```python
from terminal.types import ProductListResponse
```

Methods:

- <code title="get /product">client.product.<a href="./src/terminal/resources/product.py">list</a>() -> <a href="./src/terminal/types/product_list_response.py">ProductListResponse</a></code>

# User

Types:

```python
from terminal.types import UserUpdateResponse, UserInitResponse, UserMeResponse
```

Methods:

- <code title="put /user/me">client.user.<a href="./src/terminal/resources/user.py">update</a>(\*\*<a href="src/terminal/types/user_update_params.py">params</a>) -> <a href="./src/terminal/types/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /user/init">client.user.<a href="./src/terminal/resources/user.py">init</a>() -> <a href="./src/terminal/types/user_init_response.py">UserInitResponse</a></code>
- <code title="get /user/me">client.user.<a href="./src/terminal/resources/user.py">me</a>() -> <a href="./src/terminal/types/user_me_response.py">UserMeResponse</a></code>

# Address

Types:

```python
from terminal.types import AddressCreateResponse, AddressListResponse, AddressDeleteResponse
```

Methods:

- <code title="post /address">client.address.<a href="./src/terminal/resources/address.py">create</a>(\*\*<a href="src/terminal/types/address_create_params.py">params</a>) -> <a href="./src/terminal/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /address">client.address.<a href="./src/terminal/resources/address.py">list</a>() -> <a href="./src/terminal/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /address/{id}">client.address.<a href="./src/terminal/resources/address.py">delete</a>(id) -> <a href="./src/terminal/types/address_delete_response.py">AddressDeleteResponse</a></code>

# Card

Types:

```python
from terminal.types import CardCreateResponse, CardListResponse, CardDeleteResponse
```

Methods:

- <code title="post /card">client.card.<a href="./src/terminal/resources/card.py">create</a>(\*\*<a href="src/terminal/types/card_create_params.py">params</a>) -> <a href="./src/terminal/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /card">client.card.<a href="./src/terminal/resources/card.py">list</a>() -> <a href="./src/terminal/types/card_list_response.py">CardListResponse</a></code>
- <code title="delete /card/{id}">client.card.<a href="./src/terminal/resources/card.py">delete</a>(id) -> <a href="./src/terminal/types/card_delete_response.py">CardDeleteResponse</a></code>

# Cart

Types:

```python
from terminal.types import (
    CartListResponse,
    CartSetAddressResponse,
    CartSetCardResponse,
    CartSetItemResponse,
)
```

Methods:

- <code title="get /cart">client.cart.<a href="./src/terminal/resources/cart.py">list</a>() -> <a href="./src/terminal/types/cart_list_response.py">CartListResponse</a></code>
- <code title="put /cart/address">client.cart.<a href="./src/terminal/resources/cart.py">set_address</a>(\*\*<a href="src/terminal/types/cart_set_address_params.py">params</a>) -> <a href="./src/terminal/types/cart_set_address_response.py">CartSetAddressResponse</a></code>
- <code title="put /cart/card">client.cart.<a href="./src/terminal/resources/cart.py">set_card</a>(\*\*<a href="src/terminal/types/cart_set_card_params.py">params</a>) -> <a href="./src/terminal/types/cart_set_card_response.py">CartSetCardResponse</a></code>
- <code title="put /cart/item">client.cart.<a href="./src/terminal/resources/cart.py">set_item</a>(\*\*<a href="src/terminal/types/cart_set_item_params.py">params</a>) -> <a href="./src/terminal/types/cart_set_item_response.py">CartSetItemResponse</a></code>

# Order

Types:

```python
from terminal.types import OrderCreateResponse, OrderListResponse, OrderGetResponse
```

Methods:

- <code title="post /order">client.order.<a href="./src/terminal/resources/order.py">create</a>() -> <a href="./src/terminal/types/order_create_response.py">OrderCreateResponse</a></code>
- <code title="get /order">client.order.<a href="./src/terminal/resources/order.py">list</a>() -> <a href="./src/terminal/types/order_list_response.py">OrderListResponse</a></code>
- <code title="get /order/{id}">client.order.<a href="./src/terminal/resources/order.py">get</a>(id) -> <a href="./src/terminal/types/order_get_response.py">OrderGetResponse</a></code>

# Subscription

Types:

```python
from terminal.types import (
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="put /subscription">client.subscription.<a href="./src/terminal/resources/subscription.py">create</a>(\*\*<a href="src/terminal/types/subscription_create_params.py">params</a>) -> <a href="./src/terminal/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscription">client.subscription.<a href="./src/terminal/resources/subscription.py">list</a>() -> <a href="./src/terminal/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /subscription/{id}">client.subscription.<a href="./src/terminal/resources/subscription.py">delete</a>(id) -> <a href="./src/terminal/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Email

Types:

```python
from terminal.types import EmailCreateResponse
```

Methods:

- <code title="post /email/subscription">client.email.<a href="./src/terminal/resources/email.py">create</a>(\*\*<a href="src/terminal/types/email_create_params.py">params</a>) -> <a href="./src/terminal/types/email_create_response.py">EmailCreateResponse</a></code>
