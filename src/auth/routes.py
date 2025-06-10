from pathlib import Path
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse, HTMLResponse
from jinja2_fragments.fastapi import Jinja2Blocks


auth_router = APIRouter(tags=["Auth"])

templates_dir = Path(__file__).parent.parent / "templates/auth"
templates = Jinja2Blocks(directory=templates_dir)


@auth_router.get("/login")
def serve_login_template(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "login.html",
    )


@auth_router.post("/login")
def login() -> RedirectResponse:
    response = RedirectResponse("/home", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="token",
        value="lol",
        max_age=1221212121212,
        secure=False,
        samesite="lax",
    )
    return response
