class ModelFactory:
    dct={}
    @classmethod
    def Create(cls,name):
        return cls._Create(name)
    
    def _Create(name):        
        return ModelFactory.dct[name]()
        
    @classmethod    
    def AddToDict(cls, name, fun):
        ModelFactory.dct[name] = fun
        
class BaseModel:
    def __init__(self):
        print ("Created BaseModel")
        
    @classmethod
    def Create(cls):
        return cls()
        
    @classmethod
    def Instantiate(cls):        
        ModelFactory.AddToDict(cls.__name__, cls.Create)
    
    def CalcJacobianRowsForPoint(self, pt):
        raise Exception("CalcJacobianRowsForPoint is not implemented for {}".format(self.__name__) ) 
    
    def CalcResidualsForPoint(self, pt):
        raise Exception("CalcResidualsForPoint is not implemented for {}".format(self.__name__) ) 
                  
        