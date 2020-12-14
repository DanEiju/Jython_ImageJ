from ij import IJ
from ij import ImagePlus
from ij.plugin.frame import ColorThresholder
from ij.process import ImageProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
from ij.measure import ResultsTable
from ij.plugin.filter import ParticleAnalyzer





def ReturnColorThresholdedPicture(PICPATH , L_min , L_max , a_min , a_max , b_min , b_max):
    
    imp = IJ.openImage(PICPATH)
    imp.show()
    ImageTitle = imp.getTitle()

    LabThresold_List =[[L_min , L_max] , [a_min , a_max] , [b_min , b_max]]
    Filt_List = ["pass" , "pass" , "pass"]

    ColorThresholder.RGBtoLab()

    IJ.run(imp, "RGB Stack", "")
    IJ.run("Stack to Images", "")

    IJ.selectWindow("Red")
    IJ.run('Rename...', 'title=0') #title=hoge =(equal)の間にスペースを入れてならない。
    imp0 = IJ.getImage()
    
    IJ.selectWindow("Green")
    IJ.run('Rename...', 'title=1')
    imp1 = IJ.getImage()

    IJ.selectWindow("Blue")
    IJ.run('Rename...', 'title=2')
    imp2 = IJ.getImage()

    for i in range(3):

        WindowTitle = str(i)
        MinValue = float(LabThresold_List[i][0])
        MaxValue = float(LabThresold_List[i][1])
 
        IJ.selectWindow(WindowTitle)
        IJ.setThreshold(MinValue,MaxValue)
        IJ.run(IJ.getImage(), "Convert to Mask", "")


        if Filt_List[i] == "stop":
            ImageProcessor.invert()

    imp3 = ImageCalculator.run(imp0, imp1, "and create")
    imp4 = ImageCalculator.run(imp3,imp2, "and create")

    imp3.show()
    imp4.show()
    ResultTitle = imp4.getTitle()
    IJ.selectWindow(ResultTitle)
    imp4.setTitle(ImageTitle)


    #Saveした時点で画像の情報が失われる.
    imp.close()
    imp0.close()
    imp1.close()
    imp2.close()
    imp3.close()
    
    return imp4