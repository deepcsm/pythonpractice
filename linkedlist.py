class node():
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist():
	def __init__(self):
		self.head=None

	def append(self,new_data):
		self.new_data=new_data
		new_node=node(new_data)
		if self.head==None:
			self.head=new_node
		else:
			new_node.next=self.head
			self.head=new_node

	def lprint(self):
		temp=self.head
		while (temp):
			print temp.data
			temp=temp.next


if __name__=='__main__':
	llsit=linkedlist()
	llsit.append(5)
	llsit.append(10)
	llsit.lprint()
