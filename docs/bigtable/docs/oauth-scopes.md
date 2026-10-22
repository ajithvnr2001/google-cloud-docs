---
url: https://docs.cloud.google.com/bigtable/docs/oauth-scopes/
title: Bigtable OAuth scopes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:17.578091+00:00
---

# Bigtable OAuth scopes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/oauth-scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bigtable OAuth scopes

OAuth scopes let Google Cloud services such as Compute Engine and Dataflow authenticate and connect to Bigtable. Configuring appropriate scopes grants applications the specific data and administrative access that they require.

To connect a resource, such as a Compute Engine virtual machine instance, to Bigtable, specify the appropriate OAuth scopes and [enable access to Bigtable](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) when you create the resource. Choose the most restrictive scopes that support your application's requirements, because you can't change the scopes after you create the resource.

Bigtable supports the following scopes:

Scope URI for `gcloud` | Description  
---|---  
`https://www.googleapis.com/auth/bigtable.admin` | Alias for both `bigtable.admin.instance` and `bigtable.admin.table`.  
`https://www.googleapis.com/auth/bigtable.admin.instance` | Enables creation and management of Bigtable instances and clusters.  
`https://www.googleapis.com/auth/bigtable.admin.table` | Enables creation and management of Bigtable tables and their column families.  
`https://www.googleapis.com/auth/bigtable.data` | Enables read and write access to data stored in Bigtable tables.  
`https://www.googleapis.com/auth/bigtable.data.readonly` | Enables read-only access to data stored in Bigtable tables.  
`https://www.googleapis.com/auth/cloud-bigtable.data` | Enables read and write access to data stored in Bigtable tables.  
`https://www.googleapis.com/auth/cloud-bigtable.data.readonly` | Enables read-only access to data stored in Bigtable tables.  
`https://www.googleapis.com/auth/cloud-platform` | Enables full access to all Google Cloud products, including Bigtable.  
`https://www.googleapis.com/auth/cloud-platform.readonly` | Enables read-only access to all Google Cloud products, including Bigtable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
