from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI\SQLEXPRESS;DATABASE=RecSys;Trusted_Connection=yes;"
#'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI\SQLEXPRESS;DATABASE=RecSys;Trusted_Connection=yes;'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()