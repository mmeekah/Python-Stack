class ClassTest:
    def instance_method(self):
        print(f"Class instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")


    @staticmethod
    def static_method():
        print("Calles static_methos")
    


test = ClassTest()

test.instance_method()#1 type call
ClassTest.instance_method(test)#2 type call



ClassTest.class_method()

    
ClassTest.static_method()