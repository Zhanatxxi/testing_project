import uvicorn

from fastapi import FastAPI
from sqladmin import Admin

from collections_core.apps.db.session import engine
from collections_core.apps.service.views import api as dispatcher
from collections_core.apps.clients.views import api as client
from collections_core.apps.service.views import core
from collections_core.apps.clients.admin import UserAdmin
from collections_core.apps.service.admin import DispatcherAdmin, MessageAdmin


app = FastAPI(
    title="Testing project",
    description="""this is project for testing compnay""",
    version="0.1.0"
)

app.include_router(
    dispatcher.router
)
app.include_router(
    client.router
)
app.include_router(
    core.router
)

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(DispatcherAdmin)
admin.add_view(MessageAdmin)

def main():
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True, workers=2)

if __name__ == "__main__":
   main()



