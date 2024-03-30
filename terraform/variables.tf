variable "credentials" {
  description = "GCP Service Account Credentials"
  default="" # fill in with the path to your credentials json file
}

variable "project_id" {
    description = "GCP Project ID"
    default = "" # add your gcp project ID
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
  default = "" # add your globally unique GCS Bucket name 
}

variable "storage_class" {
    description = "GCS Bucket Storage Class"
    default = "STANDARD"
}

variable "dataproc_cluster_name" {
  description = "Name of the Dataproc Cluster"
  default = "pipeline-cluster"
}

variable "cluster_machine_type" {
   description = "Machine type for Dataproc Cluster"
    default = "n1-standard-2"
}