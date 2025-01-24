from sqlalchemy import create_engine, Column, String, Boolean, ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import uuid



# Table definitions
class Gate(Base):
    __tablename__ = "gates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    token = Column(String, nullable=False)
    is_default = Column(Boolean, default=False)
    models = relationship("Model", back_populates="gate")

class Model(Base):
    __tablename__ = "models"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    gate_id = Column(UUID(as_uuid=True), ForeignKey("gates.id"), nullable=False)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)
    absolute_path = Column(String, nullable=False)
    type = Column(String, nullable=False)
    gate = relationship("Gate", back_populates="models")
    services = relationship("Service", back_populates="model")

class Service(Base):
    __tablename__ = "services"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    model_id = Column(UUID(as_uuid=True), ForeignKey("models.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    model = relationship("Model", back_populates="services")
    parameters = relationship("ServiceParameter", back_populates="service")
    properties = relationship("ServiceProperty", back_populates="service")

class ServiceParameter(Base):
    __tablename__ = "service_parameters"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    parameter_name = Column(String, nullable=False)
    parameter_value = Column(String, nullable=False)
    service = relationship("Service", back_populates="parameters")

class ServiceProperty(Base):
    __tablename__ = "service_properties"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    property_name = Column(String, nullable=False)
    property_value = Column(String, nullable=False)
    service = relationship("Service", back_populates="properties")

class Space(Base):
    __tablename__ = "spaces"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    ram = Column(Integer, nullable=True)  # RAM in MB
    cpu_cores = Column(Integer, nullable=True)  # Number of CPU cores
    disk_space = Column(Float, nullable=True)  # Disk space in GB
    gpu = Column(String, nullable=True)  # GPU model or details
    bandwidth = Column(Float, nullable=True)  # Bandwidth in Mbps
