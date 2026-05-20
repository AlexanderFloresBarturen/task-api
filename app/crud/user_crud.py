from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user import UserCreate
from app.auth.security import hash_password

def get_user(
        db: Session,
        username: str
):
    return db.query(UserModel).filter(
        UserModel.username == username
    ).first()

#####################################################################

def register_user(
        db: Session,
        user: UserCreate
):
    new_user = UserModel(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
