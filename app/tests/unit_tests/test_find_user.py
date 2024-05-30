import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("id", [(14254), (123236765), (67868576)])
async def test_find_user(id: int, ac: AsyncClient):
    response = await ac.post("/users/find", params={"tg_id": id})
    print(response.json())
    assert response.status_code == 200
