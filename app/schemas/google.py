from pydantic import BaseModel, Field, PositiveInt


class Google(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    delta: PositiveInt
