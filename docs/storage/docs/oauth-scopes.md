---
url: https://docs.cloud.google.com/storage/docs/oauth-scopes/
title: Cloud Storage OAuth 2.0 scopes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:55.867201+00:00
---

# Cloud Storage OAuth 2.0 scopes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/oauth-scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage OAuth 2.0 scopes Stay organized with collections  Save and categorize content based on your preferences. 

Most of the operations you perform in Cloud Storage must be authenticated. The only exceptions are operations on resources that allow anonymous access. A resource has anonymous access if the `allUsers` group is included in the ACL for the resource or if the `allUsers` group is included in an IAM policy that applies to the resource. The `allUsers` group includes anyone on the Internet.

Authorization is the process of determining what permissions an authenticated identity has on a set of specified resources. OAuth 2.0 uses _scopes_ to determine if an authenticated identity is authorized. Applications use a credential (obtained from a user-centric or server-centric authentication flow) together with one or more scopes to request an access token from a Google authorization server to access protected resources. For example, application A with an access token with `read-only` scope can only read, while application B with an access token with `read-write` scope can read and modify data. Neither application can read or modify access control lists on objects and buckets; only an application with `full-control` scope can do so.

Type | Description | Scope URL  
---|---|---  
`read-only` | Only allows access to read data, including listing buckets. | `https://www.googleapis.com/auth/devstorage.read_only`  
`read-write` | Allows access to read and change data, but not metadata like IAM policies. | `https://www.googleapis.com/auth/devstorage.read_write`  
`full-control` | Allows full control over data, including the ability to modify IAM policies. | `https://www.googleapis.com/auth/devstorage.full_control`  
`cloud-platform.read-only` | View your data across Google Cloud services. For Cloud Storage, this is the same as `devstorage.read-only`.  | `https://www.googleapis.com/auth/cloud-platform.read-only`  
`cloud-platform` | View and manage data across all Google Cloud services. For Cloud Storage, this is the same as `devstorage.full-control`. | `https://www.googleapis.com/auth/cloud-platform`  
`bigquery.read-only` | View your data in Google BigQuery. For Cloud Storage, this is the same as `devstorage.read-only`.  | `https://www.googleapis.com/auth/bigquery.readonly`  
`bigquery` | Allow access to read and write data in BigQuery. For Cloud Storage, this is the same as `devstorage.read-write`. | `https://www.googleapis.com/auth/bigquery`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
