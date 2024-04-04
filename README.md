# Cincinnati Crime Data Engineering Project

## Problem Description
With populations of mid-sized cities swelling due to housing affordability challenges in major metropolitan areas, families and individuals have a number of things to consider when deciding on deiding on relocation destinations. One thing that people increasingly consider is crime in an area. This project aims to shed light on crime trends within the context of a rapidly growing mid-sized city: Cincinnati, Ohio. By examining crime data in Cincinnati and comparing it to national trends, this project seeks to provide valuable insights for potential residents and policymakers.

## Technologies Used
* [Mage](mage.ai) - Used to pull data from the Cincinnati Open Data API, partition it, and export to Google Cloud Storage
* [Docker](https://www.docker.com/) - Containerization of Mage
* [Terraform](https://www.terraform.io/) - Infrastructure as Code
* [Google Cloud Storage](https://cloud.google.com/storage) - Data lake to hold raw data from API
* [Google Dataproc](https://cloud.google.com/dataproc) - Used to run Apache Spark jobs
* [Spark](https://spark.apache.org/) - Data processing and transformation
* [Google BigQuery](https://cloud.google.com/bigquery) - Data warehouse to store processed data
* [Google Looker Studio](https://cloud.google.com/looker-studio) - Dashboard creation

## Project Architecture
![finalpipeline](https://github.com/PeterD5353/ohio-crime-data/assets/58152012/77c28ceb-4f49-4e47-a6d0-cd7ac11ded1d)

## Dashboard
![dashboard](https://github.com/PeterD5353/ohio-crime-data/assets/58152012/6362a992-ec7c-4c18-9b6d-2cb31ef90393)


## Reproducing this Project
### Prerequisites 
* [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
* [Terraform](https://developer.hashicorp.com/terraform/install)

### Steps to Reproduce
* Create a new project in GCP
* Enable Google Cloud Storage, BigQuery, and Dataproc APIs
* Clone this repo
* Create a service account with the following roles: Storage Admin, Storage Object Admin, BigQuery Data Editor, Dataproc Editor, Dataproc Worker, and Service Account User
* Create a json key for the service account and upload that key into the mage directory
* Run the following to set your credentials and verify authentication
```
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
```
* Copy dev.env to .env and remove dev.env
```
cp dev.env .env && rm dev.env
```
* Fill in .env with your information and run the following to set environment variables
```
source .env
```
* Change to the terraform directory and create the infrastructure
```
cd terraform
terraform init
terraform apply
```
* Change to the mage directory and start the mage docker compose
```
cd ../mage
docker compose up
```
* Fill in the io_config.yaml with your credentials
* Navigate to the cincinnati_api_to_gcs pipeline and run it
* Copy the pyspark file to your bucket
```
gsutil cp pyspark_gcs_to_bq.py gs://<your_bucket_name>
```
* Submit the job to dataproc
```
gcloud dataproc jobs submit pyspark \
    gs://<>your_bucket_name/pyspark_gcs_to_bq.py \
    --cluster=<YOUR_CLUSTER_NAME> \
    --region=<YOUR_REGION> \
    --project=<YOUR_PROJECT_ID> \
    --properties=spark.env.PROJECT_NAME=<your_project_id>,spark.env.TF_VAR_bucket_name=<your_bucket_name>
```
* load Looker Studio and select the BigQuery Cincinnati crime table as your data source
