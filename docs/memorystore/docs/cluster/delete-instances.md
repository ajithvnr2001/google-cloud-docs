---
url: https://docs.cloud.google.com/memorystore/docs/cluster/delete-instances/
title: Delete clusters \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:47.175777+00:00
---

# Delete clusters  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/delete-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Delete clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete clusters in Memorystore for Redis Cluster.

## Delete a cluster

You can delete clusters by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : If you delete a cluster and create another cluster with the same name, then Memorystore for Redis Cluster assigns different IP addresses to the cluster. If you hardcode the IP addresses from the cluster that you delete into your client applications, then the clients can't connect to the cluster. You must update the IP addresses to point to the cluster's new [ discovery endpoints](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#discovery_endpoint).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster that you want to delete.

  3. **Optional**. If the cluster that you want to delete is a secondary cluster, then do the following:

     1. Click the expander arrow next to the primary cluster that's the parent of the secondary cluster.
     2. Click the link of the secondary cluster.
  4. Click **Delete**.

  5. In the dialog, enter the cluster ID, and then click **Delete**.




### gcloud

To delete a cluster, use the [`gcloud redis clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/delete) command.
    
    
    gcloud redis clusters delete CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you want to delete
  * PROJECT_ID: your project ID
  * REGION_ID: the region where your cluster is located



For example:
    
    
    gcloud redis clusters delete my-cluster \
    --project=my-project \
    --region=us-central1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
