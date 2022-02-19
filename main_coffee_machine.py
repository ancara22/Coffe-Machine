from data_coffee import coffee_types

machine_resource = {
	"water": 500,
	"milk": 300,
	"coffee": 200,
	"money": 0
}


def report(water, coffee, milk, money):
	print(f"Water: {water}ml\nMilk: {milk}ml"
	      f"\nCoffee: {coffee}g\nMoney: ${money}")


def check_resources(new_coffee, resources):
	coffee = new_coffee["ingredients"]

	if resources["water"] >= coffee["water"]:
		if resources["coffee"] >= coffee["coffee"]:
			if resources["milk"] >= coffee["milk"]:
				return "Enough"
			else:
				return "Milk"
		else:
			return "Coffee"
	else:
		return "Water"


def find_coffee(coffee_name):
	name = coffee_name.lower()
	for el in coffee_types:
		if el["name"] == name:
			return el


def make_coffee(coffee_type, machine_resources):
	new_coffee = coffee_type
	resource = machine_resources

	resource["water"] -= new_coffee["ingredients"]["water"]
	resource["milk"] -= new_coffee["ingredients"]["milk"]
	resource["coffee"] -= new_coffee["ingredients"]["coffee"]

	print(f"Here is your {coffee_type['name']}, Enjoy!")
	return resource


def pay_method(coffee_cost):
	quarters = float(input("How many quarters?: ")) * 0.25
	dimes = float(input("How many dimes?: ")) * 0.10
	nickles = float(input("How many nickles?: ")) * 0.05
	pennies = float(input("How many pennies?: ")) * 0.01

	total_sum = quarters + dimes + nickles + pennies

	if total_sum < coffee_cost:
		print("Sorry that's not enough money. Money refunded.")
		return False
	elif total_sum >= coffee_cost:
		if total_sum > coffee_cost:
			rest = total_sum - coffee_cost
			print(f"Here is ${round(rest, 2)} in change.")
			return True
		return True



def main_app(machine_resource):
	operation = input("What would you like? (espresso/latte/cappucino): ")

	if operation =="report":
		report(machine_resource['water'], machine_resource['coffee'], machine_resource['milk'], machine_resource['money'])
		main_app(machine_resource)
	else:
		coffee_recipe = find_coffee(operation)
		enough_resources = check_resources(coffee_recipe, machine_resource)

		if enough_resources == "Enough":
			is_payed = pay_method(coffee_recipe["price"])
			if is_payed:
				new_resources = make_coffee(coffee_recipe, machine_resource)
				new_resources["money"] += coffee_recipe["price"]
				main_app(new_resources)
			main_app(machine_resource)

		else:
			print(f"Sorry there is not enough {enough_resources}")
			main_app(machine_resource)



main_app(machine_resource)