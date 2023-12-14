from src.admin.base import SecureModelView


class UserView(SecureModelView):
    can_create = False
    can_delete = True
    column_list = ['username', 'email', 'role']
    column_searchable_list = ['username', 'email']