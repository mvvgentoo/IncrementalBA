if __name__ == '__main__':
    from containers import Matrix, DataTypes, Vector   
    pass
else:
    from ..containers import Matrix, DataTypes   
    
from math import sin,acos, cos    
    
class RotationConverter:    
    @classmethod    
    def AxisAngleToMatrix(cls,v):
        #I + sin() * K + (1 - cos) * K^2
        theta = v.norm(2)
        vn = v.onScalar(1.0/ theta)        
        I = Matrix.identity(3)
        skew = Matrix.skew(vn)
        skewSquare = Matrix.skewSquare(vn)
        R = I + skew.onScalar(sin(theta)) + skewSquare.onScalar(1.0 - cos(theta))
        return R
    
    @classmethod    
    def MatrixToAxisAngle(cls,R):
        trace = R.trace()
        theta = acos( (trace - 1.0 ) * 0.5)
        coeff = 1.0 / (2.0 * sin(theta))
        w = [0] * 3
        w[0] = coeff * [R[2,1] - R[1,2]]
        w[1] = coeff * [R[0,2] - R[2,0]]
        w[2] = coeff * [R[1,0] - R[0,1]]
        return w

if __name__ == '__main__':
    print(RotationConverter.AxisAngleToMatrix(Vector([0,0,3.141592 * 30.0 / 180.0])))