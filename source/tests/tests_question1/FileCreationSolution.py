import os
import h5py
import numpy as np

from source.questions.commontools.Answer_choices import AnswerChoices


class FileCreationSolution: 
    
    def __initFileCreation__(self):
        self.__name = "HDF5 questions"
        self.__description = """HDF5 is a weld used file type use over the world in various industry to analyse
        and view data."""
        self.tipsToAnswer = """Read the description in the following file : Question1.pynb. 
        Then implement each method of this class."""
    
    def CreateHdf5_ProblemA(self):
        current_path = os.getcwd()
        directory = current_path + '\\source\\questions\\Question1'
        rawAscanSize = (401, 31)
        rawCscanSize = (401, 93)

        filename = "EvidentChallenge.hdf5"
        file_path = f"{directory}\\{filename}"

        rawAScanPath = directory + '\\RawCycleData\\rawAScan.txt'
        rawCScanPath = directory + '\\RawCycleData\\rawCScan.txt'

        rawAScanData = self.GetDatasetData(rawAscanSize, rawAScanPath)
        rawCScanData = self.GetDatasetData(rawCscanSize, rawCScanPath)
        
        if os.path.isfile(file_path):
            f = h5py.File(file_path, 'r+')
            f['RawAScan'][:] = rawAScanData
            f['RawCScan'][:] = rawCScanData
            f.close()
        else: 
            f = h5py.File(file_path, 'w')
            datasetRawAScan = f.create_dataset("RawAScan", shape=rawAScanData.shape, dtype=h5py.special_dtype(vlen=str))
            datasetRawCScan = f.create_dataset("RawCScan", shape=rawCScanData.shape, dtype=h5py.special_dtype(vlen=str))
            datasetRawAScan[:] = rawAScanData
            datasetRawCScan[:] = rawCScanData
            f.close()

    def CreateHdf5_ProblemB(self):
        current_path = os.getcwd()
        directory = current_path + '\\source\\questions\\Question1'
        rawAscanSize = (401, 31)
        rawCscanSize = (401, 93)
    
        filename = "EvidentChallengeBin.hdf5"
        file_path = f"{directory}\\{filename}"
        rawAScanPath = directory + '\\RawCycleData\\rawAScan.bin'
        rawCScanPath = directory + '\\RawCycleData\\rawCScan.bin'

        # The binary ascan file has a dimension of 149172 which correspond to 
        # the dimension 401x31x12. The students will have to do some calculation to 
        # find the corresponding number of byte per value necessary 
        aScanNumberOfByte = 12
        # The binary cscan file has a dimension of 895032 which correspond to 
        # the dimension 401x93x24. The students will have to do some calculation to 
        # find the corresponding number of byte per value necessary 
        cScanNumberOfByte = 24
        rawAScan = self.GetData(aScanNumberOfByte * 2, rawAScanPath, rawAscanSize)
        rawCScan = self.GetData(cScanNumberOfByte * 2, rawCScanPath, rawCscanSize)

        dtypeAScan = f'S{aScanNumberOfByte * 2 + aScanNumberOfByte-1}'
        dtypeCScan = f'S{aScanNumberOfByte * 2 + aScanNumberOfByte-1}'
        
        rawAscanByte = np.empty(rawAscanSize, dtype=dtypeAScan)
        rawCscanByte = np.empty(rawCscanSize, dtype=dtypeCScan)
        
        for i in range(rawAscanSize[0]):
            rowsAScan = rawAScan[i]
            rowsCScan = rawCScan[i]
            byte_data_rawAscan = [row.encode('utf-8') for row in rowsAScan]
            byte_data_rawCscan = [row.encode('utf-8') for row in rowsCScan]
            rawAscanByte[i] = byte_data_rawAscan
            rawCscanByte[i] = byte_data_rawCscan

        f = h5py.File(file_path, 'w')

        datasetRawAScan = f.create_dataset("RawAScan", data=rawAscanByte)
        datasetRawAScan = f.create_dataset("RawCScan", data=rawCscanByte)

        f.close()

    def GetDatasetData(self, size, path):
        arr = np.genfromtxt(path, delimiter=' ', dtype='str')
        return np.reshape(arr, size)
    
    def GetData(self, numberOfByte, path, size):
        file = open(path, 'rb').read()
        data = ''.join(['{:02x}'.format(byte) for byte in file])
        dataInHexa = [data[i:i + numberOfByte] for i in range(0, len(data), numberOfByte)]
        dataset = [' '.join([elem[i:i + 2] for i in range(0, len(elem), 2)]) for elem in dataInHexa]
        return np.array(dataset).reshape(size)
    
    def GetAScanValue_ProblemC(self):
        current_path = os.getcwd()
        directory = current_path + '\\source\\questions\\Question1'
    
        Q3List = []
        file = h5py.File(directory + '\\EvidentChallenge.hdf5', 'r')
        rawAscanValue = file['RawAScan'][28, 8]
        file.close()
        Q3List.append(rawAscanValue.decode('utf-8'))
        return Q3List   

    def GetCScanValue_ProblemD(self):
        current_path = os.getcwd()
        directory = current_path + '\\source\\questions\\Question1'
    
        Q4List = []
        file = h5py.File(directory + '\\EvidentChallenge.hdf5', 'r')
        rawCscanValue = file['RawCScan'][140, 12:15]
        Q4List.append(rawCscanValue[0].decode('utf-8'))
        Q4List.append(rawCscanValue[1].decode('utf-8'))
        Q4List.append(rawCscanValue[2].decode('utf-8'))
        file.close()
        return Q4List
    
    def MCQ_ProblemE(self):
        return AnswerChoices.C
    
    def MCQ_ProblemF(self):
        return AnswerChoices.D
