---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_pagespeedonline_v5/
title: Class /GOOG/CL_PAGESPEEDONLINE_V5 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:53.989145+00:00
---

# Class /GOOG/CL_PAGESPEEDONLINE_V5  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_pagespeedonline_v5/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_PAGESPEEDONLINE_V5 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_pagespeedonline_v5)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_pagespeedonline_v5)



## Class
    
    
    /GOOG/CL_PAGESPEEDONLINE_V5

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`PageSpeed Insights API v5`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AuditRefs` | PUBLIC  
`TY_002` | `Bucket` | PUBLIC  
`TY_003` | `Categories` | PUBLIC  
`TY_004` | `CategoryGroupV5` | PUBLIC  
`TY_005` | `ConfigSettings` | PUBLIC  
`TY_006` | `Environment` | PUBLIC  
`TY_007` | `I18n` | PUBLIC  
`TY_008` | `LhrEntity` | PUBLIC  
`TY_009` | `LighthouseAuditResultV5` | PUBLIC  
`TY_010` | `LighthouseCategoryV5` | PUBLIC  
`TY_011` | `LighthouseResultV5` | PUBLIC  
`TY_012` | `PagespeedApiLoadingExperienceV5` | PUBLIC  
`TY_013` | `PagespeedApiPagespeedResponseV5` | PUBLIC  
`TY_014` | `PagespeedVersion` | PUBLIC  
`TY_015` | `RendererFormattedStrings` | PUBLIC  
`TY_016` | `RuntimeError` | PUBLIC  
`TY_017` | `StackPack` | PUBLIC  
`TY_018` | `Timing` | PUBLIC  
`TY_019` | `UserPageLoadMetricV5` | PUBLIC  
`TY_020` | `MetricSavings` | PUBLIC  
`TY_T_001` | `AuditRefs` | PUBLIC  
`TY_T_002` | `Bucket` | PUBLIC  
`TY_T_008` | `LhrEntity` | PUBLIC  
`TY_T_017` | `StackPack` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250304 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://pagespeedonline.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | pagespeedonline:v5 | PUBLIC  
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
  
### RUNPAGESPEED_PAGESPEEDAPI

  * Description: pagespeedonline.pagespeedapi.runpagespeed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CAPTCHATOKEN` | IMPORTING | `STRING` | captchaToken  
`IV_Q_CATEGORY` | IMPORTING | `STRING` | category  
`IV_Q_LOCALE` | IMPORTING | `STRING` | locale  
`IV_Q_STRATEGY` | IMPORTING | `STRING` | strategy  
`IV_Q_URL` | IMPORTING | `STRING` | url  
`IV_Q_UTMCAMPAIGN` | IMPORTING | `STRING` | utm_campaign  
`IV_Q_UTMSOURCE` | IMPORTING | `STRING` | utm_source  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | PagespeedApiPagespeedResponseV5  
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
