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

