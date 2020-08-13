from utils.ParseExcel import ParseExcel


class TestExcel:

    @classmethod
    def setup_class(self):
        self.pe=ParseExcel()
        self.wb=self.pe.loadWorkBook(r'../data/study.xlsx')

    def test_getSheetByName(self):
        self.sheet=self.pe.getSheetByName("Sheet1")
        print(type(self.sheet))

    def test_getSheetByIndex(self):
        self.sheet=self.pe.getSheetByIndex(0)
        print(type(self.sheet))

    def test_getRowsNumber(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.rows=self.pe.getRowsNumber(self.sheet)
        print(self.rows)

    def test_getColsNumber(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.cols=self.pe.getColsNumber(self.sheet)
        print(self.cols)

    def test_getStartRowNumber(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.startrow=self.pe.getStartRowNumber(self.sheet)
        print(self.startrow)

    def test_getStartColNumber(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.startcols=self.pe.getStartColNumber(self.sheet)
        print(self.startcols)

    def test_getRow(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.rowobj=self.pe.getRow(self.sheet,1)
        print(self.rowobj)

    def test_getColumn(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.colsobj=self.pe.getColumn(self.sheet,2)
        print(self.colsobj)

    def test_getCellOfValue(self):
        self.sheet = self.pe.getSheetByIndex(0)
        value=self.pe.getCellOfValue(self.sheet,rowNo = 1, colsNo = 2)
        print(value)

    def test_getCellOfObject(self):
        self.sheet = self.pe.getSheetByIndex(0)
        obj=self.pe.getCellOfObject(self.sheet,rowNo = 1, colsNo = 2)
        print(obj)

    def test_writeCell(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.pe.writeCell(self.sheet,"失败",rowNo=15,colsNo=15,fontColor="green",fillColor="red")

    def test_writeCellCurrentTime(self):
        self.sheet = self.pe.getSheetByIndex(0)
        self.pe.writeCellCurrentTime(self.sheet,rowNo=15,colsNo=14)








