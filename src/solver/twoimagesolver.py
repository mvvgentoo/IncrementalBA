if __name__ == '__main__':    
    pass    
else:   
    from ..containers.matrix import Matrix
    from ..containers.datatypes import DataTypes
    from ..math.mathmatrix import MathMatrix
    

class Damper:
    def __init__(self):
        self.mu = 1.0
        self.nu = 1.0
        
    def GetDamperValue(self):
        return self.mu
        
    def SetDamperInitialValue(self, mu, nu):
        self.mu = mu
        self.nu = nu
        
    def UpdateDamperValue(self, params, strategy):
        self.mu, self.nu = strategy.UpdateDamper(self.mu, self.nu, params)        
        

class DamperUpdateStrategy:
    def __init__(self):
        pass
    
    def UpdateDamper(self, mu, nu, rho):
        return [mu,nu]
    
class LM_ClassicDamperUpdateStrategy(DamperUpdateStrategy):    
    def UpdateDamper(self, mu, nu, rho):
        mu = mu * max(1.0/3.0, (1.0 - (2.0* rho - 1.0)**3))
        nu = 2.0
        return [mu, nu]
        
class ClassicFallBackDamperUpdateStrategy(DamperUpdateStrategy):
    def UpdateDamper(self, mu, nu, rho):
        mu = mu * nu
        nu = nu * 2.0
        return [mu, nu]
        
class LM_Damper:
    def __init__(self):
        self.damper = Damper()
        self.damper.SetDamperInitialValue(1.0, 2.0)
        self.updateStrategy = LM_ClassicDamperUpdateStrategy()
        self.fallBackStrategy = ClassicFallBackDamperUpdateStrategy()
    
    def GetDamperValue(self):
        return self.damper.GetDamperValue()
    
    def UpdateDamper(self, params):
        self.damper.UpdateDamperValue(params, self.updateStrategy)    
    
    def UpdateDamper_FallbackStrategy(self, params):
        self.damper.UpdateDamperValue(params, self.fallBackStrategy)
    
class Solver:
    def __init__(self):
        pass    
    
    def Apply(self, model, data):
        
        #Data initialization
        numberOfPoints = data.GetNumberOfPoints()
        numberOfCameras = data.GetCamerasNumber()
        numberOfImagesOfPoints = data.GetNumberOfImagesOfPoints()
        paramsNumber = numberOfPoints + numberOfCameras
        damper = LM_Damper()
        systemMatrix = MathMatrix.zeros(paramsNumber, paramsNumber)
        
        