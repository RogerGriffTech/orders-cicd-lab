import pytest
from src.orders import calculate_revenue
 
# Step 3: Positive Case
def test_calculate_revenue_positive():
    assert calculate_revenue(10.50, 4) == 42.00
 
# Step 3: Invalid Case
def test_calculate_revenue_negative_values():
    with pytest.raises(ValueError):
        calculate_revenue(-10.50, 4)
 
# Step 3: Boundary Case
def test_calculate_revenue_zero():
    assert calculate_revenue(0.0, 100) == 0.0