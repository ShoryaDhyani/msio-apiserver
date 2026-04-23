from dotenv import load_dotenv
from pydantic import BaseModel
import os
from typing import Optional
load_dotenv()


class Settings(BaseModel):
    PROJECT_ID: str = os.getenv("PROJECT_ID")
    REDIS_URL: str = os.getenv("REDIS_URL")
    S3_REGION: str = os.getenv("S3_REGION")
    S3_ACCESS_KEY: str = os.getenv("S3_ACCESS_KEY")
    S3_SECRET_KEY: str = os.getenv("S3_SECRET_KEY")
    CLUSTER: str = os.getenv("CLUSTER")
    TASK: str = os.getenv("TASK")
    PROXY_BASE_PATH: str = os.getenv("PROXY_BASE_PATH", "localhost:9000")

class ProjectRequest(BaseModel):
    gitURL: str
    slug: Optional[str] = None
    name: Optional[str] = None


config = Settings()