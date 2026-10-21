---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-jobs-execute-jobs-on-schedule-parent-tag/
title: Running Cloud Run services on a schedule \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:47.464232+00:00
---

# Running Cloud Run services on a schedule  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-jobs-execute-jobs-on-schedule-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Running Cloud Run services on a schedule Stay organized with collections  Save and categorize content based on your preferences. 

Using Cloud Scheduler to securely trigger a Cloud Run service on a schedule. This is similar to using cron jobs.

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_project" "project" {
    }
    
    # Enable Cloud Run API
    resource "google_project_service" "cloudrun_api" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
      project            = data.google_project.project.project_id
    }
    
    # Enable Compute Engine API
    resource "google_project_service" "computeengine_api" {
      service            = "compute.googleapis.com"
      disable_on_destroy = false
      project            = data.google_project.project.project_id
    }
    
    # Enable Cloud Scheduler API
    resource "google_project_service" "cloudscheduler_api" {
      service            = "cloudscheduler.googleapis.com"
      disable_on_destroy = false
      project            = data.google_project.project.project_id
    }
    
    # Cloud Run Invoker Service Account
    resource "google_service_account" "cloud_run_invoker_sa" {
      account_id   = "cloud-run-invoker"
      display_name = "Cloud Run Invoker"
      project      = data.google_project.project.project_id
    }
    
    # Gives service account necessary privs to start job
    resource "google_project_iam_binding" "run_invoker_binding" {
      project = data.google_project.project.project_id
      role    = "roles/run.developer"
      members = ["serviceAccount:${google_service_account.cloud_run_invoker_sa.email}"]
    }
    
    resource "google_project_iam_binding" "token_creator_binding" {
      project = data.google_project.project.project_id
      role    = "roles/iam.serviceAccountTokenCreator"
      members = ["serviceAccount:${google_service_account.cloud_run_invoker_sa.email}"]
    }
    
    # Cloud Run Job
    resource "google_cloud_run_v2_job" "default" {
      name     = "cloud-run-job"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job:latest"
          }
        }
      }
    
      depends_on = [resource.google_project_service.cloudrun_api]
    }
    
    # Cloud Run Job IAM binding
    resource "google_cloud_run_v2_job_iam_binding" "binding" {
      project    = data.google_project.project.project_id
      location   = google_cloud_run_v2_job.default.location
      name       = google_cloud_run_v2_job.default.name
      role       = "roles/viewer"
      members    = ["serviceAccount:${google_service_account.cloud_run_invoker_sa.email}"]
      depends_on = [resource.google_cloud_run_v2_job.default]
    }
    
    resource "google_cloud_scheduler_job" "job" {
      name             = "schedule-job"
      description      = "test http job"
      schedule         = "*/8 * * * *"
      attempt_deadline = "320s"
      region           = "us-central1"
      project          = data.google_project.project.project_id
    
      retry_config {
        retry_count = 3
      }
    
      http_target {
        http_method = "POST"
        uri         = "https://run.googleapis.com/v2/projects/${data.google_project.project.project_id}/locations/${google_cloud_run_v2_job.default.location}/jobs/${google_cloud_run_v2_job.default.name}:run"
        body        = base64encode("{}")
    
        headers = {
          "Content-Type" = "application/json"
        }
    
        oauth_token {
          service_account_email = google_service_account.cloud_run_invoker_sa.email
        }
      }
    
      depends_on = [resource.google_project_service.cloudscheduler_api, resource.google_cloud_run_v2_job.default, resource.google_cloud_run_v2_job_iam_binding.binding]
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
