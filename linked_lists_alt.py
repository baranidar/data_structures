class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.head = None
  
    
def insert_node_at_beginning(ll,data):
    if ll is None: 
      node = Node(data)
      ll = node
      finish_up(ll)
      return ll
    node = Node(data)
    node.next = ll
    #print(node.head, node.data, node.next.data, node.next.next)
    finish_up(node)
    return node

def insert_node_at_end(ll, data):
    if ll == None:
      node = Node(data)
      ll.head = node
      finish_up(ll)
      return ll
    node = Node(data)
    current_node = ll
    while current_node:
      last_node = current_node
      current_node = current_node.next
    last_node.next = node
    finish_up(ll)
    return ll

def insert_node_at_index(ll, data, index):
    cur_pos = 1
    if ll.head == None:
      if index == 1:
        node = Node(data)
        ll.head = node
        finish_up(ll)
        return ll
    node = Node(data)
    current_node = ll
    while current_node:
      if cur_pos == index - 1:
        # switch the pointers
        node.next = current_node.next
        current_node.next = node
        finish_up(ll)
        return ll
      current_node = current_node.next
      cur_pos = cur_pos + 1
    finish_up(ll)
    return ll

def find_position_of_data(ll, item):
    current_node = ll
    if ll == None:
      print("Linked List is empty. Item not found.")
    cur_position = 0
    while current_node:
        cur_position = cur_position + 1
        if current_node.data == item:
          item_founud_at = cur_position
          print(item," was found at position ", cur_position)
          return
        current_node = current_node.next

def delete_by_data(ll, item):
    if ll == None:
      print("Linked List is empty. Cannot delete Item.")
    current_node = ll
    while current_node:
      if current_node.data == item:
        prev_node.next = current_node.next
        finish_up(ll)
        return ll
      prev_node = current_node
      current_node = current_node.next
    finish_up(ll)
    return ll

def delete_first_node(ll):
    if ll == None:
      print("Linked List is empty. Cannot delete first node.")
    ll = ll.next
    finish_up(ll)
    return ll

def delete_last_node(ll):
    if ll == None:
       print("Linked List is empty. Cannot delete last node.")
    current_node = ll
    if current_node == None:
      ll.head = None
      finish_up(ll)
      return ll
    while current_node:
      if current_node.next.next == None:
        current_node.next = None
        finish_up(ll)
        return ll
    current_node = current_node.next
    finish_up(ll)
    return ll

def delete_node_at_index(ll, index):
    if ll == None:
      print("Linked List is empty. Cannot delete node by index.")
    cur_pos = 1
    current_node = ll
    if current_node.next == None:
      self.head == None
    while current_node:
      if cur_pos == index - 1:
        current_node.next = current_node.next.next
        finish_up(ll)
        return ll
      current_node = current_node.next
      #print(current_node.data)
      cur_pos = cur_pos + 1 
    finish_up(ll)
    return ll


def size_of_linked_list(ll):
    current_node = ll
    if ll == None:
      print("Linked List is empty")
      return
    size = 0
    while current_node:
      size = size + 1
      current_node = current_node.next
    print("Size of Linked list is ", size)  

def print_linked_list(data):
    current_node = data
    if data == None:
      print("Linked List is empty")
      return
    ll = ""
    while current_node:
      ll = ll + (current_node.data + "-->") if current_node.next is not None else ll + (current_node.data)
      current_node = current_node.next
    print(ll)
 
def finish_up(root):
    print_linked_list(root)
    size_of_linked_list(root)
    
if __name__ == "__main__":
  root = Node("Banana")
  print("Added Banana at the beginning")
  root = insert_node_at_beginning(root, "Strawberry")
  print("Added Strawberry at the beginning")
  root = insert_node_at_end(root, "Mango")
  print("Added Mango at the end")
  root = insert_node_at_index(root, "Blueberry",2)
  print("Added Blueberry at index 2")
  find_position_of_data(root, "Banana")
  root = delete_by_data(root, "Blueberry")
  print("Deleted Blueberry")
  root = delete_first_node(root)
  print("Deleted first node")
  root = delete_last_node(root)
  print("Deleted last node")
  print("Insert Strawberry at the beginning")
  root = insert_node_at_beginning(root,"Strawberry")
  print("Insert Mango at the end")
  root = insert_node_at_end(root, "Mango")
  print("Insert Blueberry at index 2")
  root = insert_node_at_index(root, "Blueberry",2)
  print("Deleted index 2")
  root = delete_node_at_index(root, 2)
