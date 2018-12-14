#class definition for 'Node' which will be used as an element in a LinkedList
# each element (or 'Node') should have 3 things:
#  -payload: the actual data the element carries...
#  -prev: each element should have a reference to the previous element
#  -nextt: each element should have a reference to the next element
class Node(object): #inherit from built-in type 'object'
    #constructor for 'Node',
    #takes 3 optional parameters to be used for initialisation:
    # -payload: if not specified, default value will be 0
    # -prev: if not specified, default value will be None
    # -nextt: if not specified, default value will be None
    def __init__(self, payload=0, prev=None, nextt=None):
        if type(prev) != Node and prev != None:
            #raise if type(prev) is not Node and prev is not None
            raise TypeError
        if type(nextt) != Node and nextt != None:
            #raise if type(nextt) is not Node and nextt is not None
            raise TypeError
        #once we get here, we are sure that nextt & prev are "safe"...
        self.nextt = nextt
        self.prev = prev
        self.payload = payload

    #implement what should happen if str() is called on "this" object
    def __str__(self):
        return str(self.payload)

#helper function for 'LinkedList'
#assuming 'e' is of type 'Node', guaranteed by "MARKER1" & "MARKER2"
#returns a tuple containing (size, last_element)
def _count_elements(e):
    assert type(e) == Node, "Bad type!" #should never fail though...
    last, size = (e, 1)
    #the line above is the same as writing:
    # last = e
    # size = 1
    while last.nextt != None: #while there's a next element...
        size += 1 #increment size with 1
        last = last.nextt #adjust our last element
    return (size, last) #return result...


#class definition for 'LinkedList'
# a list in its abstract form should have at least 1 thing:
#  -start: indicates the first element of "this" list
# other than that we'll add 2 more things to make our lives easier:
#  -end: indicates the last element of "this" list,
#           prevents us from having to loop over the list
#           to find the last element when we want to append to the list
#  -size: indicates the size of "this" list,
#           prevents us from having to loop over the list
#           to count the number of elements when asked for the length
class LinkedList(object):
    #constructor for 'LinkedList'
    #takes 1 optional parameter:
    # -start: if not specified, default value is None
    #          this means we initialize an empty list...
    #         if start is specified, it means we initialize
    #          with the list with at least 1 element (could be more)
    def __init__(self, start=None):
        #start by initializing 'self.start' & 'self.end'
        #at this point we don't know nothing about the parameter 'start'
        self.start = start
        self.end = start
        #check if type(start) is not Node and start is not None
        #if so, raise a TypeError
        if type(start) != Node and start != None:
            raise TypeError
        #at this point we know that either:
        # type(start) is Node OR start is None
        if start != None: #in case start is not None -> initialize
            #"cut away" anything that precedes 'start'
            self.start.prev = None
            #MARKER1 -> we know 'start' is "safe"
            self.size, self.end = _count_elements(start)
        else: #else initialize empty list
            #'self.start' & 'self.end' are None, indicating empty list
            #only need to set 'self.size' to  0
            self.size = 0

    #implement what needs to happend when str() is called on "this" object
    def __str__(self):
        line = "Printing linked list: "
        runner = self.start #'runner' will "run" over the list
        while runner.nextt != None: #while 'runner' has a next...
            line += str(runner)+", " #add "<element>,"
            runner = runner.nextt #set 'runner' to its next
        #at this point 'runner is the last element, thus has no next
        # consequentially the loop ends before the last element is "printed"
        # thus we must "print" 'runner' one last time
        line += str(runner)
        return line

    #implement what needs to happend when len() is called on "this" object
    def __len__(self):
        return self.size

    #simple method to check if list  is empty...
    #alternatively you could also test for "self.start == None"
    def is_empty(self):
        return self.size==0

    #appends an element (which may be linked to more elements)
    # to the back  of the list
    #takes 1 mandatory argument:
    # -e: the element that should be added
    def append(self, e):
        if type(e) != Node: #if type(e) is not 'Node',
            e = Node(e) #create a Node using 'e' as payload
        #'e' is now of type 'Node'
        size, last = _count_elements(e) #MARKER2 -> 'e' should be "safe"
        if self.size != 0: #general case, non-empty list...
            #first link the current 'end' with 'e'
            self.end.nextt = e
            #then link 'e' with it's previous which is the current 'end'
            e.prev = self.end
            #now set current 'end' to the new end which is 'last'
            self.end = last
        else: #case where "this" list is still empty
            self.start = e #set 'start' to 'e'
            self.end = last #set 'end' to 'last'
        self.size += size #adjust size...

    #implement what should happen in case indexing is used, e.g. ll[2]
    #if the index >= self.size => return last element...
    def __getitem__(self, index):
        assert type(index) == int, "An integer type is required for indexing a linked list."
        runner = self.start #start at the beginning...
        while index > 0 and runner.nextt != None: #while index is bigger than 0 AND there is a next...
            runner = runner.nextt #move to the next element...
            index -= 1 #decrement index with 1
        return runner #return the current element...

    #remove an element from "this" list
    #expects 1 parameter:
    # -obj: either an integer OR the element to be deleted itself...
    def remove(self, obj):
        if type(obj) == int: #if 'obj' is an integer,
            obj = self[obj] #same as calling self.__getitem__(obj)
            #we now have the element which needs to be deleted...
        if self.start == obj: #in case we're deleting the first element,
            if obj.nextt == None: #in case this is the only element in the list...
                self.start = None
                self.end = None
                self.size = 0
                return
            #if we haven't returned, we have more than 1 element and thus "safe"...
            obj.nextt.prev = None #"cut off" second element's previous
            self.start = self.start.nextt #second element is now our start...
        elif self.end == obj: #in case we're deleting the last element,
        #no need to check if this is the only element,
        #cause in that case we would've fallen into the previous block (self.start == obj)
            obj.prev.nextt = None #"cut off" second last's next,
            self.end = self.end.prev #second last element is now our end...
        else: #otherwise...
            #suppose we have elements 1,2,3 and we're deleting 2
            #then 1's (which is 2's prev) next must become 3
            #and 3's (which is 2's next) prev must become 1
            obj.prev.nextt, obj.nextt.prev = (obj.nextt, obj.prev)
        self.size -= 1 #decrement size with 1


#what follows are examples of how to use the linked list...
if __name__ == "__main__":
    ll = LinkedList() #initialize empty list
    ll.append(Node(1)) #some examples...
    print("Size = %d" % len(ll))
    ll.append(Node(2))
    print("Size = %d" % len(ll))
    ll.append(Node(3))
    print("Size = %d" % len(ll))
    print(ll)
    print(ll[1])
    ll.remove(0)
    print("Size = %d" % len(ll))
    ll.remove(ll[1])
    print("Size = %d" % len(ll))
    ll.append("Hello")
    print("Size = %d" % len(ll))
    ll.append("World")
    print("Size = %d" % len(ll))
    nodes = [Node(0), Node(1), Node(2)] #link some nodes
    runner = None
    for i in range(len(nodes)-1):
        nodes[i].prev = runner
        nodes[i].nextt = nodes[i+1]
        runner = nodes[i]
    if runner != None: runner.nextt.prev = runner
    print(ll)
    ll.append(nodes[0]) #only append the first node...
    print("Size = %d" % len(ll))
    print(ll)
