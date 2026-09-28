def calculate_revenue(price: float, quantity: int) -> float:

    """

    Calculates total revenue and ensures valid positive pricing structures.

    """

    if price < 0 or quantity < 0:

        raise ValueError("Price and quantity must be non-negative")

    return round(float(price * quantity), 2)

 
