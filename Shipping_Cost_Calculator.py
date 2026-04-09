"""Very basic shipping cost calculator."""


def main() -> None:
	try:
		weight = float(input("Enter the package weight in kilograms: "))
		rate = float(input("Enter the shipping rate per kilogram: "))
	except ValueError:
		print("Error: Please enter numeric values only.")
		return

	if weight < 0 or rate < 0:
		print("Error: Weight and rate must be non-negative.")
		return

	shipping_cost = weight * rate
	print(f"Shipping Cost: {shipping_cost:.2f} USD")


if __name__ == "__main__":
	main()
