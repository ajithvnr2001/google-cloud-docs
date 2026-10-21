---
url: https://docs.cloud.google.com/memorystore/docs/valkey/simulate-maintenance/
title: Simulate maintenance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:24.464537+00:00
---

# Simulate maintenance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/simulate-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Simulate maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes maintenance simulation and explains how to run a simulated maintenance event on Memorystore for Valkey. For more information about maintenance updates and maintenance windows, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).

To ensure that your applications correctly handle a planned maintenance event, Memorystore for Valkey offers a _simulate maintenance event_ feature. This feature lets you simulate the maintenance process by performing planned failovers on all nodes within the instance. This process is similar to a regular maintenance operation. We strongly recommend that you use this feature in a test environment or during periods of low traffic. For an overview of the maintenance process, see [Gradual deployment strategy](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#gradual_deployment_strategy) and [Create-before-destroy lifecycle strategy](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#create-before-destroy_lifecycle_strategy).

By observing your application's behavior during a simulated maintenance event, you can identify potential issues and verify that your application can handle maintenance correctly. For more information about best practices regarding client configurations, see [Configure your client application](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#configure_your_client_application).

## Run maintenance simulation on an instance

### gcloud

To run a maintenance simulation on Memorystore for Valkey, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command:
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --simulate-maintenance-event
    

Replace the following:

  * INSTANCE_ID: the ID of the instance for which you want to run a simulated maintenance 
  * REGION_ID: the region where your instance is located



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
