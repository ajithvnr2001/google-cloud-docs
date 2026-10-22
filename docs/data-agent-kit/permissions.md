---
url: https://docs.cloud.google.com/data-agent-kit/permissions/
title: Permissions and APIs \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:13.447663+00:00
---

# Permissions and APIs  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Permissions and APIs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To work with Google Cloud data resources in Google Cloud Data Agent Kit, you need certain permissions and APIs enabled.

Data Agent Kit notifies you when you are missing a permission required to accomplish a task. You only need permissions for the services that you use, and the permissions that you need depend on the action that you want to perform.

To gain these permissions, ask your administrator to grant you a role on the project that you are working in that includes the permissions that you need. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

Similarly, you must enable the APIs for the services that you use. For more information about enabling APIs, see [Enable APIs](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.datacloud).

## Data analytics

The following roles let you work with Google Cloud data analytics services.

  * BigQuery 
    * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
    * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)
    * [Data Lineage Viewer (`roles/datalineage.viewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#datalineage.viewer)
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)
  * Knowledge Catalog 
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)
  * Dataflow 
    * [Dataflow Viewer (`roles/dataflow.viewer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.viewer)
  * BigLake Iceberg catalog 
    * [BigLake Viewer (`roles/biglake.viewer`)](https://docs.cloud.google.com/lakehouse/docs/iam-roles#biglake.viewer)
  * Managed Service for Apache Spark 
    * [Dataproc Viewer (`roles/dataproc.viewer`)](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam#dataproc.viewer)
    * [Dataproc Editor (`roles/dataproc.editor`)](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam#dataproc.editor)



Depending on your use case, you must enable the following data analytics APIs:

  * BigLake API
  * BigQuery API
  * BigQuery Data Transfer Service API
  * Cloud Composer API
  * Cloud Resource Manager API
  * Dataplex API
  * Dataflow API
  * Data Lineage API
  * Dataproc API
  * Dataproc Release Manager API



## Databases

The following roles let you work with Google Cloud databases in Data Agent Kit.

  * AlloyDB for PostgreSQL 
    * [AlloyDB Viewer (`roles/alloydb.viewer`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles)
    * [AlloyDB Database User (`roles/alloydb.databaseUser`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles)
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)
  * Bigtable 
    * [Bigtable Viewer (`roles/bigtable.viewer`)](https://docs.cloud.google.com/bigtable/docs/access-control#roles)
    * [Bigtable User (`roles/bigtable.user`)](https://docs.cloud.google.com/bigtable/docs/access-control#roles)
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)
  * Cloud SQL 
    * [Cloud SQL Viewer (`roles/cloudsql.viewer`)](https://docs.cloud.google.com/sql/docs/mysql/iam-roles#roles)
    * [Cloud SQL Instance User (`roles/cloudsql.instanceUser`)](https://docs.cloud.google.com/sql/docs/mysql/iam-roles#roles) or [Cloud SQL Studio User (`roles/cloudsql.studioUser`)](https://docs.cloud.google.com/sql/docs/mysql/iam-roles#roles)
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)
  * Spanner 
    * [Cloud Spanner Viewer (`roles/spanner.viewer`)](https://docs.cloud.google.com/spanner/docs/iam#spanner.viewer)
    * [Cloud Spanner Database User (`roles/spanner.databaseUser`)](https://docs.cloud.google.com/spanner/docs/iam#spanner.databaseUser) or [Cloud Spanner Database Reader (`roles/spanner.databaseReader`)](https://docs.cloud.google.com/spanner/docs/iam#spanner.databaseReader)
    * [Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer)



Depending on your use case, you must enable the following database APIs:

  * AlloyDB API
  * Cloud Bigtable Admin API
  * Cloud Bigtable Data API
  * Cloud Spanner API
  * Cloud SQL
  * Cloud SQL Admin API



## Other services

The following role lets you work with Google Cloud storage services in Data Agent Kit.

  * Cloud Storage 
    * [Storage Viewer (`roles/storage.viewer`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.viewer)



Depending on your use case, you'll need to enable the following APIs:

  * Cloud Storage API
  * Secret Manager API
  * Vertex AI API



## View APIs that you need to enable (extension only)

If you're using the Data Agent Kit extension in your IDE, the extension checks which required APIs are enabled when you select services.

  1. In the activity bar, click the **Google Cloud Data Agent Kit** icon.
  2. Expand **Settings** , and then click **Settings**.
  3. Click **Service Integrations**.
  4. Select the services that you want to use, and then click **Next**.

If any required APIs are disabled, the **Missing permissions** page lists them under **APIs to enable**.


**Note:** If you don't have the Service [Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) IAM role, ask your administrator to either grant you that role or enable these APIs for you. For more information, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

## What's next

  * [Mitigate prompt injection risks](https://docs.cloud.google.com/data-agent-kit/prompt-injection-risk)
  * [Codelab: Analytics with the Data Agent Kit and Antigravity](https://codelabs.developers.google.com/dak-analytics-eng-antigravity-ide#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
