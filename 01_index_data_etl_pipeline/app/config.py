from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite:///./index_pipeline.db"
    aws_region: str = "ap-south-1"
    s3_bucket: str | None = None
    s3_input_key: str | None = None
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
