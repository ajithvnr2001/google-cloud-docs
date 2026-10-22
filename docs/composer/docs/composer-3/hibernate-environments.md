---
url: https://docs.cloud.google.com/composer/docs/composer-3/hibernate-environments/
title: Hibernate development mode environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:36.883800+00:00
---

# Hibernate development mode environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/hibernate-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Hibernate development mode environments Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page explains how to hibernate and resume a development mode environment.

For instructions about creating a development mode environment, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#development-mode).

If you want to run an Airflow environment for development purposes locally instead, see [Run a local Airflow environment](https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments).

## About development mode environments

A development mode environment is a type of environment that can be used for development purposes. You can hibernate a development mode environment when you're not using it and resume it later.

Development mode environments have the following constraints:

  * Only Managed Airflow (Gen 3) with Airflow 3.
  * Only [standard resilience mode](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments).
  * Small environment size and default resource limits provided by the [Small environment preset](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#presets). It's not possible to change the number of Airflow components or resource limits of a development mode environment.

**Important:** Development mode environments are intended **only for development purposes**. Don't use development mode environments in production.

You can save and load [snapshots](https://docs.cloud.google.com/composer/docs/composer-3/save-load-snapshots) of development mode environments. In this way, you can transfer your DAGs and other data from and to a development mode environment.

## About environment hibernation

An environment in hibernation works in the following way:

  * Airflow components of your environment aren't running. DAG runs won't be created, queued, or scheduled for execution while the environment is hibernated. DAGs won't be parsed or synchronized from the environment's bucket.

**Important:** Make sure that schedule and catch up configuration of your DAGs takes the hibernation period into account. For example, if you configure catch up, Airflow can start creating DAG runs for the hibernation period after you resume the environment.
  * Pods in the `composer-user-workloads` namespace don't run while the environment is hibernated.

  * The environment [consumes DCUs](https://cloud.google.com/products/managed-service-for-apache-airflow/pricing#managed-service-for-apache-airflow-gen-3) only for storing the hibernated environment components. Most of the environment costs are reduced to zero.

  * Automatic upgrades within [maintenance windows](https://docs.cloud.google.com/composer/docs/composer-3/specify-maintenance-windows) might still occur.

  * It's not possible to [update](https://docs.cloud.google.com/composer/docs/composer-3/update-environments) or [upgrade](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) a hibernated environment.




## Before you begin

  * Make sure that your environment is [created in the development mode](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#development-mode). It's not possible to switch an existing environment to the development mode.
  * Your Google Account must have a role that [can trigger environment update operations](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account).



## Hibernate a development mode environment

###  Console 

To hibernate an environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Click pause_circle **Hibernate**.

  4. Wait until the environment is hibernated.




###  gcloud 

The `gcloud beta composer environments hibernate` command hibernates your environment:
    
    
    gcloud beta composer environments hibernate \
      ENVIRONMENT_NAME \
      --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud beta composer environments hibernate \
      example-environment \
      --location us-central1
    

###  API 

Construct an [`environments.hibernate`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/hibernate) API request:

Example:
    
    
    // POST https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment:hibernate
    

## Resume a development mode environment

###  Console 

To resume a hibernated environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Click play_circle **Resume**.

  4. Wait until the environment is resumed.




###  gcloud 

The `gcloud beta composer environments resume` command resumes your environment:
    
    
    gcloud beta composer environments resume \
      ENVIRONMENT_NAME \
      --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud beta composer environments resume \
      example-environment \
      --location us-central1
    

###  API 

Construct an [`environments.resume`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/resume) API request:

Example:
    
    
    // POST https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment:resume
    

## What's next

  * [Create an environment in development mode](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#development-mode)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
