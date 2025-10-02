from typing import List,Tuple,Union,Dict
#Fixed type of data type cant do mistakes 


n: int =3

name:str="Hammad"

def sum (a: int,b:int) -> int:
    return a+b

#Advance Types 

numbers : List[int]=[1,23,3,5]

Person : Tuple[str,int] = ("Jawad",35)

Scores : Dict[str,int]={"Science":47,"Urdu":90}

Unions :Union[int ,str] = "13asd31"
