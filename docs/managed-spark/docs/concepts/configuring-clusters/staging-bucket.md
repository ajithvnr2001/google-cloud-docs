---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket/
title: Managed Service for Apache Spark staging and temp buckets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:34.581575+00:00
---

# Managed Service for Apache Spark staging and temp buckets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark staging and temp buckets Stay organized with collections  Save and categorize content based on your preferences. 

When you create a cluster, HDFS is used as the default filesystem. You can override this behavior by setting the defaultFS as a Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/buckets). By default, Managed Service for Apache Spark also creates a Cloud Storage staging and a Cloud Storage temp bucket in your project or reuses existing Managed Service for Apache Spark-created staging and temp buckets from previous cluster creation requests.

  * Staging bucket: Used to stage cluster job dependencies, [job driver output](https://docs.cloud.google.com/managed-spark/docs/guides/job-output), and cluster config files. Also receives output from [Snapshot diagnostic data collection](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters#snapshot_diagnostic_data_collection).

  * Temp bucket: Used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. Also stores [checkpoint diagnostic data](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters#checkpoint_diagnostic_data_collection) collected during the lifecycle of a cluster.




If you do not specify a staging or temp bucket when you create a cluster, Managed Service for Apache Spark sets a [Cloud Storage location in US, ASIA, or EU](https://docs.cloud.google.com/storage/docs/locations#location-mr) for your cluster's staging and temp buckets according to the Compute Engine zone where your cluster is deployed, and then creates and manages these project-level, per-location buckets. Managed Service for Apache Spark-created staging and temp buckets are shared among clusters in the same region, and are created with a Cloud Storage [soft delete retention](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) duration set to 0 seconds. If you specify your own staging and temp buckets, consider tuning the soft delete retention in order to reduce storage charges incurred by soft-deleted objects.

The temp bucket contains ephemeral data, and has a TTL of 90 days. The staging bucket, which can contain configuration data and dependency files needed by multiple clusters, does not have a TTL. However, you can [apply a lifecycle rule to your dependency files](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix) (files with a ".jar" filename extension located in the staging bucket folder) to schedule the removal of your dependency files when they are no longer needed by your clusters.

To locate the default Managed Service for Apache Spark staging and temp buckets using the Google Cloud console **[Cloud Storage Browser](https://console.cloud.google.com/storage/browser)** , filter results using the "dataproc-staging-" and "dataproc-temp-" prefixes. 

## Create your own staging and temp buckets

Instead of relying on the creation of a default staging and temp bucket, you can specify existing Cloud Storage buckets that Managed Service for Apache Spark will use as your cluster's staging and temp bucket.

**Note:** When you use an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/deploy-resource) for regulatory compliance, the cluster, VPC network, and Cloud Storage buckets must be contained within the Assured Workloads environment.

### Google Cloud console

To specify or select the cluster staging bucket:

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Customization & Other**.
  4. In the panel that opens, in the **Cloud Storage staging bucket** section, specify a bucket.



Note: Specifying a temp bucket using the Google Cloud console is not supported.

### gcloud CLI

Run the `gcloud dataproc clusters create` command with the [`--bucket`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--bucket) and/or [`--temp-bucket`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--temp-bucket) flags locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) to specify your cluster's staging and/or temp bucket.
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --bucket=bucket-name \
        --temp-bucket=bucket-name \
        other args ...
    

### REST API

Use the [`ClusterConfig.configBucket`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#FIELDS.config_bucket) and [`ClusterConfig.tempBucket`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#FIELDS.temp_bucket) fields in a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request to specify your cluster's staging and temp buckets.

Managed Service for Apache Spark uses a defined folder structure for Cloud Storage buckets attached to clusters, and also supports attaching more than one cluster to a bucket. The folder structure used for saving job driver output in Cloud Storage is the following:
    
    
    cloud-storage-bucket-name
      - google-cloud-dataproc-metainfo
        - list of cluster IDs
            - list of job IDs
              - list of output logs for a job
    

You can use the `gcloud` command line tool, Dataproc API, or Google Cloud console to list the name of a cluster's staging and temp buckets.

### Google Cloud console

  * You can view cluster details, which includes the name of the cluster staging bucket, on the [Clusters](https://console.cloud.google.com/project/_/managed-spark/clusters) page in the Google Cloud console.
  * On the Google Cloud console **[Cloud Storage Browser](https://console.cloud.google.com/storage/browser)** page, filter results that contain "dataproc-temp-".



### gcloud CLI

Run the [`gcloud dataproc clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/describe) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true). The staging and temp buckets associated with your cluster are listed in the output.
    
    
    gcloud dataproc clusters describe cluster-name \
        --region=region \
    ...
    clusterName: cluster-name
    clusterUuid: daa40b3f-5ff5-4e89-9bf1-bcbfec ...
    config:
        **configBucket:** dataproc-...
        ...
        **tempBucket:** dataproc-temp...
    

### REST API

Call [clusters.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/get) to list the cluster details, including the name of the cluster's staging and temp buckets.
    
    
    {
     "projectId": "vigilant-sunup-163401",
     "clusterName": "cluster-name",
     "config": {
      **"configBucket":** "dataproc-...",
    ...
      **"tempBucket":** "dataproc-temp-...",
    }
    

## defaultFS

You can set `core:fs.defaultFS` to a bucket location in Cloud Storage (`gs://defaultFS-bucket-name`) to set Cloud Storage as the default filesystem. This also sets `core:fs.gs.reported.permissions`, the reported permission returned by the Cloud Storage connector for all files, to `777`.

**Note:** When you use an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/deploy-resource) for regulatory compliance, the cluster, VPC network, and Cloud Storage buckets must be contained within the Assured Workloads environment.

If Cloud Storage is not set as the default file system, HDFS will be used, and the `core:fs.gs.reported.permissions` property will return `700`, the default value. 
    
    
    gcloud dataproc clusters create cluster-name \
        --properties=core:fs.defaultFS=gs://defaultFS-bucket-name \
        --region=region \
        --bucket=staging-bucket-name \
        --temp-bucket=temp-bucket-name \
        other args ...
    

**Note:** Console display of the defaultFS bucket is not supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
