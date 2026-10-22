---
url: https://docs.cloud.google.com/composer/docs/composer-2/dbt-composer-integration/
title: Create an integrated DBT and Managed Airflow operations environment \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:37.616998+00:00
---

# Create an integrated DBT and Managed Airflow operations environment  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/dbt-composer-integration/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Create an integrated DBT and Managed Airflow operations environment Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/dbt-composer-integration "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page describes how to use Terraform to create an integrated DBT and Managed Airflow operations environment.

## About the terraform-google-dbt-composer-blueprint` module

The [`terraform-google-dbt-composer-blueprint` module](https://github.com/GoogleCloudPlatform/terraform-google-dbt-composer-blueprint/) uses Terraform to do the following:

  * Applies required APIs and permissions in the project.
  * Creates documentation (for DBT) bucket.
  * Creates a Managed Airflow environment, including networking configuration, and a service account.
  * Copies across DAG utilities for Managed Airflow
  * Exports audit logs for the project into a BigQuery project, including two materialized views and a view on top to support dashboards.



In addition, the module provides an end-to-end example of using the DAG utilities and creating an example DBT job in Managed Airflow.

## Module's code on GitHub

For more information and code samples, see [`terraform-google-dbt-composer-blueprint` module](https://github.com/GoogleCloudPlatform/terraform-google-dbt-composer-blueprint/) page on GitHub.

## What's next

  * [Test, synchronize, and deploy your DAGs from GitHub](https://docs.cloud.google.com/composer/docs/composer-2/dag-cicd-github)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
