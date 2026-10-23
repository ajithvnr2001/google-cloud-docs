---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-connect-cloud-sql-parent-tag/
title: Create a Cloud Run service with Cloud SQL connectivity via Secret Manager secrets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:09.871372+00:00
---

# Create a Cloud Run service with Cloud SQL connectivity via Secret Manager secrets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-connect-cloud-sql-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Create a Cloud Run service with Cloud SQL connectivity via Secret Manager secrets Stay organized with collections  Save and categorize content based on your preferences. 

This Terraform shows a full example of creating a Cloud SQL instance with authentication stored in Secret Manager, and configuring a Cloud Run instance with those secrets

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_project" "project" {
    }
    
    # Enable Secret Manager API
    resource "google_project_service" "secretmanager_api" {
      service            = "secretmanager.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable SQL Admin API
    resource "google_project_service" "sqladmin_api" {
      service            = "sqladmin.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Cloud Run API
    resource "google_project_service" "cloudrun_api" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    # Creates SQL instance (~15 minutes to fully spin up)
    resource "google_sql_database_instance" "default" {
      name             = "mysql-instance-1"
      region           = "us-central1"
      database_version = "MYSQL_8_0"
      root_password    = "abcABC123!"
    
      settings {
        tier = "db-f1-micro"
        password_validation_policy {
          min_length                  = 6
          complexity                  = "COMPLEXITY_DEFAULT"
          reuse_interval              = 2
          disallow_username_substring = true
          enable_password_policy      = true
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
      depends_on          = [google_project_service.sqladmin_api]
    }
    
    
    # Create dbuser secret
    resource "google_secret_manager_secret" "dbuser" {
      secret_id = "dbusersecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbuser secret
    resource "google_secret_manager_secret_version" "dbuser_data" {
      secret      = google_secret_manager_secret.dbuser.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbuser secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbuser" {
      secret_id = google_secret_manager_secret.dbuser.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    
    
    
    
    # Create dbpass secret
    resource "google_secret_manager_secret" "dbpass" {
      secret_id = "dbpasssecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbpass secret
    resource "google_secret_manager_secret_version" "dbpass_data" {
      secret      = google_secret_manager_secret.dbpass.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbpass secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbpass" {
      secret_id = google_secret_manager_secret.dbpass.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    
    
    
    # Create dbname secret
    resource "google_secret_manager_secret" "dbname" {
      secret_id = "dbnamesecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbname secret
    resource "google_secret_manager_secret_version" "dbname_data" {
      secret      = google_secret_manager_secret.dbname.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbname secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbname" {
      secret_id = google_secret_manager_secret.dbname.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello:latest" # Image to deploy
    
          # Sets a environment variable for instance connection name
          env {
            name  = "INSTANCE_CONNECTION_NAME"
            value = google_sql_database_instance.default.connection_name
          }
          # Sets a secret environment variable for database user secret
          env {
            name = "DB_USER"
            value_source {
              secret_key_ref {
                secret  = google_secret_manager_secret.dbuser.secret_id # secret name
                version = "latest"                                      # secret version number or 'latest'
              }
            }
          }
          # Sets a secret environment variable for database password secret
          env {
            name = "DB_PASS"
            value_source {
              secret_key_ref {
                secret  = google_secret_manager_secret.dbpass.secret_id # secret name
                version = "latest"                                      # secret version number or 'latest'
              }
            }
          }
          # Sets a secret environment variable for database name secret
          env {
            name = "DB_NAME"
            value_source {
              secret_key_ref {
                secret  = google_secret_manager_secret.dbname.secret_id # secret name
                version = "latest"                                      # secret version number or 'latest'
              }
            }
          }
    
          volume_mounts {
            name       = "cloudsql"
            mount_path = "/cloudsql"
          }
        }
        volumes {
          name = "cloudsql"
          cloud_sql_instance {
            instances = [google_sql_database_instance.default.connection_name]
          }
        }
      }
      client     = "terraform"
      depends_on = [google_project_service.secretmanager_api, google_project_service.cloudrun_api, google_project_service.sqladmin_api]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
