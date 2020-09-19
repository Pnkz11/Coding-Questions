'''
Video: https://www.youtube.com/watch?v=RBSGKlAvoiM&list=PLlj-NlbOH_8RNqFXRZjNpgrf9X0arbiyK&index=3&ab_channel=freeCodeCamp.org 
Code: https://github.com/akzare/Algorithms/blob/master/src/main/python/algorithms/datastructures/stack/Stack.py
'''

'''
Abstract Classes in Python
An abstract class can be considered as a blueprint for other classes. 
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
A class which contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation. 
While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.
 
Why use Abstract Base Classes :
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 
This capability is especially useful in situations where a third-party is going to provide implementations, 
such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes in your mind is difficult or not possible.
'''

from abc import ABC, abstractmethod

class Stack(ABC):

	@abstractmethod
	def size(self):
		'''
		return the number fo elements in the stack
		'''
		pass

	@abstractmethod
	def isEmpty(self):
		'''
		Check if the stack is empty
		'''
		pass

	@abstractmethod
	def push(self):
		'''
		push the element on the stack
		'''
		pass

	@abstractmethod
	def pop(self):
		'''
		pop the element of the stack
		'''
		pass

	@abstractmethod
	def peek(self):
		'''
		look at the top of the stack
		'''
		pass
		

