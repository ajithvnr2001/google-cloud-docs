---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview/
title: Managed Service for Apache Spark components \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:00.485038+00:00
---

# Managed Service for Apache Spark components  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark components Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the different types of components available in Managed Service for Apache Spark clusters. Understanding these components is essential for configuring your clusters to include the necessary tools and services for your big data workloads. Managed Service for Apache Spark components are categorized as installed, optional, or initialization action components.

## Types of components

Managed Service for Apache Spark clusters feature the following types of components:

  * Installed components: Components that are installed in the image and activated when the cluster is created.

  * Optional components: Components that you select to install and use on your cluster when you create the cluster. Managed Service for Apache Spark installs and activates optional components depending on the cluster image version as follows:

    * **`2.2` and earlier image versions**: Optional components are automatically installed. Selected optional components are activated and non-selected optional components are uninstalled at cluster creation.

    * **`2.3` and later image versions**: All optional components are installed during cluster creation except the Jupyter, Iceberg, and Delta Lake optional components, which are pre-installed in `2.3` and later image versions. Pre-installed optional components are removed from a `2.3` or later image version cluster if they are not enabled when the cluster is created. For more information, see [Managed Service for Apache Spark 2.3.x release versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.3). To avoid increased startup time for `2.3` and later image version clusters, create a [custom image](https://docs.cloud.google.com/managed-spark/docs/guides/images#generate_a_custom_image) with optional components pre-installed. You can do this by running [`generate_custom_image.py`](https://github.com/GoogleCloudDataproc/custom-images?tab=readme-ov-file#generate-custom-image) with the [`--optional-components`](https://docs.cloud.google.com/managed-spark/docs/guides/images#run_the_code) flag.

  * Initialization action components: Components installed on a cluster as part of an [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) that you specify when you create a cluster.




Optional components are installed on a cluster before [initialization actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions)[](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview/) are run on the cluster.

The [Managed Service for Apache Spark image version pages](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) list the components and component types available in the latest Managed Service for Apache Spark image releases.

Optional components have the following advantages over initialization actions used to install components:

  * Optional components are tested as compatible with specific Managed Service for Apache Spark versions.
  * Optional components are enabled with a cluster creation parameter; initialization actions require a script.



## Available optional components

Optional component | Component name  
in Google Cloud CLI commands and API requests | Image Version | Release Stage  
---|---|---|---  
[Delta Lake](https://docs.cloud.google.com/managed-spark/docs/concepts/components/delta) | DELTA  | [2.2.46](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Docker](https://docs.cloud.google.com/managed-spark/docs/concepts/components/docker) | DOCKER  | [1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Flink](https://docs.cloud.google.com/managed-spark/docs/concepts/components/flink) | FLINK  | [1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[HBase](https://docs.cloud.google.com/managed-spark/docs/concepts/components/hbase) | HBASE  | [1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and later  
(not available in [2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1) and later)  | [Deprecated](https://cloud.google.com/products/#product-launch-stages)  
[Hive WebHCat](https://docs.cloud.google.com/managed-spark/docs/concepts/components/hivewebhcat) | HIVE_WEBHCAT  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Hudi](https://docs.cloud.google.com/managed-spark/docs/concepts/components/hudi) | HUDI  | [1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Iceberg](https://docs.cloud.google.com/managed-spark/docs/concepts/components/iceberg) | ICEBERG  | [2.2](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Jupyter Notebook](https://docs.cloud.google.com/managed-spark/docs/concepts/components/jupyter) | JUPYTER  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Pig](https://docs.cloud.google.com/managed-spark/docs/concepts/components/pig) | PIG  | [1.5*](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Presto](https://docs.cloud.google.com/managed-spark/docs/concepts/components/presto) | PRESTO  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  
(not available in [2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1) and later)  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Ranger](https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger) | RANGER  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Solr](https://docs.cloud.google.com/managed-spark/docs/concepts/components/solr) | SOLR  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Trino](https://docs.cloud.google.com/managed-spark/docs/concepts/components/trino)[](https://docs.cloud.google.com/managed-spark/docs/concepts/components/trino) | TRINO  | [2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[Zeppelin Notebook](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin) | ZEPPELIN  | [1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
[ZooKeeper](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zookeeper) | ZOOKEEPER  | [1.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.0) and later  | [GA](https://cloud.google.com/products/#product-launch-stages)  
  
Notes:

  * Apache Pig is an optional component in image versions 2.3 and later. It was pre-installed in `2.2` and earlier image versions.

See [Cluster web interfaces](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/cluster-web-interfaces) for connecting to component Web interfaces running on clusters. Also see the Managed Service for Apache Spark [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways), which lets you connect to the web interfaces of Managed Service for Apache Spark core and optional components, including YARN, HDFS, Jupyter, and Zeppelin UIs, without requiring the use of [SSH tunnels](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/cluster-web-interfaces#create_an_ssh_tunnel) or the [modification of firewall rules](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network) to allow inbound traffic. 

## Add optional components

**Note:** The following usage examples apply to [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages) components.

### Google Cloud console

  1. In the Google Cloud console, open [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkboxes for the optional components that you want to install on your cluster, then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster and install one or more optional components on the cluster, use the `gcloud beta dataproc clusters create cluster-name ` command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
      --optional-components=COMPONENT-NAME(s) \
      ... other flags
    

### REST API

Optional components can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
