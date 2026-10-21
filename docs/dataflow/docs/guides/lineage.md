---
url: https://docs.cloud.google.com/dataflow/docs/guides/lineage/
title: Use data lineage in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:50.078878+00:00
---

# Use data lineage in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/lineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use data lineage in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Data lineage is a Dataflow feature that lets you track how data moves through your systems: where it comes from, where it is passed to, and what transformations are applied to it.

Each pipeline that you run by using Dataflow has several associated data assets. The lineage of a data asset includes its origin, what happens to it, and where it moves over time. With data lineage, you can track the end-to-end movement of your data assets, from origin to eventual destination.

When you enable data lineage for your Dataflow jobs, Dataflow captures lineage events and publishes them to the Knowledge Catalog [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest).

To access lineage information through Knowledge Catalog, see [Use data lineage with Google Cloud systems](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).

## Before you begin

Set up your project: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Dataplex, BigQuery, and Data lineage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com,datalineage.googleapis.com)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataplex, BigQuery, and Data lineage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com,datalineage.googleapis.com)


**Caution:** Data lineage is enabled on a per-project basis, not a per-service basis. After you enable the Data Lineage API, lineage information is automatically reported for multiple Google Cloud services in the project, depending on their product-level lineage control. For more details, see [Data lineage considerations and limitations](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-considerations). 

In Dataflow, you also need to enable lineage at the job level. See Enable data lineage in Dataflow in this document.

### Required roles

To get the permissions that you need to view lineage visualization graphs, ask your administrator to grant you the following IAM roles: 

  * [Dataplex Catalog viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the Knowledge Catalog resource project
  * [Data Lineage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`) on the project where you use Dataflow
  * [Dataflow viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.viewer) (`roles/dataflow.viewer`) on the project where you use Dataflow



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about data lineage roles, see [Predefined roles for data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#lineage-roles).

## Support and limitations

Data lineage in Dataflow has the following limitations:

  * Data lineage is supported in the Apache Beam SDK versions 2.63.0 and later.
  * You must enable data lineage on a per-job basis.
  * Data capture isn't instantaneous. It can take a few minutes for Dataflow job lineage data to appear in Knowledge Catalog.
  * The following sources and sinks are supported:

    * Apache Kafka
    * BigQuery (Streaming jobs in Python use the legacy [`STREAMING_INSERT`](https://docs.cloud.google.com/bigquery/docs/samples/bigquery-table-insert-rows) method, which doesn't support data lineage. To use data lineage, switch to the recommended [`STORAGE_WRITE_API`](https://docs.cloud.google.com/bigquery/docs/write-api) method. For more information, see [Write from Dataflow to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery).)
    * Bigtable
    * Cloud Storage
    * JDBC (Java Database Connectivity)
    * Pub/Sub
    * Spanner (Change Stream is not supported)

[Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) that use these sources and sinks also automatically capture and publish lineage events.




## Enable data lineage in Dataflow

You need to enable lineage at the job level. To enable data lineage, use the `enable_lineage` [Dataflow service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options) as follows:

### Java
    
    
    --dataflowServiceOptions=enable_lineage=true
    

### Python
    
    
    --dataflow_service_options=enable_lineage=true
    

### Go
    
    
    --dataflow_service_options=enable_lineage=true
    

###  gcloud 

Use the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command with the `additional-experiments` option. If you're using Flex Templates, use the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
    
    
    --additional-experiments=enable_lineage=true
    

Optionally, you can specify one or both of the following parameters with the service option:

  * `process_id`: A unique identifier that Knowledge Catalog uses to group job runs. If not specified, the job name is used.
  * `process_name`: A human-readable name for the data lineage process. If not specified, the job name prefixed with `"Dataflow "` is used.



Specify these options as follows:

### Java
    
    
    --dataflowServiceOptions=enable_lineage=process_id=PROCESS_ID;process_name=DISPLAY_NAME
    

### Python
    
    
    --dataflow_service_options=enable_lineage=process_id=PROCESS_ID;process_name=DISPLAY_NAME
    

### Go
    
    
    --dataflow_service_options=enable_lineage=process_id=PROCESS_ID;process_name=DISPLAY_NAME
    

###  gcloud 
    
    
    --additional-experiments=enable_lineage=process_id=PROCESS_ID;process_name=DISPLAY_NAME
    

## View lineage in Knowledge Catalog

Data lineage provides information about the relations between your project resources and the processes that created them. You can view data lineage information in the Google Cloud console in the form of a graph or a single table. You can also retrieve data lineage information from the Data Lineage API in the form of JSON data.

For more information, see [Use data lineage with Google Cloud systems](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).

## Disable data lineage in Dataflow

If data lineage is enabled for a specific job and you want to disable it, cancel the existing job and run a new version of the job without the `enable_lineage` service option.

## Billing

Using data lineage in Dataflow doesn't impact your Dataflow bill, but it might incur additional charges on your Knowledge Catalog bill. For more information, see [Data lineage considerations](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-considerations) and [Knowledge Catalog pricing](https://cloud.google.com/dataplex/pricing).

## What's next

  * Learn more about [data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage).
  * Learn how to [use data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
