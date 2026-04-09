# Shipping Rate Engine

Very basic Python project to calculate shipping cost.

This repository now also includes a very simple HTML page.

## What It Does

- Reads package weight (kg)
- Reads shipping rate (USD per kg)
- Calculates: `shipping_cost = weight * rate`
- Displays the result in USD

## File

- `Shipping_Cost_Calculator.py`: Main script
- `web/index.html`: Simple HTML page with JavaScript calculator
- `web/styles.css`: Basic styling

## Requirements

- Python 3.x

## Run

```bash
python Shipping_Cost_Calculator.py
```

No server is required for this Python script.

## Run HTML Page (Very Simple)

1. Open `web/index.html` in your browser.
2. Enter weight and rate.
3. Click **Calculate**.

## Example

Input:
- Weight: `10`
- Rate: `2.5`

Output:
- `Shipping Cost: 25.00 USD`

## Basic Validation

- Shows an error if input is not numeric
- Shows an error if weight or rate is negative
