from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Farm-to-Buyer Coordination System"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB: str = "farm_to_buyer"

    JWT_SECRET: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    MPESA_CONSUMER_KEY: str = ""
    MPESA_CONSUMER_SECRET: str = ""
    MPESA_PASSKEY: str = ""
    MPESA_SHORTCODE: str = "174379"
    MPESA_ENV: str = "sandbox"
    MPESA_CALLBACK_URL: str = ""

    AI_PROVIDER: str = ""
    AI_API_KEY: str = ""
    AI_MODEL: str = ""

    SMS_PROVIDER: str = ""
    SMS_API_KEY: str = ""
    SMS_SENDER_ID: str = ""

    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = ""

    MAPS_API_KEY: str = ""
    UPLOAD_DIR: str = "static/uploads"
    MAX_UPLOAD_MB: int = 10

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
