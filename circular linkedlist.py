#Implementaing Circular doubly linked list 
### ###
class Node:
    def __init__(self, Name, ON):#ON = office Number
        self.Name= Name;
        self.ON= ON;
        self.next= None;
        self.prev= None;

class CircularLinkedList:
    def __init__(self):
        self.head= None;
        self.tail= None;
    #def prepend(self, name, ON):

    def insertathead(self, Name, ON):
        newNode= Node(Name, ON);
        if self.head is None:
            self.head = newNode;
            self.head.next = self.head;
            self.head.prev = self.head;
        else:
            curr = self.head;
            while curr.next != self.head:
                curr = curr.next;
            newNode.next= self.head;
            newNode.prev=curr;
            curr.next=newNode;
            self.head=newNode
        print("Value inserted at head successfully");

    def append(self, Name, ON):
        newNode= Node(Name, ON); # new Node is created to append at the end
        if self.head is None:
            self.head = newNode;
            self.tail = newNode;
            self.head.next = self.head;
            self.head.prev = self.head;
        else:
            curr = self.head;
            #print(curr.next.Name, " ",curr.ON);
            while curr.next != self.head:
                curr= curr.next;

            curr.next=newNode;
            newNode.next=self.head;
            newNode.prev= curr.next;
            self.tail= newNode;
            
    def display(self):
        if self.head is None:
            return False;
        else:
            counter = 1;
            curr= self.head;
            while curr.next != self.head:
                print(counter, "Node data Information\n Name \t\t\t\t\tOffice Number");
                print(" ",curr.Name, "\t\t", curr.ON);
                curr= curr.next;
                counter +=1;
            print(counter, "Node data Information\n Name \t\t\t\t\tOffice Number");
            print(" ",curr.Name, "\t\t", curr.ON);
            print( "list displayed succefully.");
            print(self.tail.Name," ", self.tail.ON);
    def insert_before(self,offNo,Name,ON):#Insertion of a record before the given “ON” if present. If “ON” not present then leave the list as it is
        curr = self.head;
        curr0=curr;
        newNode = Node(Name, ON);
        if curr.ON == offNo:
            newNode.next=self.head;
            self.head.prev=newNode;
            self.tail.next=newNode;
            newNode.prev=self.tail;
            self.head=newNode
        while curr.next != self.head:
            if curr.ON == offNo:
                curr0.next=newNode;
                newNode.prev=curr0;
                newNode.next=curr;
                curr.prev=newNode;
                print("Node before office number inserted successfully.");
                break
            curr0=curr
            curr= curr.next;
        print("wth??")
        if curr.ON ==offNo:
            curr0.next=newNode;
            newNode.prev=curr0;
            newNode.next=curr;
            curr.prev=newNode;
            print("Node before office number inserted successfully.");
    def deleteatEnd(self): #Deletion of a record at the end.
        curr = self.head;
        temp = self.tail;
        while curr.next != self.tail:
            curr = curr.next;
        temp.prev = None;
        temp.next = None;
        curr.next = self.head;
        self.head.prev = curr;
        self.tail = curr;
        x= temp.Name; y= temp.ON;
        del temp;
        print("Deleted Data are:",x," And ",y);

    def delete_double(self, pos):#Deletion of a record at at pos and pos+1
        curr = self.head;
        counter = 2;
        while curr.next != self.head:
            if pos == 1:
                temp1 = self.head;
                temp2 = self.head.next;
                temp = temp2.next;
                temp2.next = None;
                temp2.prev = None;
                temp1.prev = None;
                temp1.next = None;

                temp.prev = self.tail;
                self.tail.next = temp;
                self.head = temp;
                del temp1;
                del temp2;
              
                print("First 2 nodes are deleted successfully");
                break
            elif pos == counter:
                curr0 = curr.prev;
                curr0.next = curr.next.next;
                temp = curr.next.next;
                temp.prev = curr0;
                curr.prev = None;
                temp.prev = None;
                del curr.next;
                del curr;
                print (" Nodes deletd Successfully.");
                break
            counter += 1;
            curr = curr.next;
            print("wth");

    
    def search_Node(self, Name):#Search node based on Name
        if self.head is None:
            print("List is empty.");
        else:
            curr= self.head;
            while curr.next != self.head:
                if curr.Name == Name:
                    print("Node found");
                    print("Information of Searched Node");
                    print("Name :\t", curr.Name, "\nOffice Number :\t", curr.ON);
                    break
                curr= curr.next;
            
            if curr.Name == Name:
                print("Node found");
                print("Information of Searched Node");
                print("Name :\t", curr.Name, "\nOffice Number :\t", curr.ON);

#main
#now gonna create an object
obj = CircularLinkedList();
obj.append("Malik Muhammad Kashif Saeed", 1);
obj.append("Malik Muhammad Awais Saeed", 2);
obj.append("Malik Shahzaib Zahid", 3);
obj.append("Raja Wasi ur Rehman Pasha", 4);
print("Gonna Display the list");
obj.display();
obj.insertathead("Muhammad Siddiqi", 5);
obj.display();
obj.insert_before(4,"Hamza Bin Attique", 6);
obj.display();
print("\t\t\t--------------------------------\t\t\t");
#obj.deleteatEnd();
#obj.display()
#obj.deleteatEnd();
#obj.display()
#obj.delete_double(3);
obj.search_Node("Raja Wasi ur Rehman Pasha");
#obj.display()
