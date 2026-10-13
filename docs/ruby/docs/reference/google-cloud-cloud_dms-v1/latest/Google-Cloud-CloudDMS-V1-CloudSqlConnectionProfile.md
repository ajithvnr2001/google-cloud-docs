---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlConnectionProfile/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:20.096099+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlConnectionProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile.

Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_public_ip
    
    
    def additional_public_ip() -> ::String

**Returns**

  * (::String) — Output only. The Cloud SQL database instance's additional (outgoing) public IP. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). 



### #cloud_sql_id
    
    
    def cloud_sql_id() -> ::String

**Returns**

  * (::String) — Output only. The Cloud SQL instance ID that this connection profile is associated with. 



### #private_ip
    
    
    def private_ip() -> ::String

**Returns**

  * (::String) — Output only. The Cloud SQL database instance's private IP. 



### #public_ip
    
    
    def public_ip() -> ::String

**Returns**

  * (::String) — Output only. The Cloud SQL database instance's public IP. 



### #settings
    
    
    def settings() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings)) — Immutable. Metadata used to create the destination Cloud SQL database. 



### #settings=
    
    
    def settings=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings)) — Immutable. Metadata used to create the destination Cloud SQL database. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings)) — Immutable. Metadata used to create the destination Cloud SQL database. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
