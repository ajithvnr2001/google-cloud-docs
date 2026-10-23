---
url: https://docs.cloud.google.com/managed-spark/docs/guides/start-stop/
title: Stop and start clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:24.499082+00:00
---

# Stop and start clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/start-stop/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Stop and start clusters Stay organized with collections  Save and categorize content based on your preferences. 

After you create a cluster, you can stop it, then restart it when you need it. Stopping an idle cluster avoids incurring charges and avoids the need to delete an idle cluster, then create a cluster with the same configuration later.

Notes:

  * The cluster start and stop feature is available on clusters created with images released on or after the following image versions: 
    * 1.4.35-debian10/ubuntu18
    * 1.5.10-debian10/ubuntu18
    * 2.0.0-RC6-debian10/ubuntu18
  * Stopping individual cluster nodes is not recommended since the status of a stopped VM may not be in sync with cluster status, which can result in errors.
  * Clusters using [flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) cannot use the start and stop feature.

**Note:** To schedule stopping a cluster, see [Cluster scheduled stop](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-stop).

## Stopping a cluster

Stopping a cluster stops all cluster Compute Engine VMs. You don't pay for VMs while they are stopped. However, you continue to pay for any associated cluster resources, such as [persistent disks](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/persistent-disks).

Notes:

  * **Running operations:** If a cluster has running operations, such as update or diagnose operations, the stop request will fail.
  * **Running jobs:** If a cluster has running jobs, the stop request will succeed: the VMs will stop, and the running jobs will fail.
  * **Stop Response:** When the stop request returns a stop operation, the cluster will be in a `STOPPING` state, and no further jobs will be allowed to be submitted (`SubmitJob` requests will fail).
  * **Autoscaling:** If you stop a cluster that has [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) enabled, the Managed Service for Apache Spark autoscaler will stop scaling the cluster. It will resume scaling the cluster once the cluster is restarted. If you enable autoscaling on a stopped cluster, the autoscaling policy will take effect once the cluster has been restarted.



### Monitoring the stop operation

You can run [`gcloud dataproc operations describe operation-id`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/operations/describe) to monitor the long-running cluster stop operation. You can use the [`gcloud dataproc clusters describe cluster-name`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/describe) command to monitor the transitioning of the cluster's status from `RUNNING` to `STOPPING` to `STOPPED`.

### Limitations

  * You cannot stop:

    * clusters with [secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms)
    * clusters with [local ssds](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds)
  * When a cluster is stopped, you cannot:

    * update the cluster
    * submit jobs to the cluster
    * access notebooks running on the cluster using the [Managed Service for Apache Spark component gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways)



## Starting a cluster

  * When you restart a stopped cluster, any initialization actions won't be re-run. Initialization actions only run on cluster nodes when the cluster is created or when nodes are added when the cluster is scaled up.

  * After the start operation completes, you can immediately submit jobs to the cluster. However, execution of the jobs can be delayed—approximately 30 seconds—to allow HDFS and YARN to become operational.


**Important:** When a cluster restarts, its VMs and other resources are reprovisioned. Resource provisioning is subject to availability, and regional stockouts can cause a cluster restart to fail. To aid restart provisioning, you can [reserve cluster resources](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

## How to stop and start a cluster

You can stop and start a cluster using the Google Cloud console, gcloud CLI, or the Managed Service for Apache Spark API.

### Google Cloud console

  1. Click the cluster name from the [Clusters](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console.
  2. On the cluster details page that opens, click **STOP** to stop the cluster. When ready to resume cluster operations, click **START** to restart the cluster.



### gcloud CLI

**Stop a cluster**
    
    
    gcloud dataproc clusters stop CLUSTER_NAME \
        --region=REGION
    

**Start a cluster**
    
    
    gcloud dataproc clusters start CLUSTER_NAME \
        --region=REGION
    

### REST API

**Stop a cluster**

Submit a [clusters.stop](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/stop) request.

**Start a cluster**

Submit a [clusters.start](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/start) request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
