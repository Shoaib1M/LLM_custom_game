from sqlalchemy import Column, Integer, String, Text, ForeignKey,Boolean,DateTime,JSON
from sqlalchemy.sql import func

from Backend.db.database import base


class StoryJob(base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True)
    session_id = Column(String, index=True)
    theme = Column(String, index=True)
    status = Column(String, index=True)
    story_id = Column(Integer,index =True)
    error = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    