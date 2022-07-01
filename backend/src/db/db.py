import os, datetime
from more_itertools import last
import sqlalchemy as sa
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


engine = sa.create_engine(
    'mariadb+pymysql://{}:{}@{}:{}/{}'.format(
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
    type_of_stroke = sa.Column(sa.Integer, sa.ForeignKey(Type_of_stroke.id))
    date_of_stroke = sa.Column(sa.Date)
    is_knew_reason = sa.Column(sa.Boolean())
    percent_of_information = sa.Column(sa.Integer)
    is_injured_leg_movemented = sa.Column(sa.Boolean())
    percent_of_injured_leg_movemented = sa.Column(sa.Integer)
    is_injured_ankle_movemented = sa.Column(sa.Boolean())
    is_can_sit = sa.Column(sa.Boolean())
    is_can_state = sa.Column(sa.Boolean())
    is_patient_walk_with_supports = sa.Column(sa.Boolean())
    is_knee_work = sa.Column(sa.Boolean())
    is_injured_arm_movemented = sa.Column(sa.Boolean())
    percent_of_injured_arm_movemented = sa.Column(sa.Integer)
    is_elbow_work = sa.Column(sa.Boolean())
    is_forearm_work = sa.Column(sa.Boolean())
    is_injured_finger_movemented = sa.Column(sa.Boolean())


class Genders(Base):
    __tablename__ = 'Genders'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30))


class Countries(Base):
    __tablename__ = 'Countries'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100))


class Users(Base):
    __tablename__ = 'Users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    last_name = sa.Column(sa.String(255))
    date_of_birth = sa.Column(sa.Date)
    gender = sa.Column(sa.Integer, sa.ForeignKey(Genders.id))
    Country = sa.Column(sa.Integer, sa.ForeignKey(Countries.id))
    Phone = sa.Column(sa.String(20))
    Stroke = sa.Column(sa.Integer, sa.ForeignKey(Strokes.id))


class DB_get:
    def string_to_datetime(self, s):
        if s == "":
            return None
        return datetime.datetime.strptime(s[:10], '%Y-%m-%d').date()

    def bool_in_bd(self, val):
        if val == "":
            return None
        return val

    def int_in_bd(self, val):
        if val == "":
            return None
        try:
            return int(val)
        except:
            return int(val[:-1])

    def get_type_of_stroke(self, name):
        if name == "":
            return None
        with create_session() as session:
            req = session.query(Type_of_stroke).filter(
                    Type_of_stroke.name == name).all()
            if req is None:
                return None
            return req[0].id

    def get_gender(self, name):
        if name == "":
            return None
        with create_session() as session:
            req = session.query(Genders).filter(
                    Genders.name == name).all()
            if req is None:
                return None
            return req[0].id
    
    def get_country(self, name):
        if name == "":
            return None
        with create_session() as session:
            req = session.query(Countries).filter(
                    Countries.name == name).all()
            if req is None:
                return None
            return req[0].id
       
    def get_id_stroke(self, data):
        with create_session() as session:
            stroke_resp = session.query(Strokes).filter(
                Strokes.is_stroked == True,
                Strokes.type_of_stroke == self.get_type_of_stroke(data["type_of_stroke"]),
                Strokes.date_of_stroke == self.string_to_datetime(data["date_of_stroke"]),
                Strokes.is_knew_reason == self.bool_in_bd(data["know_reason"]),
                Strokes.percent_of_information == self.int_in_bd(data["percent_of_information"]),
                Strokes.is_injured_leg_movemented == self.bool_in_bd(data["is_injured_leg_movemented"]),
                Strokes.percent_of_injured_leg_movemented == self.int_in_bd(data["percent_of_injured_leg_movemented"]),
                Strokes.is_injured_ankle_movemented == self.bool_in_bd(data["is_injured_ankle_movemented"]),
                Strokes.is_can_sit == self.bool_in_bd(data["is_can_sit"]),
                Strokes.is_can_state == self.bool_in_bd(data["is_can_state"]),
                Strokes.is_patient_walk_with_supports == self.bool_in_bd(data["is_patient_walk_with_supports"]),
                Strokes.is_knee_work == self.bool_in_bd(data["is_knee_work"]),
                Strokes.is_injured_arm_movemented == self.bool_in_bd(data["is_injured_arm_movemented"]),
                Strokes.percent_of_injured_arm_movemented == self.int_in_bd(data["percent_of_injured_arm_movemented"]),
                Strokes.is_elbow_work == self.bool_in_bd(data["is_elbow_work"]),
                Strokes.is_forearm_work == self.bool_in_bd(data["is_forearm_work"]),
                Strokes.is_injured_finger_movemented == self.bool_in_bd(data["is_injured_finger_movemented"]),
            ).all()
            return stroke_resp[0].id

    
