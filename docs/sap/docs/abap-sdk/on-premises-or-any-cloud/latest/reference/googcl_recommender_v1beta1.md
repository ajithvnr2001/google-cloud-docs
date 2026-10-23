---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_recommender_v1beta1/
title: Class /GOOG/CL_RECOMMENDER_V1BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:49.550995+00:00
---

# Class /GOOG/CL_RECOMMENDER_V1BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_recommender_v1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_RECOMMENDER_V1BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_recommender_v1beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_recommender_v1beta1)



## Class
    
    
    /GOOG/CL_RECOMMENDER_V1BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Recommender API v1beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleCloudLocationListLocationsResponse` | PUBLIC  
`TY_002` | `GoogleCloudLocationLocation` | PUBLIC  
`TY_003` | `GoogleCloudRecommenderV1beta1CostProjection` | PUBLIC  
`TY_004` | `GoogleCloudRecommenderV1beta1Impact` | PUBLIC  
`TY_005` | `GoogleCloudRecommenderV1beta1Insight` | PUBLIC  
`TY_006` | `GoogleCloudRecommenderV1beta1InsightRecommendationReference` | PUBLIC  
`TY_007` | `GoogleCloudRecommenderV1beta1InsightStateInfo` | PUBLIC  
`TY_008` | `GoogleCloudRecommenderV1beta1InsightType` | PUBLIC  
`TY_009` | `GoogleCloudRecommenderV1beta1InsightTypeConfig` | PUBLIC  
`TY_010` | `GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig` | PUBLIC  
`TY_011` | `GoogleCloudRecommenderV1beta1ListInsightTypesResponse` | PUBLIC  
`TY_012` | `GoogleCloudRecommenderV1beta1ListInsightsResponse` | PUBLIC  
`TY_013` | `GoogleCloudRecommenderV1beta1ListRecommendationsResponse` | PUBLIC  
`TY_014` | `GoogleCloudRecommenderV1beta1ListRecommendersResponse` | PUBLIC  
`TY_015` | `GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest` | PUBLIC  
`TY_016` | `GoogleCloudRecommenderV1beta1MarkRecommendationClaimedReques` | PUBLIC  
`TY_017` | `GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequ` | PUBLIC  
`TY_018` | `GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest` | PUBLIC  
`TY_019` | `GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequ` | PUBLIC  
`TY_020` | `GoogleCloudRecommenderV1beta1Operation` | PUBLIC  
`TY_021` | `GoogleCloudRecommenderV1beta1OperationGroup` | PUBLIC  
`TY_022` | `GoogleCloudRecommenderV1beta1Recommendation` | PUBLIC  
`TY_023` | `GoogleCloudRecommenderV1beta1RecommendationContent` | PUBLIC  
`TY_024` | `GoogleCloudRecommenderV1beta1RecommendationInsightReference` | PUBLIC  
`TY_025` | `GoogleCloudRecommenderV1beta1RecommendationStateInfo` | PUBLIC  
`TY_026` | `GoogleCloudRecommenderV1beta1RecommenderConfig` | PUBLIC  
`TY_027` | `GoogleCloudRecommenderV1beta1RecommenderGenerationConfig` | PUBLIC  
`TY_028` | `GoogleCloudRecommenderV1beta1RecommenderType` | PUBLIC  
`TY_029` | `GoogleCloudRecommenderV1beta1ReliabilityProjection` | PUBLIC  
`TY_030` | `GoogleCloudRecommenderV1beta1SecurityProjection` | PUBLIC  
`TY_031` | `GoogleCloudRecommenderV1beta1SustainabilityProjection` | PUBLIC  
`TY_032` | `GoogleCloudRecommenderV1beta1ValueMatcher` | PUBLIC  
`TY_033` | `GoogleTypeMoney` | PUBLIC  
`TY_T_002` | `GoogleCloudLocationLocation` | PUBLIC  
`TY_T_004` | `GoogleCloudRecommenderV1beta1Impact` | PUBLIC  
`TY_T_005` | `GoogleCloudRecommenderV1beta1Insight` | PUBLIC  
`TY_T_006` | `GoogleCloudRecommenderV1beta1InsightRecommendationReference` | PUBLIC  
`TY_T_008` | `GoogleCloudRecommenderV1beta1InsightType` | PUBLIC  
`TY_T_020` | `GoogleCloudRecommenderV1beta1Operation` | PUBLIC  
`TY_T_021` | `GoogleCloudRecommenderV1beta1OperationGroup` | PUBLIC  
`TY_T_022` | `GoogleCloudRecommenderV1beta1Recommendation` | PUBLIC  
`TY_T_024` | `GoogleCloudRecommenderV1beta1RecommendationInsightReference` | PUBLIC  
`TY_T_028` | `GoogleCloudRecommenderV1beta1RecommenderType` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250301 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://recommender.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | recommender:v1beta1 | PUBLIC  
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
  
### GET_CONFIG_INSIGHT_TYPES

  * Description: billingAccounts.locations.insightTypes.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_INSIGHT_TYPES1

  * Description: recommender.organizations.locations.insightTypes.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_INSIGHT_TYPES2

  * Description: recommender.projects.locations.insightTypes.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_RECOMMENDERS

  * Description: billingAccounts.locations.recommenders.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_RECOMMENDERS1

  * Description: recommender.organizations.locations.recommenders.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_RECOMMENDERS2

  * Description: recommender.projects.locations.recommenders.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSIGHTS

  * Description: billingAccounts.locations.insightTypes.insights.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSIGHTS1

  * Description: recommender.folders.locations.insightTypes.insights.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSIGHTS2

  * Description: organizations.locations.insightTypes.insights.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSIGHTS3

  * Description: recommender.projects.locations.insightTypes.insights.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECOMMENDATIONS

  * Description: billingAccounts.locations.recommenders.recommendations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECOMMENDATIONS1

  * Description: folders.locations.recommenders.recommendations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECOMMENDATIONS2

  * Description: organizations.locations.recommenders.recommendations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECOMMENDATIONS3

  * Description: projects.locations.recommenders.recommendations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSIGHTS

  * Description: billingAccounts.locations.insightTypes.insights.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleCloudRecommenderV1beta1ListInsightsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSIGHTS1

  * Description: recommender.folders.locations.insightTypes.insights.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleCloudRecommenderV1beta1ListInsightsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSIGHTS2

  * Description: organizations.locations.insightTypes.insights.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleCloudRecommenderV1beta1ListInsightsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSIGHTS3

  * Description: recommender.projects.locations.insightTypes.insights.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleCloudRecommenderV1beta1ListInsightsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSIGHT_TYPES

  * Description: recommender.insightTypes.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | GoogleCloudRecommenderV1beta1ListInsightTypesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS

  * Description: recommender.billingAccounts.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudLocationListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS1

  * Description: recommender.folders.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudLocationListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS2

  * Description: recommender.organizations.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudLocationListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS3

  * Description: recommender.projects.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudLocationListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RECOMMENDATIONS

  * Description: billingAccounts.locations.recommenders.recommendations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | GoogleCloudRecommenderV1beta1ListRecommendationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RECOMMENDATIONS1

  * Description: folders.locations.recommenders.recommendations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | GoogleCloudRecommenderV1beta1ListRecommendationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RECOMMENDATIONS2

  * Description: organizations.locations.recommenders.recommendations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | GoogleCloudRecommenderV1beta1ListRecommendationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RECOMMENDATIONS3

  * Description: projects.locations.recommenders.recommendations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | GoogleCloudRecommenderV1beta1ListRecommendationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RECOMMENDERS

  * Description: recommender.recommenders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | GoogleCloudRecommenderV1beta1ListRecommendersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_ACCEPTED_INSIGHTS

  * Description: locations.insightTypes.insights.markAccepted 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`IS_INPUT` | IMPORTING | `TY_015` | GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_ACCEPTED_INSIGHTS1

  * Description: folders.locations.insightTypes.insights.markAccepted 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`IS_INPUT` | IMPORTING | `TY_015` | GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_ACCEPTED_INSIGHTS2

  * Description: organizations.locations.insightTypes.insights.markAccepted 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`IS_INPUT` | IMPORTING | `TY_015` | GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_ACCEPTED_INSIGHTS3

  * Description: projects.locations.insightTypes.insights.markAccepted 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IV_P_INSIGHTS_ID` | IMPORTING | `STRING` | insightsId  
