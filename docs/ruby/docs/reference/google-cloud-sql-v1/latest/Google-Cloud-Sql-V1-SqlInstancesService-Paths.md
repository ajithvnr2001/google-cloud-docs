---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Paths/
title: Cloud SQL Admin V1 API - Module Google::Cloud::Sql::V1::SqlInstancesService::Paths (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:26.948429+00:00
---

# Cloud SQL Admin V1 API - Module Google::Cloud::Sql::V1::SqlInstancesService::Paths (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Module Google::Cloud::Sql::V1::SqlInstancesService::Paths (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API module Google::Cloud::Sql::V1::SqlInstancesService::Paths.

Path helper methods for the SqlInstancesService API.

## Extended By

  * [Google::Cloud::Sql::V1::SqlInstancesService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Paths)



## Included In

  * [Google::Cloud::Sql::V1::SqlInstancesService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Client)
  * [Google::Cloud::Sql::V1::SqlInstancesService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Paths)
  * [Google::Cloud::Sql::V1::SqlInstancesService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesService-Rest-Client)



## Methods 

### #backup_path
    
    
    def backup_path(project:, backup:) -> ::String
    def backup_path(project:, location:, backupvault:, datasource:, backup:) -> ::String

Create a fully-qualified Backup resource string.

**Overloads**
    
    
    def backup_path(project:, backup:) -> ::String

The resource will be in the following format:

`projects/{project}/backups/{backup}`

**Parameters**

  * **project** (String) 
  * **backup** (String) 


    
    
    def backup_path(project:, location:, backupvault:, datasource:, backup:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **backupvault** (String) 
  * **datasource** (String) 
  * **backup** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #network_path
    
    
    def network_path(project:, network:) -> ::String

Create a fully-qualified Network resource string.

The resource will be in the following format:

`projects/{project}/global/networks/{network}`

**Parameters**

  * **project** (String) 
  * **network** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #secret_version_path
    
    
    def secret_version_path(project:, secret:, secret_version:) -> ::String
    def secret_version_path(project:, location:, secret:, secret_version:) -> ::String

Create a fully-qualified SecretVersion resource string.

**Overloads**
    
    
    def secret_version_path(project:, secret:, secret_version:) -> ::String

The resource will be in the following format:

`projects/{project}/secrets/{secret}/versions/{secret_version}`

**Parameters**

  * **project** (String) 
  * **secret** (String) 
  * **secret_version** (String) 


    
    
    def secret_version_path(project:, location:, secret:, secret_version:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **secret** (String) 
  * **secret_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_connection_policy_path
    
    
    def service_connection_policy_path(project:, region:, service_connection_policy:) -> ::String

Create a fully-qualified ServiceConnectionPolicy resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/serviceConnectionPolicies/{service_connection_policy}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **service_connection_policy** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
