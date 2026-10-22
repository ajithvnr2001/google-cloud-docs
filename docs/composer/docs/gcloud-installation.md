---
url: https://docs.cloud.google.com/composer/docs/gcloud-installation/
title: Using Google Cloud CLI with Managed Airflow \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:13.157230+00:00
---

# Using Google Cloud CLI with Managed Airflow  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/gcloud-installation/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Reference ](https://docs.cloud.google.com/composer/docs/apis)



Send feedback 

#  Using Google Cloud CLI with Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get started using Google Cloud CLI with Managed Service for Apache Airflow environments.

## Before you begin

  * Google Cloud CLI uses Cloud Composer API to run `gcloud composer` commands, so you must [enable the API](https://docs.cloud.google.com/composer/docs/latest/enable-composer-service).
  * Install [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) on your local client.



## Getting started with the gcloud command-line tool

You can manage and access Managed Airflow environments with `gcloud composer` commands provided by [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

To start with the `gcloud` tool, review the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/docs). You can get help for the tool, resources, and commands by using the `--help` flag:
    
    
    gcloud composer environments --help
    

The help displayed with the `--help` flag is also available in the [Google Cloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/composer) for `gcloud composer`.

## Setting the default project and location in your local client

Most `gcloud composer` commands require a location. You can specify the location by using the `--location` flag or by setting the default location.

To set the default project and location for Managed Airflow:

  1. Set the default project by running the following command:
         
         gcloud config set project PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project where your Managed Airflow environment is located.
  2. Configure the Managed Airflow location by running the following command:
         
         gcloud config set composer/location LOCATION
         

Replace the following:

     * `LOCATION`: the region where the environment is located, such as `us-central1` or `europe-west1`.
  3. (Optional) To list the configuration for Google Cloud CLI, you can run the following command:
         
         gcloud config list
         




## What's next

  * [Add and update Airflow DAGs](https://docs.cloud.google.com/composer/docs/latest/manage-dags)
  * [`gcloud composer` reference](https://docs.cloud.google.com/sdk/gcloud/reference/composer)
  * [`gcloud beta composer` reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
