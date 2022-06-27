"""
Storage service for fetching data as Delta tables.
"""

from deltalake import DeltaTable
import storage.config as storage_config
from pyarrow import dataset

config = storage_config.get_config()

options: dict[str, str] = {
    "AWS_ACCESS_KEY_ID": config.access_key,
    "AWS_SECRET_ACCESS_KEY": config.secret_key,
}

def get_data(id:str) -> dataset.Dataset:
    """Get participant aggregated data from flow"""
    participant_dt = DeltaTable(config.data_path + "data/", storage_options=options)
    return participant_dt.to_pyarrow_dataset([("id", "=", id)])
