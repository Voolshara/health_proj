import os, datetime
import re
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from types import new_class
import sqlalchemy as sa
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from typer import Typer


engine = sa.create_engine(
    'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        os.getenv('MySQL_NAME'),
        os.getenv('MySQL_PASSWORD'),
        os.getenv('MySQL_HOST'),
        os.getenv('MySQL_PORT'),
        os.getenv('MySQL_DB_NAME_2'),
    )
)


Session = sessionmaker(bind=engine)
Base = declarative_base()


@contextmanager
def create_session(**kwargs):
    new_session = Session(**kwargs) 
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()

    
class Type_of_stroke(Base):
    __tablename__ = 'Type_of_stroke'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30))


class Strokes(Base):
    __tablename__ = 'Strokes'
    id = sa.Column(sa.Integer, primary_key=True)
    is_stroked = sa.Column(sa.Boolean())
    problem_no_stroke = sa.Column(sa.String(1000))
    type_of_stroke = sa.Column(sa.Integer, sa.ForeignKey(Type_of_stroke.id))
    is_kwon_date = sa.Column(sa.Boolean)
    date_of_stroke = sa.Column(sa.Date)
    percent_of_information = sa.Column(sa.Integer)
    is_injured_leg_movemented = sa.Column(sa.Boolean())
    percent_of_injured_leg_movemented = sa.Column(sa.Integer)
    is_injured_ankle_movemented = sa.Column(sa.Boolean())
    is_can_sit = sa.Column(sa.Boolean())
    is_can_state = sa.Column(sa.Boolean())
    is_patient_walk_with_supports = sa.Column(sa.Boolean())
    is_knee_bend = sa.Column(sa.Boolean())
    is_knee_unbend = sa.Column(sa.Boolean())
    video_leg_file = sa.Column(sa.String(50))
    is_injured_arm_movemented = sa.Column(sa.Boolean())
    percent_of_injured_arm_movemented = sa.Column(sa.Integer)
    is_elbow_bend = sa.Column(sa.Boolean())
    is_elbow_unbend = sa.Column(sa.Boolean())
    is_forearm_bend = sa.Column(sa.Boolean())
    is_forearm_unbend = sa.Column(sa.Boolean())
    is_injured_finger_movemented = sa.Column(sa.Boolean())
    video_arm_file = sa.Column(sa.String(50))
    now_year_to_repair = sa.Column(sa.String(5))
    where_to_repair = sa.Column(sa.String(15))


class Genders(Base):
    __tablename__ = 'Genders'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30))


class Countries(Base):
    __tablename__ = 'Countries'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100))


class Users_Info(Base):
    __tablename__ = 'Users_Info'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    last_name = sa.Column(sa.String(255))
    date_of_birth = sa.Column(sa.Date)
    gender = sa.Column(sa.Integer, sa.ForeignKey(Genders.id))
    Country = sa.Column(sa.Integer, sa.ForeignKey(Countries.id))
    City = sa.Column(sa.String(100))
    Phone = sa.Column(sa.String(20))
    Stroke = sa.Column(sa.Integer, sa.ForeignKey(Strokes.id))


class Users(Base):
    __tablename__ = 'Users'
    id = sa.Column(sa.Integer, primary_key=True)
    Email = sa.Column(sa.String(500))
    Password = sa.Column(sa.String(500))
    Now_Token = sa.Column(sa.String(500))
    User_Info = sa.Column(sa.Integer, sa.ForeignKey(Users_Info.id))


class Panel():
    def __init__(self):
        pass
    
    def all_users(self):
        with create_session() as session:
            req = session.query(Users).all()
            OUT = []
            for user in req:
                OUT.append([
                    user.name, 
                    user.last_name, 
                    "М" if user.gender == 1 else "Ж", 
                    session.query(Countries).filter(
                    Countries.id == user.Country).one().name,
                    True if user.Stroke is not None else False,
                    user.id,
                    user.date_of_birth
                ])
            return OUT
    
    def one_user(self, user_id):
        Sel = Selection()

        with create_session() as session:
            OUT = {}
            req = session.query(Users).filter(Users.id == user_id).one()
            OUT["id"] = req.id
            OUT["email"] = req.Email
            OUT["name"] = req.name
            OUT["last_name"] = req.last_name
            OUT["date_of_birth"] = req.date_of_birth
            OUT["gender"] = session.query(Genders).filter(Genders.id == req.gender).one().name
            OUT["Country"] = session.query(Countries).filter(Countries.id == req.Country).one().name
            OUT["City"] = req.City
            OUT["Phone"] = req.Phone
            OUT["Selection_dict"] = Sel.get_data(req.Stroke)
            return OUT


class Authentication:
    def __init__(self):
        pass

    def check_auth(self, json_data):
        with create_session() as session:
            if json_data["email"] == "" or json_data["password"] == "":
                return None
            req = session.query(Users).filter(
                    Users.Email == json_data['email']).one_or_none()
            if not req or not check_password_hash(req.Password, json_data["password"]):
                return None
            return json_data["email"]
            

