from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from lovedatabase import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
class Love_calculate(BaseModel):
    name1:str
    name2:str

@app.post('/Love')
def love(data:Love_calculate,db=Depends(get_db)):
    rec=db.query(Love_table).filter(Love_table.name1==data.name1,Love_table.name2==data.name2).first()
    
    
    if rec:
            return {'perc':rec.perc,
                    'message':f'Data already present {data.name1} and {data.name2} your love={rec.perc}% '} 
    else:
        import random
        love=random.randint(10,100)
        new_rec=Love_table(name1=data.name1,name2=data.name2,perc=love)
        db.add(new_rec)
        db.commit()

        if love>90:
                return {'perc':love,
                'message':f'{data.name1} and {data.name2} your love={love}% Your love is very strong get married soon '}
        elif 71<=love<=89:
                return {'perc':love,
                'message':f'{data.name1} and {data.name2} your love={love}% Your love is good continue your love some more time '}
        elif 50<=love<=70:
                return {'perc':love,
                'message':f'{data.name1} and {data.name2} your love={love}% Your love is 50-50 Think again have 2nd chance '}
        elif 35<=love<=49:
                return {'perc':love,
                        'message':f'{data.name1} and {data.name2} your love={love}% love is not good option. Being friends is a best choice'}
        else:
            return {'perc':love,
                'message':f'{data.name1} and {data.name2} your love={love}% {data.name1} please dont love anyone be single always..........! '}
        new_rec=Love_table(name1=data.name1,name2=data.name2,perc=love)
        db.add(new_rec)
        db.commit()