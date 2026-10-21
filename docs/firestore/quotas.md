---
url: https://docs.cloud.google.com/firestore/quotas/
title: Quotas and limits \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:08.156602+00:00
---

# Quotas and limits  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Resources ](https://docs.cloud.google.com/firestore/native/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This page identifies the request quotas and limits for Firestore.

## Free Tier usage

Firestore offers a free tier that lets you get started with Firestore at no cost. The free tier amounts are listed in the following table.

Free tier amounts are applied daily and reset at midnight Pacific time.

The free tier applies to only one Firestore database per project. The first database that is created in a project without a free tier database will get the free tier. If the database with the free tier applied is deleted, the next database created will receive the free tier.

### Standard edition

Free tier | Quota  
---|---  
Stored data | 1 GiB  
Document reads | 50,000 per day  
Document writes | 20,000 per day  
Document deletes | 20,000 per day  
Outbound data transfer | 10 GiB per month  
  
### Enterprise edition

Free tier | Quota  
---|---  
Stored data | 1 GiB  
Read units | 50,000 per day  
Real-time update units | 50,000 per day  
Write units | 40,000 per day  
Outbound data transfer | 10 GiB per month  
  
The following operations and features don't include free usage. You must [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project) to use these features:

  * Managed deletes (TTL)
  * PITR data
  * Backup data
  * Restore operations
  * Clone operations



## Limits

The following tables show the limits that apply to Firestore. These are hard limits unless otherwise noted.

### Databases

### Standard edition

