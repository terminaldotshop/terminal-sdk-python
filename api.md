# Products

Types:

```python
from terminal.types import Product, ProductVariant, ProductListResponse
```

Methods:

- <code title="get /products">client.products.<a href="./src/terminal/resources/products.py">list</a>() -> <a href="./src/terminal/types/product_list_response.py">ProductListResponse</a></code>

# Users

Types:

```python
from terminal.types import User, UserUpdateResponse, UserInitResponse, UserMeResponse
```

Methods:

- <code title="put /users/me">client.users.<a href="./src/terminal/resources/users.py">update</a>(\*\*<a href="src/terminal/types/user_update_params.py">params</a>) -> <a href="./src/terminal/types/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /users/init">client.users.<a href="./src/terminal/resources/users.py">init</a>() -> <a href="./src/terminal/types/user_init_response.py">UserInitResponse</a></code>
- <code title="get /users/me">client.users.<a href="./src/terminal/resources/users.py">me</a>() -> <a href="./src/terminal/types/user_me_response.py">UserMeResponse</a></code>

# Addresses

Types:

```python
from terminal.types import (
    Address,
    AddressCreateResponse,
    AddressListResponse,
    AddressDeleteResponse,
)
```

Methods:

- <code title="post /addresses">client.addresses.<a href="./src/terminal/resources/addresses.py">create</a>(\*\*<a href="src/terminal/types/address_create_params.py">params</a>) -> <a href="./src/terminal/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /addresses">client.addresses.<a href="./src/terminal/resources/addresses.py">list</a>() -> <a href="./src/terminal/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /addresses/{id}">client.addresses.<a href="./src/terminal/resources/addresses.py">delete</a>(id) -> <a href="./src/terminal/types/address_delete_response.py">AddressDeleteResponse</a></code>

# Cards

Types:

```python
from terminal.types import Card, CardCreateResponse, CardListResponse, CardDeleteResponse
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/terminal/resources/cards.py">create</a>(\*\*<a href="src/terminal/types/card_create_params.py">params</a>) -> <a href="./src/terminal/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /cards">client.cards.<a href="./src/terminal/resources/cards.py">list</a>() -> <a href="./src/terminal/types/card_list_response.py">CardListResponse</a></code>
- <code title="delete /cards/{id}">client.cards.<a href="./src/terminal/resources/cards.py">delete</a>(id) -> <a href="./src/terminal/types/card_delete_response.py">CardDeleteResponse</a></code>

# Cart

Types:

```python
from terminal.types import (
    Cart,
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

# Orders

Types:

```python
from terminal.types import Order, OrderCreateResponse, OrderListResponse, OrderGetResponse
```

Methods:

- <code title="post /orders">client.orders.<a href="./src/terminal/resources/orders.py">create</a>() -> <a href="./src/terminal/types/order_create_response.py">OrderCreateResponse</a></code>
- <code title="get /orders">client.orders.<a href="./src/terminal/resources/orders.py">list</a>() -> <a href="./src/terminal/types/order_list_response.py">OrderListResponse</a></code>
- <code title="get /orders/{id}">client.orders.<a href="./src/terminal/resources/orders.py">get</a>(id) -> <a href="./src/terminal/types/order_get_response.py">OrderGetResponse</a></code>

# Subscriptions

Types:

```python
from terminal.types import (
    Subscription,
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="put /subscriptions">client.subscriptions.<a href="./src/terminal/resources/subscriptions.py">create</a>(\*\*<a href="src/terminal/types/subscription_create_params.py">params</a>) -> <a href="./src/terminal/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscriptions">client.subscriptions.<a href="./src/terminal/resources/subscriptions.py">list</a>() -> <a href="./src/terminal/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /subscriptions/{id}">client.subscriptions.<a href="./src/terminal/resources/subscriptions.py">delete</a>(id) -> <a href="./src/terminal/types/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Emails

Types:

```python
from terminal.types import EmailCreateResponse
```

Methods:

- <code title="post /emails">client.emails.<a href="./src/terminal/resources/emails.py">create</a>(\*\*<a href="src/terminal/types/email_create_params.py">params</a>) -> <a href="./src/terminal/types/email_create_response.py">EmailCreateResponse</a></code>
