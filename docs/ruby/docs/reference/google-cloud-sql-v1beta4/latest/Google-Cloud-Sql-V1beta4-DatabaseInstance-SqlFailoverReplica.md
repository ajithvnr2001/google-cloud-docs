---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-DatabaseInstance-SqlFailoverReplica/
title: Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::DatabaseInstance::SqlFailoverReplica (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:25.047131+00:00
---

# Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::DatabaseInstance::SqlFailoverReplica (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-DatabaseInstance-SqlFailoverReplica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::DatabaseInstance::SqlFailoverReplica (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Cloud SQL Admin V1BETA4 API class Google::Cloud::Sql::V1beta4::DatabaseInstance::SqlFailoverReplica.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #available
    
    
    def available() -> ::Google::Protobuf::BoolValue

**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Protobuf-BoolValue)) — The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only failover to the failover replica when the status is true. 



### #available=
    
    
    def available=(value) -> ::Google::Protobuf::BoolValue

**Parameter**

  * **value** ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Protobuf-BoolValue)) — The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only failover to the failover replica when the status is true. 



**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Protobuf-BoolValue)) — The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only failover to the failover replica when the status is true. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID. 



**Returns**

  * (::String) — The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
