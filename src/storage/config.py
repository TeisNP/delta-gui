"""
Env config loader
"""

from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    """Data class for config"""
    access_key: str
    secret_key: str
    data_path: str


def get_config() -> Config:
    """Load envs into config"""
    env = Env()
    env.read_env(".env", recurse=False)

    return Config(
        access_key=env("AWS_ACCESS_KEY_ID", ""),
        secret_key=env("AWS_SECRET_ACCESS_KEY", ""),
        data_path=env("DATA_PATH", ""),
    )