Limit | Details  
---|---  
Maximum number of databases per project |  100 You can [contact support](https://docs.cloud.google.com/support-hub) to request an increase to this limit.   
Maximum number of [customer-managed encryption keys (CMEK) databases](https://docs.cloud.google.com/firestore/docs/cmek) per project |  0 By default the quota is 0 because this feature is behind an allowlist. You can request to increase the quota by filling in [the CMEK access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).   
  
### Enterprise edition

Limit | Details  
---|---  
Maximum number of databases per project |  100 You can [contact support](https://docs.cloud.google.com/support-hub) to request an increase to this limit.   
Maximum number of [customer-managed encryption keys (CMEK) databases](https://docs.cloud.google.com/firestore/docs/cmek) per project |  0 By default the quota is 0 because this feature is behind an allowlist. You can request to increase the quota by filling in [the CMEK access request form](https://docs.google.com/forms/d/e/1FAIpQLSfKs8wJf4IXu1NizvfyU2vT59JDbdPvkehMVZ2ab5l_aDLIIA/viewform?resourcekey=0-O15dlRFvA0JIDmh6VFUEcA).   
  
### Collections, documents, and fields

### Standard edition

Limit | Details  
---|---  
Constraints on collection IDs | 

  * Must be valid UTF-8 characters
  * Must be no longer than 1,500 bytes
  * Cannot contain a forward slash (`/`)
  * Cannot solely consist of a single period (`.`) or double periods (`..`)
  * Cannot match the regular expression `__.*__`

  
Maximum depth of subcollections | 100  
Constraints on document IDs | 

  * Must be valid UTF-8 characters
  * Must be no longer than 1,500 bytes
  * Cannot contain a forward slash (`/`)
  * Cannot solely consist of a single period (`.`) or double periods (`..`)
  * Cannot match the regular expression `__.*__`
  * If you import Datastore entities into a Firestore database, numeric entity IDs are exposed as `__id[0-9]+__`

  
Maximum size for a document name  | 6 KiB  
Maximum size for a document | 1 MiB (1,048,576 bytes)  
Constraints on field names | 

  * Must be valid UTF-8 characters
  * Cannot match the regular expression `__.*__`

  
Maximum size of a field name | 1,500 bytes  
Constraints on field paths | 

  * Must separate field names with a single period (`.`)
  * May be passed as a dot-delimited (`.`) string of segments where each segment is either a simple field name or a quoted field name (defined below). 

A simple field name is one where all of the following are true: 
  * Contains only the characters `a-z`, `A-Z`, `0-9`, and underscore (`_`)
  * Does not start with `0-9`

A quoted field name starts and ends with the backtick character (```). For example, `foo.`x&y`` refers to the `x&y` field nested under the `foo` field. To construct a field name with the backtick character, escape the backtick character with the backslash character (`\`). For convenience, you can avoid quoted field names by passing the field path as a FieldPath object ([for example, see JavaScript FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath)).   
Maximum size of a field path | 1,500 bytes  
Maximum size of a field value | 1 MiB - 89 bytes (1,048,487 bytes)  
Maximum depth of fields in a map or array | 20 Map and array fields add one level to the overall depth of an object. For example, the following object has a total depth of three levels: 
    
    
    {
      nested_map: {         #depth 1
        nested_array: [     #depth 2
          {
            foo: "bar"      #depth 3
          }
        ]
      }
    }
            
  
### Enterprise edition

Limit | Details  
---|---  
Constraints on collection IDs | 

  * Must be valid UTF-8 characters
  * Must be no longer than 1,500 bytes
  * Cannot contain a forward slash (`/`)
  * Cannot solely consist of a single period (`.`) or double periods (`..`)
  * Cannot match the regular expression `__.*__`

  
Maximum depth of subcollections | 100  
Constraints on document IDs | 

  * Must be valid UTF-8 characters
  * Must be no longer than 1,500 bytes
  * Cannot contain a forward slash (`/`)
  * Cannot solely consist of a single period (`.`) or double periods (`..`)
  * Cannot match the regular expression `__.*__`
  * If you import Datastore entities into a Firestore database, numeric entity IDs are exposed as `__id[0-9]+__`

  
Maximum size for a document name  | 6 KiB  
Maximum size for a document | 1 MiB (1,048,576 bytes)  
Constraints on field names | 

  * Must be valid UTF-8 characters
  * Cannot match the regular expression `__.*__`

  
Maximum size of a field name | 1,500 bytes  
Constraints on field paths | 

  * Must separate field names with a single period (`.`)
  * May be passed as a dot-delimited (`.`) string of segments where each segment is either a simple field name or a quoted field name (defined below). 

A simple field name is one where all of the following are true: 
  * Contains only the characters `a-z`, `A-Z`, `0-9`, and underscore (`_`)
  * Does not start with `0-9`

A quoted field name starts and ends with the backtick character (```). For example, `foo.`x&y`` refers to the `x&y` field nested under the `foo` field. To construct a field name with the backtick character, escape the backtick character with the backslash character (`\`). For convenience, you can avoid quoted field names by passing the field path as a FieldPath object ([for example, see JavaScript FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath)).   
Maximum size of a field path | 1,500 bytes  
Maximum size of a field value | 1 MiB - 89 bytes (1,048,487 bytes)  
Maximum depth of fields in a map or array | 20 Map and array fields add one level to the overall depth of an object. For example, the following object has a total depth of three levels: 
    
    
    {
      nested_map: {         #depth 1
        nested_array: [     #depth 2
          {
            foo: "bar"      #depth 3
          }
        ]
      }
    }
            
  
### Writes and transactions

### Standard edition

Limit | Details  
---|---  
Maximum API request size | 10 MiB  
The memory limit for a query | 128 MiB  
Time limit for a transaction | 270 seconds, with a 60-second idle expiration time  
Maximum number of field transformations that can be performed on a single document in a `Commit` operation or in a transaction | 500  
  
### Enterprise edition

Limit | Details  
---|---  
Maximum API request size | 10 MiB  
Time limit for a transaction | 270 seconds, with a 60-second idle expiration time  
Maximum number of field transformations that can be performed on a single document in a `Commit` operation or in a transaction | 500  
  
### Indexes

### Standard edition

Limit | Details  
---|---  
Maximum number of composite indexes for a database | 

  * 200 when you have not enabled billing for your Google Cloud project.  If you need more quota, you must [enable billing for your Google Cloud project.](https://cloud.google.com/billing/docs/how-to/modify-project)
  * 1000 when you enable billing for your Google Cloud project.  You can [contact support](https://docs.cloud.google.com/support-hub) to request an increase to this limit. 

  
Maximum number of single-field configurations for a database | 

  * 200 when you have not enabled billing for your Google Cloud project.  If you need more quota, you must [enable billing for your Google Cloud project.](https://cloud.google.com/billing/docs/how-to/modify-project)
  * 1000 when you enable billing for your Google Cloud project. 

One field level configuration can contain multiple configurations for the same field. For example, a single-field indexing exemption and a TTL policy on the same field count as one field configuration towards the limit.  
Maximum number of index entries for each document | 40,000 The number of index entries is the sum of the following for a document:

  * The number of single-field index entries
  * The number of composite index entries

To see how Firestore turns a document and a set of indexes into index entries, see [this index entry count example](https://docs.cloud.google.com/firestore/docs/concepts/index-overview#index_entries).  
Maximum number of fields in a composite index | 100  
Maximum size of an index entry |  7.5 KiB To see how Firestore calculates index entry size, see [index entry size](https://docs.cloud.google.com/firestore/docs/storage-size#index-entry-size).  
Maximum sum of the sizes of a document's index entries |  8 MiB The total size is the sum of the following for a document:
* The sum of the size of a document's single-field index entries
* The sum of the size of a document's composite index entries  
Maximum size of an indexed field value |  1500 bytes Field values over 1500 bytes are truncated. Queries involving truncated field values may return inconsistent results.  
  
### Enterprise edition

Limit | Details  
---|---  
Maximum number of indexes for a database | 

  * 200 when you have not enabled billing for your Google Cloud project.  If you need more quota, you must [enable billing for your Google Cloud project.](https://cloud.google.com/billing/docs/how-to/modify-project)
  * 1000 when you enable billing for your Google Cloud project.  You can [contact support](https://docs.cloud.google.com/support-hub) to request an increase to this limit. 

  
Maximum number of index entries for each document | 40,000  
Maximum number of fields in an index | 100  
Maximum size of an index entry |  7.5 KiB To see how Firestore calculates index entry size, see [index entry size](https://docs.cloud.google.com/firestore/docs/storage-size#index-entry-size).  
Maximum sum of the sizes of a document's index entries |  8 MiB  
  
### Time-to-live (TTL)

### Standard edition

Limit | Details  
---|---  
Maximum number of TTL configurations for a database |  1000  
  
### Enterprise edition

Limit | Details  
---|---  
Maximum number of TTL configurations for a database |  1000  
  
### Export/Import

The following limits apply to [managed import and export operations](https://docs.cloud.google.com/firestore/docs/manage-data/export-import):

### Standard edition

Limit | Details  
---|---  
Maximum total number of both export and import requests for a project allowed per minute | 20  
Maximum number of concurrent exports and imports | 50  
Maximum number of collection ID filters for export and import requests | 100  
  
### Enterprise edition

Limit | Details  
---|---  
Maximum total number of both export and import requests for a project allowed per minute | 20  
Maximum number of concurrent exports and imports | 50  
Maximum number of collection ID filters for export and import requests | 100  
  
### Security rules

### Standard edition

Limit | Details  
---|---  
Maximum number of `exists()`, `get()`, and `getAfter()` calls per request | 

  * 10 for single-document requests and query requests.
  * 20 for multi-document reads, transactions, and batched writes. The previous limit of 10 also applies to each operation.  For example, imagine you create a batched write request with 3 write operations and that your security rules use 2 document access calls to validate each write. In this case, each write uses 2 of its 10 access calls and the batched write request uses 6 of its 20 access calls. 

Exceeding either limit results in a permission denied error. Some document access calls may be cached, and cached calls do not count towards the limits.  
Maximum nested `match` statement depth | 10  
Maximum path length, in path segments, allowed within a set of nested `match` statements | 100  
Maximum number of path capture variables allowed within a set of nested `match` statements | 20  
Maximum function call depth | 20  
Maximum number of function arguments | 7  
Maximum number of `let` variable bindings per function | 10  
Maximum number of recursive or cyclical function calls | 0 (not permitted)  
Maximum number of expressions evaluated per request | 1,000  
Maximum size of a ruleset | Rulesets must obey two size limits: 

  * a 256 KB limit on the size of the ruleset text source published from the Firebase console or from the CLI using `firebase deploy`. 
  * a 250 KB limit on the size of the compiled ruleset that results when Firebase processes the source and makes it active on the back-end. 

  
  
### Enterprise edition

Limit | Details  
---|---  
Maximum number of `exists()`, `get()`, and `getAfter()` calls per request | 

  * 10 for single-document requests and query requests.
  * 20 for multi-document reads, transactions, and batched writes. The previous limit of 10 also applies to each operation.  For example, imagine you create a batched write request with 3 write operations and that your security rules use 2 document access calls to validate each write. In this case, each write uses 2 of its 10 access calls and the batched write request uses 6 of its 20 access calls. 

Exceeding either limit results in a permission denied error. Some document access calls may be cached, and cached calls do not count towards the limits.  
Maximum nested `match` statement depth | 10  
Maximum path length, in path segments, allowed within a set of nested `match` statements | 100  
Maximum number of path capture variables allowed within a set of nested `match` statements | 20  
Maximum function call depth | 20  
Maximum number of function arguments | 7  
Maximum number of `let` variable bindings per function | 10  
Maximum number of recursive or cyclical function calls | 0 (not permitted)  
Maximum number of expressions evaluated per request | 1,000  
Maximum size of a ruleset | Rulesets must obey two size limits: 

  * a 256 KB limit on the size of the ruleset text source published from the Firebase console or from the CLI using `firebase deploy`. 
  * a 250 KB limit on the size of the compiled ruleset that results when Firebase processes the source and makes it active on the back-end. 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
