---
url: https://docs.cloud.google.com/composer/docs/beta-support/
title: Preview feature support \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:40.521279+00:00
---

# Preview feature support  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/beta-support/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Preview feature support Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and use Preview (Beta) features in Managed Service for Apache Airflow.

Managed Airflow uses two terms to indicate launch stages of its features: _Preview_ and _Beta_. These terms are identical.

Typically, Preview features are indicated in the interface that you're accessing the feature through. For example, the API endpoint URL includes `beta` in the version, and in the Google Cloud console, there's a "Preview" tag next to the field that you use to configure a Preview feature. Managed Airflow documentation also specifies that a feature is in Preview.

For more information about launch stages and Preview features, see the [product launch stages](https://cloud.google.com/products#product-launch-stages).

## Preview features

To find out what features are in Preview, see the [Release notes](https://docs.cloud.google.com/composer/docs/release-notes).

To use the Preview features in Managed Airflow:

Interface | Method  
---|---  
Google Cloud CLI | [gcloud beta composer](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer)  
Cloud Composer API | v1beta1 [REST](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments) or [RPC](https://docs.cloud.google.com/composer/docs/reference/rpc/google.cloud.orchestration.airflow.service.v1beta1) API  
Google Cloud console | Enable Preview features  
**Note:** When you create an environment that uses a Preview feature, you must also use one of the interfaces in the table to update or delete the environment.

## Enabling Beta features in the Google Cloud console

Beta features are marked in the UI with a "Preview" badge. Enabling one or more of these features results in your environment using the [v1beta1 API](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
