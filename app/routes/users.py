from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, Token

from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token
from app.crud import user_crud

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = user_crud.get_user(
        db,
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    
    return user_crud.register_user(
        db,
        user
    )

#####################################################################

@router.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    current_user = user_crud.get_user(
        db,
        user.username
    )

    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    if not verify_password(
        user.password,
        current_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    access_token = create_access_token(
        {
            "sub": current_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
