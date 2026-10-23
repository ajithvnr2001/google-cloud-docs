---
url: https://docs.cloud.google.com/logging/docs/analyze/data-security-with-analytics/
title: Data security with Observability Analytics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:27.982551+00:00
---

# Data security with Observability Analytics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/data-security-with-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Data security with Observability Analytics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes Google Cloud features that can help prevent data exfiltration through phishing, insider attacks, or external entities when you are using Observability Analytics. It also describes the two query engines available for Observability Analytics and how the choice of query engine affects what data you can query.

## Organization restrictions

You can use [organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/overview) to restrict principals such that they only have access to resources in authorized Google Cloud organizations. Essentially, when you configure organization restrictions you are configuring an egress proxy. For example, you can use organization restrictions to prevent data stored by the organization from being combined with external data when you use Observability Analytics.

For more information, see [Configure organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions).

## VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) helps protect against accidental or targeted action by external entities or insider entities, which helps to minimize unwarranted data exfiltration risks from Google Cloud services such as Cloud Storage and BigQuery. You can use VPC Service Controls to create perimeters that protect the resources and data of services that you explicitly specify.

A VPC Service Controls _perimeter_ is a security boundary around Google Cloud resources. It allows free communication within the perimeter but, by default, blocks communication to Google Cloud services across the perimeter. A perimeter doesn't block access to any third-party APIs or services on the internet.

Don't confuse a VPC Service Controls perimeter with a [virtual private cloud network](https://docs.cloud.google.com/vpc/docs/vpc). A VPC Service Controls perimeter is a security boundary.

For more information, see [Set up a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter).

For information about Logging and VPC Service Controls, see [Supported products: Logging](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_logging).

## Choose your Observability Analytics query engine

Observability Analytics lets you run SQL queries on either the default Logging engine or the BigQuery engine.

Both query engines provide the same level of data security, but they use different permission layers. The default engine checks Logging permissions, while the BigQuery engine checks BigQuery permissions.

To set the query engine, on the **Observability Analytics** page, use the _settings_ **Settings** menu:

[Go to **Log Analytics**](https://console.cloud.google.com/logs/analytics)

### Run queries on the default query engine

The default query engine is managed by Google Cloud Observability. When you use this engine, you can query the following:

  * [Log views](https://docs.cloud.google.com/logging/docs/logs-views)
  * [Analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views)



The following table summarizes how Cloud Logging uses [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/overview) to control access to the data it stores:

Source queried by Observability Analytics | Required IAM role(s) to read source data  
---|---  
`_AllLogs` view  
on the `_Required` log bucket | [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)  
on the project that stores the `_Required` log bucket.  
`_AllLogs` view  
on the `_Default` log bucket | [Private Logs Viewer (`roles/logging.privateLogViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer)  
on the project that stores the `_Default` log bucket.  
`_Default` view  
on the `_Default` log bucket | [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)  
on the project that stores the `_Default` log bucket.  
Custom log views  
(on any log bucket) | For read access to all log views in a project:  
[Logs View Accessor (`roles/logging.viewAccessor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) on the project. For read access to only a specific log view in a project, one of the following:

  * [Logs View Accessor (`roles/logging.viewAccessor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor)  
on the project. However, include an IAM condition on the role that restricts the grant to a specific log view.
  * A binding for your ID is included in the IAM policy for the log view.

  
Analytics views | All of the following:

  * [Observability Analytics User (`roles/observability.analyticsUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser)  
on the project.
  * An IAM role that provides read-access to the log view that is queried by the analytics view.

  
  
For information about Logging roles, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

### Run queries on the BigQuery engine

The BigQuery engine can run queries that include joins of a log view with other BigQuery tables. However, to use this engine, you must create a link to a [linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) on the corresponding [log bucket](https://docs.cloud.google.com/logging/docs/store-log-entries). A linked BigQuery dataset is a read-only BigQuery dataset that serves as a pointer to a shared dataset.

If you create linked BigQuery datasets for your log buckets, then you expand the security boundary of that data to include BigQuery services. That is, BigQuery services can now query your log data by issuing a query to a linked BigQuery dataset.

If you set the query engine to be BigQuery, then the following are true:

  * You can query log views when a linked BigQuery dataset exists for the associated log bucket. However, the Observability Analytics service enhances queries that are sent to the BigQuery engine. For this reason, if you view BigQuery metadata, it might be different than expected.

  * Before a query is run, your [BigQuery IAM permissions](https://docs.cloud.google.com/bigquery/docs/access-control) are checked.

  * Queries that you run on the BigQuery engine are subject to BigQuery pricing.




The following table summarizes how the BigQuery engine uses IAM to control access to the source data:

Source queried by Observability Analytics | Required IAM role(s) to read source data  
---|---  
`_AllLogs` view  
on the `_Required` log bucket | All of the following:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)  
on the project or on the linked BigQuery dataset for the `_Required` log bucket.
  * An IAM role that includes the [`logging.links.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.links.list) permission.

  
`_AllLogs` view  
on the `_Default` log bucket | All of the following:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)  
on the project or on the linked BigQuery dataset for the `_Default` log bucket.
  * An IAM role that includes the [`logging.links.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.links.list) permission.

  
`_Default` view  
on the `_Default` log bucket | All of the following:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)  
on the project or on the linked BigQuery dataset for the `_Default` log bucket.
  * An IAM role that includes the [`logging.links.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.links.list) permission.

  
Custom log views  
(on any log bucket) | All of the following:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)  
on the project or on the linked BigQuery dataset for the log bucket.
  * An IAM role that includes the [`logging.links.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.links.list) permission.

  
Analytics views | Not supported.  
Log view joined with  
a BigQuery table | All of the following:

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)  
on the project or on the linked BigQuery datasets for the log bucket and the other BigQuery table.
  * An IAM role that includes the [`logging.links.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.links.list) permission.

  
  
For information about managing access to linked BigQuery datasets, see [BigQuery Access Control](https://docs.cloud.google.com/bigquery/docs/access-control).

## What's next

  * [Save and share a SQL query](https://docs.cloud.google.com/logging/docs/analyze/save-share-query).
  * [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples).
  * [Chart SQL query results](https://docs.cloud.google.com/logging/docs/analyze/charts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
