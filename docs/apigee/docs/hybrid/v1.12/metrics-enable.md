---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-enable/
title: Configure metrics collection \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:20.352311+00:00
---

# Configure metrics collection  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-enable.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/metrics-enable.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/metrics-enable.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/metrics-enable.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/metrics-enable.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-enable.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/metrics-enable.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/metrics-enable.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/metrics-enable.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/metrics-enable.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/metrics-enable.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/metrics-enable.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/metrics-enable.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/metrics-enable.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/metrics-enable.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/metrics-enable.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/metrics-enable.html)



This section describes configuration properties for sending Apigee hybrid metrics data to [Cloud Operations for GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine). Metrics collection is enabled by default. See also [Metrics collection overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-collection). 

In some cases, you may wish to use your own metrics collection system, such as Prometheus or Grafana, in parallel with or instead of the default metrics collection system provided by Apigee. For details on using your own metrics collection system, see the article [Bring your own Prometheus (and Grafana) to monitor Apigee hybrid](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/BYOP-Bring-your-own-Prometheus-and-Grafana-to-monitor-Apigee/ta-p/499772) in the Apigee Community.

##  Required configuration 

The following overrides file settings configure metrics collection:
    
    
    gcp:
      region: $GCP_REGION
      projectID: $GCP_PROJECT_ID
    
    metrics:
      serviceAccountPath: $SERVICE_ACCOUNT_PATH

Where: 

  * `$GCP_REGION` identifies the Google Cloud [region](https://cloud.google.com/compute/docs/regions-zones#available) where the `apigee-logger` and the `apigee-metrics` push their data.
  * `$GCP_PROJECT_ID` identifies the Google Cloud project where `apigee-logger` and the `apigee-metrics` push their data.
  * `$SERVICE_ACCOUNT_PATH` is the path on your filesystem to the Google Cloud service account key file that was downloaded during the Apigee hybrid [installation procedure](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-overview). The service account associated with the key must have the **Monitoring Metrics Writer** role. For details on creating service accounts, see [About service accounts: Create the service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sa-about#create-the-service-accounts). 



Example: 
    
    
    gcp:
      region: us-central1
      projectID: acme-project
    
    metrics:
      serviceAccountPath: ./service-accounts/metrics-sa.json

## How to disable metrics collection

To disable metrics collection, add the following configuration to your overrides and apply it to the cluster: 
    
    
    metrics:
      enabled: false

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
  *[Google Cloud]: Google Cloud
