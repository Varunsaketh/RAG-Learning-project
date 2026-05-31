class dataquery:
    def get_query(self):
        data =  str(input("Enter your query: "))
        query = [data]
        return query

obj = dataquery()
dataquery = obj.get_query()
print(dataquery)