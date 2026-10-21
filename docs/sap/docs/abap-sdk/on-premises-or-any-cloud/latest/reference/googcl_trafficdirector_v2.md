---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v2/
title: Class /GOOG/CL_TRAFFICDIRECTOR_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:34.353756+00:00
---

# Class /GOOG/CL_TRAFFICDIRECTOR_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_TRAFFICDIRECTOR_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_trafficdirector_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_trafficdirector_v2)



## Class
    
    
    /GOOG/CL_TRAFFICDIRECTOR_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Traffic Director API v2`

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
`TY_009` | `DynamicCluster` | PUBLIC  
`TY_010` | `DynamicListener` | PUBLIC  
`TY_011` | `DynamicListenerState` | PUBLIC  
`TY_012` | `DynamicRouteConfig` | PUBLIC  
`TY_013` | `DynamicScopedRouteConfigs` | PUBLIC  
`TY_014` | `Extension` | PUBLIC  
`TY_015` | `GoogleRE2` | PUBLIC  
`TY_016` | `InlineScopedRouteConfigs` | PUBLIC  
`TY_018` | `ListenersConfigDump` | PUBLIC  
`TY_019` | `Locality` | PUBLIC  
`TY_020` | `Node` | PUBLIC  
`TY_021` | `NodeMatcher` | PUBLIC  
`TY_023` | `PathSegment` | PUBLIC  
`TY_024` | `PerXdsConfig` | PUBLIC  
`TY_025` | `Pipe` | PUBLIC  
`TY_026` | `RegexMatcher` | PUBLIC  
`TY_027` | `RoutesConfigDump` | PUBLIC  
`TY_028` | `ScopedRoutesConfigDump` | PUBLIC  
`TY_029` | `SemanticVersion` | PUBLIC  
`TY_030` | `SocketAddress` | PUBLIC  
`TY_031` | `StaticCluster` | PUBLIC  
`TY_032` | `StaticListener` | PUBLIC  
`TY_033` | `StaticRouteConfig` | PUBLIC  
`TY_034` | `StringMatcher` | PUBLIC  
`TY_035` | `StructMatcher` | PUBLIC  
`TY_036` | `UpdateFailureState` | PUBLIC  
`TY_T_001` | `Address` | PUBLIC  
`TY_T_003` | `ClientConfig` | PUBLIC  
`TY_T_009` | `DynamicCluster` | PUBLIC  
`TY_T_010` | `DynamicListener` | PUBLIC  
`TY_T_012` | `DynamicRouteConfig` | PUBLIC  
`TY_T_013` | `DynamicScopedRouteConfigs` | PUBLIC  
`TY_T_014` | `Extension` | PUBLIC  
`TY_T_016` | `InlineScopedRouteConfigs` | PUBLIC  
`TY_T_021` | `NodeMatcher` | PUBLIC  
`TY_T_023` | `PathSegment` | PUBLIC  
`TY_T_024` | `PerXdsConfig` | PUBLIC  
`TY_T_031` | `StaticCluster` | PUBLIC  
`TY_T_032` | `StaticListener` | PUBLIC  
`TY_T_033` | `StaticRouteConfig` | PUBLIC  
`TY_T_035` | `StructMatcher` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250219 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://trafficdirector.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | trafficdirector:v2 | PUBLIC  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
