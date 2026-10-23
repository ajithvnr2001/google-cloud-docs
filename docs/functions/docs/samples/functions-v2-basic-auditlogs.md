---
url: https://docs.cloud.google.com/functions/docs/samples/functions-v2-basic-auditlogs/
title: Deploy Cloud Function 2nd gen with Audit Log trigger using Terraform \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:37.323340+00:00
---

# Deploy Cloud Function 2nd gen with Audit Log trigger using Terraform  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-v2-basic-auditlogs/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Deploy Cloud Function 2nd gen with Audit Log trigger using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Full terraform config to deploy an event-driven Cloud Function 2nd gen with resources

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # This example follows the examples shown in this Google Cloud Community blog post
    # https://medium.com/google-cloud/applying-a-path-pattern-when-filtering-in-eventarc-f06b937b4c34
    # and the docs:
    # https://cloud.google.com/eventarc/docs/path-patterns
    
    resource "google_storage_bucket" "source-bucket" {
      name     = "gcf-source-bucket"
      location = "US"
      uniform_bucket_level_access = true
    }
    
    resource "google_storage_bucket_object" "object" {
      name   = "function-source.zip"
      bucket = google_storage_bucket.source-bucket.name
      source = "function-source.zip"  # Add path to the zipped function source code
    }
    
    resource "google_service_account" "account" {
      account_id   = "gcf-sa"
      display_name = "Test Service Account - used for both the cloud function and eventarc trigger in the test"
    }
    
    # Note: The right way of listening for Cloud Storage events is to use a Cloud Storage trigger.
    # Here we use Audit Logs to monitor the bucket so path patterns can be used in the example of
    # google_cloudfunctions2_function below (Audit Log events have path pattern support)
    resource "google_storage_bucket" "audit-log-bucket" {
      name     = "gcf-auditlog-bucket"
      location = "us-central1"  # The trigger must be in the same location as the bucket
      uniform_bucket_level_access = true
    }
    
    # Permissions on the service account used by the function and Eventarc trigger
    resource "google_project_iam_member" "invoking" {
      project = "my-project-name"
      role    = "roles/run.invoker"
      member  = "serviceAccount:${google_service_account.account.email}"
    }
    
    resource "google_project_iam_member" "event-receiving" {
      project = "my-project-name"
      role    = "roles/eventarc.eventReceiver"
      member  = "serviceAccount:${google_service_account.account.email}"
      depends_on = [google_project_iam_member.invoking]
    }
    
    resource "google_project_iam_member" "artifactregistry-reader" {
      project = "my-project-name"
      role     = "roles/artifactregistry.reader"
      member   = "serviceAccount:${google_service_account.account.email}"
      depends_on = [google_project_iam_member.event-receiving]
    }
    
    resource "google_cloudfunctions2_function" "function" {
      depends_on = [
        google_project_iam_member.event-receiving,
        google_project_iam_member.artifactregistry-reader,
      ]
      name = "gcf-function"
      location = "us-central1"
      description = "a new function"
    
      build_config {
        runtime     = "nodejs12"
        entry_point = "entryPoint" # Set the entry point in the code
        environment_variables = {
          BUILD_CONFIG_TEST = "build_test"
        }
        source {
          storage_source {
            bucket = google_storage_bucket.source-bucket.name
            object = google_storage_bucket_object.object.name
          }
        }
      }
    
      service_config {
        max_instance_count  = 3
        min_instance_count = 1
        available_memory    = "256M"
        timeout_seconds     = 60
        environment_variables = {
            SERVICE_CONFIG_TEST = "config_test"
        }
        ingress_settings = "ALLOW_INTERNAL_ONLY"
        all_traffic_on_latest_revision = true
        service_account_email = google_service_account.account.email
      }
    
      event_trigger {
        trigger_region = "us-central1" # The trigger must be in the same location as the bucket
        event_type = "google.cloud.audit.log.v1.written"
        retry_policy = "RETRY_POLICY_RETRY"
        service_account_email = google_service_account.account.email
        event_filters {
          attribute = "serviceName"
          value = "storage.googleapis.com"
        }
        event_filters {
          attribute = "methodName"
          value = "storage.objects.create"
        }
        event_filters {
          attribute = "resourceName"
          value = "/projects/_/buckets/${google_storage_bucket.audit-log-bucket.name}/objects/*.txt" # Path pattern selects all .txt files in the bucket
          operator = "match-path-pattern" # This allows path patterns to be used in the value field
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
