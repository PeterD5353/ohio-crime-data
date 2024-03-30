terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project = var.project_id
  region = var.region
}

# Resources
resource "google_storage_bucket" "data-lake" {
    name = var.bucket_name
    location = var.location
    force_destroy = true
    storage_class = var.storage_class
    }

resource "google_bigquery_dataset" "data-warehouse" {
  dataset_id = var.dataset_id
  location = var.location
}

resource "google_dataproc_cluster" "pyspark-cluster" {
  name = var.dataproc_cluster_name
  region = var.region

  cluster_config {
    master_config {
      num_instances = 1
      machine_type = var.cluster_machine_type
    }
    worker_config {
      num_instances = 2
      machine_type = var.cluster_machine_type
    }
  }
}