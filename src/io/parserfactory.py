# -*- coding: utf-8 -*-

if __name__ == '__main__':
    pass    
else:
    from .pairfileheaderparser import PairFileHeaderParser
    from .pointdatafileparser import PointDataFileParser
    from .parser import FileParser
    

class FileParserFactory:
    @classmethod
    def CreatePointFileParser(cls, filename):
        return FileParser(filename, PairFileHeaderParser(), PointDataFileParser())