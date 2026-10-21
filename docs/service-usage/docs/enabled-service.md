---
url: https://docs.cloud.google.com/service-usage/docs/enabled-service/
title: Enabled services \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:36.519887+00:00
---

# Enabled services  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/enabled-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enabled services

To use most Google Cloud APIs and services, you must first enable them in a Google Cloud project. Enabling APIs and services in a Google Cloud project results in the following changes:

  * Associates them with the project.
  * Adds monitoring pages in the Google Cloud console.
  * Enables billing for the APIs and services if billing is enabled for the project.
  * In some cases, [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles only become visible when you enable the associated service.



## Calling a service

The typical high-level requirements for using Google Cloud APIs and services are the following:

  1. You should have a Google Cloud project. For details on creating a Google Cloud project, see [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  2. You should enable the API or service for the project. To learn how to enable APIs and services, see [Enable and disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

  3. You should have authentication credentials for the service you enabled. To learn how to authenticate to a [Google Cloud API](https://docs.cloud.google.com/apis), see [Authentication for Google Cloud APIs and services](https://docs.cloud.google.com/docs/authentication).




The credentials you use to call Google Cloud APIs and services are associated with the project you use to create them.

## IAM role visibility

Some IAM roles are only visible if the associated service is enabled in a Google Cloud project. For example, the `roles/compute.admin` role is only visible after the `compute.googleapis.com` API is enabled in a project. To learn how to list the available roles to grant in a project, see [Viewing the grantable roles on resources](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).

## Services enabled by default

When you create a Google Cloud project using the Google Cloud console or Google Cloud CLI, the following APIs and services are enabled by default:

**Note:** You can disable any of the following services, just like any other service you enable.Service name | API endpoint  
---|---  
[App Topology API](https://docs.cloud.google.com/app-topology) | `apptopology.googleapis.com`  
[BigQuery sharing (formerly Analytics Hub)](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) | [`analyticshub.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest)  
[BigQuery API](https://docs.cloud.google.com/bigquery) | [`bigquery.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/rest)  
[BigQuery Connection API](https://docs.cloud.google.com/bigquery/docs/connections-api-intro) | [`bigqueryconnection.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest)  
BigQuery Data Policy API | [`bigquerydatapolicy.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest)  
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) | [`bigquerydatatransfer.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest)  
[BigQuery Migration API](https://docs.cloud.google.com/bigquery/docs/migration-intro) | [`bigquerymigration.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/migration/rest)  
BigQuery Reservation API | [`bigqueryreservation.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest)  
[BigQuery Storage API](https://docs.cloud.google.com/bigquery/docs/storage_overview) | [`bigquerystorage.googleapis.com`](https://docs.cloud.google.com/bigquery/docs/reference/storage/rpc)  
[Cloud Dataform API](https://docs.cloud.google.com/dataform) | [`dataform.googleapis.com`](https://docs.cloud.google.com/dataform/reference/rest)  
[Cloud Dataplex API](https://docs.cloud.google.com/dataplex) | [`dataplex.googleapis.com`](https://docs.cloud.google.com/dataplex/docs/reference/rest)  
[Cloud Datastore API](https://docs.cloud.google.com/datastore) | [`datastore.googleapis.com`](https://docs.cloud.google.com/datastore/docs/reference/data/rest)  
[Cloud Logging API](https://docs.cloud.google.com/logging) | [`logging.googleapis.com`](https://docs.cloud.google.com/logging/docs/reference/api-overview)  
[Cloud Monitoring API](https://docs.cloud.google.com/monitoring) | [`monitoring.googleapis.com`](https://docs.cloud.google.com/monitoring/api/v3)  
[Cloud SQL](https://docs.cloud.google.com/sql) | `sql-component.googleapis.com`  
[Cloud Storage](https://docs.cloud.google.com/storage) | `storage-component.googleapis.com`  
[Cloud Storage API](https://docs.cloud.google.com/storage) | [`storage.googleapis.com`](https://docs.cloud.google.com/storage/docs/json_api/v1)  
[Cloud Trace API](https://docs.cloud.google.com/trace) | [`cloudtrace.googleapis.com`](https://docs.cloud.google.com/trace/docs/reference/v1/rest)  
[Google Cloud APIs](https://docs.cloud.google.com/apis/docs/overview) | `cloudapis.googleapis.com`  
[Google Cloud Storage JSON API](https://docs.cloud.google.com/storage) | `storage-api.googleapis.com`  
[Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started) | [`servicemanagement.googleapis.com`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest)  
[Service Usage API](https://docs.cloud.google.com/service-usage) | [`serviceusage.googleapis.com`](https://docs.cloud.google.com/service-usage/docs/reference/rest)  
Telemetry API | [`telemetry.googleapis.com`](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
