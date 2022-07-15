import os, datetime
import re
import sqlalchemy as sa
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
# from werkzeug.security import generate_password_hash, check_password_hash


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
    is_knee_bend = sa.Column(sa.Boolean())
    is_knee_unbend = sa.Column(sa.Boolean())
    is_injured_arm_movemented = sa.Column(sa.Boolean())
    percent_of_injured_arm_movemented = sa.Column(sa.Integer)
    is_elbow_bend = sa.Column(sa.Boolean())
    is_elbow_unbend = sa.Column(sa.Boolean())
    is_forearm_bend = sa.Column(sa.Boolean())
    is_forearm_unbend = sa.Column(sa.Boolean())
    is_injured_finger_movemented = sa.Column(sa.Boolean())
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
                Strokes.is_knee_bend == self.bool_in_bd(data["is_knee_bend"]),
                Strokes.is_knee_unbend == self.bool_in_bd(data["is_knee_unbend"]),
                Strokes.is_injured_arm_movemented == self.bool_in_bd(data["is_injured_arm_movemented"]),
                Strokes.percent_of_injured_arm_movemented == self.int_in_bd(data["percent_of_injured_arm_movemented"]),
                Strokes.is_elbow_bend == self.bool_in_bd(data["is_elbow_bend"]),
                Strokes.is_elbow_unbend == self.bool_in_bd(data["is_elbow_unbend"]),
                Strokes.is_forearm_bend == self.bool_in_bd(data["is_forearm_bend"]),
                Strokes.is_forearm_unbend == self.bool_in_bd(data["is_forearm_unbend"]),
                Strokes.is_injured_finger_movemented == self.bool_in_bd(data["is_injured_finger_movemented"]),
                Strokes.now_year_to_repair == data["now_year_to_repair"],
                Strokes.where_to_repair == data["where_to_repair"]
            ).all()
            return stroke_resp[0].id


class DB_panel:
    def __init__(self) -> None:
        self.DBS = DB_get()

    def new_date_of_birth(self, date):
        date = date.replace("Jan", "Янв")
        date = date.replace("Feb", "Фев")
        date = date.replace("Mar", "Мар")   
        date = date.replace("Apr", "Апр")
        date = date.replace("May", "Май")
        date = date.replace("Jun", "Июнь")
        date = date.replace("Jul", "Июль")
        date = date.replace("Aug", "Авг")
        date = date.replace("Sept", "Сент")
        date = date.replace("Oct", "Окт")
        date = date.replace("Nov", "Ноя")
        date = date.replace("Dec", "Дек")
        return 

    def get_all_users(self):
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
                    self.new_date_of_birth(user.date_of_birth)
                ])
            return OUT

    def get_user_data(self, user_id):
        with create_session() as session:
            OUT = {}
            req = session.query(Users).filter(Users.id == user_id).one()
            OUT["id"] = req.id
            OUT["name"] = req.name
            OUT["last_name"] = req.last_name
            OUT["date_of_birth"] = req.date_of_birth
            OUT["gender"] = session.query(Genders).filter(Genders.id == req.gender).one().name
            OUT["Country"] = session.query(Countries).filter(Countries.id == req.Country).one().name
            OUT["Phone"] = req.Phone
            if req.Stroke is not None:
                OUT["Selection"] = True 
                req_stroke = session.query(Strokes).filter(Strokes.id == req.Stroke).one()
                OUT["Selection_dict"] = {
                    "type_of_stroke" : session.query(Type_of_stroke).filter(Type_of_stroke.id == req_stroke.type_of_stroke).one().name,
                    "date_of_stroke" : req_stroke.date_of_stroke,
                    "is_knew_reason" : "Да" if req_stroke.is_knew_reason else "Нет",
                    "percent_of_information" : req_stroke.percent_of_information,
                    "is_injured_leg_movemented" :  "Да" if req_stroke.is_injured_leg_movemented else "Нет",
                    "percent_of_injured_leg_movemented" : req_stroke.percent_of_injured_leg_movemented,
                    "is_injured_ankle_movemented" :  "Да" if req_stroke.is_injured_ankle_movemented else "Нет",
                    "is_can_sit" : "Да" if req_stroke.is_can_sit else "Нет",
                    "is_can_state" :  "Да" if req_stroke.is_can_state else "Нет",
                    "is_patient_walk_with_supports" :  "Да" if req_stroke.is_patient_walk_with_supports else "Нет",
                    "is_knee_bend" :  "Да" if req_stroke.is_knee_bend else "Нет",
                    "is_knee_unbend" :  "Да" if req_stroke.is_knee_unbend else "Нет",
                    "is_injured_arm_movemented" :  "Да" if req_stroke.is_injured_arm_movemented else "Нет",
                    "percent_of_injured_arm_movemented" : req_stroke.percent_of_injured_arm_movemented, 
                    "is_elbow_bend" :  "Да" if req_stroke.is_elbow_bend else "Нет",
                    "is_elbow_unbend" :  "Да" if req_stroke.is_elbow_unbend else "Нет",
                    "is_forearm_bend" :  "Да" if req_stroke.is_forearm_bend else "Нет",
                    "is_forearm_unbend" :  "Да" if req_stroke.is_forearm_unbend else "Нет",
                    "is_injured_finger_movemented" :  "Да" if req_stroke.is_injured_finger_movemented else "Нет",
                    "now_year_to_repair" : req_stroke.now_year_to_repair,
                    "where_to_repair" : req_stroke.where_to_repair
                } 
            else:
                OUT["Selection"] = False
        return OUT
    
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
                is_knee_bend = self.DBS.bool_in_bd(data["is_knee_bend"]),
                is_knee_unbend = self.DBS.bool_in_bd(data["is_knee_unbend"]),
                is_injured_arm_movemented = self.DBS.bool_in_bd(data["is_injured_arm_movemented"]),
                percent_of_injured_arm_movemented = self.DBS.int_in_bd(data["percent_of_injured_arm_movemented"]),
                is_elbow_bend = self.DBS.bool_in_bd(data["is_elbow_bend"]),
                is_elbow_unbend = self.DBS.bool_in_bd(data["is_elbow_unbend"]),
                is_forearm_bend = self.DBS.bool_in_bd(data["is_forearm_bend"]),
                is_forearm_unbend = self.DBS.bool_in_bd(data["is_forearm_unbend"]),
                is_injured_finger_movemented = self.DBS.bool_in_bd(data["is_injured_finger_movemented"]),
                now_year_to_repair = data["now_year_to_repair"],
                where_to_repair = data["where_to_repair"]
            ))
        with create_session() as session:
            stroke_id = self.DBS.get_id_stroke(data)
        return stroke_id


    def create_new_user(self, form_data):
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
