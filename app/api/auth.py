from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.schemas import UserLogin
from app.core.security import verify_password
from app.database.database import get_db
from app.database.schemas import UserRegister
from app.database import crud

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = crud.get_user_by_username(
        db,
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = crud.create_user(
        db,
        user.username,
        user.password
    )

    return {
        "id": new_user.id,
        "username": new_user.username,
        "message": "User created successfully"
    }
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = crud.get_user_by_username(
        db,
        user.username
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {
        "message": "Login successful",
        "username": existing_user.username
    }
