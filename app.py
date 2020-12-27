from controllers.moderator_controller import *
from controllers.article_controller import *
from controllers.user_controller import *

if __name__ == '__main__':
    db.create_all()
    app.run()
