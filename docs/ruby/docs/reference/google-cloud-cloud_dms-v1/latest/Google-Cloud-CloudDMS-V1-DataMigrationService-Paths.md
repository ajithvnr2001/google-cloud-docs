---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Paths/
title: Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DataMigrationService::Paths (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:26.371553+00:00
---

# Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DataMigrationService::Paths (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DataMigrationService::Paths (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API module Google::Cloud::CloudDMS::V1::DataMigrationService::Paths.

Path helper methods for the DataMigrationService API.

## Extended By

  * [Google::Cloud::CloudDMS::V1::DataMigrationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Paths)



## Included In

  * [Google::Cloud::CloudDMS::V1::DataMigrationService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client)
  * [Google::Cloud::CloudDMS::V1::DataMigrationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Paths)



## Methods 

### #connection_profile_path
    
    
    def connection_profile_path(project:, location:, connection_profile:) -> ::String

Create a fully-qualified ConnectionProfile resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/connectionProfiles/{connection_profile}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **connection_profile** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #conversion_workspace_path
    
    
    def conversion_workspace_path(project:, location:, conversion_workspace:) -> ::String

Create a fully-qualified ConversionWorkspace resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **conversion_workspace** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #mapping_rule_path
    
    
    def mapping_rule_path(project:, location:, conversion_workspace:, mapping_rule:) -> ::String

Create a fully-qualified MappingRule resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **conversion_workspace** (String) 
  * **mapping_rule** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #migration_job_path
    
    
    def migration_job_path(project:, location:, migration_job:) -> ::String

Create a fully-qualified MigrationJob resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/migrationJobs/{migration_job}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **migration_job** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #networks_path
    
    
    def networks_path(project:, network:) -> ::String

Create a fully-qualified Networks resource string.

The resource will be in the following format:

`projects/{project}/global/networks/{network}`

**Parameters**

  * **project** (String) 
  * **network** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #private_connection_path
    
    
    def private_connection_path(project:, location:, private_connection:) -> ::String

Create a fully-qualified PrivateConnection resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/privateConnections/{private_connection}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **private_connection** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
