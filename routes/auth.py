from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from database import get_db
from schemas.user import UserLogin, UserRegister, UserData, UserRegistered, UserAuthFailed
from models.main import UserModel
from utils import get_password_hash, verify_password

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login", response_class=JSONResponse, status_code=200, responses={
  200: {"model": UserData}, 401: {"description": "Invalid email or password"}, 404: {"description": "UserModel not found"}
})
def login(user_data: UserLogin, response: Response, db = Depends(get_db)):
    try:
      result: UserLogin = db.query(UserModel).filter(UserModel.email == user_data.email).first()
      if (verify_password(user_data.password, result.password)):
        return {
          "id": result.id,
          "email": result.email,
          "name": result.name,
          "lastname": result.lastname,
        }
      else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return None
    except Exception as e:
      raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@auth_router.post("/register", response_class=JSONResponse, status_code=201, responses={
  201: {"model": UserRegistered}, 409: {"model": UserAuthFailed}
})
def register(user_data: UserRegister, response: Response, db = Depends(get_db)):
    try:
      print(user_data)
      ## Verify if email or username already exists
      verify_email = db.query(UserModel).filter(UserModel.email == user_data.email).first()
      verify_username = db.query(UserModel).filter(UserModel.username == user_data.username).first()
      
      if (verify_email or verify_username):
        response.status_code = status.HTTP_409_CONFLICT
        response_data = {"isValid": False, "fields": {}}
        if (verify_email):
          response_data["fields"]["email"] = "El email ya se encuentra registrado"
        if (verify_username):
          response_data["fields"]["username"] = "Nombre de usuario ocupado"
        print(response_data)
        return response_data
      
      ## Create user
      db_user = UserModel(email=user_data.email, name=user_data.name, lastname=user_data.lastname, username=user_data.username, password=get_password_hash(user_data.password))
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return {
        "isValid": True,
        "data": {
          "id": db_user.id,
          "email": db_user.email,
          "name": db_user.name,
          "lastname": db_user.lastname,
        }
      }
    except Exception as e:
      print(e)
      raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
