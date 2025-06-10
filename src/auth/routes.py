from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from jinja2_fragments.fastapi import Jinja2Blocks

from src.auth.dependencies import user_repo
from src.dependencies import get_block_name
from src.repositories.user import UserRepo

auth_router = APIRouter(tags=["Auth"])

templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Blocks(directory=templates_dir)


@auth_router.get("/login")
def serve_login_template(
    request: Request,
    block_name: Annotated[str | None, Depends(get_block_name)],
) -> HTMLResponse:
    if request.cookies.get("token"):
        return RedirectResponse("/home", status_code=303)
    return templates.TemplateResponse(
        request,
        "auth/login.html",
        block_name=block_name,
    )


@auth_router.post("/login")
def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    repo: Annotated[UserRepo, Depends(user_repo)],
    block_name: Annotated[str | None, Depends(get_block_name)],
    request: Request,
) -> RedirectResponse:
    response = RedirectResponse("/home", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="token",
        value="lol",
        max_age=1221212121212,
        secure=False,
        samesite="lax",
    )
    return response
