from fastapi import APIRouter, Depends
from app.db.schema.user import UserInCreate, UserInLogin, UserWithToken, UserOutput
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.service.userService import UserService
authRouter = APIRouter()

@authRouter.post("/login", status_code=200, response_model=UserWithToken)
def login(loginDetails : UserInLogin, session: Session = Depends(get_db)):
    try:
        return UserService(session=session).login(login_details=loginDetails)
    except Exception as error:
        print(error)
        raise error
    

@authRouter.post("/signup", status_code=201, response_model=UserOutput)
def signUp(signUpDetails : UserInCreate, session : Session = Depends(get_db)):
    try:
        return UserService(session=session).signup(user_details=signUpDetails)
    except Exception as error:
        print(error)
        raise error
   

# router -> service -> repository -> db
# router <- service <- repository <- db