class Selection:
    def __init__(self):
        pass

    def get_data(self, stroke_id):
        with create_session() as session:
            req_stroke = session.query(Strokes).filter(Strokes.id == stroke_id).one()
            return {
                    "is_stroked" : req_stroke.is_stroked,
                    "problem_no_stroke" : req_stroke.problem_no_stroke,
                    "type_of_stroke" : session.query(Type_of_stroke).filter(Type_of_stroke.id == req_stroke.type_of_stroke).one().name,
                    "is_kwon_date" : req_stroke.is_kwon_date,
                    "date_of_stroke" : req_stroke.date_of_stroke,
                    "percent_of_information" : req_stroke.percent_of_information,
                    "is_injured_leg_movemented" :  "Да" if req_stroke.is_injured_leg_movemented else "Нет",
                    "percent_of_injured_leg_movemented" : req_stroke.percent_of_injured_leg_movemented,
                    "is_injured_ankle_movemented" :  "Да" if req_stroke.is_injured_ankle_movemented else "Нет",
                    "is_can_sit" : "Да" if req_stroke.is_can_sit else "Нет",
                    "is_can_state" :  "Да" if req_stroke.is_can_state else "Нет",
                    "is_patient_walk_with_supports" :  "Да" if req_stroke.is_patient_walk_with_supports else "Нет",
                    "is_knee_bend" :  "Да" if req_stroke.is_knee_bend else "Нет",
                    "is_knee_unbend" :  "Да" if req_stroke.is_knee_unbend else "Нет",
                    "video_leg_file" : "",
                    "is_injured_arm_movemented" :  "Да" if req_stroke.is_injured_arm_movemented else "Нет",
                    "percent_of_injured_arm_movemented" : req_stroke.percent_of_injured_arm_movemented, 
                    "is_elbow_bend" :  "Да" if req_stroke.is_elbow_bend else "Нет",
                    "is_elbow_unbend" :  "Да" if req_stroke.is_elbow_unbend else "Нет",
                    "is_forearm_bend" :  "Да" if req_stroke.is_forearm_bend else "Нет",
                    "is_forearm_unbend" :  "Да" if req_stroke.is_forearm_unbend else "Нет",
                    "is_injured_finger_movemented" :  "Да" if req_stroke.is_injured_finger_movemented else "Нет",
                    "video_arm_file" : "",
                    "now_year_to_repair" : req_stroke.now_year_to_repair,
                    "where_to_repair" : req_stroke.where_to_repair
                } 

    def new_user(self, json_data):
        # print(json_data)
        if not json_data['stroke']:
            stroke_id = self.without_stroke(json_data)
        else:
            stroke_id = self.with_stroke(json_data)
  
        with create_session() as session:
            country = session.query(Countries).filter(
                    Countries.name == json_data["region"]).one()
            country_id = country.id

        with create_session() as session:
            gender = session.query(Genders).filter(
                    Genders.name == json_data["gender"]).one()
            gender_id = gender.id

        user_info_id = self.add_user_inf(json_data, gender_id, country_id, stroke_id)
        password, pass_hash = self.password()
        
        with create_session() as session:
            session.add(Users(
                Email = json_data["email"],
                Password = pass_hash,
                Now_Token = "",
                User_Info = user_info_id
            ))

        return password

    def password(self):
        passwd = ""
        for _ in range(8):
            passwd += chr(randint(ord("a"), ord("z")))
        return passwd, generate_password_hash(passwd)

    def add_user_inf(self, json_data, gender_id, country_id, stroke_id):
        with Session() as session:
            new_info = Users_Info(
                name = json_data["name"],
                last_name = json_data["last_name"],
                date_of_birth = string_to_datetime(json_data["date_of_birth"]),
                gender = gender_id,
                Country = country_id,
                City = json_data["city"],
                Phone = json_data["phone"],
                Stroke = stroke_id,
            )

            session.add(new_info)
            session.commit()
            session_id = new_info.id
        return session_id

    def with_stroke(self, data):
        with Session() as session:
            # get type of stroke
            type_of_stroke = session.query(Type_of_stroke).filter(
                    Type_of_stroke.name == data["type_of_stroke"]).one()
            type_of_stroke_id = type_of_stroke.id

        with Session() as session:
            if data["date_of_stroke"] == "none":
                new_stroke = Strokes(
                    is_stroked = True,
                    problem_no_stroke = data["problem_no_stroke"],
                    type_of_stroke = type_of_stroke_id,
                    is_kwon_date = False,
                    date_of_stroke = datetime.datetime.now(),
                    percent_of_information = int(data["percent_of_information"][:-1]),
                    is_injured_leg_movemented = data["is_injured_leg_movemented"],
                    percent_of_injured_leg_movemented = int(data["percent_of_injured_leg_movemented"][:-1]) if data["percent_of_injured_leg_movemented"] is not None else 0,
                    is_injured_ankle_movemented = data["is_injured_ankle_movemented"],
                    is_can_sit = data["is_can_sit"],
                    is_can_state = data["is_can_state"],
                    is_patient_walk_with_supports = data["is_patient_walk_with_supports"],
                    is_knee_bend = data["is_knee_bend"],
                    is_knee_unbend = data["is_knee_unbend"],
                    video_leg_file = data["video_leg_file"],
                    is_injured_arm_movemented = data["is_injured_arm_movemented"],
                    percent_of_injured_arm_movemented = int(data["percent_of_injured_arm_movemented"][:-1]) if data["percent_of_injured_arm_movemented"] is not None else 0,
                    is_elbow_bend = data["is_elbow_bend"],
                    is_elbow_unbend = data["is_elbow_unbend"],
                    is_forearm_bend = data["is_forearm_bend"],
                    is_forearm_unbend = data["is_forearm_unbend"],
                    is_injured_finger_movemented = data["is_injured_finger_movemented"],
                    video_arm_file = data["video_arm_file"],
                    now_year_to_repair = data["now_year_to_repair"],
                    where_to_repair = data["where_to_repair"]
                )
            else:
                new_stroke = Strokes(
                    is_stroked = True,
                    problem_no_stroke = data["problem_no_stroke"],
                    type_of_stroke = type_of_stroke_id,
                    is_kwon_date = True,
                    date_of_stroke = string_to_datetime(data["date_of_stroke"]),
                    percent_of_information = int(data["percent_of_information"][:-1]),
                    is_injured_leg_movemented = data["is_injured_leg_movemented"],
                    percent_of_injured_leg_movemented = int(data["percent_of_injured_leg_movemented"][:-1]) if data["percent_of_injured_leg_movemented"] is not None else 0,
                    is_injured_ankle_movemented = data["is_injured_ankle_movemented"],
                    is_can_sit = data["is_can_sit"],
                    is_can_state = data["is_can_state"],
                    is_patient_walk_with_supports = data["is_patient_walk_with_supports"],
                    is_knee_bend = data["is_knee_bend"],
                    is_knee_unbend = data["is_knee_unbend"],
                    video_leg_file = data["video_leg_file"],
                    is_injured_arm_movemented = data["is_injured_arm_movemented"],
                    percent_of_injured_arm_movemented = int(data["percent_of_injured_arm_movemented"][:-1]) if data["percent_of_injured_arm_movemented"] is not None else 0,
                    is_elbow_bend = data["is_elbow_bend"],
                    is_elbow_unbend = data["is_elbow_unbend"],
                    is_forearm_bend = data["is_forearm_bend"],
                    is_forearm_unbend = data["is_forearm_unbend"],
                    is_injured_finger_movemented = data["is_injured_finger_movemented"],
                    video_arm_file = data["video_arm_file"],
                    now_year_to_repair = data["now_year_to_repair"],
                    where_to_repair = data["where_to_repair"]
                )
            session.add(new_stroke)
            session.commit()
            session_id = new_stroke.id
        return session_id

    def without_stroke(self, data):
        with Session() as session:
            new_stroke = Strokes(
                is_stroked = False,
                problem_no_stroke = data["problem_no_stroke"],
                type_of_stroke = 1,
                date_of_stroke = datetime.datetime.now(),
                percent_of_information = 0,
                is_injured_leg_movemented = False,
                percent_of_injured_leg_movemented = 0,
                is_injured_ankle_movemented = False,
                is_can_sit = False,
                is_can_state = False,
                is_patient_walk_with_supports = False,
                is_knee_bend = False,
                is_knee_unbend = False,
                video_leg_file = "",
                is_injured_arm_movemented = False,
                percent_of_injured_arm_movemented = 0,
                is_elbow_bend = False,
                is_elbow_unbend = False,
                is_forearm_bend = False,
                is_forearm_unbend = False,
                is_injured_finger_movemented = False,
                video_arm_file = "",
                now_year_to_repair = "",
                where_to_repair = "",
            )
            session.add(new_stroke)
            session.commit()
            session_id = new_stroke.id
        return session_id


def string_to_datetime(s):
    return datetime.datetime.strptime(s[:10], '%Y-%m-%d').date()            


def set_all_genders():
    with create_session() as session:
        genders_list = ["Мужской", "Женский", "Другое"] 
        for gender_item in genders_list:       
            session.add(Genders(name=gender_item))


def set_all_strokes():
    with create_session() as session:
        strokes_list = ["Ишемический", "Геморрагический", "Другое"] 
        for stroke in strokes_list:
            session.add(Type_of_stroke(name=stroke))


def set_all_counters():
    with create_session() as session:
        country_list = ["США", "Россия"] 
        for country in country_list:
            session.add(Countries(name=country))  


def create_all_tables():
    Base.metadata.create_all(engine)
    set_all_genders()
    set_all_strokes()
    set_all_counters()