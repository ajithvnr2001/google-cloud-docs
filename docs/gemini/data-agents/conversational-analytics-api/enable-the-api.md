---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api/
title: Enable the Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:10.366452+00:00
---

# Enable the Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Enable the Conversational Analytics API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps for enabling the Conversational Analytics API (accessed through `geminidataanalytics.googleapis.com` or regional endpoints) for your Google Cloud project. The Conversational Analytics API is the first capability under the [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com) in the Google Cloud console.

## Before you begin

Before you can use the Conversational Analytics API, you must have a Google Cloud project that can access the data that you want to work with. To set up your project, complete the following steps:

  1. Identify the data that you want to use with the Conversational Analytics API. You can use data sources like BigQuery tables, Looker Explores, Data Studio reports, and data from AlloyDB for PostgreSQL, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL.

  2. In the Google Cloud console, on the project selector page, [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) that can access the data that you want to use with the Conversational Analytics API.

**Note:** There is no billing for the Conversational Analytics API at this time.

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)




### Looker and Data Studio Pro requirements

If you use the Conversational Analytics API with Looker, your Looker instance must meet specific requirements:

  * [Looker (original)](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#before_you_begin)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#before_you_begin)



To use the Conversational Analytics API with Data Studio Pro, your Pro subscription must be outside of a VPC-SC perimeter.

### AlloyDB requirements

If you use the Conversational Analytics API with AlloyDB, your AlloyDB instance must meet specific requirements. Complete all of the steps in [Before you begin](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#before-begin).

### Cloud SQL for MySQL requirements

If you use the Conversational Analytics API with Cloud SQL for MySQL, your Cloud SQL instance must meet specific requirements. Complete all of the steps in [Before you begin](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#before-begin).

### Cloud SQL for PostgreSQL requirements

If you use the Conversational Analytics API with Cloud SQL for PostgreSQL, your Cloud SQL instance must meet specific requirements. Complete all of the steps in [Before you begin](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents#before-begin).

### Spanner requirements

If you use the Conversational Analytics API with Spanner, your Spanner instance must meet specific requirements. Complete all of the steps in [Before you begin](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/spanner/create-data-agents#before-begin).

## Enable the required APIs

To use the Conversational Analytics API, you must enable a set of required APIs in your Google Cloud project. If you plan to use the Conversational Analytics API from a Colab Enterprise environment, you must also enable additional APIs.

### Required APIs

**Note:** If you don't have permission to enable the APIs, ask your project administrator to enable the APIs for you from the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard). Alternatively, your project administrator can grant you the [Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`)](https://docs.cloud.google.com/service-usage/docs/access-control) role in the Google Cloud console, which lets you manage APIs for the current project.

### console

Enable the following APIs, if they're not already enabled, for the Google Cloud project that you will use with the Conversational Analytics API.

[ Enable the Gemini Data Analytics API](https://console.cloud.google.com/apis/enableflow?apiid=geminidataanalytics.googleapis.com)

[Enable the Gemini for Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=cloudaicompanion.googleapis.com)

[ Enable the BigQuery API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com)

**Tip:** When you enable an API, you might need to refresh the Google Cloud console page to confirm that it's enabled.

###  gcloud 

With the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), run the following [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) commands to enable the Gemini Data Analytics API, the Gemini for Google Cloud API, and the BigQuery API, respectively:
    
    
    gcloud services enable geminidataanalytics.googleapis.com --project=project_id
    gcloud services enable cloudaicompanion.googleapis.com --project=project_id
    gcloud services enable bigquery.googleapis.com --project=project_id
    

In the previous sample gcloud CLI commands, replace `project_id` with your Google Cloud project ID.

**Note:** Only enable the BigQuery API if you're using BigQuery.

### APIs for Colab Enterprise

If you plan to use the Conversational Analytics API from a Colab Enterprise environment, also confirm that the following APIs are enabled:

[ Enable the Dataform API](https://console.cloud.google.com/apis/enableflow?apiid=dataform.googleapis.com)

[ Enable the Compute Engine API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

[ Enable the Vertex AI API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

**Tip:** When you enable an API, you might need to refresh the Google Cloud console page to confirm that it's enabled.

## Grant required roles

To use the Conversational Analytics API, principals (such as users or service accounts) require Identity and Access Management (IAM) roles that provide access to both the API and the underlying data sources.

To grant these roles, use the Google Cloud console:

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

### Gemini Data Analytics roles

To enable principals to create Conversational Analytics API agents and use the stateful chat method for conversations, grant the following IAM roles:

  * [Gemini Data Analytics Data Agent Creator (`roles/geminidataanalytics.dataAgentCreator`)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#data-agent-creator): required to start creating agents only in BigQuery, Looker, and Data Studio Pro.
  * [Gemini for Google Cloud User (`roles/cloudaicompanion.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user): required to use the stateful chat method for conversations.



In addition, permissions for actions like managing agents are controlled by **Gemini Data Analytics** roles, as described in [Conversational Analytics API access control with IAM](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

### BigQuery roles

To enable principals to query BigQuery data sources through the Conversational Analytics API, grant the following IAM roles:

  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user): required to access data in BigQuery.
  * [BigQuery Studio User (`roles/bigquery.studioUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser): required if you use BigQuery Studio and data canvas.



### Looker roles

To enable principals to query Looker data sources through the Conversational Analytics API, grant the following IAM roles:

  * [Looker Instance User (`roles/looker.instanceUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.instanceUser): required to access data from a Looker (Google Cloud core) instance.



To use Conversational Analytics and the Conversational Analytics API, a Looker user must be assigned a [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) that contains the `gemini_in_looker` permission for the models that they interact with.

### Database roles

To enable principals to query AlloyDB, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, or Spanner data sources through the Conversational Analytics API, grant the following IAM roles:

  * [AlloyDB Database User (`roles/alloydb.databaseUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.databaseUser): required to access data from an AlloyDB instance.
  * [Cloud SQL for MySQL and Cloud SQL for PostgreSQL Studio User (`roles/cloudsql.studioUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser): required to use the Google Cloud console to view and manage Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances.
  * [Cloud SQL for MySQL and Cloud SQL for PostgreSQL Instance User (`roles/cloudsql.instanceUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser): required to connect to Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances.
  * [Spanner Database Reader (`roles/spanner.databaseReader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseReader): required to read data from a GoogleSQL for Spanner database.



Optionally, if you use context sets ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) with database data sources, to create, upload, and manage context sets, enable the [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com) and grant one of the following [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions) at the project level:

  * [Dataplex Catalog Editor (`roles/dataplex.catalogEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor): grants access to create, update, delete, upload, and download context sets.
  * [Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin): grants full administrative access to context sets.



## What's next

  * Learn about [access control for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).
  * Learn how to configure [VPC Service Controls for the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/vpc-sc).



## What's next

  * Learn how to [Authenticate to your data source and the API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn how to [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).
  * Learn how to [Build a data agent using HTTP and Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
