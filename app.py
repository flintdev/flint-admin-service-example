from admin_service import create_app
from login import authentication


app = create_app()
app.register_authentication(authentication)

if __name__ == "__main__":
    app.start()
