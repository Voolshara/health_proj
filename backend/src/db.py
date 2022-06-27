import os
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
    percent_of_injured_leg_movemented = sa.Column(sa.Boolean())
    is_injured_ankle_movemented = sa.Column(sa.Boolean())
    is_injured_toes_movemented = sa.Column(sa.Boolean())
    is_patient_state_or_sit = sa.Column(sa.Boolean())
    is_patient_walk_with_supports = sa.Column(sa.Boolean())
    is_knee_work = sa.Column(sa.Boolean())
    is_injured_arm_movemented = sa.Column(sa.Boolean())
    percent_of_injured_arm_movemented = sa.Column(sa.Boolean())
    is_elbow_work = sa.Column(sa.Boolean())
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
    fio = sa.Column(sa.String(255))
    date_of_birth = sa.Column(sa.Date)
    gender = sa.Column(sa.Integer, sa.ForeignKey(Genders.id))
    Country = sa.Column(sa.Integer, sa.ForeignKey(Countries.id))
    Phone = sa.Column(sa.String(20))
    Stroke = sa.Column(sa.Integer, sa.ForeignKey(Strokes.id))
    


class DB_new:
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
