maximum_number = 50


def isPrime(value):
	for i in range(2,value):
		if not value % i:
				return False
	return True

def main():
	print("Starting to compute prime numbers up to " + str(maximum_number))

	for i in range(0, maximum_number):
		if isPrime(i):
			print('Number ' + str(i) + ' is prime.')
		else:
			print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
	main()
