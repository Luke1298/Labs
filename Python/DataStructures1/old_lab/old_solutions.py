from Node import LinkedListNode as Node

class DLNode(Node):
	
	def __init__(self, data):
		Node.__init__(self, data)
		self.prev = None


class DoublyLinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self, data):
	
		new_node = DLNode(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
			'''
			current_node = self.head
			while current_node.next is not None:
				current_node = current_node.next

			current_node.next = new_node
			new_node.prev = current_node
			'''

	def remove_node(self, data):
		
		if self.head.data == data:
			self.head = self.head.next
			self.head.prev = None
		else:
			current_node = self.head
			while current_node.data != data:
				current_node = current_node.next
			current_node.prev.next = current_node.next
			current_node.next.prev = current_node.prev
			

	def insert_node(self, new_data, search_data):
		
		new_node = DLNode(new_data)

		if self.head.data == search_data:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = self.head.prev
		else:
			current_node = self.head
			while current_node.next.data != search_data:
				current_node = current_node.next
			
			new_node.next = current_node.next
			new_node.prev = current_node
			current_node.next = new_node
			new_node.next.prev = new_node

	def find(self, data):
		current = self.head
		
		while current.data != data:
			current = current.next
		
		return current


	def __str__(self):
		strlist = []
		if self.head is None:
			return "Empty"
		else:
			current_node = self.head
			strlist.append(self.head.data)
			while current_node.next is not None:
				current_node = current_node.next
				strlist.append(current_node.data)
			return str(strlist)

class SortedLinkedList(DoublyLinkedList):

	def add_node(self, data):
		#new_node = DLNode(data)
		if self.head is None:
			self.head = DLNode(data)
		else:
			current_node = self.head
			if self.head.data < data:
				while current_node.next is not None and current_node.next.data < data:
					current_node = current_node.next
				#print current_node.data
				if current_node.next is None:
					DoublyLinkedList.add_node(self, data)
				else:
					#print data, current_node.data
					DoublyLinkedList.insert_node(self, data, current_node.next.data)
			else:
				DoublyLinkedList.insert_node(self, data, self.head.data)

	def get_list(self):
		current_node = self.head
		li = []
		li.append(current_node.data)
		while current_node.next is not None:
			current_node = current_node.next
			li.append(current_node.data)
		return li




