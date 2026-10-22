---
url: https://docs.cloud.google.com/datastore/docs/concepts/limits/
title: Limits \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:20.435922+00:00
---

# Limits  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/concepts/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Resources ](https://docs.cloud.google.com/datastore/docs/resources)



Send feedback 

#  Limits Stay organized with collections  Save and categorize content based on your preferences. 

This page describes production limits for Firestore in Datastore mode.

**Note:** These values are subject to change.

## Firestore in Datastore mode limits

In addition to these limits, see the [best practices](https://docs.cloud.google.com/datastore/docs/best-practices) for Firestore in Datastore mode.

Limit | Amount  
---|---  
Maximum number of databases per project |  100 You can [contact support](https://cloud.google.com/support-hub) to request an increase to this limit.   
Maximum number of [customer-managed encryption keys (CMEK) databases](https://docs.cloud.google.com/datastore/docs/cmek) per project |  0 By default the quota is 0 because this feature is behind an allowlist. You can request to increase the quota by filling in [the CMEK access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).   
Maximum API request size.This limit applies when Datastore mode is used outside of Google App Engine. If Datastore mode is used from App Engine, the limit depends on the client library that is used. | 10 MiB  
Maximum size for a transaction | 10 MiB  
Maximum [size](https://docs.cloud.google.com/datastore/docs/concepts/storage-size) for an entity | 1,048,572 bytes  
(1 MiB - 4 bytes)  
Maximum number of property transformations that can be performed on a single entity in a `Commit` operation or in a transaction.  For array transforms like `"appendMissingElements"`, each array element counts towards the limit.  | 500  
Maximum size for an entity key | 6 KiB  
Maximum depth of nested entity values | 20  
Maximum number of keys allowed for a `Lookup` operation in the Datastore API | 1,000  
Maximum size of an indexed string property's UTF-8 encoding | 1,500 bytes  
Maximum size for an unindexed property | 1,048,487 bytes  
(1 MiB - 89 bytes)  
Maximum sum of the sizes of an entity's [composite index](https://cloud.google.com/datastore/docs/concepts/indexes#composite_indexes) entries | 2 MiB  
Maximum number of composite indexes for a database | 

  * 200 when you have not enabled billing for your Google Cloud project. If you need more quota, you must [enable billing for your Google Cloud project.](https://cloud.google.com/billing/docs/how-to/modify-project)
  * 1000 when you enable billing for your Google Cloud project. You can [contact support](https://cloud.google.com/support-hub) to request an increase to this limit. 

  
Maximum sum of the following for an entity:

  * the number of indexed property values
  * the number of composite index entries

| 20,000  
Maximum number of properties in a composite index | 2 MiB  
Maximum total number of both export and import requests for a project allowed per minute | 20  
Maximum number of concurrent exports and imports | 50  
Maximum number of entity filters for export and import requests When the export or import request specifies an `entity_filter`, each combination of filtered kind and namespace counts as a separate filter towards this limit. For example: A request with `kinds=['foo', 'bar']` and `namespace_ids=['', 'ns1']`  
results in 4 filters towards this limit: `[('', 'foo'), ('', 'bar'), ('ns1', 'foo'), ('ns1', 'bar')]` | 100  
Maximum number of time-to-live (TTL) policies allowed per database. | 1000  
  
## legacy Cloud Datastore limits

If you have not yet upgraded from Datastore to [Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore#cloud_firestore_in_datastore_mode), the following limits also apply to your database instance:

Limit | Amount  
---|---  
Maximum number of entity groups that can be accessed in a transaction | 25  
Maximum rate of transactions reading from or writing to an entity group | [1 per sec](https://docs.cloud.google.com/datastore/docs/concepts/cloud-datastore-transactions#transactions_and_entity_groups)  
Maximum write rate to an entity group.Note you can batch writes together for an entity group. This allows you to write multiple entities to an entity group within this limit. | 1 per second  
  
## What's next

  * Learn about [Pricing and Quota](https://docs.cloud.google.com/datastore/docs/pricing)
  * Learn about [Storage Size Calculations](https://docs.cloud.google.com/datastore/docs/concepts/storage-size)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
