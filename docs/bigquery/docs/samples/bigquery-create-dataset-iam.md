---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-dataset-iam/
title: Create a dataset and grant access to it \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:15.497079+00:00
---

# Create a dataset and grant access to it  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-dataset-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a dataset and grant access to it Stay organized with collections  Save and categorize content based on your preferences. 

The following example creates a dataset named mydataset, then uses the google_bigquery_dataset_iam_policy resource to grant access to it.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_bigquery_dataset" "default" {
      dataset_id                      = "mydataset"
      default_partition_expiration_ms = 2592000000  # 30 days
      default_table_expiration_ms     = 31536000000 # 365 days
      description                     = "dataset description"
      location                        = "US"
      max_time_travel_hours           = 96 # 4 days
    
      labels = {
        billing_group = "accounting",
        pii           = "sensitive"
      }
    }
    
    # Update the user, group, or service account
    # provided by the members argument with the
    # appropriate principals for your organization.
    data "google_iam_policy" "default" {
      binding {
        role = "roles/bigquery.dataOwner"
        members = [
          "user:raha@altostrat.com",
        ]
      }
      binding {
        role = "roles/bigquery.admin"
        members = [
          "user:raha@altostrat.com",
        ]
      }
      binding {
        role = "roles/bigquery.user"
        members = [
          "group:analysts@altostrat.com",
        ]
      }
      binding {
        role = "roles/bigquery.dataViewer"
        members = [
          "serviceAccount:bqcx-1234567891011-abcd@gcp-sa-bigquery-condel.iam.gserviceaccount.com",
        ]
      }
    }
    
    resource "google_bigquery_dataset_iam_policy" "default" {
      dataset_id  = google_bigquery_dataset.default.dataset_id
      policy_data = data.google_iam_policy.default.policy_data
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
