from fastapi import FastAPI
from sqladmin import Admin
from app.admin.views import UsersAdmin
from app.news.router import router as news_router
from app.users.router import router as users_router
from app.database import engine
from app.admin.auth import authentication_backend

app = FastAPI()

app.include_router(news_router)
app.include_router(users_router)

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)