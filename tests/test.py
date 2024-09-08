def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total    

def test_calculate_total_with_empty_list():
    print("prueba")
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product(): 
    products = [
        {
            "name":"Notebook",
            "price":5
        }
    ]   
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product(): 
    products = [
        {
            "name":"Notebook",
            "price":5
        },
        {
            "name":"Book",
            "price":10
        },
        {
            "name":"Mouse",
            "price":3
        }
    ]   
    assert calculate_total(products) == 18

if __name__ == "__main__" :
    test_calculate_total_with_empty_list()   
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()