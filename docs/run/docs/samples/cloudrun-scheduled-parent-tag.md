---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-scheduled-parent-tag/
title: Call Cloud Run on a schedule \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:10.753255+00:00
---

# Call Cloud Run on a schedule  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-scheduled-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Call Cloud Run on a schedule Stay organized with collections  Save and categorize content based on your preferences. 

Use Cloud Scheduler to generate POST calls on a schedule to a Cloud Run service. 

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_project_service" "run_api" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "iam_api" {
      service            = "iam.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "resource_manager_api" {
      service            = "cloudresourcemanager.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "scheduler_api" {
      service            = "cloudscheduler.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "my-scheduled-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.run_api
      ]
    }
    
    resource "google_service_account" "default" {
      account_id   = "scheduler-sa"
      description  = "Cloud Scheduler service account; used to trigger scheduled Cloud Run jobs."
      display_name = "scheduler-sa"
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.iam_api
      ]
    }
    
    resource "google_cloud_run_service_iam_member" "default" {
      location = google_cloud_run_v2_service.default.location
      service  = google_cloud_run_v2_service.default.name
      role     = "roles/run.invoker"
      member   = "serviceAccount:${google_service_account.default.email}"
    }
    
    resource "google_cloud_scheduler_job" "default" {
      name             = "scheduled-cloud-run-job"
      region           = "us-central1"
      description      = "Invoke a Cloud Run container on a schedule."
      schedule         = "*/8 * * * *"
      time_zone        = "America/New_York"
      attempt_deadline = "320s"
    
      retry_config {
        retry_count = 1
      }
    
      http_target {
        http_method = "POST"
        uri         = google_cloud_run_v2_service.default.uri
    
        oidc_token {
          service_account_email = google_service_account.default.email
        }
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.scheduler_api
      ]
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
