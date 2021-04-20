from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from py_expression import Exp

app = FastAPI()
exp = Exp()

@app.get("/health")
async def health():
    return {"message": "Ok"}


class SolveReq(BaseModel):
    expression: str
    context: Optional[dict]  = None

@app.post("/expression/solve")
async def solve(data:SolveReq ):
    return exp.solve(data.expression,data.context) 


class TreeReq(BaseModel):
    expression: str

@app.post("/expression/tree")
async def tree(data:TreeReq ):
    operand= exp.parse(data.expression) 
    return exp.tree(operand)         