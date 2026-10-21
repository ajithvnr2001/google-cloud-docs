---
url: https://docs.cloud.google.com/functions/docs/samples/functions-v2-basic/
title: Deploy Cloud Function 2nd gen with HTTP trigger using Terraform \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:34.641411+00:00
---

# Deploy Cloud Function 2nd gen with HTTP trigger using Terraform  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-v2-basic/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Deploy Cloud Function 2nd gen with HTTP trigger using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Full terraform config to deploy a Cloud Function 2nd gen with resources

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Terraform Tutorial](https://docs.cloud.google.com/functions/docs/tutorials/terraform)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = ">= 4.34.0"
        }
      }
    }
    
    resource "random_id" "default" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name                        = "${random_id.default.hex}-gcf-source" # Every bucket name must be globally unique
      location                    = "US"
      uniform_bucket_level_access = true
    }
    
    data "archive_file" "default" {
      type        = "zip"
      output_path = "/tmp/function-source.zip"
      source_dir  = "functions/hello-world/"
    }
    resource "google_storage_bucket_object" "object" {
      name   = "function-source.zip"
      bucket = google_storage_bucket.default.name
      source = data.archive_file.default.output_path # Add path to the zipped function source code
    }
    
    resource "google_cloudfunctions2_function" "default" {
      name        = "function-v2"
      location    = "us-central1"
      description = "a new function"
    
      build_config {
        runtime     = "nodejs22"
        entry_point = "helloHttp" # Set the entry point
        source {
          storage_source {
            bucket = google_storage_bucket.default.name
            object = google_storage_bucket_object.object.name
          }
        }
      }
    
      service_config {
        max_instance_count = 1
        available_memory   = "256M"
        timeout_seconds    = 60
      }
    }
    
    resource "google_cloud_run_service_iam_member" "member" {
      location = google_cloudfunctions2_function.default.location
      service  = google_cloudfunctions2_function.default.name
      role     = "roles/run.invoker"
      member   = "allUsers"
    }
    
    output "function_uri" {
      value = google_cloudfunctions2_function.default.service_config[0].uri
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
