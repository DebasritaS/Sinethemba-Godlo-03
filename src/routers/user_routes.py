from fastapi import APIRouter, HTTPException
from models.user import UserCreateRequest, UserResponse

router = APIRouter()

@router.post("/users", response_model=UserResponse, summary="Create a new user")
def create_user(user: UserCreateRequest):
    """
    Create a new user in the system.
    
    - **user_id**: Unique user identifier
    - **name**: Full name
    - **email**: Email address
    - **roles**: List of user roles
    """
    # Here you would call your service, e.g., user_service.create(user)
    return user  # just echoing for example

@router.get("/users/{user_id}", response_model=UserResponse, responses={
    404: {"description": "User not found"},
})
def get_user(user_id: str):
    """
    Get a user by ID.

    Returns 404 if the user does not exist.
    """
    if user_id != "123":  # simulate not found
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(user_id="123", name="Test User", email="test@example.com", roles=["Admin"])
