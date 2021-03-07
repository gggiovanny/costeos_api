from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = ""


class DotEnvSettings(BaseSettings):
    use_dev_api: str = "0"

    class Config:
        env_file = ".env"


settings = Settings()
dotenvsettings = DotEnvSettings()
