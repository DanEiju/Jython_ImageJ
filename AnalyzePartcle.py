from ij import IJ
from ij import ImagePlus
from ij.plugin.frame import ColorThresholder
from ij.process import ImageProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
from ij.measure import ResultsTable
from ij.plugin.filter import ParticleAnalyzer





#最終的にはSave先を引数に入れる。SavePath + "/" + Filename closeの方法
def AnalyzeParticle(IMP):
    rm = RoiManager().getInstance2()
    rt = ResultsTable()

    #再現性確保のために最終的には実装
    #IJ.run("Set Measurements...","area  centroid fit redirect=None decimal=3")

    #https://imagej.nih.gov/ij/developer/api/constant-values.html#ij.plugin.filter.ParticleAnalyzer.SHOW_RESULTS
    #表示オプション無し、resultは全部選択
    PA = ParticleAnalyzer(0 , 1043199 , rt, 10000, 300000, 0.2, 1.0)
    PA.setRoiManager(rm)
    PA.analyze(IMP)

    #IJ.run(IMP, "Analyze Particles...", "display clear include add")
    rm.runCommand("Save", "C:/Users/For  Programming/Documents/Python Scripts/OutletHDD/aaa.zip")
    rt.saveAs("C:/Users/For  Programming/Documents/Python Scripts/OutletHDD/aaa.csv")


    #最後に全ての結果をCloseする。
　　#写真を先に消さないとバグる。
    IMP.close()
    rm.close()
    rt.reset()