from sqladmin import ModelView


from app.users.model import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.tg_id]
    can_delete = True
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"