---
url: https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access/
title: Configure access to the internet when installing PyPI packages \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:53.496948+00:00
---

# Configure access to the internet when installing PyPI packages  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Configure access to the internet when installing PyPI packages Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page explains how to disable or enable internet access when installing PyPI packages in your environment.

For information about installing packages and configuring custom sources (such as a repository in your VPC network), see [Install Python dependencies](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies).

If you want to enable access to your VPC network from an environment, see [Connect an environment to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network). For example, you can configure your VPC network so that your environment can access the internet through it.

If you want to change your environment to Private IP, see [Change environment networking type (Private or Public IP)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type).

## About the internet access when installing PyPI packages

  * By default, your Managed Airflow (Gen 3) environment **can access the internet when installing PyPI packages**.

  * Packages can now be installed from both public and private sources at the same time. This wasn't possible in Managed Airflow (Gen 2).

  * This environment configuration option is independent of the environment's networking type (Private or Public IP). For example, you can install packages from [Python Package Index](https://pypi.org) in a Private IP environment.

  * You can set this configuration option when you [create an environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) and it's possible to change this option for an existing environment.




## Disable or enable internet access when installing PyPI packages

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Network configuration** section, find the **Access to public PyPI package repositories** item and click **Edit**.

  5. In the **Access to public PyPI package repositories** dialog:

     * To enable internet access, select **Allow installation of packages from public internet repositories**.

     * To disable internet access, select **Don't allow installation of packages from public internet repositories**.

  6. Click **Save**.




###  gcloud 

The following Google Cloud CLI arguments specify internet access configuration when installing PyPI packages:

  * `--disable-private-builds-only` **enables** internet access when installing packages (default).

  * `--enable-private-builds-only` **disables** internet access when installing packages.




To enable internet access when installing packages, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --disable-private-builds-only
    

To disable internet access when installing packages, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --enable-private-builds-only
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located



Example (disable internet access):
    
    
    gcloud beta composer environments update example-environment \
      --location us-central1 \
      --enable-private-builds-only
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.private_environment_config.enable_private_builds_only` mask.

     2. In the request body, in the `enablePrivateBuildsOnly` field, set the required value:

        * `false`: enable internet access when installing PyPI packages (default).
        * `true`: disable internet access when installing PyPI packages.



Example (disable internet access):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.private_environment_config.enable_private_builds_only
    
    "config": {
      "privateEnvironmentConfig": {
        "enablePrivateBuildsOnly": true
      }
    }
    

###  Terraform 

The `enable_private_builds_only` field in the `config` block specifies internet access configuration when installing PyPI packages:

  * `false` or omitted: **enables** internet access when installing packages (default).

  * `true`: **disables** internet access when installing packages.



    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        enable_private_builds_only = PRIVATE_BUILDS_MODE
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `PRIVATE_BUILDS_MODE`: whether the internet access is disabled when installing PyPI packages.



Example (disable internet access):
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        enable_private_builds_only = true
    
        ... other configuration parameters
    
      }
    

## What's next

  * [Install Python dependencies](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies)
  * [Connect an environment to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network)
  * [Change environment networking type (Private or Public IP)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
