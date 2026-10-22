---
url: https://docs.cloud.google.com/datastream/docs/sources-dataverse/
title: Stream data from Microsoft Dataverse \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:29.888520+00:00
---

# Stream data from Microsoft Dataverse  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-dataverse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Microsoft Dataverse Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Datastream supports replicating change events from a Microsoft Dataverse instance. Dataverse is a cloud-based data platform that lets you securely store and manage data used by business applications.

This page contains information about:

  * The key terms that you need to understand when replicating from Dataverse.
  * The behavior of how Datastream handles data that's being pulled from a source Dataverse environment.
  * The versions of Dataverse that Datastream supports.
  * Known limitations for using Dataverse as a source.



## Key terms

Dataverse operates using the following concepts:

  * A **table** , formerly an _entity_ , is similar to a table in relational databases. Dataverse includes standard tables by default, but you can also create custom tables.
  * A **column** , formerly a _field_ , is an attribute of a table, and is similar to a column in relational databases.
  * A **row** is a specific record in a table, and is similar to a row in relational databases.



## Behavior

The Dataverse source support in Datastream relies on the Dataverse Web API, which uses the Open Data Protocol (OData). Datastream polls for source changes based on the interval that you set.

When replicating data from a Dataverse source, the following behavior is observed:

  * **API interaction** : Datastream interacts with the Dataverse Web API using RESTful requests. The base environment URL is `https://ORGANIZATION_ID.crm.dynamics.com/api/data/v9.1/`. Standard headers (`Accept: application/json`, `OData-MaxVersion: 4.0`, `OData-Version: 4.0`) are used.
  * **Authentication** : Datastream handles authentication using OAuth 2.0 with the client credentials grant type. Datastream obtains tokens from the Microsoft Identity Platform.
  * **Schema discovery** : Dataverse schemas are dynamic. Datastream discovers object names and schemas by querying the `/EntityDefinitions` endpoint.

    * **Object names** : Datastream fetches object names by sending a `GET` request to the `/EntityDefinitions` entity set path with the `$filter=TableType ne 'Virtual' and IsPrivate eq false` filter and the `$select=EntitySetName` parameter.
    * **Object schema** : Datastream fetches the object schema per-entity by sending a `GET` request to the `/EntityDefinitions` entity set path with the `$expand=Attributes($select=LogicalName,AttributeType,AttributeTypeName)` parameter and the `$filter=EntitySetName eq '[objectName]'` filter.
  * **Data replication** :

    * Datastream replicates standard and custom Dataverse tables. It excludes virtual and private tables.
    * **Historical backfill** : if configured for a stream, Datastream replicates all historical data for included tables. This is achieved by sending an initial `GET` request to the entity set and iterating through all pages using the `@odata.nextLink` property provided in API responses. The `Prefer: odata.maxpagesize=5000` header is used.
    * **Incremental sync** : Datastream replicates insert and update events. This is achieved by using timestamp-based synchronization, filtering records where the `modifiedon` field is greater than the last synchronization time (`$filter=modifiedon gt [last_sync_timestamp]`). Datastream doesn't capture delete events.
  * **Polling interval** : Datastream polls for changes according to the polling interval that you set when you create your stream. The interval is reflected in the stream's data freshness metric.




All replicated objects support both incremental synchronization, using the `modifiedon` field, and complete backfill.

## Versions

Datastream uses the Dataverse Web API version v9.1.

## Known limitations

Known limitations for using Dataverse as a source include:

  * The incremental synchronization method, based on the `modifiedon` timestamp, doesn't capture delete events.
  * Datastream doesn't support the Dataverse recommended change tracking feature that uses delta links (`@odata.deltaLink`). This is because storing the delta link URL required for subsequent incremental pulls isn't supported.
  * Replication is limited to standard and custom tables. Virtual and private tables aren't supported.
  * Accurate updating of the `modifiedon` field in the source tables is critical to ensure incremental sync works as expected.
  * To retrieve the labels for `Picklist` fields, data requests must include the `Prefer: data.include-annotations="*"` header, not just the integer values.



## What's next

  * Learn how to [configure a Dataverse source](https://docs.cloud.google.com/datastream/docs/configure-dataverse) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
