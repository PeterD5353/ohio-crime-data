import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


bucket_name = os.environ.get("BUCKET_NAME")
project_id = os.environ.get("PROJECT_ID")

table_name = "cincinnati_crime_data"

root_path = f"{bucket_name}/{table_name}"


@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['REPORTED_DATE'],
        filesystem = gcs
    )





