---
url: https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments/
title: Create environments with Terraform \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:47.764071+00:00
---

# Create environments with Terraform  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Create environments with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/terraform-create-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/terraform-create-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page is a companion to the main page about [creating environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments). It demonstrates how to set up a Managed Airflow environment and a user-managed service account for this environment in an existing Google Cloud project with [Terraform](https://www.terraform.io). You can use this page as a start, then add more configuration parameters for your environment, as needed.

## About Terraform modules for Managed Airflow

Google maintains the [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs), which includes the [google_composer_environment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment) resource. This is the officially supported module for Terraform.

There are other Terraform modules maintained by the open source community. To resolve problems with such modules, you can create issues in their repositories on GitHub. One example of an open source project maintaned on GitHub is the [terraform-google-composer](https://github.com/terraform-google-modules/terraform-google-composer) module, which is a part of [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints). While Google contributes to this project, the module is not maintained by Google and is not related to the Terraform provider for Google Cloud.

## Before you begin

  * This guide assumes that you have a Google Cloud project with configured billing:

    * You can use an existing project.
    * You can [create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) using Google Cloud console, Google Cloud CLI, API, or a Python client library.
    * You can create and manage your project using Terraform. For more information, see Terraform documentation for the [`google_project`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project) resource.
  * [Install gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).




## Authenticate with Google Cloud

To authenticate with Google Cloud, run:
    
    
    gcloud auth application-default login
    

For more information about this command, see [`gcloud auth application-default`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login).

## Configure the Google provider in Terraform

Specify your existing [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and a default region for resources. Your Managed Airflow environment uses this region.

The `google-beta` provider supports Managed Airflow features that are in Preview. If you want to use only GA features of Managed Airflow, use the `google` provider instead of `google-beta`.
    
    
    provider "google-beta" {
      project = "example-project"
      region  = "us-central1"
    }
    

## Enable the Cloud Composer API

Enable the Cloud Composer API in your project:
    
    
    resource "google_project_service" "composer_api" {
      provider = google-beta
      project = "example-project"
      service = "composer.googleapis.com"
      // Disabling Cloud Composer API might irreversibly break all other
      // environments in your project.
      // This parameter prevents automatic disabling
      // of the API when the resource is destroyed.
      // We recommend to disable the API only after all environments are deleted.
      disable_on_destroy = false
      // this flag is introduced in 5.39.0 version of Terraform. If set to true it will
      //prevent you from disabling composer_api through Terraform if any environment was
      //there in the last 30 days
      check_if_service_has_usage_on_destroy = true
    }
    

## Create an environment's service account in your project

This guide demonstrates how to create an environment's service account that has all required permissions to run a Managed Airflow environment.

We strongly recommend to [set up a user-managed service account](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account) for your Managed Airflow environments that has only **permissions required to run your environment and operations in your DAGs** , as described in this guide.

**Warning:** Your environment's service account can have **too broad permissions on your project**. Because your environment runs DAGs on behalf of your environment's service account, users who can add and modify DAGs in your environment's bucket **can run their code on behalf of the environment's service account** and **exercise all permissions of this account**. Make sure that you are familiar with [security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security) and understand how this account interacts with permissions and roles that you grant to individual users in your project.

The service account of your environment might need additional permissions to access other resources in your project. For example, if your DAGs transfer data into BigQuery, this account might need permissions or roles specific to BigQuery.

Define a custom service account with the following roles and permissions:
    
    
    resource "google_service_account" "custom_service_account" {
      provider = google-beta
      account_id   = "custom-service-account"
      display_name = "Example Custom Service Account"
    }
    
    resource "google_project_iam_member" "custom_service_account" {
      provider = google-beta
      project  = "example-project"
      member   = format("serviceAccount:%s", google_service_account.custom_service_account.email)
      // Role for Public IP environments
      role     = "roles/composer.worker"
    }
    

## Create an environment

Create your environment using Terraform.

The example demonstrates how to create an environment that uses a custom service account. You can add more parameters that define other configuration parameters of your environment, such as custom scale and performance parameters, or additional PyPI packages.

For more information about other parameters, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments).

**Caution:** If you use [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases) in the `image_version` parameter, then your environment might upgrade to a later version when you run `terraform apply`. To avoid this, use a specific version in this parameter.
    
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example-environment"
    
      config {
    
        software_config {
          image_version = "composer-1.20.12-airflow-1.10.15"
        }
    
        node_config {
          service_account = google_service_account.custom_service_account.email
        }
    
      }
    }
    

## Full Terraform script
    
    
    provider "google-beta" {
      project = "example-project"
      region  = "us-central1"
    }
    
    resource "google_project_service" "composer_api" {
      provider = google-beta
      project = "example-project"
      service = "composer.googleapis.com"
      // Disabling Cloud Composer API might irreversibly break all other
      // environments in your project.
      disable_on_destroy = false
      // this flag is introduced in 5.39.0 version of Terraform. If set to true it will
      //prevent you from disabling composer_api through Terraform if any environment was
      //there in the last 30 days
      check_if_service_has_usage_on_destroy = true
    }
    
    resource "google_service_account" "custom_service_account" {
      provider = google-beta
      account_id   = "custom-service-account"
      display_name = "Example Custom Service Account"
    }
    
    resource "google_project_iam_member" "custom_service_account" {
      provider = google-beta
      project  = "example-project"
      member   = format("serviceAccount:%s", google_service_account.custom_service_account.email)
      // Role for Public IP environments
      role     = "roles/composer.worker"
    }
    
    resource "google_composer_environment" "example_environment" {
      provider = google-beta
      name = "example-environment"
    
      config {
    
        software_config {
          image_version = "composer-1.20.12-airflow-1.10.15"
        }
    
        node_config {
          service_account = google_service_account.custom_service_account.email
        }
    
      }
    }
    

## What's next

See other documentation pages for information about configuring your environment with Terraform. For example:

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations)
  * [Set environment variables](https://docs.cloud.google.com/composer/docs/composer-1/set-environment-variables)
  * [Install Python dependencies](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies)
  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
