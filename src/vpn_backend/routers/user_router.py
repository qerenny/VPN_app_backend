from typing import List, Optional

from fastapi import APIRouter, Depends, status

from vpn_backend.schemas.user_schema import UserRegistrationSchema, UserLoginSchema
from vpn_backend.services.user_service import UserService
from vpn_backend.configs.database.engine import get_db_connection

UserRouter = APIRouter(
    prefix="/users", tags=["user"]
)

@UserRouter.post(
    "/registration",
)
async def registration(
    user: UserRegistrationSchema,
    userService: UserService = Depends(get_db_connection),
):
    return await userService.registration(user)


@UserRouter.post(
    "/login"
)
async def login(
    user: UserLoginSchema,
    userService: UserService = Depends(get_db_connection),
):
    return await userService.login(user)


@UserRouter.get("/get-all")
async def get_all(
    userService: UserService = Depends(get_db_connection),
):
    return await userService.list()

@UserRouter.get("/{id}")
async def get(id: int, userService: UserService = Depends(get_db_connection)):
    return await userService.get(id).normalize()


# @UserRouter.post(
#     "/",
#     response_model=AuthorSchema,
#     status_code=status.HTTP_201_CREATED,
# )
# def create(
#     author: AuthorPostRequestSchema,
#     authorService: AuthorService = Depends(),
# ):
#     return authorService.create(author).normalize()
#
#
# @UserRouter.patch("/{id}", response_model=AuthorSchema)
# def update(
#     id: int,
#     author: AuthorPostRequestSchema,
#     authorService: AuthorService = Depends(),
# ):
#     return authorService.update(id, author).normalize()
#
#
# @UserRouter.delete(
#     "/{id}", status_code=status.HTTP_204_NO_CONTENT
# )
# def delete(
#     id: int, authorService: AuthorService = Depends()
# ):
#     return authorService.delete(id)
