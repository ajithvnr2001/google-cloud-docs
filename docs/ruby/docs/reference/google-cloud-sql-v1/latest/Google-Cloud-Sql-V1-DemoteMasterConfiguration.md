---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterConfiguration/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterConfiguration (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:16.192457+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterConfiguration (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterConfiguration (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::DemoteMasterConfiguration.

Read-replica configuration for connecting to the on-premises primary instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#demoteMasterConfiguration`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#demoteMasterConfiguration`. 



**Returns**

  * (::String) — This is always `sql#demoteMasterConfiguration`. 



### #mysql_replica_configuration
    
    
    def mysql_replica_configuration() -> ::Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration

**Returns**

  * ([::Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterMySqlReplicaConfiguration)) — MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory. 



### #mysql_replica_configuration=
    
    
    def mysql_replica_configuration=(value) -> ::Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterMySqlReplicaConfiguration)) — MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory. 



**Returns**

  * ([::Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterMySqlReplicaConfiguration)) — MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