`IS_INPUT` | IMPORTING | `TY_015` | GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleCloudRecommenderV1beta1Insight  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_CLAIMED_RECOMMENDATION

  * Description: locations.recommenders.recommendations.markClaimed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_016` | GoogleCloudRecommenderV1beta1MarkRecommendationClaimedReques  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_CLAIMED_RECOMMENDATION1

  * Description: folders.locations.recommenders.recommendations.markClaimed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_016` | GoogleCloudRecommenderV1beta1MarkRecommendationClaimedReques  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_CLAIMED_RECOMMENDATION2

  * Description: locations.recommenders.recommendations.markClaimed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_016` | GoogleCloudRecommenderV1beta1MarkRecommendationClaimedReques  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_CLAIMED_RECOMMENDATION3

  * Description: projects.locations.recommenders.recommendations.markClaimed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_016` | GoogleCloudRecommenderV1beta1MarkRecommendationClaimedReques  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_DISMISSED_RECOMMENDATI

  * Description: locations.recommenders.recommendations.markDismissed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_DISMISSED_RECOMMENDATI1

  * Description: locations.recommenders.recommendations.markDismissed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_DISMISSED_RECOMMENDATI2

  * Description: locations.recommenders.recommendations.markDismissed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_DISMISSED_RECOMMENDATI3

  * Description: locations.recommenders.recommendations.markDismissed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_FAILED_RECOMMENDATIONS

  * Description: locations.recommenders.recommendations.markFailed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_018` | GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_FAILED_RECOMMENDATIONS1

  * Description: folders.locations.recommenders.recommendations.markFailed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_018` | GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_FAILED_RECOMMENDATIONS2

  * Description: locations.recommenders.recommendations.markFailed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_018` | GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_FAILED_RECOMMENDATIONS3

  * Description: projects.locations.recommenders.recommendations.markFailed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_018` | GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_SUCCEEDED_RECOMMENDATI

  * Description: locations.recommenders.recommendations.markSucceeded 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_019` | GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_SUCCEEDED_RECOMMENDATI1

  * Description: locations.recommenders.recommendations.markSucceeded 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_019` | GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_SUCCEEDED_RECOMMENDATI2

  * Description: locations.recommenders.recommendations.markSucceeded 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_019` | GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MARK_SUCCEEDED_RECOMMENDATI3

  * Description: locations.recommenders.recommendations.markSucceeded 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IV_P_RECOMMENDATIONS_ID` | IMPORTING | `STRING` | recommendationsId  
`IS_INPUT` | IMPORTING | `TY_019` | GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleCloudRecommenderV1beta1Recommendation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_INSIGHT_TYPES

  * Description: billingAccounts.locations.insightTypes.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IS_INPUT` | IMPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_INSIGHT_TYPES1

  * Description: organizations.locations.insightTypes.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IS_INPUT` | IMPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_INSIGHT_TYPES2

  * Description: recommender.projects.locations.insightTypes.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSIGHT_TYPES_ID` | IMPORTING | `STRING` | insightTypesId  
`IS_INPUT` | IMPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | GoogleCloudRecommenderV1beta1InsightTypeConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_RECOMMENDERS

  * Description: billingAccounts.locations.recommenders.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_BILLING_ACCOUNTS_ID` | IMPORTING | `STRING` | billingAccountsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IS_INPUT` | IMPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_RECOMMENDERS1

  * Description: organizations.locations.recommenders.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IS_INPUT` | IMPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONFIG_RECOMMENDERS2

  * Description: recommender.projects.locations.recommenders.updateConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_RECOMMENDERS_ID` | IMPORTING | `STRING` | recommendersId  
`IS_INPUT` | IMPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudRecommenderV1beta1RecommenderConfig  
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
