---
url: https://docs.cloud.google.com/datastream/docs/sources-workday/
title: Stream data from Workday \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:53.091057+00:00
---

# Stream data from Workday  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-workday/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Workday Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Datastream supports replicating data from a Workday instance. Workday is a cloud-based enterprise resource planning (ERP) platform. The platform focuses on financial and human capital management, and lets you manage all aspects of the employee lifecycle, such as recruiting, onboarding, compensation, or time tracking.

This page contains information about:

  * The behavior of how Datastream handles data that's being pulled from a source Workday instance.
  * Supported objects.
  * Known limitations for using Workday as a source.



## Behavior

The Workday connector in Datastream relies on the [Workday SOAP API](https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html). Because Workday doesn't expose its internal table schema to users, Datastream treats SOAP API endpoints as tables.

Datastream supports two primary replication methods to ensure data integrity and performance: historical backfill and incremental synchronization.

  * **Historical backfill** : the Workday connector allows for full historical synchronization of all existing records in an endpoint. To ensure consistency across backfill queries, Datastream uses the `as_of_entry_date_time` parameter. This lets the connector consistently fetch one page of data at a time.

  * **Incremental synchronization** : the incremental synchronization method captures changes, such as inserts and updates, that occur after the initial backfill. Datastream uses server-side incremental synchronization by selecting endpoints that support transaction logs. These logs enable the connector to filter queries by the `updated_through` field, which only selects records that have been updated since a specific date.




## Supported objects

The Workday connector leverages a dynamic discovery mechanism to identify the entire set of objects within an instance. The connector fetches the Web Services Description Language (WSDL) files corresponding to each SOAP API service.

For each endpoint in each service, the connector uses the WSDL file to determine whether the endpoint supports transaction logs.

The following table lists the objects that Datastream supports and their replication types:

Object | Replication type  
---|---  
`Financial_Management_Organizations` | Backfill, incremental sync  
`Human_Resources_Job_Profiles` | Backfill, incremental sync  
`Human_Resources_Organizations` | Backfill, incremental sync  
`Human_Resources_Workers` | Backfill, incremental sync  
`Recruiting_Candidates` | Backfill, incremental sync  
`Recruiting_Evergreen_Requisitions` | Backfill, incremental sync  
`Recruiting_Job_Requisitions` | Backfill, incremental sync  
`Recruiting_Organizations` | Backfill, incremental sync  
`Recruiting_Positions` | Backfill, incremental sync  
`Staffing_Organizations` | Backfill, incremental sync  
`Staffing_Positions` | Backfill, incremental sync  
`Staffing_Workers` | Backfill, incremental sync  
  
## Known limitations

Known limitations for using Workday as a source include:

  * Datastream doesn't support replicating delete events.
  * Datastream doesn't replicate events fetched from endpoints that don't support transaction logs.



## What's next

  * Learn how to [configure a Workday source](https://docs.cloud.google.com/datastream/docs/configure-workday) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
