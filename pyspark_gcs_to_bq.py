import os 
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, to_date
from pyspark.sql.types import IntegerType

TABLE_NAME = "cincinnati_data"
DATASET_NAME = "ohio_crime_data"
PROJECT_NAME = os.environ.get("PROJECT_NAME")
BUCKET_NAME = os.environ.get("TF_VAR_bucket_name")
path = "gs://{}/cincinnati_crime_data".format(BUCKET_NAME)

spark = SparkSession.builder \
    .appName("Process Cincinnati Crime Data") \
    .getOrCreate()

parq_df = spark.read.parquet(path)

def encode_violent(ucr_group):
  if ucr_group in ['AGGRAVATED ASSAULTS', 'HOMICIDE', 'RAPE', 'ROBBERY']:
    return 1
  else:
    return 0

encode_violent_udf = udf(encode_violent, IntegerType())

violent_df = parq_df.withColumn('VIOLENT', encode_violent_udf('UCR_GROUP'))

output_df = violent_df

date_columns = ['DATE_REPORTED', 'DATE_FROM', 'DATE_OF_CLEARANCE', 'REPORTED_DATE']

for column in date_columns: 
  output_df = output_df.withColumn(column, to_date(col(column), 'yyyy-MM-dd'))

write_options = {
    "table": f"{PROJECT_NAME}.{DATASET_NAME}.{TABLE_NAME}",
    "project": PROJECT_NAME,
    "dataset": DATASET_NAME,
    "location": "US",
    "timePartitioning": {
        "type": "MONTH",  
        "field": "REPORTED_DATE"  # Specify the partitioning field
    }}

output_df.write.format("bigquery") \
    .option("table", write_options["table"]) \
    .option("project", write_options["project"]) \
    .option("dataset", write_options["dataset"]) \
    .option("location", write_options["location"]) \
    .option("timePartitioning", write_options["timePartitioning"]) \
    .save()
