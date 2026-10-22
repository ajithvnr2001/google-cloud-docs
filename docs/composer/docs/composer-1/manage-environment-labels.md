---
url: https://docs.cloud.google.com/composer/docs/composer-1/manage-environment-labels/
title: Manage environment labels and break down environment costs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:52.701489+00:00
---

# Manage environment labels and break down environment costs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/manage-environment-labels/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Manage environment labels and break down environment costs Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/manage-environment-labels "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/manage-environment-labels "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to assign labels to your Managed Airflow environments and then break down billing costs based on these labels.

## About environment labels

Environment labels are key-value pairs that you can assign to your environments. For example, if `owner:engineering-team` is a custom label, then `owner` is the key, and `engineering-team` is the value.

Each environment can have multiple labels, but the label keys for a single environment must be unique. You can assign a same key and value to several environments.

## Environment labels in billing reports

Environment labels that you assign to your environments are visible in billing reports, so you can break down costs based on both keys and values from the labels.

**Important:** It might take **up to 1 day** for environment labels to propagate to billing reports. However, the billing costs are labeled starting from the moment when you assigned the label to your environment.

Labels don't apply retroactively. For example, if you assign a label on May 15, billing costs for May 14 do not contain the assigned label.

## Assign labels to new environments

You can assign labels when you create an environment. For more information, see [Creating environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments#labels).

## Assign labels to existing environments

###  Console 

  1. Go to the **Environments** page in the Google Cloud console:

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select your environment.

  3. Go to the **Labels** tab.

  4. Click **Edit** , then click **Add label**.

  5. Add a key-value pair for the label, then click **Save**.

  6. Wait until the environment updates.




###  gcloud 

When you update an environment using the [`gcloud composer`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/update) command, the following arguments specify labels for the environment:

  * `--clear-labels` removes all labels.

  * `--update-labels` updates specified labels; creates new labels if they don't already exist.

  * `--remove-labels` removes specified labels; specified label that do not exist are ignored.




If you use several of these arguments, they are applied in the following order: `--clear-labels`, `--update-labels`, `--remove-labels`.

**Update or create labels**
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --update-labels LABEL_KEY=LABEL_VALUE
    

**Remove specified labels**
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --remove-labels LABEL_KEY
    

**Remove all labels**
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --clear-labels
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `LABEL_KEY` with the environment label key that you want to create, update, or remove.
  * `LABEL_VALUE` with the environment label value.



**Example**

The following example updates the `owner` label, creates the new `env` label, and removes the `misc` label:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --update-labels owner=engineering-team,env=production \
        --remove-labels misc
    

###  API 

When you update an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, specify new labels of your environment.

**Replace all labels**

To replace all labels, include `labels` in the `updateMask` query parameter and provide a replacement in the request body.
    
    
    // PATCH https://composer.googleapis.com/v1/
    // ?{name=projects/*/locations/*/environments/*}
    // &updateMask.fieldPaths=labels
    
    {
      "labels":{
          "LABEL_KEY": "LABEL_VALUE"
        }
    }
    

Replace:

  * `LABEL_KEY` with a key of the environment label.
  * `LABEL_VALUE` with a new value for the environment label.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/
    // ?{name=projects/*/locations/*/environments/*}
    // &updateMask.fieldPaths=labels
    
    {
      "labels": {
        "owner": "engineering-team",
        "env": "production"
      }
    }
    

**Remove all labels**

To remove all labels, include `labels` in the `updateMask` query parameter and do not provide the replacement value.

**Update individual labels**

To update a label or add a new label to existing labels, include `labels.LABEL_KEY` in the `updateMask` query parameter and provide a replacement in the request body.
    
    
    // PATCH https://composer.googleapis.com/v1/
    // ?{name=projects/*/locations/*/environments/*}
    // &updateMask=labels.LABEL_KEY
    
    {
      "labels":{
          "LABEL_KEY": "LABEL_VALUE"
        }
    }
    

Replace:

  * `LABEL_KEY` with a key of the environment label.
  * `LABEL_VALUE` with a new value for the environment label.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/
    // ?name=projects/example-project/locations/
    // us-central1/environments/example-environment
    // &updateMask=labels.owner,labels.env
    
    {
      "labels": {
        "owner": "engineering-team",
        "env": "production"
      }
    }
    

**Remove individual labels**

To remove labels, include `labels.LABEL_KEY` in the `updateMask` query parameter and do not provide the replacement value.

###  Terraform 

To create an environment with default parameters is a specified location, edit the `labels` block in your Terraform configuration and run `terraform apply`.
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      labels = {
        LABEL_KEY = "LABEL_VALUE"
      }
    
    }
    

Replace:

  * `LABEL_KEY` with the environment label key that you want to create or update. To remove labels, delete their fields.
  * `LABEL_VALUE` with the environment label value.



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      labels = {
        owner = "engineering-team"
        env = "production"
      }
    }
    

## View labels in reports

After the labels for your environment propagate to billing reports, you can break down billing costs based on these labels:

  1. [View Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports#getting_started) for your Cloud Billing account.

  2. On the **Reports** page:

     1. Click **Show filters**.
     2. In the **Filters** dialog, expand the **Labels** section.
     3. [Filter the displayed data](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) based on keys and values of your environment labels.



## What's next

  * [Managed Airflow pricing](https://docs.cloud.google.com/composer/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
