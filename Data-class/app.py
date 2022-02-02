from dataclasses import dataclass, field

'''Usual method, need an constructor(__init__ method) to instantiate the objects'''
# class Person:
#     name: str
#     status: str
#     age: int

#     def __init__(self, name, status, age) -> None:
#         self.name = name
#         self.status = status
#         self.age = age

'''Now we define Person as a dataclass. dataclass doesn't need an constructor. but the variable type should be given.'''
#enabled order to compare the objects in the dataclass.
@dataclass(order=True)
class Person:
    sort_index: int = field(init = False, repr= False)
    #repr allows excluding the sorting index in the output.
    name: str
    status: str
    age: int
    '''we are using age as sorting index and initializing it with __post_init__ method. so all the values are already initialized'''
    def __post_init__(self):
        self.sort_index = self.age


person1 = Person('dodgeboi','boink', 24)
person2 = Person('daniboi', 'yoink', 69)
person3 = Person('daniboi', 'yoink', 69)

print(f"Id of person2 =",id(person2))
print(f"Id of person3",id(person3))
print(f"Person1:",person1)
'''what if we want to campare objects with fields?we can do that using sort_index'''
print(person1 > person2)
print(f"is person2 and person3 are similar?",person2 == person3)