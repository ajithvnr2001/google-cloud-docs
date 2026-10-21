---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/presto/
title: Managed Service for Apache Spark optional Presto component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:25.269840+00:00
---

# Managed Service for Apache Spark optional Presto component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/presto/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Presto component Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The [Presto Optional Component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/presto) is available as [Trino Optional Component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/trino) in 2.1 and later image versions.

You can install additional components like Presto when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes how you can optionally install Presto component on a Managed Service for Apache Spark cluster.

Presto ([Trino](https://trino.io/)) is an open source distributed SQL query engine. The Presto server and Web UI are by default available on port `8060` (or port `7778` if Kerberos is enabled) on the cluster's first master node.

By default, Presto on Managed Service for Apache Spark is configured to work with `Hive`, `BigQuery`, `Memory`, `TPCH` and `TPCDS` [connectors](https://trino.io/docs/current/connector.html).

After creating a cluster with the Presto component, you can run queries:

  * from a local terminal with the [`gcloud dataproc jobs submit presto`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/presto) command
  * from a terminal window on the cluster's first master node using the `presto` CLI (Command Line Interface)—see [Use Trino with Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/tutorials/trino-dataproc)



## Install the component

Install the component when you create a Managed Service for Apache Spark cluster. Components can be added to clusters created with Managed Service for Apache Spark [version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Presto**.



### gcloud CLI command

To create a Managed Service for Apache Spark cluster that includes the Presto component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.

When creating the cluster, use [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--enable-component-gateway` flag, as shown in the following example, to enable connecting to the Presto Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 
    
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=PRESTO \
        --region=region \
        --enable-component-gateway \
        ... other flags
    

#### Configuring properties

Add the [`--properties` ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#how_the_properties_flag_works) flag to the `gcloud dataproc clusters create` command to set presto, presto-jvm and presto-catalog config properties.

  * **Application properties:** Use cluster properties with the `presto:` prefix to configure [Presto application properties](https://trino.io/docs/current/admin/properties.html)—for example, `--properties="presto:join-distribution-type=AUTOMATIC"`.
  * **JVM configuration properties:** Use cluster properties with the `presto-jvm:` prefix to configure JVM properties for Presto coordinator and worker Java processes—for example, `--properties="presto-jvm:XX:+HeapDumpOnOutOfMemoryError"`.
  * **Creating new catalogs and adding catalog properties:** Use `presto-catalog:catalog-name.property-name` to configure Presto catalogs. 

**Example:** The following `properties` flag can be used with the `gcloud dataproc clusters create` command to create a Presto cluster with a "prodhive" Hive catalog. A `prodhive.properties` file will be created under`/usr/lib/presto/etc/catalog/` to enable the prodhive catalog.
        
        --properties="presto-catalog:prodhive.connector.name=hive-hadoop2,presto-catalog:prodhive.hive.metastore.uri=thrift://localhost:9083




### REST API

The Presto component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

Using the [Dataproc `v1` API](https://docs.cloud.google.com/managed-spark/docs/reference/rest), set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#endpointconfig) property to `true` as part of the clusters.create request to enable connecting to the Presto Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
