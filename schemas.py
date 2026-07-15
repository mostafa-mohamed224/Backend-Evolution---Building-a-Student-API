from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    id: int
    name: str
    age: int = Field(gt=0)
    grade: str


class StudentUpdate(BaseModel):
    name: str
    age: int = Field(gt=0)
    grade: str


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    grade: str

    class Config:
        from_attributes = True
