---
url: https://docs.cloud.google.com/storage/docs/samples/storage-new-bucket-parent-tag/
title: Create an object in a Cloud Storage bucket \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:07.709814+00:00
---

# Create an object in a Cloud Storage bucket  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-new-bucket-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create an object in a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create an object in a Cloud Storage bucket

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create new storage bucket in the US multi-region
    # with coldline storage
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "static" {
      name          = "${random_id.bucket_prefix.hex}-new-bucket"
      location      = "US"
      storage_class = "COLDLINE"
    
      uniform_bucket_level_access = true
    }
    
    # Create a text object in Cloud Storage
    resource "google_storage_bucket_object" "default" {
      name = "new-object"
      # Use `source` or `content`
      # source       = "/path/to/an/object"
      content      = "Data as string to be uploaded"
      content_type = "text/plain"
      bucket       = google_storage_bucket.static.id
    }
    
    # Get object metadata
    data "google_storage_bucket_object" "default" {
      name   = google_storage_bucket_object.default.name
      bucket = google_storage_bucket.static.id
    }
    
    output "object_metadata" {
      value = data.google_storage_bucket_object.default
    }
    
    # Get bucket metadata
    data "google_storage_bucket" "default" {
      name = google_storage_bucket.static.id
    }
    
    output "bucket_metadata" {
      value = data.google_storage_bucket.default
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
