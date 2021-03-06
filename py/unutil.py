#General Utilities
debug = True

#Just what it says it is
def quicksort(word):
	if len(word) == 0:
		return []
	pivot = word[0]
	return quicksort([x for x in word[1:] if x < pivot]) + [pivot] + quicksort([y for y in word[1:] if y >= pivot])

#Use a quicksort to filter out repeated terms
def noReps(word):
	if len(word) == 0:
		return []
	hd = word[0]
	return noReps([i for i in word[1:] if i < hd]) + [hd] + noReps([j for j in word[1:] if j > hd])

#Memoization free, naive factorial finder
def factorial(a):
	if a == 0:
		return 1
	else:
		return a * factorial(a - 1)

#Memoization free, naive combination finder
def choose(a, b):
	if b > a:
		return 0
	elif b == a:
		return 1
	else:
		return factorial(a) // factorial(b) // factorial(a - b)

if debug == True:
	print(choose(8, 5))
	print(choose(6, 4))
	print(choose(3, 3))
	print(choose(3, 4))

#Prime number generator!
def Eratosthesis(limit):
	numbers = [x for x in range(2, limit+1)]
	p = 2
	j = 0
	done = False
	while not done:
		for i, n in enumerate(numbers):
			if n % p == 0 and n != p:
				numbers.pop(i)
		j += 1
		p = numbers[j]
		if p**2 > n:
			done = True
	return numbers

#Getting divisors given a list of primes
#This is not the most efficient way to count said divisors
def makeFactors(intg, primes):
	acc = [1, intg]
	for idx,val in enumerate(primes):
		if idx + 2 == intg:
			pass
		elif val == True:
			prime = idx + 2
			med = intg
			count = 0
			while med % prime == 0:
				count += 1
				if med == 1:
					break
				med //= prime
				if prime ** count != intg:
					acc.append(prime ** count)
				acc.append(med)
	return noReps(acc)
#Needs some tests


#Class that produces factoradic numbers
class Factorad:
	def __init__(self, n):
		factoid = []
		i = 1
		while n != 0:
			factoid.append(math.floor(n % i))
			n //= i
			i += 1
		self.data = reverse(factoid)
		self.pos = n

	def get(self):
		return self.data

	#Getter methods
	def position(self):
		return self.pos

	#Retrieve the premutation corresponding to the factoriad
	#of a given order
	def permutation(self, order):
		temp = [x + 1 for x in self.data]
		acc = [1]
		for x in reverse(temp[:-1]):
			for idx,j in enumerate(acc):
				if j >= x:
					acc[idx] = j + 1
			acc = [x] + acc
#		while len(acc) < order:
#			acc.append(1)
		return [x - 1 for x in acc]

	#It would be better to directly compute the inverse of the
	#factoriad to permutation map, but I'm frankly a bit lazy
	@classmethod
	def fromPermutation(lz):
		def getRepetitions(word):
			acc = {}
			repList = []
			for character in word:
				if character in acc:
					acc[character] += 1
					if not character in repList:
						repList.append(character)
				else:
					acc[character] = 1
			return acc, repList
		#Now the body of the code
		#Count the number of permutations above
		def count(word):
			if len(word) == 0:
				return 1
			acc = 0
			uniqTerms = noReps(word)
			reps, repsList = getRepetitions(word)
			lessThanHead = [x for x in uniqTerms if x < word[0]]
			fullPrevTree = factorial(len(word) - 1)
			for character in lessThanHead:
				med = fullPrevTree
				for rep in repsList:
					if rep != character:
						med //= factorial(reps[rep])
					else:
						med //= factorial(reps[character] - 1)
				acc += med
			return acc + count(word[1:])
		#Just make a factoriad from that integer
		return Factorad(count(lz))

	def __str__(self):
		return self.data.__str__()

if debug == True:
	#do some tests here
	pass

#Class that produces combinadic numbers!
class Combinad:
	def __init__(self, intg, order):
		self.decimal = intg
		acc = []
		while order >= 0:
			i = 1
			while True:
				if choose(i, order) > intg:
					rez = choose(i - 1, order)
					order -= 1
					intg -= rez
					acc.append(i - 1)
					break
				i += 1
		self.data = acc

	def combinations(self):
		return self.data

	# I AM NOT 100% ON THIS! NOTICE THE OFF BY ONE HACK
	@classmethod
	def fromCombinations(cls, lz, order):
		acc = 0
		for idx,val in enumerate(lz):
			acc += choose(val, order - idx)
		return Combinad(acc - 1, order)

	def position(self):
		return self.decimal

	def __str__(self):
		return self.data.__str__()

if debug == True:
	print(Combinad(72, 5))
	print(Combinad(72, 5).position())
	print(Combinad(72, 5).combinations())
	print(Combinad.fromCombinations(Combinad(72,5).combinations(), 5))
	print(Combinad(19, 5).combinations())
	print(Combinad.fromCombinations(Combinad(19,5).combinations(), 5))