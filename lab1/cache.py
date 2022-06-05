class TLRU:
	def __init__(self, capacity:int = 32) -> None:
		self.capacity = capacity
		self.data = {}
		self.size = 0
	
	def Get(self, key:str) -> str:
		if key in self.data:
			data = self.data[key][:]
			del self.data[key]
			self.data[key] = data
			return data
		return "No such element"

	def Print(self) -> None:
		for i in self.data:
			print(i)

	def Set(self, key:str, data:str) -> None:
		if key in self.data:
			del self.data[key]
			self.data[key] = data
		else:
			if self.size == self.capacity: 
				del self.data[next(iter(self.data.keys()))]
				self.size -= 1
			self.data[key] = data
			self.size += 1
			
	def Del(self, key:str) -> None:
		if key in self.data:
			del self.data[key]
			self.size -= 1
