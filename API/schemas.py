from pydantic import BaseModel

class Customer(BaseModel):
    CustomerID: int

class Forecast(BaseModel):
    Date: str