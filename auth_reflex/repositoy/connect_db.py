from sqlmodel import create_engine

def connect():
    engine = create_engine("mysql+pymysql://username:password@host_of_data_base:port/name_data_base")
    return engine