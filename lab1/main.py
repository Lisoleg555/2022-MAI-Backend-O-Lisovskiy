from cache import *

if __name__ == '__main__':
	myCache = TLRU()
	for i in range(32):
		myCache.Set(str(i), str(i + 2))
	for i in range(0, 32, 2):
		print(myCache.Get(str(i)))
	for i in range(24, 32, 3):
		myCache.Del(str(i))
		print(myCache.Get(str(i)))
	for i in range(27, 41):
		myCache.Set(str(i + 2), str(i + 20))
	myCache.Print()

