---
url: https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster/
title: Manage a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:22.684959+00:00
---

# Manage a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Manage a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to update and delete an existing Managed Service for Apache Spark cluster.

## Update a cluster

You can update a cluster by issuing a Dataproc API [clusters.patch](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch) request, running a [gcloud dataproc clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) command in a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), or by editing cluster parameters from the Configuration tab of the Cluster details page for the cluster in the [Google Cloud console](https://console.cloud.google.com/dataproc/clusters).

The following cluster parameters can be updated:

  * the number of standard worker nodes in a cluster—see [Scaling clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/scaling-clusters)
  * the number of secondary worker nodes in a cluster— see [Managed Service for Apache Spark secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms)
  * whether to use [graceful decommissioning](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters#graceful_decommissioning) to control shutting down a worker after its jobs are completed
  * adding or deleting cluster [labels](https://docs.cloud.google.com/managed-spark/docs/concepts/labels)



### Cluster update error

Managed Service for Apache Spark issues an `ERROR_DUE_TO_UPDATE` error when a cluster update operation fails. This error places the cluster in a fail-safe state to avoid data loss, and restricts further cluster operations: jobs can continue to be submitted to the cluster, the cluster can be deleted, but further cluster update operations are not permitted.

Recommendation: After receiving an `ERROR_DUE_TO_UPDATE` on a cluster, [recreate the cluster](https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster#recreate_and_update_a_cluster) by exporting the cluster configuration to create a new cluster, then delete the failed cluster. If recreating the cluster fails, contact [Cloud Customer Care](https://docs.cloud.google.com/support) for help in restoring the cluster to a `RUNNING` state.

**Note:** A cluster can enter the `ERROR_DUE_TO_UPDATE` state if you attempt to update cluster resources through Compute Engine API operations. To update cluster resources, use [Managed Service for Apache Spark update](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#update_a_cluster) operations.

## Delete a cluster

You can delete a cluster via a Dataproc API [clusters.delete](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/delete) HTTP or programmatic request, using the Google Cloud CLI [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/delete) command-line tool locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), or from the [Google Cloud console](https://console.cloud.google.com/dataproc/clusters).

**Deletion is permanent:** Once deleted, clusters cannot be restored. You can, however, quickly create new Managed Service for Apache Spark clusters as you need them. 

### Google Cloud CLI

To delete a Managed Service for Apache Spark cluster, use the gcloud CLI [gcloud dataproc clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/delete) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true).
    
    
    gcloud dataproc clusters delete cluster-name \
        --region=region
    

### REST API

Use the Managed Service for Apache Spark [clusters.delete](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/delete) API to delete a cluster.

### Console

Open the Managed Service for Apache Spark [Clusters](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console. Select the cluster by checking the box to the left of the cluster name, then Click **Delete** to delete the cluster.

![](https://docs.cloud.google.com/static/managed-spark/images/dataproc-1-delete.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
