from sqlalchemy import Column, Integer, String, Float
from database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    image_size = Column(Float)
    real_size = Column(Float)
    unit = Column(String)