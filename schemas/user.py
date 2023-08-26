from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str
    
    
class UserRegister(BaseModel):
    username: str
    name: str
    lastname: str
    email: str
    password: str
    
class UserData(BaseModel):
    username: str
    name: str
    lastname: str
    email: str
        
class UserRegistered(BaseModel):
    isValid: bool
    data: UserData
    
class UserAuthFailed(BaseModel):
    isValid: bool
    fields: dict