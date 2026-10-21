---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/solr/
title: Managed Service for Apache Spark optional Solr component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:40.864456+00:00
---

# Managed Service for Apache Spark optional Solr component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/solr/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Solr component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Solr when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes the Solr component.

The [Apache Solr](https://lucene.apache.org/solr/) component is an open source enterprise search platform. The Solr server and Web UI are available on port `8983` on the cluster's master node(s).

**Persisting Solr files:** By default, Solr writes and reads the index and transaction log files in [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html). To persist Solr files, use a Cloud Storage path as the Solr home directory by setting the `dataproc:solr.gcs.path` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties) when you install the component.

## Install the component

Install the component when you create a Managed Service for Apache Spark cluster. Components can be added to clusters created with Managed Service for Apache Spark [version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Solr** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Solr component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag. The sample command below uses the optional `properties` flag to set a Cloud Storage path as the Solr home directory.

When creating the cluster, use [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--enable-component-gateway` flag, as shown below, to enable connecting to the Solr Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --optional-components=SOLR \
        --enable-component-gateway \
        ... other flags
    

Add the `--properties="dataproc:solr.gcs.path=gs://bucket-name/"` [ cluster property ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to the `gcloud dataproc clusters create` command to set a Cloud Storage bucket where Solr documents will be stored (Solr home directory).

### REST API

The Solr component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

As part of your `clusters.create` request, you can: 

  1. Set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#EndpointConfig.description) property to `true` to enable connecting to the Solr Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 
  2. Set the `"dataproc:solr.gcs.path=gs://bucket-name"` [ cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) in the [SoftwareConfig.Component.properties](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties) field to set a Cloud Storage bucket where Solr documents will be stored (Solr home directory). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
