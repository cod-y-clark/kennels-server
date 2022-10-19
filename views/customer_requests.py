CUSTOMERS = [
    {
        "id": 1,
        "name": "John"
    },
    {
        "id": 2,
        "name": "Jim"
    }
]


def get_all_customers():
    """_summary_
    """
    return CUSTOMERS


def get_single_customer(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """_summary_

    Args:
        location (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
