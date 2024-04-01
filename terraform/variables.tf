variable "credentials" {
  description = "GCP Service Account Credentials"
  type = string
}

variable "project_id" {
    description = "GCP Project ID"
    type = string
}

variable "region" {
  description = "GCP Region"
  default = "us-central1"
}

variable "location" {
  description = "GCP Project Location"
  default = "US"
}

variable "dataset_id" {
  description = "BigQuery Dataset Name"
  default = "ohio_crime_data" 
}

variable "bucket_name" {
  description = "GCS Bucket Name"
  type = string
}

variable "storage_class" {
    description = "GCS Bucket Storage Class"
    default = "STANDARD"
}

variable "dataproc_cluster_name" {
  description = "Name of the Dataproc Cluster"
  type = string
}

variable "cluster_machine_type" {
   description = "Machine type for Dataproc Cluster"
    default = "n1-standard-2"
}

