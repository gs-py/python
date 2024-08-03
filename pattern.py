"""

   * 
  ***
 *****
*******
 *****
  ***
   


def pattern(ht):
   
    for i in range(1,ht+1):
      
            print(" "*(ht-i) ,end=" ")
            print("*"*(2*i-1))
        
    for i in range(1,ht):
        print(" "*i,end=" ")
        print("*"*(2*(ht-i) -1))        
nm = int(input("enter the number"))
pattern(nm)
-------------------------------------------------------------------------------------------------------------
"""
"""
class node:
        def __init__(self,data):
                self.data=data
                self.next=None
                
                
class linked_list:
        def __init__(self) :
                self.head=None
        
        @staticmethod
        def printlist(temp):
                
                while(temp):
                        print(temp.data)
                        temp=temp.next
            
if __name__ == '__main__':
        llist = linked_list()
        llist.head = node(1)
        second=node(4)
        thrid=node(87)
        
        llist.head.next =second
        second.next=thrid
        
        linked_list.printlist(llist.head)
        
-------------------------------------------------------------------------------------------------------------"""

"""from collections import Counter

def cn(lsot):
        count1= Counter(lsot)
        return sorted(set(count1.items()))
        
        
lst=[2,4,5,2,1,7,4,2,1]
g=cn(lst)
print(type(g))
print( cn(lst))
"""
def minimumLength(s):
        l=len(s)

        while(s[0] == s[l-1]):
            s=s[1:(l-2)]
            print(s)
            l=len(s)

        return len(s)

f="aabccabba"
print(minimumLength(f))