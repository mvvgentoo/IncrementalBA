if __name__ == '__main__':
    pass
else:
    from ..containers.matrix import Matrix
    from ..containers.datatypes import DataTypes
    from ..math.mathmatrix import MathMatrix
    from damper import *


class DataGainingHelperForPair:

    def __init__(self, arr):
        self.data = arr

    def GetNumberOfPoints(self):
        return len(self.data)

    def GetNumberOfCameras(self):
        return 2

    def GetNumberOfImagesOfPoints(self):
        return len(self.data) * 2

    def GetArray(self):
        return self.data


class TwoImageSolver:

    def __init__(self):
        pass

    def UpdateNormalSystemParams(self, model, params, data, Residuals):

        np = data.GetNumberOfPoints()
        nc = data.GetNumberOfCameras()
        counter = 0
        shift = 0

        RHSVector = [0.0] * len(ResResiduals)
        SystemMatrix = MathMatrix.zeros(paramsNumber, paramsNumber)

        for currPointIndex in range(0, np):
            for currCameraIndex in [0,1]:
                jacRowGroup = model.CalcJacobianRowsForPoint(params, np, nc,
                                                         currPointIndex,
                                                         currCameraIndex)

                jU = jacRowGroup.GetU()
                jV = jacRowGroup.GetV()

                MathHelper.DiadMultWithAdditionTo(jU, jU, SysMatrix)
                MathHelper.DiadMultWithAdditionTo(jV, jV, SysMatrix)

                MathHelper.ColumnMultWithAddition(jU, Residuals[shift],
                                                             RHSVector)
                MathHelper.ColumnMultWithAddition(jV, Residuals[shift + 1],
                                                             RHSVector)

        return [SystemMatrix, RHSVector]

    #Model, DataGainingHelperForPair
    def Apply(self, model, data, initialSolution):

        #Data initialization
        numberOfPoints = data.GetNumberOfPoints()
        numberOfCameras = data.GetCamerasNumber()
        numberOfImagesOfPoints = data.GetNumberOfImagesOfPoints()

        paramsNumber = numberOfPoints + numberOfCameras
        damper = LM_Damper()

        res = model.CalcResidualsForPoint()
        [A, rhs] = UpdateNormalSystemParams(model, params, data, res)





