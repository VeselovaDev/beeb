from unittest.mock import patch
from src.auth.models import User
from src.auth.schemas import UserSchema
from src.repositories.user import UserRepo
from tests.test_auth.conftest import pass_login


def test_get_login_page_exists(unauthenticated_client):
    response = unauthenticated_client.get("/login")
    assert response.status_code == 200


def test_get_login_has_correct_template(unauthenticated_client):
    response = unauthenticated_client.get("/login")
    assert response.template.name == "auth/login.html"


def test_get_login_redirects_home_if_request_has_valid_cookie(authenticated_client):
    response = authenticated_client.get("/login")
    assert response.status_code == 303
    assert response.headers.get("location") == "/home"


@patch.object(UserRepo, "login", pass_login)
def test_post_login_success(unauthenticated_client):
    response = unauthenticated_client.post(
        "/login", data={"username": "lol", "password": "kek"}
    )

    # if there are no Exceptions, the page always redirects /home
    assert response.status_code == 303


def test_post_login_no_username(unauthenticated_client):
    response = unauthenticated_client.post("/login", data={"password": "kek"})
    assert response.status_code == 422


def test_post_login_no_password(unauthenticated_client):
    response = unauthenticated_client.post("/login", data={"username": "lol"})
    assert response.status_code == 422


def test_post_login_no_username_no_password(unauthenticated_client):
    response = unauthenticated_client.post("/login")
    assert response.status_code == 422


def test_post_login_username_is_empty_string(unauthenticated_client):
    response = unauthenticated_client.post(
        "/login", data={"username": "", "password": "kek"}
    )
    assert response.status_code == 422


def test_post_login_username_is_too_long(unauthenticated_client):
    response = unauthenticated_client.post(
        "/login", data={"username": "boop" * 256, "password": "kek"}
    )
    assert response.status_code == 422
