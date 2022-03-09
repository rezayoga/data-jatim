from dataclasses import dataclass
import time
import uuid
from werkzeug.security import generate_password_hash, \
    check_password_hash
from app import db


@dataclass
class User(db.Model):
    __tablename__ = 'tb_users'

    id: int
    public_id: str
    username: str
    password: str
    fullname: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.String(24), nullable=False)
    movie = db.relationship('Movie', backref='user',
                            lazy=True, cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __init__(self, username, password, fullname):
        self.public_id = str(uuid.uuid4())
        self.username = username
        self.set_password(password)
        self.fullname = fullname
        self.created_at = time.strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'<User id: {self.id} - {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passsword, password)


@dataclass
class Movie(db.Model):
    __tablename__ = 'tb_movies'

    id: int
    user_id: int
    genre: str
    title: str
    directors: str
    actors: str
    year: str
    billboard: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'tb_users.id'), nullable=False)
    genre = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    directors = db.Column(db.String(256), nullable=False)
    actors = db.Column(db.String(256), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    billboard = db.Column(db.String(256), nullable=True)
    created_at = db.Column(db.String(24))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Movie id: {self.id} - {self.title} - {self.genre} - {self.year}>'

