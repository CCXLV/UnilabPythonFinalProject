from src.admin.base import SecureModelView


class PostView(SecureModelView):
    edit_modal = True
    create_modal = True
    column_editable_list = ['title']

    column_list = ['title', 'content']

