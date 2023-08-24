from Day_15_coffeMachine import resources, check_resources, processing_coins, make_coffee

def test_check_resources_enough():
    chosen_item = "espresso"
    result = check_resources(chosen_item, resources)
    assert result is True

def test_check_resources_not_enough():
    chosen_item = "latte"
    test_resources = {
        "water": 0,   # Adjust the water quantity to be less than required for a latte
        "milk": 2,
        "coffee": 0,
    }
    result = check_resources(chosen_item, test_resources)
    print(test_resources)
    print(result)
    assert result is False

def test_processing_coins_enough():
    item_cost = 2.5
    total_inserted = 3.0
    result = processing_coins(item_cost, total_inserted)
    assert result is True

def test_processing_coins_not_enough():
    item_cost = 1.5
    total_inserted = 1.0
    result = processing_coins(item_cost, total_inserted)
    assert result is False

def test_make_coffee():
    chosen_item = "cappuccino"
    make_coffee(chosen_item, resources)
    # Add assertions to check that the resources were updated correctly
    assert resources["water"] == 50
    assert resources["milk"] == 100
    assert resources["coffee"] == 76
