---
url: https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.FirestoreDatabaseReference
title: Google Cloud Gemini Data Analytics V1beta Client - Class FirestoreDatabaseReference (0.14.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:14.159892+00:00
---

# Google Cloud Gemini Data Analytics V1beta Client - Class FirestoreDatabaseReference (0.14.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.FirestoreDatabaseReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Gemini Data Analytics V1beta Client - Class FirestoreDatabaseReference (0.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Gemini Data Analytics V1beta Client class FirestoreDatabaseReference.

Message representing a reference to a single Firestore database.

Generated from protobuf message `google.cloud.geminidataanalytics.v1beta.FirestoreDatabaseReference`

## Namespace

Google \ Cloud \ GeminiDataAnalytics \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ project_id` |  `string`   
Required. Project the firestore database belongs to.  
`↳ database_id` |  `string`   
Required. The database id.  
`↳ collection_ids` |  `string[]`   
Optional. The collection ids. Denotes all collections if unset.  
`↳ database_table_references` |  `array<[DatabaseTableReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.DatabaseTableReference)>`   
Optional. References to collections within the database. Each reference specifies a collection and can optionally include the collection's schema to provide context for the query.  
  
### getProjectId

Required. Project the firestore database belongs to.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProjectId

Required. Project the firestore database belongs to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDatabaseId

Required. The database id.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDatabaseId

Required. The database id.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCollectionIds

Optional. The collection ids. Denotes all collections if unset.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setCollectionIds

Optional. The collection ids. Denotes all collections if unset.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDatabaseTableReferences

Optional. References to collections within the database. Each reference specifies a collection and can optionally include the collection's schema to provide context for the query.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[DatabaseTableReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.DatabaseTableReference)>` |   
  
### setDatabaseTableReferences

Optional. References to collections within the database. Each reference specifies a collection and can optionally include the collection's schema to provide context for the query.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[DatabaseTableReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.DatabaseTableReference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
