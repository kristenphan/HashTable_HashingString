# python3


# this class stores the data for each query
# 3 query types: add, del, find, deck
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

    def __str__(self):
        str = 'query type = {}'.format(self.type)

# this class is a node that makes up doubly linked lists which are then stringed together in an array that represents a hash table
# each node contains the string being added to the hash table and associated with a particular hash value and 2 pointers
# one pointer pointing to the next node (containing the next string in the linked list with the same hash value)
# and another pointing to the previous node (containing the previous string in the linked list with the same hash value)
# the default value of the two pointers are None
class Node:
    def __init__(self, s):
        self.key = s
        self.next = None
        self.prev = None

    def __str__(self):
        str = "key = {}. next = {}. prev = {}".format(self.key, self.next, self.prev)
        return str

# this class contains the properties and methods to initialize a hash table
# and process a series of queries to modify the hash table
# this hash table is implementing using chaining technique but not dynamic array as the size of the hash table is fixed (bucket_count = 43)
# 4 type of queries:
# add: add a string to the hash table. if said string already exists, ignore the query
# del: remove a string from the hash table. if said string does not exist, ignore the query
# find: return yes if a particular string is found in the hash table. otherwise, return no
# check: return a chain in the hash table associated with the passed in index. if the chain is empty, return a blank line
class QueryProcessor:
    _multiplier = 263 # given as part of the assignment
    _prime = 1000000007 # given as part of the assignment

    # this method initializes a hash table using the passed in bucket_count
    # the value of bucket_count is the cardinallity of the hash table and is the same as the number of chains in the hash table
    # each of the element in array A will serve as a pointer to a doubly linked list (ie. this pointer is the head of a chain in the hash table)
    # chains (ie. linked lists) contain nodes which store a string whose hash value is the same as the index of the chain
    # all heads of chains are initialized to None, representing to an empty chain initially
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.A = self.make_array(self.bucket_count)


    def make_array(self, bucket_count):
        """
        Returns a new array with a bucket_count as specified
        """
        A = (bucket_count * ctypes.py_object)()
        for hash in range(bucket_count):
            A[hash] = None

        return A


    # this method returns a list representation of all chains in the hash table for printing purposes
    def chain_lst(self):
        chains = [[] for _ in range(self.bucket_count)]
        for i in range(self.bucket_count):
            head = self.A[i]
            if self.A[i] == None:
                chains[i].append('Chain is empty')
            else:
                while head.next != None:
                    chains[i].append(head.key)
                    head = head.next
                chains[i].append(head.key)

        return chains

    # this method generates a hash value for each string to be added to or removed from the hash table
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    # this method returns the input and returns a query to be processed
    def read_query(self):
        return Query(input().split())

    # this method removes the passed in string with corresponding hash value from the hash table
    # if a string does not exist, ignore the query
    # the operations required to remove such string depend on the position of the node that stores the string
    # there are 5 possible scenarios for different node positions
    # 1 - node to be deleted is the only node in a chain - operations required: (1) head = None
    # 2 - node to be deleted is the last element in a chain of at least 2 nodes - operations required: (1) node.prev.next = None
    # 3 - node to be deleted is surrounded by 2 nodes (the chain head is not considered a node) - operations required: (1) node.prev.next = node.next (2) node.next.prev = node.prev
    # 4 - node to be deleted is the first element in a chain of 2 nodes - operations required: (1) head = node.next (2) node.next.prev = None
    # 5 - node to be deleted is the first element in the chain of at least 3 nodes - operations required: (1) curr_node.next.prev = None (2) head = curr_node.next
    # Note: commonality between scenario 1 and 2: the current node being inspected is the last node in the chain (node.next = None)
    def del_(self, hash, string):
        # go down the chain (go until the second to last node, then check the last node - if found string, apply scenario 1)
        # find string, if yes, check for 4 scenarios listed above and perform appropriate operations
        # need to fixate on the head
        curr_node = self.A[hash] # temp represents the node being inspected. temp.key will be checked against the passed in string
        while curr_node.next != None: # iterate from the first node to the second from last node in the chain
            # inspect the current node to see if the string matches
            if curr_node.key == string:
                if curr_node != self.A[hash]: # scenario 3
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    curr_node = curr_node.next
                    continue
                if curr_node == self.A[hash] and curr_node.next.next == None: # scenario 4
                    self.A[hash] = curr_node.next
                    curr_node.next.prev = None
                    curr_node = curr_node.next
                    continue
                if curr_node == self.A[hash] and curr_node.next.next != None: # scenario 5
                    curr_node.next.prev = None
                    self.A[hash] = curr_node.next

            # move on to inspecting the next node in the chain
            curr_node = curr_node.next

        # check if the last node stores the same string:
        if curr_node != self.A[hash] and curr_node.key == string: # scenario 2
            curr_node.prev.next = None

        if curr_node == self.A[hash] and curr_node.key == string: # scenario 1
            self.A[hash] = None


    # this method processes each query according to the query type: add, del, find, check
    def process_query(self, query):

        if query.type == 'add':
            hash = self._hash_func(query.s)
            new_node = Node(query.s)
            # if the chain (doubly linked list) associated with the hash value is empty (ie. value of None),
            # set its value to the first node containing the string being added to the hash table
            if self.A[hash] == None:
                self.A[hash] = new_node
            # traverse through the chain check if the string already exists in the chain
            # if yes, ignore the query
            # if no, create a new node to store this string and add the new node to the beginning of the chain
            else:
                curr_node = self.A[hash]
                count = 0
                while curr_node.next != None:
                    if curr_node.key == query.s:
                        return
                    curr_node = curr_node.next
                if curr_node.key == query.s: # check if the last node stores the same string
                    return
                new_node.next = self.A[hash]
                self.A[hash].prev = new_node
                self.A[hash] = new_node

         if query.type == 'find':
            hash = self._hash_func(query.s)
            # if there is the array element associated with the hash value does not point to any list,
            # that means the string does not yet exist in the hash table. print 'no'
            if self.A[hash] == None:
                print('no')
            # otherwise, traverse through the linked list pointed at by the array element and look for the string
            # print 'yes' if the string is found in the hash table
            # otherwise, print 'no'
            else:
                head = self.A[hash]
                count = 0
                while head.next != None: # traverse through the linked list until the second from last node
                    if head.key == query.s:
                        print('yes')
                        count += 1
                        break
                    else:
                        head = head.next
                if count == 0:
                    if head.key == query.s: # check if the string is stored in the last node. head now represents the last node
                        if head.key == query.s:
                            print('yes')
                            count += 1
                    if count == 0: # if no string is found in the entire list, print 'no'
                        print('no')

        if query.type == 'del':
            hash = self._hash_func(query.s)
            # if there is the array element associated with the hash value does not point to any list,
            # that means the string does not yet exist in the hash table. ignore the query
            if self.A[hash] == None:
                return
            # otherwise, traverse through the linked list pointed at by the array element and look for the string
            # delete the string from the linked list if found
            # if there is more than one string (node) in the linked list, update the pointer next of the previous node and, if needed, the pointer prev of the next node
            # if there are multiple instances of the same string in the chain, delete them all
            else:
                self.del_(hash, query.s)

        if query.type == 'check':
            result = []
            if self.A[query.ind] == None:
                print() # print a blank line if the chain is empty
            else:
                curr_node = self.A[query.ind]
                while curr_node.next != None:
                    result.append(curr_node.key)
                    curr_node = curr_node.next
                result.append(curr_node.key) # append the string stored in the last node to result
                print(' '.join(result)) # print the chain with the passed in index

    # this method reads the input that contains all queries and subsequently calls in process_query() method to process individual queries
    def process_queries(self):
       fname = '06'
        with open(fname, 'r') as testfile:
            queries = []
            for line in testfile.readlines():
                line = line.strip()
                if line != '\n':
                    queries.append(Query(line.split()))
        n = len(queries)
        for i in range(n):
            self.process_query(queries[i])
            #chain_lst = self.chain_lst()
            #print(chain_lst) # print the hash table after each query


if __name__ == '__main__':
    bucket_count = 43 # given as part of the assignment
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

