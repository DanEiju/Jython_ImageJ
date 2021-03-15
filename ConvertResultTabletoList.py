from ij import IJ
from ij import ImagePlus
from ij.plugin.frame import ColorThresholder
from ij.process import ImageProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
from ij.measure import ResultsTable
from ij.plugin.filter import ParticleAnalyzer
from ij.process import ImageConverter
from ij.gui import PolygonRoi
from ij.gui import Roi



#/**
# * @Parameter ResultTable<type 'ij.measure.ResultsTable'>
# * RTオブジェクトを二次元配列に変換する。
# * rt.saveAs(path)の時は、適度に数字が丸められてFloat型やint型になるが、この方法だと全てのDataがFloat型
# * @return　二次元配列(ヘッダー込み)
# */

def Convert_ResultTabel_to_2Dlis(RT_OBJECT):

    RT_Header_Lis = list(RT_OBJECT.getHeadings())
    
    RT_NumbertParts_Length = int(RT_OBJECT.size())
    
    Result_Lis = [[] for i in range(RT_NumbertParts_Length)]
    
    for ColumnString in (RT_Header_Lis):
    
        for RowNumber in range(RT_NumbertParts_Length):
            
            Result_Value = (RT_OBJECT.getValue(ColumnString,int(RowNumber))) # 	getValueAsDouble でやるとバグる。scフォーラムにも出てくるけど解決策は分らん。

            (Result_Lis[RowNumber]).append((Result_Value))
                
    
    Result_Lis.insert(0,RT_Header_Lis)

    return Result_Lis