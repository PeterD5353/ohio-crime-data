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


## Reproducing this Project

