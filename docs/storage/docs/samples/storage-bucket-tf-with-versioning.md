---
url: https://docs.cloud.google.com/storage/docs/samples/storage-bucket-tf-with-versioning/
title: Create a Bucket to store Terraform state \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:56.220221+00:00
---

# Create a Bucket to store Terraform state  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-bucket-tf-with-versioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a Bucket to store Terraform state Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a Bucket with Object Versioning enabled in the US multi-region to store Terraform state.

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "default" {
      name          = "${random_id.bucket_prefix.hex}-bucket-tfstate"
      force_destroy = false
      location      = "US"
      storage_class = "STANDARD"
      versioning {
        enabled = true
      }
      encryption {
        default_kms_key_name = google_kms_crypto_key.terraform_state_bucket.id
      }
      depends_on = [
        google_project_iam_member.default
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
