from Grid import *
class DrawingInformationHolder():
    """this class holds information about positioning of general structure and particular components on the field.
    
    Component is a group of same elements (like grid of tiles or row/column numbers). Positioning of each individual element is handled in the field class (at least for now).  
    """
    def __init__(self,grid:Grid,fontSize:int,paddingVertical = 30,paddingHorizontal=20):
        self.grid:Grid = grid
        self.legendTile ={'beginPosH':None,'beginPosV':None,'endPosH':None,'endPosV':None}
        self.legendTileLabel = {'beginPosH':None,'beginPosV':None,'endPosH':None,'endPosV':None}
        self.header = {'marginBetweenElementsV':5,'marginBetweenElementsH':2,
                       'legendTile':self.legendTile,'legendTileLabel':self.legendTileLabel}
        
        self.numbersV = {'beginPosH':None,'beginPosV':None,'endPosH':None,'endPosV':None}
        self.numbersH = {'beginPosH':None,'beginPosV':None,'endPosH':None,'endPosV':None}
        self.gridTiles = {'beginPosH':None,'beginPosV':None,'endPosH':None,'endPosV':None}
        self.body = {'marginBetweenElementsV':2,'marginBetweenElementsH':2,'numbersV':self.numbersV,'numbersH':self.numbersH,'grid':self.gridTiles}
        self.footer ={}
        
        marginBetweenSections = 10
        
        self.structure = {'paddingV':paddingVertical,'paddingH':paddingHorizontal,'marginBetweenSections':marginBetweenSections,
                        'fieldBeginPosV':None,'fieldBeginPosH':None,
                        'header':self.header,'headerBeginPosV':None,'headerBeginPosH':None,'headerEndPosV':None,'headerEndPosH':None,
                        'body':self.body,'bodyBeginPosV':None,'bodyBeginPosH':None,'bodyEndPosV':None,'bodyEndPosH':None,
                        'footer':self.footer,'footerBeginPosV':None,'footerBeginPosH':None,'footerEndPosV':None,'footerEndPosH':None,
                        'fieldEndPosV':None,'fieldEndPosH':None
        }
        self.initStructureCoordinates(fontSize)
        self.initHeaderCoordinates()
        self.initBodyCoordinates(fontSize)
        
    def initStructureCoordinates(self,fontSize):
        # marginBetweenSections = 10
        
        fieldBeginPosV = 0
        fieldBeginPosH = 0
        self.structure["fieldBeginPosV"] = fieldBeginPosV
        self.structure["fieldBeginPosH"] = fieldBeginPosH
        
        headerBeginPosV = fieldBeginPosV+self.structure['paddingV']
        headerBeginPosH = fieldBeginPosH+self.structure['paddingH']
        desiredHeaderSectionSize = 40
        headerEndPosV = headerBeginPosV+desiredHeaderSectionSize
        headerEndPosH = headerBeginPosH+self.grid.sizeH # ok
        self.structure["headerBeginPosV"] = headerBeginPosV
        self.structure["headerBeginPosH"] = headerBeginPosH
        self.structure["headerEndPosV"] = headerEndPosV
        self.structure["headerEndPosH"] = headerEndPosH
        
        reservedHSpaceForNumbers = fontSize

        stepV = self.grid.rectHeight+self.grid.margin        
        counter = (self.grid.sizeV)//stepV
        while(counter//10 >0):
            reservedHSpaceForNumbers+=fontSize
            counter = counter//10
        
        reservedVSpaceForNumbers = fontSize
        bodyBeginPosV = headerEndPosV+self.structure['marginBetweenSections']
        bodyBeginPosH = headerBeginPosH
        bodyEndPosV = bodyBeginPosV+self.grid.sizeV+reservedVSpaceForNumbers
        bodyEndPosH = bodyBeginPosH+self.grid.sizeH+reservedHSpaceForNumbers
        self.structure["bodyBeginPosV"] = bodyBeginPosV
        self.structure["bodyBeginPosH"] = bodyBeginPosH
        self.structure["bodyEndPosV"] = bodyEndPosV
        self.structure["bodyEndPosH"] = bodyEndPosH
        
        fieldEndPosV = bodyEndPosV+self.structure['paddingV']
        fieldEndPosH = bodyEndPosH+self.structure['paddingH']
        self.structure["fieldEndPosV"] = fieldEndPosV
        self.structure["fieldEndPosH"] = fieldEndPosH
 
        # Footer is not implemented
            
    def initHeaderCoordinates(self):
        
        desiredLegendTileHeight = 20
        desiredLegendTileLength = 40
        self.legendTile['beginPosH'] = self.structure['headerBeginPosH']
        self.legendTile['endPosH'] = self.legendTile['beginPosH']+desiredLegendTileLength
        
        self.legendTile['beginPosV'] = self.structure['headerBeginPosV']
        self.legendTile['endPosV'] = self.legendTile['beginPosV']+desiredLegendTileHeight
        
        self.legendTileLabel['beginPosH'] = self.legendTile['endPosH']
        self.legendTileLabel['beginPosV'] = self.legendTile['endPosV']+self.header['marginBetweenElementsV']
        
        self.legendTileLabel['endPosH'] = self.legendTileLabel['beginPosH']
        self.legendTileLabel['endPosV'] = self.structure["headerEndPosV"]
    
    def initBodyCoordinates(self,fontSize:int):
        stepV = self.grid.rectHeight+self.grid.margin
        fontOffsetFromCentre=fontSize//2
        
        horizontalSpaceForNumberV = fontSize
        counter = (self.grid.sizeV)//stepV
        while(counter//10 >0):
            horizontalSpaceForNumberV+=fontSize
            counter = counter//10
            
        self.numbersV['beginPosH'] = self.structure['bodyBeginPosH']
        self.numbersV['beginPosV'] = self.structure['bodyBeginPosV']
        
        self.numbersV['endPosH'] = self.numbersV['beginPosH']+horizontalSpaceForNumberV 
        self.numbersV['endPosV'] = self.numbersV['beginPosV']+self.grid.sizeV
        
        self.gridTiles['beginPosH'] = self.numbersV['endPosH']+self.body['marginBetweenElementsH']
        self.gridTiles['endPosH'] = self.gridTiles['beginPosH']+self.grid.sizeH
        
        self.gridTiles['beginPosV'] = self.numbersV['beginPosV']
        self.gridTiles['endPosV'] = self.gridTiles['beginPosH']+self.grid.sizeV
        
        self.numbersH['beginPosH'] = self.gridTiles['beginPosH']
        self.numbersH['endPosH'] = self.gridTiles['endPosH']
        
        self.numbersH['beginPosV'] = self.gridTiles['endPosV']+self.body['marginBetweenElementsV']+fontOffsetFromCentre
        self.numbersH['endPosV'] = self.structure["bodyEndPosV"]