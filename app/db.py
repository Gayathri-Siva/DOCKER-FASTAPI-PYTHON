import databases
import sqlalchemy
from pydantic import BaseModel


DATABASE_URL = "sqlite:///./fresher_details.db"

database = databases.Database(DATABASE_URL)


metadata = sqlalchemy.MetaData()

fresher_recruiter_details = sqlalchemy.Table(
    "job_application_details",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("course", sqlalchemy.String),
    sqlalchemy.Column("department", sqlalchemy.String),
    sqlalchemy.Column("college_name", sqlalchemy.String),
    sqlalchemy.Column("cgpa", sqlalchemy.Integer),
    sqlalchemy.Column("year_of_passing", sqlalchemy.Integer),
    sqlalchemy.Column("apllied_position", sqlalchemy.String),
    sqlalchemy.Column("status_of_application", sqlalchemy.String)
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)


class Job_application_Detail_In(BaseModel):
    name: str
    course: str
    department: str
    college_name: str
    cgpa: int
    year_of_passing: int
    apllied_position: str
    status_of_application: str

class Job_application_Detail(BaseModel):
    id: int
    name: str
    course: str
    department: str
    college_name: str
    cgpa: int
    year_of_passing: int
    apllied_position: str
    status_of_application: str
