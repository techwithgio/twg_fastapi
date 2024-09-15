from pydantic import EmailStr, BaseModel
from typing import Union


class UserInCreate(BaseModel):
    first_name: str
    last_name : str
    email : EmailStr
    password : str

class UserOutput(BaseModel):
    id : int
    first_name: str
    last_name : str
    email : EmailStr

class UserInUpdate(BaseModel):
    id : int
    first_name: Union[str, None ] = None
    last_name : Union[str, None ] = None
    email : Union[EmailStr, None ] = None
    password : Union[str, None ] = None 

class UserInLogin(BaseModel):
    email : EmailStr
    password : str

class UserWithToken(BaseModel):
    token : str
