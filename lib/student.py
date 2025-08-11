#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, new_knowledge: str):
        self.knowledge.append(new_knowledge)
        return self.knowledge

s1 = Student(first_name="Collins", last_name="Joash")
print(s1.first_name)
print(s1.last_name)

s1.learn("I am learning append function in Python") 
print(s1.knowledge[-1]) 