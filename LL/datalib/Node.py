'''
Created on Jul 30, 2017

@author: Eugene
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.data = data
        

class LLNode(Node):
    def __init__(self, data=None, next=None):
        self.next = next
        super(LLNode, self).__init__(data)
        
