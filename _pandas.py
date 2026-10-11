import pandas as pd
data={"day1":1750,"day2":2100,"day3":1700}
serie=pd.Series(data)#declaration of 1d labeled array(series)
print(serie)
# day1    1750
# day2    2100
# day3    1700
# dtype: int64

print(serie[serie>1700])#filtering

data=[10,20,30,40]
serie=pd.Series(data,index=['a','b','c','d'])#series with custom indexing(Default is whole numbers)
print(serie)
# a    10
# b    20
# c    30
# d    40
# dtype: int64
print(serie.loc['a'])#search by custom index
print(serie.iloc[0])#search by tradional whole number

#dataframe
data={"Name": ['rahul','raghu','ali'],
      "age":[18,19,20]}
df= pd.DataFrame(data,index=['employe1','employe2','employe3']);
print(df)
#            Name  age
# employe1  rahul   18
# employe2  raghu   19
# employe3    ali   20
print(df.loc['employe1'])#same as series gievs row

#adding a new collumn
df['Job']=['masti','programer','HR']
#adding a new row
new_rows=pd.DataFrame([{"Name":'Rekha',"age":20,"Job":"masti"},{"Name":"deepak","age":49,"Job":"CEO"}],index=["employe3",'employe4'])
df=pd.concat([df,new_rows])
print(df)

#reading file

df=pd.read_csv("data/data.csv",index_col=1)#imort csv file and selection the second collum as the index which is name in this case
print(df)#prints first 5 and the last 5  rows
print(df.to_string())#prints all rows

df=pd.read_json("data/pokemon.json")
#just converts json/csv to a dataframe
# selection by collumn
print(df)
print(df[["No","Height"]]) #Print Name and Height collumn

#selection by rows
print(df.loc["Bulbasaur"])
print(df.loc["Bulbasaur",["No","Type1"]])#just prints the no and type1 collumn for bulbasaur
print(df.loc["Bulbasaur":"Venusaur",["No","Type1"]])#just prints the no and type1 collumn for pokemon from bulbasaur ro venusaur
print(df.iloc[0:3,0:3])#just prints the collumn numbered 0 to 2 for pokemon number 0 to 2

# example
pokemon = input("Enter name of pokemon: ")
try:
    print(df.loc[pokemon])
except:
    print("not found")

#  filtering
tallpoke=df[(df["Height"]>1 )&(df["Type1"]=="Fire")]
print(tallpoke)

#agregate
#for whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.median(numeric_only=True))
print(df.min(numeric_only=True))
print(df.count())

#single collumn
print(df["Height"].mean())

df=pd.read_csv("data/data.csv")
group1 = df.groupby("Type1")
print(group1["Height"].mean())
print(group1["No"].count())
#data cleaning

df=df.drop(columns=["Legendary","No"])#drop Legendary and No collumn
df=df.dropna(subset=["Type2"])#drop all rows where Type3 is empty
df=df.fillna({'Type2':"None"})#fill  all rows where Type3 is empty with None

df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Fire":"FIRE"})#replace Grass and Fire with GRASS and FIRE respectively

df["Name"]=df["Name"].str.lower()
df["Legendary"]=df["Legendary"].replace({0:False,1:True})#df["Legendary"]=df["Legendary"].astype(bool)

#removing duplicates
df=df.drop_duplicates()
print(df.to_string())
