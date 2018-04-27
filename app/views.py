import app.consumers


def ext_f():

    app.consumers.WSDialog.group_send('test', {"message": 'tamere'})
