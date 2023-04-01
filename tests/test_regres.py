from pytest_voluptuous import S
from utils.base_session import regres
import schema.schema


def test_create_user():
    create_user = regres.post("/users", {"name": "Nikita", "job": "Quality Assurance"})
    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Nikita"
    assert create_user.json()["job"] == "Quality Assurance"
    assert create_user.json()["createdAt"] is not None
    assert create_user.json()["id"] is not None
    assert S(schema.schema.create_user) == create_user.json()


def test_update_user():
    update_user = regres.put("/users/2", {"name": "Nikita Fedotov", "job": "Quality Control"})
    assert update_user.status_code == 200
    assert update_user.json()["name"] == "Nikita Fedotov"
    assert update_user.json()["job"] == "Quality Control"
    assert update_user.json()["updatedAt"] is not None
    assert S(schema.schema.update_user) == update_user.json()


def test_login_successful():
    login_successfully = regres.post("/login", {"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert login_successfully.status_code == 200
    assert login_successfully.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert S(schema.schema.login_successfully) == login_successfully.json()


def test_login_unsuccessfully():
    login_unsuccessfully = regres.post("/login", {"email": "wrong@email"})
    assert login_unsuccessfully.status_code == 400
    assert len(login_unsuccessfully.content) != 0
    assert S(schema.schema.login_unsuccessfully) == login_unsuccessfully.json()


def test_delete_user():
    delete_user = regres.delete("/users/2")
    assert delete_user.status_code == 204
