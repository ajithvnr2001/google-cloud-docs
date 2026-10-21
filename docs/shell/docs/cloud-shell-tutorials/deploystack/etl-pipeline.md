---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/etl-pipeline/
title: ETL Pipeline \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.222063+00:00
---

# ETL Pipeline  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/etl-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  ETL Pipeline Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-batchetl.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-batchetl.svg)

ETL Pipeline is an architecture for running batch data processing pipelines using the extract, transform, load method. This architecture consists of the following components:

  * **Google Cloud Storage** for landing source data
  * **Dataflow** for performing transformations on the source data
  * **BigQuery** as a destination for the transformed data
  * **Cloud Composer** environment for orchestrating the ETL process



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-etl-pipeline&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-etl-pipeline)

* * *

## ETL Pipeline components

The ETL Pipeline architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/bigquery.svg) | **BigQuery** |  BigQuery is a serverless, cost-effective and multicloud data warehouse designed to help you turn big data into valuable business insights.  |  [smart_display](https://www.youtube.com/watch?v=CFw4peH2UwU) |  [description](https://cloud.google.com/bigquery/docs) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=bigquery__bigquery-quickstart-query-public-dataset)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_composer.svg) | **Cloud Composer** |  A fully managed workflow orchestration service built on Apache Airflow.  |  [smart_display](https://www.youtube.com/watch?v=bwZOAXnCMf8) |  [description](https://cloud.google.com/composer/docs) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=composer--cloud-composer-create-environment)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_storage.svg) | **Cloud Storage** |  Cloud Storage provides file storage and public serving of images over http(s).  |  [smart_display](https://www.youtube.com/watch?v=zvqJ-pcQChE) |  [description](https://cloud.google.com/storage/docs/quickstart-console) |  [keyboard](https://console.cloud.google.com/?tutorial=storage--quickstart-basic-tasks)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying ETL Pipeline. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable Services

Google Cloud Services are disabled in a project by default. In order to use any of the solutions here we have to activate the following:

  * **IAM** — Manages identity and access for Google Cloud resources
  * **Storage** — Service for storing and accessing your data on Google Cloud
  * **Dataflow** — Managed service for executing a wide variety of data processing patterns
  * **BigQuery** — Data platform to create, manage, share, and query data
  * **Composer** — Manages Apache Airflow environments on Google Cloud
  * **Compute** — Virtual machines and Networking Services (used by Composer)


    
    
    variable "gcp_service_list" {
      description = "The list of apis necessary for the project"
      type        = list(string)
      default = [
        "dataflow.googleapis.com",
        "compute.googleapis.com",
        "composer.googleapis.com",
        "storage.googleapis.com",
        "bigquery.googleapis.com",
        "iam.googleapis.com"
      ]
    }
    
    resource "google_project_service" "all" {
      for_each           = toset(var.gcp_service_list)
      project            = var.project_number
      service            = each.key
      disable_on_destroy = false
    }
    

#### Create service account

Creates service account to be used by Composer and Dataflow.
    
    
    resource "google_service_account" "etl" {
      account_id   = "etlpipeline"
      display_name = "ETL SA"
      description  = "user-managed service account for Composer and Dataflow"
      project = var.project_id
      depends_on = [google_project_service.all]
    }
    

#### Assign roles

Grants roles needed to the service account, and grants the Cloud Composer v2 API Service Agent Extension role to the Cloud Composer Service Agent (required for Composer 2 environments).

variable "build_roles_list" { description = "The list of roles that Composer and Dataflow needs" type = list(string) default = [ "roles/composer.worker", "roles/dataflow.admin", "roles/dataflow.worker", "roles/bigquery.admin", "roles/storage.objectAdmin", "roles/dataflow.serviceAgent", "roles/composer.ServiceAgentV2Ext" ] }
    
    
    resource "google_project_iam_member" "allbuild" {
      project    = var.project_id
      for_each   = toset(var.build_roles_list)
      role       = each.key
      member     = "serviceAccount:${google_service_account.etl.email}"
      depends_on = [google_project_service.all,google_service_account.etl]
    }
    
    resource "google_project_iam_member" "composerAgent" {
      project    = var.project_id
      role       = "roles/composer.ServiceAgentV2Ext"
      member     = "serviceAccount:service-${var.project_number}@cloudcomposer-accounts.iam.gserviceaccount.com"
      depends_on = [google_project_service.all]
    }
    
    

#### Create Composer environment

Airflow depends on many micro-services to run, so Cloud Composer provisions the Google Cloud components to run your workflows. These components are collectively known as a Cloud Composer environment.
    
    
    # Create Composer environment
    resource "google_composer_environment" "example" {
      project   = var.project_id
      name      = "example-environment"
      region    = var.region
      config {
    
        software_config {
          image_version = "composer-2.0.12-airflow-2.2.3"
          env_variables = {
            AIRFLOW_VAR_PROJECT_ID  = var.project_id
            AIRFLOW_VAR_GCE_ZONE    = var.zone
            AIRFLOW_VAR_BUCKET_PATH = "gs://${var.basename}-${var.project_id}-files"
          }
        }
        node_config {
          service_account = google_service_account.etl.name
        }
      }
      depends_on = [google_project_service.all, google_service_account.etl, google_project_iam_member.allbuild, google_project_iam_member.composerAgent]
    }
    

#### Create BigQuery dataset and table

Creates a dataset and table in BigQuery to hold the processed data and to make it available for analytics.
    
    
    resource "google_bigquery_dataset" "weather_dataset" {
      project    = var.project_id
      dataset_id = "average_weather"
      location   = "US"
      depends_on = [google_project_service.all]
    }
    
    resource "google_bigquery_table" "weather_table" {
      project    = var.project_id
      dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
      table_id   = "average_weather"
      deletion_protection = false
    
      schema     = <<EOF
    [
      {
        "name": "location",
        "type": "GEOGRAPHY",
        "mode": "REQUIRED"
      },
      {
        "name": "average_temperature",
        "type": "INTEGER",
        "mode": "REQUIRED"
      },
       {
        "name": "month",
        "type": "STRING",
        "mode": "REQUIRED"
      },
       {
        "name": "inches_of_rain",
        "type": "NUMERIC",
        "mode": "NULLABLE"
      },
       {
        "name": "is_current",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
       {
        "name": "latest_measurement",
        "type": "DATE",
        "mode": "NULLABLE"
      }
    ]
    EOF
      depends_on = [google_bigquery_dataset.weather_dataset]
    }
    

#### Create Cloud Storage bucket and add files

Creates a storage bucket to hold files needed for the pipeline, including the source data (inputFile.txt), the target schema (jsonSchema.json), and the user-defined function for the transformation (transformCSCtoJSON.js).
    
    
    # Create Cloud Storage bucket and add files
    resource "google_storage_bucket" "pipeline_files" {
      project       = var.project_number
      name          = "${var.basename}-${var.project_id}-files"
      location      = "US"
      force_destroy = true
      depends_on    = [google_project_service.all]
    }
    
    resource "google_storage_bucket_object" "json_schema" {
      name       = "jsonSchema.json"
      source     = "${path.module}/files/jsonSchema.json"
      bucket     = google_storage_bucket.pipeline_files.name
      depends_on = [google_storage_bucket.pipeline_files]
    }
    
    resource "google_storage_bucket_object" "input_file" {
      name       = "inputFile.txt"
      source     = "${path.module}/files/inputFile.txt"
      bucket     = google_storage_bucket.pipeline_files.name
      depends_on = [google_storage_bucket.pipeline_files]
    }
    
    resource "google_storage_bucket_object" "transform_CSVtoJSON" {
      name       = "transformCSVtoJSON.js"
      source     = "${path.module}/files/transformCSVtoJSON.js"
      bucket     = google_storage_bucket.pipeline_files.name
      depends_on = [google_storage_bucket.pipeline_files]
    }
    

#### Upload DAG file

First uses a data source to determine the appropriate Cloud Storage bucket path for adding the DAG file, then adds the DAG files to the bucket. The DAG file defines the workflows, dependencies, and schedules for Airflow to orchestrate your pipeline.
    
    
    data "google_composer_environment" "example" {
      project    = var.project_id
      region     = var.region
      name       = google_composer_environment.example.name
      depends_on = [google_composer_environment.example]
    }
    
    resource "google_storage_bucket_object" "dag_file" {
      name       = "dags/composer-dataflow-dag.py"
      source     = "${path.module}/files/composer-dataflow-dag.py"
      bucket     = replace(replace(data.google_composer_environment.example.config.0.dag_gcs_prefix, "gs://", ""),"/dags","")
      depends_on = [google_composer_environment.example, google_storage_bucket.pipeline_files, google_bigquery_table.weather_table]
    }
    

* * *

## Conclusion

Once run you should now have an a Composer Environment set up to run ETL jobs on the data presented in the example. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
