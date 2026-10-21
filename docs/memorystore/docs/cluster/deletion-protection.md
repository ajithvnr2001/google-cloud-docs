---
url: https://docs.cloud.google.com/memorystore/docs/cluster/deletion-protection/
title: Prevent deletion of a cluster \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:09.361990+00:00
---

# Prevent deletion of a cluster  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/deletion-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Prevent deletion of a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Cluster deletion protection lets you prevent the accidental removal of existing and new clusters. Using cluster deletion protection, you can safeguard clusters that are important to your applications and services.

You can set the deletion protection option when you create a cluster. Additionally, you can set this option on an existing cluster. In both cases, deletion is prevented at the cluster level. By default, the deletion protection option is deactivated unless you use Terraform to create a cluster.

## Plan for deletion protection

If you plan to create a cluster, then decide whether you want to protect the cluster from accidental deletion. For example, you might want to protect a critical cluster in this way.

Also consider whether there are existing clusters that you want to protect from accidental deletion. If you have multiple clusters to protect, then set the option on each cluster.

### Plan to delete a cluster

If you plan to delete a cluster, then do the following:

  * Confirm that it's safe to delete the cluster.
  * Confirm that deletion protection is deactivated.
  * If necessary, edit the cluster to deactivate deletion protection.



### Limitations of deletion protection

Deletion protection on a cluster doesn't prevent the following actions from occurring:

  * Editing the cluster
  * Suspending the cluster because of billing issues
  * Deleting the suspended cluster because of billing issues
  * Deleting the cluster because a Google Cloud project is deleted



## Required permissions

To set deletion protection on a cluster, you must have the `redis.instances.update` permission.

## Set deletion protection on a new cluster

You can set deletion protection on a new cluster by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

By default, deletion protection is deactivated unless you use Terraform to create a cluster. If you enable deletion protection, then an attempt to delete the cluster fails.

### gcloud

To enable deletion protection while creating a cluster, follow the instructions at [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances), and add the following flag:
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --deletion-protection
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you want to protect from being deleted
  * REGION_ID: the region where the cluster is located



## Set or remove deletion protection on an existing cluster

You can set or remove deletion protection on an existing cluster by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). If you enable deletion protection, then a subsequent attempt to delete the cluster fails.

### gcloud

To enable deletion protection for an existing cluster, use the following command:
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --deletion-protection
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you want to protect from being deleted
  * REGION_ID: the region where the cluster is located



To deactivate deletion protection for an existing cluster, use the following command:
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --no-deletion-protection
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
