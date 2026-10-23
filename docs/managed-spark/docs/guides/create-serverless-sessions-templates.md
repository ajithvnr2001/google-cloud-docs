---
url: https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates/
title: Create interactive sessions and session templates \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:51.602955+00:00
---

# Create interactive sessions and session templates  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create interactive sessions and session templates Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create Managed Service for Apache Spark interactive sessions and session templates. A session template can be used to create multiple interactive sessions based on the session template configuration.

**Note:** Managed Service for Apache Spark interactive sessions are associated with interactive notebooks. For an example of session use with Jupyter notebooks, see [Use the Managed Service for Apache Spark JupyterLab plugin for serverless batch and interactive notebook sessions](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions). For examples of session use in BigQuery Studio notebooks, see [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark).

## Create an interactive session

You can use the Google Cloud CLI or the Managed Service for Apache Spark API to create a Managed Service for Apache Spark interactive session.

### gcloud

You can use the [`gcloud beta dataproc sessions create command SESSION_NAME`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create) to create a Managed Service for Apache Spark interactive session.
    
    
    gcloud beta dataproc sessions create spark SESSION_ID \
        --location=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
        optional flags ...
    

Replace or add the following:

  * SESSION_ID: Required. An ID for the session.

  * REGION: Required. An [available region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to locate your session.

  * [`--version`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--version): Optional. A supported [Spark runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). If you don't use this flag to specify a version, the current default Spark runtime version is used.

  * [`--container-image`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--container-image): Optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your session.

  * [`--property`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--property): Optional. One or more comma-separated [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties) for your session.

  * [`--service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--service-account): Optional. The [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#console) to use for your session. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`--subnet`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--subnet): Optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).




### REST

You can use the Managed Service for Apache Spark [`sessions.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions/create) API to create a Managed Service for Apache Spark interactive session.

Notes:

  * [`name`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions#Session.FIELDS.name): Required. Session name.

  * [`version`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.version): Optional. Any of the supported [Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) for your session. If you don't specify a version, the current default version is used.

  * [`containerImage`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.container_image): Optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your session.

  * [`properties`](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.properties): Optional. A mapping of session property names to values. See [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties).

  * [`serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.service_account): Optional. The [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#console) to use to run your session. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`subnetworkUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.subnetwork_uri): Optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).




## Create a session template

A Managed Service for Apache Spark session template defines the configuration settings for creating one or more Managed Service for Apache Spark interactive sessions. You can use the Google Cloud console, the gcloud CLI, or the Managed Service for Apache Spark API to create a Managed Service for Apache Spark session template for a Jupyter or [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html) session.

**Note:** You can create a session in a BigQuery Studio notebook from a Managed Service for Apache Spark session template. This section explains how to configure the template to use it in a BigQuery Studio notebook. 

### Console

To create a Managed Service for Apache Spark session template using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Session Templates** page.

[Go to Session Templates](https://console.cloud.google.com/dataproc/sessionTemplates)

     1. Click **Create**.
  2. In the **Create session template** page, input or confirm the template configuration settings. Note the following:

     * **Template runtime ID:** Required. Accept the default ID (name) or specify a template runtime name.
     * **Region** : Required. Accept the default region or specify an [available region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for template sessions.
     * **Runtime version:** Optional. Selectable session runtimes correspond to [Managed Service for Apache Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions). 
       * **BigQuery Studio notebook session requirement:** If you are creating a template to use for [BigQuery Studio notebook Spark Connect sessions](https://docs.cloud.google.com/bigquery/docs/use-spark#dataproc_serverless_bq_spark_session-Templated%20Spark%20session), it must use [Spark runtime version 2.3+](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.3).
     * **Template configuration type:** Required. Select a type. If you select `Jupyter`, specify the **Display name** and select the **Jupyter kernel type**. Also see [Launch a Jupyter notebook on Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#launch_a_jupyter_notebook_on). 
       * **BigQuery Studio notebook session requirement:** [BigQuery Studio notebook sessions](https://docs.cloud.google.com/bigquery/docs/use-spark#dataproc_serverless_bq_spark_session-Templated%20Spark%20session) must specify **Spark Connect** as the template configuration type.
     * **Service account:** Optional. The [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#console) to use to run templated sessions. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.
     * **Custom container image:** Optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your templated sessions.
     * **Properties:** Optional. Click **Add Item** for each property to set for your templated sessions. For more information, see [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties).
     * **Network configuration:** * Required. Select a **subnetwork** in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the specified subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).
  3. Click **Submit** to create the session template.




### gcloud

You can't directly create a Managed Service for Apache Spark session template using the gcloud CLI, but you can use the `gcloud beta dataproc session-templates import` command to import an existing session template. You can edit the imported template, and then export it using the `gcloud beta dataproc session-templates export` command. 

### REST

You can use the Managed Service for Apache Spark [`sessionTemplates.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates/create) API to create a Managed Service for Apache Spark session template.

Notes:

  * [`name`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates#Session.SessionTemplate.FIELDS.name): Required. Session template name.

  * [`version`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.version): Optional. Any of the supported [Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) for your templated sessions. If you don't specify a version, the default version is used.

    * **BigQuery Studio notebook session requirement:** If you are creating a template to use for [BigQuery Studio notebook Spark Connect sessions](https://docs.cloud.google.com/bigquery/docs/use-spark#dataproc_serverless_bq_spark_session-Templated%20Spark%20session), it must use [Spark runtime version 2.3+](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.3).
  * [`sessionConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates#SessionTemplate.FIELDS.spark_connect_session): Specify either `jupyter_session` or `spark_connect_session`. If you specify `jupyter_session`, also specify the [`JupyterConfig.display_name`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JupyterConfig#FIELDS.display_name) and [`JupyterConfig.kernel`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JupyterConfig#kernel). Also see [Launch a Jupyter notebook on Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#launch_a_jupyter_notebook_on).

    * **BigQuery Studio notebook session requirement:** [BigQuery Studio notebook sessions](https://docs.cloud.google.com/bigquery/docs/use-spark#dataproc_serverless_bq_spark_session-Templated%20Spark%20session) must specify **Spark Connect** as the template configuration type.
  * [`containerImage`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.container_image): Optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your templated sessions.

  * [`properties`](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.properties): Optional. A mapping of session property names to values. See [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties).

  * [`serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.service_account): Optional. A [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#console) to use to run your templated sessions,. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`subnetworkUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.subnetwork_uri): Optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
