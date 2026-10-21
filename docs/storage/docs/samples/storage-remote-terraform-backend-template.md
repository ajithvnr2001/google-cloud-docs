---
url: https://docs.cloud.google.com/storage/docs/samples/storage-remote-terraform-backend-template/
title: Setup Terraform for a Cloud Storage backend \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:38.043142+00:00
---

# Setup Terraform for a Cloud Storage backend  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-remote-terraform-backend-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Setup Terraform for a Cloud Storage backend Stay organized with collections  Save and categorize content based on your preferences. 

Use Terraform to create a config file for storing Terraform state in Cloud Storage

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Store Terraform state in a Cloud Storage bucket](https://docs.cloud.google.com/docs/terraform/resource-management/store-state)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "random_id" "default" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name     = "${random_id.default.hex}-terraform-remote-backend"
      location = "US"
    
      force_destroy               = false
      public_access_prevention    = "enforced"
      uniform_bucket_level_access = true
    
      versioning {
        enabled = true
      }
    }
    
    resource "local_file" "default" {
      file_permission = "0644"
      filename        = "${path.module}/backend.tf"
    
      # You can store the template in a file and use the templatefile function for
      # more modularity, if you prefer, instead of storing the template inline as
      # we do here.
      content = <<-EOT
      terraform {
        backend "gcs" {
          bucket = "${google_storage_bucket.default.name}"
        }
      }
      EOT
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
