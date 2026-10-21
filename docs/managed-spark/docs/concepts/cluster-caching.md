---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-caching/
title: Cluster caching \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:35.736794+00:00
---

# Cluster caching  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-caching/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster caching Stay organized with collections  Save and categorize content based on your preferences. 

When you enable Managed Service for Apache Spark cluster caching, the cluster caches Cloud Storage data frequently accessed by your Spark jobs.

## Benefits

  * **Improved performance:** Caching can improve job performance by reducing the amount of time spent retrieving data from storage.
  * **Reduced storage costs:** Since hot data is cached on local disk, fewer API calls are made to storage to retrieve data.
  * **Spark job applicability** : When cluster caching is enabled on a cluster, it applies to all Spark jobs run on the cluster, whether submitted to the Managed Service for Apache Spark or run independently on the cluster.



## Limitations and requirements

  * Caching applies to Managed Service for Apache Spark jobs only.
  * Only Cloud Storage data is cached.
  * Caching only applies to clusters that meet the following requirements: 
    * The cluster has one master and `n` workers ([High Availability (HA)](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability) and [single node](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) clusters are not supported).
    * This feature is available in Managed Service for Apache Spark [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) `2.0.72+`, `2.1.20+`, and `2.2.0+`.
    * Each cluster node must have [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds) attached with the [NVME (Non-Volatile Memory Express)](https://docs.cloud.google.com/compute/docs/disks/local-ssd#nvme) interface (Persistent Disks (PDs) are not supported). Data is cached on NVME local SSDs only.
    * The cluster uses the [default VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) for authentication. [Custom VM service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account) are not supported.



## Enable cluster caching

You can enable cluster caching when you create a Managed Service for Apache Spark cluster using the Google Cloud console, Google Cloud CLI, or the Dataproc API.

### Google Cloud console

  1. Open the Google Cloud console [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Customization & Other**.
  4. In the panel that opens, in the **Cluster properties** section, click **\+ Add properties**.
  5. Select **dataproc** in the **Prefix** list, then add the key `dataproc.cluster.caching.enabled` and value `true`.



### gcloud CLI

Run the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) using the `dataproc:dataproc.cluster.caching.enabled=true` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table).

Example:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --properties dataproc:dataproc.cluster.caching.enabled=true \
        --num-master-local-ssds=2 \
        --master-local-ssd-interface=NVME \
        --num-worker-local-ssds=2 \
        --worker-local-ssd-interface=NVME \
        other args ...
      

### REST API

Set [SoftwareConfig.properties](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties) to include the `"dataproc:dataproc.cluster.caching.enabled": "true"` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
