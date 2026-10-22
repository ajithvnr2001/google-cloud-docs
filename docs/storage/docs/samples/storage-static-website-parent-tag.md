---
url: https://docs.cloud.google.com/storage/docs/samples/storage-static-website-parent-tag/
title: Create a configured Cloud Storage bucket \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:43.435794+00:00
---

# Create a configured Cloud Storage bucket  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-static-website-parent-tag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a configured Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Create new storage bucket in the US multi-region, and settings for main_page_suffix and not_found_page

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create new storage bucket in the US multi-region
    # and settings for main_page_suffix and not_found_page
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "static_website" {
      name                        = "${random_id.bucket_prefix.hex}-static-website-bucket"
      location                    = "US"
      storage_class               = "STANDARD"
      uniform_bucket_level_access = true
      website {
        main_page_suffix = "index.html"
        not_found_page   = "404.html"
      }
    }
    
    # Make bucket public by granting allUsers storage.objectViewer access
    resource "google_storage_bucket_iam_member" "public_rule" {
      bucket = google_storage_bucket.static_website.name
      role   = "roles/storage.objectViewer"
      member = "allUsers"
    }
    
    # Upload a simple index.html page to the bucket
    resource "google_storage_bucket_object" "indexpage" {
      name         = "index.html"
      content      = "<html><body>Hello World!</body></html>"
      content_type = "text/html"
      bucket       = google_storage_bucket.static_website.id
    }
    
    # Upload a simple 404 / error page to the bucket
    resource "google_storage_bucket_object" "errorpage" {
      name         = "404.html"
      content      = "<html><body>404!</body></html>"
      content_type = "text/html"
      bucket       = google_storage_bucket.static_website.id
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
