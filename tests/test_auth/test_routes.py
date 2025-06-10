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


def test_post_login_route_exists(unauthenticated_client):
    response = unauthenticated_client.post(
        "/login", data={"username": "lol", "password": "kek"}
    )
    assert response.status_code == 303
