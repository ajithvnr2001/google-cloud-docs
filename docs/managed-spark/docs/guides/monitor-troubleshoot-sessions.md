---
url: https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-sessions/
title: Monitor and troubleshoot interactive sessions \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:35.627318+00:00
---

# Monitor and troubleshoot interactive sessions  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-sessions/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Monitor and troubleshoot interactive sessions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor and troubleshoot Managed Service for Apache Spark [interactive sessions](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions) using the Spark UI. 

## Spark UI

The Spark UI collects Apache Spark execution details from Managed Service for Apache Spark interactive sessions. There is no charge for the Spark UI feature, which is enabled by default. Data collected by the Spark UI feature is retained for 90 days.

**Note:** The Spark UI also collects and displays execution details from Managed Service for Apache Spark batch workloads. See [Monitor and troubleshoot batch workloads](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches) for more information.

### Required Identity and Access Management permissions and roles

The following permissions are required to use the Spark UI feature with interactive sessions:

  * Data collection permission: `dataproc.sessions.sparkApplicationWrite`. This permission must be granted to the service account that runs interactive sessions. It is included in the [`Managed Service for Apache Spark Worker`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role, which is automatically granted to the Compute Engine default service account that Managed Service for Apache Spark uses by default. However, if you specify a [custom service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account) for your [session](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--service-account) or [session runtime template](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#dataproc_create_serverless_runtime_template_yaml-Complex%20YAML), you must add this `dataproc.sessions.sparkApplicationWrite` permission to that service account (typically, by granting the service account the Managed Service for Apache Spark `Worker` role).

  * Spark UI access permission: `dataproc.sessions.sparkApplicationRead`. This permission must be granted to a user to access the Spark UI in the Google Cloud console. It is included in the [`Dataproc Viewer`, `Dataproc Editor` and `Dataproc Administrator`](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#roles) roles. To open the Spark UI in the Google Cloud console, you must have one of these roles or have a custom role that includes this permission.




### Open the Spark UI

The Spark UI page is available in the Google Cloud console.

  1. [Go to Managed Service for Apache Spark Interactive Sessions](https://console.cloud.google.com/managed-spark/interactive)

  2. Click an **Interactive Session ID** to open the **Interactive Session Details** page.
  3. Click **View Spark UI** in the top menu.



**Is the _View Spark UI_ link disabled?** If a required permission is not granted, or if you clear the **Enable Spark UI** checkbox on the interactive session details page or set the `spark.dataproc.appContext.enabled` property to `false` (default: `true`) when you [create a session](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create/spark#--property) or [create a session runtime template](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#create_a_serverless_runtime_template), the **View Spark UI** button will be disabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
