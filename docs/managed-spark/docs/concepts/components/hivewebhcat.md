---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hivewebhcat/
title: Managed Service for Apache Spark optional Hive WebHCat component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.842749+00:00
---

# Managed Service for Apache Spark optional Hive WebHCat component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hivewebhcat/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Hive WebHCat component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Hive WebHCat when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes the Hive WebHCat component.

The [Hive WebHCat](https://cwiki.apache.org/confluence/display/Hive/WebHCat) component provides a REST API for HCatalog. The REST service is available on port `50111` on the cluster's first master node.

## Install the component

Install the component when you create a Managed Service for Apache Spark cluster. Components can be added to clusters created with Managed Service for Apache Spark [version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Hive WebHCat** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Hive WebHCat component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=HIVE_WEBHCAT \
        --region=region \
        ... other args
    

### REST API

The Hive WebHCat component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
