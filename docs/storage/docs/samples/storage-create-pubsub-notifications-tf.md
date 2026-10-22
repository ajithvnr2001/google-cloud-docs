---
url: https://docs.cloud.google.com/storage/docs/samples/storage-create-pubsub-notifications-tf/
title: Create a Pub/Sub notification on a Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:52.309003+00:00
---

# Create a Pub/Sub notification on a Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-create-pubsub-notifications-tf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a Pub/Sub notification on a Bucket Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a Pub/Sub notification configuration on a Bucket that sends notifications for all supported events.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/reporting-changes)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    // Create a Pub/Sub notification.
    resource "google_storage_notification" "notification" {
      provider       = google-beta
      bucket         = google_storage_bucket.bucket.name
      payload_format = "JSON_API_V1"
      topic          = google_pubsub_topic.topic.id
      depends_on     = [google_pubsub_topic_iam_binding.binding]
    }
    
    // Enable notifications by giving the correct IAM permission to the unique service account.
    data "google_storage_project_service_account" "gcs_account" {
      provider = google-beta
    }
    
    // Create a Pub/Sub topic.
    resource "google_pubsub_topic_iam_binding" "binding" {
      provider = google-beta
      topic    = google_pubsub_topic.topic.id
      role     = "roles/pubsub.publisher"
      members  = ["serviceAccount:${data.google_storage_project_service_account.gcs_account.email_address}"]
    }
    
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    // Create a new storage bucket.
    resource "google_storage_bucket" "bucket" {
      name                        = "${random_id.bucket_prefix.hex}-example-bucket-name"
      provider                    = google-beta
      location                    = "US"
      uniform_bucket_level_access = true
    }
    
    resource "google_pubsub_topic" "topic" {
      name     = "your_topic_name"
      provider = google-beta
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
