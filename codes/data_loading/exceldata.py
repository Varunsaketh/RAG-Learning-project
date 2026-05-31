'''
we inmported an excel sheet doc but internally it already consists of 3 sheets in it 
for excel sheets we cant directly convert it to the document type so what we load it using pandas and using it we convert it to the doc format
1.we used xls to load entire excel files using pd.ExcelFile() this func is effeciently used to load excel than the read_excel
2.then for every sheet we created a datafram using pd.read_excel() and then we iterated through every row of the dataframe and created a document for every row
3.we used the column name and value to create the content of the document and also we added the metadata for every document to know from which sheet it is coming and also the source of the document
'''
import pandas as pd
from langchain_core.documents import Document
class exceltodocument:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_excel(self):
       xls = pd.ExcelFile(self.filepath)
       exceldoc = []
       for sheet in xls.sheet_names:
           df = pd.read_excel(self.filepath,sheet_name = sheet)
           for index, row in df.iterrows():
               content = "".join(f"{col} : {value}" for col,value in row.items() if pd.notna(value))
               doc = Document(
                   page_content = content,
                   metadata = {"source": self.filepath, "sheet": sheet}
               )
               exceldoc.append(doc)
       return exceldoc

sol = exceltodocument("Data/excelfiles/python librearies.xlsx")
exceldocuments = sol.load_excel()
print("Excel data loading module executed successfully.")

