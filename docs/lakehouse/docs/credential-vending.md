---
url: https://docs.cloud.google.com/lakehouse/docs/credential-vending/
title: Credential vending overview \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:51.350092+00:00
---

# Credential vending overview  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/credential-vending/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Credential vending overview Stay organized with collections  Save and categorize content based on your preferences. 

Credential vending for the _Lakehouse runtime catalog_ lets you delegate storage access and apply fine-grained permissions to your data files. As part of _borderless Lakehouse_ , this capability lets you manage Identity and Access Management (IAM) policies at the table level for tables stored in Cloud Storage.

You can use the `gcloud` CLI to get and set these policies to control access to your resources.

## How credential vending works

When you use credential vending, the sequence of operations changes slightly to enforce policies before storage is accessed. The following diagram illustrates how query engines obtain downscoped storage tokens from the catalog to securely read and write data directly in Cloud Storage:

![Credential vending architecture diagram illustrating how query engines obtain downscoped storage tokens from the Lakehouse runtime catalog to securely access Cloud Storage.](https://docs.cloud.google.com/static/lakehouse/images/credential-vending-diagram.svg)Credential vending workflow delegating Cloud Storage access.

The sequence of operations shown in the preceding diagram is as follows:

  1. **Request:** A user submits a SQL statement, such as a query, DML, or DDL operation, to a supported engine. For example, Apache Spark or BigQuery.
  2. **Metadata lookup:** The engine sends a request to the Lakehouse runtime catalog to resolve the table.
  3. **Authentication and policy:** The catalog authenticates the user and checks their IAM permissions on Google Cloud's _Lakehouse_ resources.
  4. **Response:** Because credential vending is enabled, the catalog returns the metadata and a short-lived **storage token** (downscoped storage credentials) to the engine. The token is scoped to the paths associated with the table and downscoped to the minimum required permissions (for example, read-only access for queries that don't need to write files).
  5. **Access:** The engine uses this token to read or write the specific authorized files directly from Cloud Storage.
  6. **Compute:** The engine processes the data or executes the operation, and returns the results.



## Supported engines

In order to use credential vending with query engines, your Lakehouse Iceberg REST catalog must be configured to support credential vending.

  * **Open source engines:** Supported engines like Apache Spark and Trino use short-lived storage tokens vended by the catalog. Your client application must specify support for credential vending in the `X-Iceberg-Access-Delegation` header.
  * **BigQuery:** BigQuery uses vended credentials for Cloud Storage access instead of end-user credentials.



## Required service account permissions

When credential vending is enabled, ensure the following service accounts have the necessary roles:

  * **Auto-provisioned Lakehouse runtime catalog service account** : You must grant the Storage Object User role (`roles/storage.objectUser`) to this account on all associated Cloud Storage buckets. Without this access, vended credentials can't read or write to storage. If you use the Google Cloud console, clicking **Set bucket permissions** verifies this role. For the gcloud CLI, Terraform, or the API, you must grant this role manually.
  * **Query engine service accounts** : Service accounts running query engine jobs (such as Managed Service for Apache Spark, Managed Service for Apache Spark, or Dataflow) require the BigLake Editor role (`roles/biglake.editor`) to obtain vended credentials with write scope.

**Note:** Creation of the auto-provisioned catalog service account is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## What's next

  * Learn how to [create a catalog in credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#create_a_catalog).
  * Learn how to [enable credential vending for an existing catalog using the Google Cloud console](https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending). 
    * Learn how to [configure your client application for credential vending](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#configure-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
