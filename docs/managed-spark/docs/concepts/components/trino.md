---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/trino/
title: Managed Service for Apache Spark optional Trino component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:27.920204+00:00
---

# Managed Service for Apache Spark optional Trino component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/trino/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Trino component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Trino when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes how you can optionally install the Trino component on a Managed Service for Apache Spark cluster.

[Trino](https://trino.io/) is an open source distributed SQL query engine. The Trino server and Web UI are by default available on port `8060` (or port `7778` if Kerberos is enabled) on the cluster's first master node.

By default, Trino on Managed Service for Apache Spark is configured to work with `Hive`, `BigQuery`, `Memory`, `TPCH` and `TPCDS` [connectors](https://trino.io/docs/current/connector.html).

After creating a cluster with the Trino component, you can run queries:

  * from a local terminal with the [`gcloud dataproc jobs submit trino`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino) command
  * from a terminal window on the cluster's first master node using the `trino` CLI (Command Line Interface)—see [Use Trino with Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/tutorials/trino-dataproc).



## Install the component

Install the component when you create a Managed Service for Apache Spark cluster.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Trino** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Trino component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --optional-components=TRINO \
        --region=region \
        --enable-component-gateway \
        ... other flags
        

Notes: 

  * CLUSTER_NAME: The name of the cluster.
  * REGION: A [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located.



#### Configuring properties

Add the [`--properties` ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#how_the_properties_flag_works) flag to the `gcloud dataproc clusters create` command to set `trino`, `trino-jvm` and `trino-catalog` config properties.

  * **Application properties:** Use cluster properties with the `trino:` prefix to configure [Trino application properties](https://trino.io/docs/current/admin/properties.html)—for example, `--properties="trino:join-distribution-type=AUTOMATIC"`.
  * **JVM configuration properties:** Use cluster properties with the `trino-jvm:` prefix to configure JVM properties for Trino coordinator and worker Java processes—for example, `--properties="trino-jvm:XX:+HeapDumpOnOutOfMemoryError"`.
  * **Creating new catalogs and adding catalog properties:** Use `trino-catalog:catalog-name.property-name` to configure Trino catalogs. 

**Example:** The following `properties` flag can be used with the `gcloud dataproc clusters create` command to create a Trino cluster with a "prodhive" Hive catalog. A `prodhive.properties` file will be created under`/usr/lib/trino/etc/catalog/` to enable the prodhive catalog.
        
        --properties="trino-catalog:prodhive.connector.name=hive,trino-catalog:prodhive.hive.metastore.uri=thrift://localhost:9000"




### REST API

The Trino component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

Using the [Dataproc `v1` API](https://docs.cloud.google.com/managed-spark/docs/reference/rest), set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#endpointconfig) property to `true` as part of the clusters.create request to enable connecting to the Trino Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
