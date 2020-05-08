class HashTable():
	def __init__(self):
		self.size = 1024
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def hashfunciton(self,key,size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def put(self,key,data):
		hashvalue = self.hashfunciton(key,len(self.slots))
		if self.slots[hashvalue]==None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue]==key:
				self.data[hashvalue]=data
			else:
				nextslot = self.rehash(hashvalue,len(self.slots))
				while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
					nextslot = self.rehash(nextslot,len(self.slots))
				if self.slots[nextslot]==None:
					self.slots[nextslot]=key
					self.data[nextslot]=data
				else:
					self.data[nextslot]=data

	def get(self,key):
		startslot = self.hashfunciton(key,len(self.slots))
		data = None
		stop = False
		found = False
		postion = startslot
		while self.slots[postion]!=None and not found and not stop:
			if self.slots[postion]==key:
				found = True
				data = self.data[postion]
			else:
				postion = self.rehash(postion,len(self.slots))
				if postion==startslot:
					stop = True
		return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)


ht = HashTable()
ht[1]='abs'
print(ht[1])
ht[1024]='gg'
print(ht[1024])
