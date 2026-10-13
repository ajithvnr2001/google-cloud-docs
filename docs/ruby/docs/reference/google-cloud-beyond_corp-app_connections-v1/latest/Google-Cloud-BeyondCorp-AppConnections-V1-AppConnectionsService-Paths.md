---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connections-v1/latest/Google-Cloud-BeyondCorp-AppConnections-V1-AppConnectionsService-Paths/
title: BeyondCorp AppConnections V1 API - Module Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths (v0.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:01.095813+00:00
---

# BeyondCorp AppConnections V1 API - Module Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths (v0.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connections-v1/latest/Google-Cloud-BeyondCorp-AppConnections-V1-AppConnectionsService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BeyondCorp AppConnections V1 API - Module Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths (v0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.2  0.4.2  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the BeyondCorp AppConnections V1 API module Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths.

Path helper methods for the AppConnectionsService API.

## Extended By

  * [Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connections-v1/latest/Google-Cloud-BeyondCorp-AppConnections-V1-AppConnectionsService-Paths)



## Included In

  * [Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connections-v1/latest/Google-Cloud-BeyondCorp-AppConnections-V1-AppConnectionsService-Client)
  * [Google::Cloud::BeyondCorp::AppConnections::V1::AppConnectionsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-beyond_corp-app_connections-v1/latest/Google-Cloud-BeyondCorp-AppConnections-V1-AppConnectionsService-Paths)



## Methods 

### #app_connection_path
    
    
    def app_connection_path(project:, location:, app_connection:) -> ::String

Create a fully-qualified AppConnection resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/appConnections/{app_connection}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app_connection** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #app_connector_path
    
    
    def app_connector_path(project:, location:, app_connector:) -> ::String

Create a fully-qualified AppConnector resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/appConnectors/{app_connector}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app_connector** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #app_gateway_path
    
    
    def app_gateway_path(project:, location:, app_gateway:) -> ::String

Create a fully-qualified AppGateway resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/appGateways/{app_gateway}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app_gateway** (String) 



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
