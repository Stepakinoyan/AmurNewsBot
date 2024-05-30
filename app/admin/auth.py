from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.config import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Validate username/password credentials
        # And update session
        if username == "admin" and password == "123456":
            request.session.update({"token": "21b878e587c75d39d160f058b940d6c776c70923a385f240bf01acabf1dc9f49"})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)

