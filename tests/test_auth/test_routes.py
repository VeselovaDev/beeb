def test_get_login_page_exists(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_get_login_has_correct_template(client):
    response = client.get("/login")
    assert response.template.name == "login.html"


def test_get_login_redirects_if_request_has_valid_cookie(client):
    client.post("/login")
    response = client.get("/login")
    assert response.cookies.get("token")


def test_login_post_route_exists(client):
    response = client.post("/login")
    assert response.status_code == 303


def test_login_post_sets_cookie(client):
    response = client.post("/login")
    assert response.cookies.get("token")
