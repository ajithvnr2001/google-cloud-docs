---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v3/
title: Class /GOOG/CL_TRAFFICDIRECTOR_V3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:58.996840+00:00
---

# Class /GOOG/CL_TRAFFICDIRECTOR_V3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_TRAFFICDIRECTOR_V3 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_trafficdirector_v3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v3)



## Class
    
    
    /GOOG/CL_TRAFFICDIRECTOR_V3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Traffic Director API v3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Address` | PUBLIC  
`TY_002` | `BuildVersion` | PUBLIC  
`TY_003` | `ClientConfig` | PUBLIC  
`TY_004` | `ClientStatusRequest` | PUBLIC  
`TY_005` | `ClientStatusResponse` | PUBLIC  
`TY_006` | `ClustersConfigDump` | PUBLIC  
`TY_007` | `ContextParams` | PUBLIC  
`TY_010` | `DynamicCluster` | PUBLIC  
`TY_011` | `DynamicEndpointConfig` | PUBLIC  
`TY_012` | `DynamicListener` | PUBLIC  
`TY_013` | `DynamicListenerState` | PUBLIC  
`TY_014` | `DynamicRouteConfig` | PUBLIC  
`TY_015` | `DynamicScopedRouteConfigs` | PUBLIC  
`TY_016` | `EndpointsConfigDump` | PUBLIC  
`TY_017` | `EnvoyInternalAddress` | PUBLIC  
`TY_018` | `Extension` | PUBLIC  
`TY_019` | `GenericXdsConfig` | PUBLIC  
`TY_020` | `GoogleRE2` | PUBLIC  
`TY_021` | `InlineScopedRouteConfigs` | PUBLIC  
`TY_023` | `ListenersConfigDump` | PUBLIC  
`TY_024` | `Locality` | PUBLIC  
`TY_025` | `Node` | PUBLIC  
`TY_026` | `NodeMatcher` | PUBLIC  
`TY_029` | `PathSegment` | PUBLIC  
`TY_030` | `PerXdsConfig` | PUBLIC  
`TY_031` | `Pipe` | PUBLIC  
`TY_032` | `RegexMatcher` | PUBLIC  
`TY_033` | `RoutesConfigDump` | PUBLIC  
`TY_034` | `ScopedRoutesConfigDump` | PUBLIC  
`TY_035` | `SemanticVersion` | PUBLIC  
`TY_036` | `SocketAddress` | PUBLIC  
`TY_037` | `StaticCluster` | PUBLIC  
`TY_038` | `StaticEndpointConfig` | PUBLIC  
`TY_039` | `StaticListener` | PUBLIC  
`TY_040` | `StaticRouteConfig` | PUBLIC  
`TY_041` | `StringMatcher` | PUBLIC  
`TY_042` | `StructMatcher` | PUBLIC  
`TY_043` | `TypedExtensionConfig` | PUBLIC  
`TY_044` | `UpdateFailureState` | PUBLIC  
`TY_T_001` | `Address` | PUBLIC  
`TY_T_003` | `ClientConfig` | PUBLIC  
`TY_T_010` | `DynamicCluster` | PUBLIC  
`TY_T_011` | `DynamicEndpointConfig` | PUBLIC  
`TY_T_012` | `DynamicListener` | PUBLIC  
`TY_T_014` | `DynamicRouteConfig` | PUBLIC  
`TY_T_015` | `DynamicScopedRouteConfigs` | PUBLIC  
`TY_T_018` | `Extension` | PUBLIC  
`TY_T_019` | `GenericXdsConfig` | PUBLIC  
`TY_T_021` | `InlineScopedRouteConfigs` | PUBLIC  
`TY_T_026` | `NodeMatcher` | PUBLIC  
`TY_T_029` | `PathSegment` | PUBLIC  
`TY_T_030` | `PerXdsConfig` | PUBLIC  
`TY_T_037` | `StaticCluster` | PUBLIC  
`TY_T_038` | `StaticEndpointConfig` | PUBLIC  
`TY_T_039` | `StaticListener` | PUBLIC  
`TY_T_040` | `StaticRouteConfig` | PUBLIC  
`TY_T_042` | `StructMatcher` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250219 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://trafficdirector.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | trafficdirector:v3 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLIENT_STATUS_DISCOVERY

  * Description: trafficdirector.discovery.client_status 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_004` | ClientStatusRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | ClientStatusResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
