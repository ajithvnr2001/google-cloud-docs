---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin/
title: Managed Service for Apache Spark optional Zeppelin component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:30.469148+00:00
---

# Managed Service for Apache Spark optional Zeppelin component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Zeppelin component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Zeppelin when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes the Zeppelin component.

The [Zeppelin Notebook](https://zeppelin.apache.org/) component is a Web-based notebook for interactive data analytics. The Zeppelin Web UI is available on port `8080` on the cluster's first master node.

By default, notebooks are saved in Cloud Storage in the Managed Service for Apache Spark staging bucket, which is specified by the user or [auto-created](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#auto-created_staging_bucket) when the cluster is created. The location can be changed at cluster creation time via the [`zeppelin:zeppelin.notebook.gcs.dir` property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties).

  * Zeppelin can be configured by providing `zeppelin` and `zeppelin-env` prefixed [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#formatting). 
    * To reduce the risk of remote code execution over unsecured notebook server APIs, the default `zeppelin:zeppelin.server.addr` cluster property setting for image versions 1.3+ is `127.0.0.1`, which restricts connections to `localhost` when [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) is enabled.



## Install the component

Install the component when you create a Managed Service for Apache Spark cluster. Components can be added to clusters created with Managed Service for Apache Spark [version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later.

See [Supported Dataproc versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Zeppelin Notebook** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Zeppelin component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.

When creating the cluster (image version 1.3.29 or later), use [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--enable-component-gateway` flag, as shown below, to enable connecting to the Zeppelin notebook Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 
    
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=ZEPPELIN \
        --region=region \
        --enable-component-gateway \
        ... other flags
    

### REST API

The Zeppelin component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. Using the [Dataproc `v1` API](https://docs.cloud.google.com/managed-spark/docs/reference/rest), set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#endpointconfig) property to `true` as part of the clusters.create request to enable connecting to the Zeppelin notebook Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 

## Open the Zeppelin notebook

See [Viewing and Accessing Component Gateway URLs](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways#viewing_and_accessing_component_gateway_urls) to click Component Gateway links on the Google Cloud console to open the Zeppelin notebook UI running on the cluster's master node in your local browser.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
