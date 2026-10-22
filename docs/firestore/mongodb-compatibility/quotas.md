---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/quotas/
title: Quotas and limits \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:42.886296+00:00
---

# Quotas and limits  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Resources ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This page describes the request quotas and limits for Firestore with MongoDB compatibility.

## Free tier usage

Firestore with MongoDB compatibility offers a free tier that lets you get started with Firestore with MongoDB compatibility at no cost. The free tier amounts are listed in the following table.

Free tier amounts are applied daily and reset at midnight Pacific time.

The free tier applies to only one Firestore with MongoDB compatibility database per project. The first database that is created in a project without a free tier database will get the free tier. If the database with the free tier applied is deleted, the next database created will receive the free tier.

Free tier | Quota  
---|---  
Stored data | 1 GiB  
Read units | 50,000 per day  
Write units | 40,000 per day  
Outbound data transfer | 10 GiB per month  
  
The following operations and features don't include free usage. You must [enable billing](https://cloud.google.com/billing/docs/how-to/modify-project) to use these features:

  * Managed deletes (TTL)
  * Backup data
  * Restore operations



For more information about how these features are billed, see [Storage pricing](https://docs.cloud.google.com/firestore/enterprise/pricing#storage-size).

## Standard limits

The following tables show the limits that apply to Firestore with MongoDB compatibility. These are hard limits unless otherwise noted.

### Databases

Limit | Details  
---|---  
Maximum number of databases per project |  100 [Contact support](https://cloud.google.com/support-hub) to request an increase to this limit.   
Maximum number of [customer-managed encryption keys (CMEK) databases](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/cmek) per project |  0 By default the quota is 0 because this feature is behind an allowlist. You can request to increase the quota by filling in [the CMEK access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).   
  
### Collections, documents, and fields

Limit | Details  
---|---  
Constraints on collection names | 

  * Must be valid UTF-8 characters
  * Must be no longer than 1,500 bytes
  * Can't match the regular expression `__.*__`
  * Can't contain `$`
  * Can't be the empty string (`""`)
  * Can't contain the null character
  * Can't begin with `system.` and can't contain `.system.`.

  
Constraints on document IDs (`_id`) | 

  * Must be an ObjectId, String, 64-bit integer, 32-bit integer, Double, Binary, or Object. Other BSON types are not supported.
  * Must be no larger than 1,500 bytes
  * For Object-typed IDs:
    * Each value within an Object-typed ID must also be of a supported ID type (ObjectId, String, 64-bit integer, 32-bit integer, Double, Binary, or Object) or an Array of values, each of which is of a supported ID type.
  * For String-typed IDs:
    * Must be valid UTF-8 characters
    * Can't match the regular expression `__.*__`

  
Maximum size for a document | 16 MiB  
Constraints on field names | 

  * Must be valid UTF-8 characters
  * Can't be the empty string (`""`)
  * Can't match the regular expression `__.*__`

  
Maximum size of a field name | 1,500 bytes  
Maximum size of a field path | 1,500 bytes  
Maximum size of a field value | 16MiB - 89 bytes  
Maximum depth of fields in a map or array | 20 Map and array fields add one level to the overall depth of an object. For example, the following object has a total depth of three levels:
    
    
    {
      nested_object: {      #depth 1
        nested_array: [     #depth 2
          {
            foo: "bar"      #depth 3
          }
        ]
      }
    }  
  
### Reads, writes, and transactions

Limit | Details  
---|---  
Memory limit for a query | 128 MiB  
Time limit for a transaction | 270 seconds, with a 60-second idle expiration time  
  
### Indexes

Limit | Details  
---|---  
Maximum number of indexes for a database |  1000 [Contact support](https://cloud.google.com/support-hub) to request an increase to this limit.   
Maximum number of index entries for each document | 40,000  
Maximum number of fields in an index | 100  
Maximum size of an index entry |  7.5 KiB  
Maximum sum of the sizes of a document's index entries |  8 MiB  
  
### Time to live (TTL)

Limit | Details  
---|---  
Maximum number of TTL configurations for a database |  500  
  
### Saved queries limits

**Preview — Saved queries**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Value | Limit  
---|---  
Maximum number of saved queries per project (including saved queries for other Google Cloud products) | 10,000  
Maximum size for each query | 1 MiB  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
