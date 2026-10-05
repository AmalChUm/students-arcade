import random

AUTHOR = "Nolan Hughes"
APP_NAME = "Fibonacci sequence"

def fib(n):
	if n == 1:
		return [0]

	result = [0, 1]
	for i in range(2, n):
		result.append(result[i - 1] + result[i - 2])

	return result;

def run():
	result = fib(10)
	return f"{APP_NAME}: {result}"
