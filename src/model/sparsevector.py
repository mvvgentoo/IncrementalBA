
class SparseVector:
    def __init__(self, realSize, allocSize):
        self.realSize = realSize
        self.allocSize = allocSize
        self.dat = [None] * allocSize
        self.indexes = [None] * allocSize
        self.last = 0
        self.current = 0

    def SetItem(self, index, value):
        self.dat[self.last] = value
        self.indexes[self.last] = index
        self.last = self.last + 1 % self.allocSize

    def SetItemForce(self, index, value, allocIndex):
        if allocIndex >= self.allocSize:
            raise Exception(index, "wrong index in SetItemForce")

        self.dat[allocIndex] = value
        self.indexes[allocIndex] = index

    def GetItem(self, index):
        if index >= self.allocSize:
            raise Exception(index, "wrong index in SetItemForce")

        return (self.indexes[index], self.dat[index])

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.allocSize:
            raise StopIteration
        else:
            index = self.current
            self.current = self.current +  1
            return (self.indexes[index], self.dat[index])

    def GetIndexes(self):
        return self.indexes

    def GetValues(self):
        return self.dat


class JacobianRow:
    def __init__(self, cameraParams, pointParams):
        self.CameraParams = SparseVector(cameraParams[0], cameraParams[1])
        self.PointParams = SparseVector(pointParams[0], pointParams[1])

    def GetCameraValues(self):
        return self.CameraParams()

    def GetPointValues(self):
        return self.PointValues()


class JacobianRowGroup:

    def __init__(self, cameraParams, pointParams):
        self.U = JacobianRow(cameraParams, pointParams)
        self.V = JacobianRow(cameraParams, pointParams)

    def GetU(self):
        return self.U

    def GetV(self):
        return self.V

a = SparseVector(50,3)
a.SetItem(1,33)
a.SetItem(2,43)
a.SetItem(3,333)

for i in a:
    print(i)