class DB_new:
    def __init__(self) -> None:
        self.DBS = DB_get()

    def create_new_stroke(self, data):
        with create_session() as session:
            session.add(Strokes(
                is_stroked = True,
                type_of_stroke = self.DBS.get_type_of_stroke(data["type_of_stroke"]),
                date_of_stroke = self.DBS.string_to_datetime(data["date_of_stroke"]),
                is_knew_reason = self.DBS.bool_in_bd(data["know_reason"]),
                percent_of_information = self.DBS.int_in_bd(data["percent_of_information"]),
                is_injured_leg_movemented = self.DBS.bool_in_bd(data["is_injured_leg_movemented"]),
                percent_of_injured_leg_movemented = self.DBS.int_in_bd(data["percent_of_injured_leg_movemented"]),
                is_injured_ankle_movemented = self.DBS.bool_in_bd(data["is_injured_ankle_movemented"]),
                is_can_sit = self.DBS.bool_in_bd(data["is_can_sit"]),
                is_can_state = self.DBS.bool_in_bd(data["is_can_state"]),
                is_patient_walk_with_supports = self.DBS.bool_in_bd(data["is_patient_walk_with_supports"]),
                is_knee_work = self.DBS.bool_in_bd(data["is_knee_work"]),
                is_injured_arm_movemented = self.DBS.bool_in_bd(data["is_injured_arm_movemented"]),
                percent_of_injured_arm_movemented = self.DBS.int_in_bd(data["percent_of_injured_arm_movemented"]),
                is_elbow_work = self.DBS.bool_in_bd(data["is_elbow_work"]),
                is_forearm_work = self.DBS.bool_in_bd(data["is_forearm_work"]),
                is_injured_finger_movemented = self.DBS.bool_in_bd(data["is_injured_finger_movemented"]),
            ))
        with create_session() as session:
            stroke_id = self.DBS.get_id_stroke(data)
        return stroke_id


    def create_new_user(self, form_data):
        print(form_data)
        with create_session() as session:
            if form_data["stroke"]:
                stroke_id = self.create_new_stroke(form_data)
            else:
                stroke_id = None
            session.add(Users(
                name = form_data["name"],
                last_name = form_data["last_name"],
                date_of_birth = self.DBS.string_to_datetime(form_data["date_of_birth"]),
                gender = self.DBS.get_gender(form_data["gender"]),
                Country = self.DBS.get_country(form_data["region"]),
                Phone = form_data["phone"],
                Stroke = stroke_id,
            ))

    def set_all_genders(self):
        genders_list = ["Мужской", "Женский", "Другое"] 
        for gender_item in genders_list:
            with create_session() as session:
                session.add(Genders(name=gender_item))

    def set_all_strokes(self):
        strokes_list = ["Ишемический", "Геморрагический", "Другое"] 
        for stroke in strokes_list:
            with create_session() as session:
                session.add(Type_of_stroke(name=stroke))

    def set_all_counters(self):
        country_list = ["США", "Россия", "..."] 
        for country in country_list:
            with create_session() as session:
                session.add(Countries(name=country))    

    def create_all_tables(self):
        Base.metadata.create_all(engine)
        self.set_all_genders()
        self.set_all_strokes()
        self.set_all_counters()


# DBN = DB_new()
# DBN.create_all_tables()
