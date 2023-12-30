from flask_admin import Admin

from src.admin.base import SecureIndexView, SecureModelView
from src.admin.user import UserView
from src.admin.post import PostView

admin = Admin(index_view=SecureIndexView(), template_mode='bootstrap4')