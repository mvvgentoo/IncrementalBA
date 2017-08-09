# -*- coding: utf-8 -*-

from math import sqrt


class ImageDimension:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def GetW(self):
        return self.w

    def GetH(self):
        return self.h


class DataNormalizationStrategy:

    def __init__(self):
        pass

    def Normalize(self, data):
        raise NotImplementedError


class DataNormalizationDimensionBased(DataNormalizationStrategy):

    def __init__(self, params):  # : ImageDimension
        super(DataNormalizationDimensionBased, self).__init__()
        self.params = params

    def Normalize(self, data):
        w = self.params.GetW()
        h = self.params.GetH()
        center = [w / 2.0, h / 2.0]

        ndata = []
        normCoeff = 1.0 / sqrt(w * h)

        for line in data:
            tempArray = [None] * 4

            for i in range(0,4):
                tempArray[i] = (line[i] - center[i % 2]) * normCoeff

            ndata.append(tempArray)

        return ndata


