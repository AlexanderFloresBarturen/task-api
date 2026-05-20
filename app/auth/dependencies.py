from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.user_model import UserModel
from app.config import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    user = db.query(UserModel).filter(
        UserModel.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user
