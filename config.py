import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id', 'image': "http://www.lehigh.edu/google/google_search.png"},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com', 'image':"http://wepartypatriots.com/wp/wp-content/uploads/2013/01/Yahoo_Dock_Icon_by_MazMorris.png"},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>', 'image':"http://icons.iconseeker.com/png/fullsize/3d-cartoon-icons-pack-iii/aol-instant-messenger.png"},
]
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')