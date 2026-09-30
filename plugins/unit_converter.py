"""
Unit Converter Plugin for Students Arcade.
Converts common metric and imperial units (Kilometers to Miles, Kilograms to Pounds, Celsius to Fahrenheit).
Zero external dependencies (Python standard library only).
"""

import random

AUTHOR = "lui01212"
APP_NAME = "Unit Converter Arcade"

CONVERSIONS = [
    {
        "name": "Kilometers to Miles",
        "val": 5.0,
        "src": "km",
        "res": 3.11,
        "dst": "mi",
    },
    {
        "name": "Kilograms to Pounds",
        "val": 10.0,
        "src": "kg",
        "res": 22.05,
        "dst": "lbs",
    },
    {
        "name": "Celsius to Fahrenheit",
        "val": 25.0,
        "src": "C",
        "res": 77.0,
        "dst": "F",
    },
    {
        "name": "Meters to Feet",
        "val": 2.0,
        "src": "m",
        "res": 6.56,
        "dst": "ft",
    },
    {
        "name": "Liters to Gallons",
        "val": 3.79,
        "src": "L",
        "res": 1.0,
        "dst": "gal",
    },
]


def run() -> str:
    """Main execution function called by main.py."""
    c = random.choice(CONVERSIONS)
    return f"[Unit Converter] {c['val']} {c['src']} = {c['res']} {c['dst']} ({c['name']})"
