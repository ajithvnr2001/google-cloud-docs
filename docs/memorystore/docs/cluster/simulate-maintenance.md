---
url: https://docs.cloud.google.com/memorystore/docs/cluster/simulate-maintenance/
title: Simulate maintenance \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:30.034478+00:00
---

# Simulate maintenance  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/simulate-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Simulate maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes maintenance simulation and explains how to run a simulated maintenance event on Memorystore for Redis Cluster. For more information about maintenance updates and maintenance windows, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

To ensure that your applications correctly handle a planned maintenance event, Memorystore for Redis Cluster offers a _simulate maintenance event_ feature. This feature lets you simulate the maintenance process by performing planned failovers on all nodes within a cluster. This process is similar to a regular maintenance operation. We strongly recommend that you use this feature in a test environment or during periods of low traffic. For an overview of the maintenance process, see [Gradual deployment strategy](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#gradual_deployment_strategy) and [Create-before-destroy lifecycle strategy](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#create-before-destroy_lifecycle_strategy).

By observing your application's behavior during a simulated maintenance event, you can identify potential issues and verify that your application can handle maintenance correctly. For more information about best practices regarding client configurations, see [Configure your client application](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#configure_your_client_application).

## Run maintenance simulation on a cluster

### gcloud

To run a maintenance simulation on Memorystore for Redis Cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command:
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --simulate-maintenance-event
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster for which you want to run a simulated maintenance
  * REGION_ID: the region where your cluster is located



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
