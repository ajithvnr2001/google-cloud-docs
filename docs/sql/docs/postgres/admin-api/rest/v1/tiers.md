---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/tiers/
title: REST Resource: tiers \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:24.728079+00:00
---

# REST Resource: tiers  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  REST Resource: tiers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Tier
    * JSON representation
  * Methods



## Resource: Tier

A Google Cloud SQL service tier resource.

JSON representation  
---  
      
    
    {
      "tier": string,
      "RAM": string,
      "kind": string,
      "DiskQuota": string,
      "region": [
        string
      ]
    }  
  
Fields  
---  
`tier` |  `string` An identifier for the machine type, for example, `db-custom-1-3840`. For related information, see [Pricing](https://docs.cloud.google.com/sql/pricing).  
`RAM` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum ram usage of this tier in bytes.  
`kind` |  `string` This is always `sql#tier`.  
`DiskQuota` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum disk size of this tier in bytes.  
`region[]` |  `string` The applicable regions for this tier.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/tiers/list)`

|  Lists all available machine types (tiers) for Cloud SQL, for example, `db-custom-1-3840`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
