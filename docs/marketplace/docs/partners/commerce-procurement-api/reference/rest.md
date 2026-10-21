---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/
title: Cloud Commerce Partner Procurement API \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:09.480213+00:00
---

# Cloud Commerce Partner Procurement API  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Cloud Commerce Partner Procurement API Stay organized with collections  Save and categorize content based on your preferences. 

Partner API for the Cloud Commerce Procurement Service.

  * REST Resource: v1.providers.accounts
  * REST Resource: v1.providers.entitlements



## Service: cloudcommerceprocurement.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudcommerceprocurement.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudcommerceprocurement.googleapis.com`



## REST Resource: [v1.providers.accounts](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts)

Methods  
---  
`[approve](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/approve)` |  `POST /v1/{name=providers/*/accounts/*}:approve`   
Grants an approval on an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/get)` |  `GET /v1/{name=providers/*/accounts/*}`   
Gets a requested `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)` resource.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/list)` |  `GET /v1/{parent=providers/*}/accounts`   
Lists `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`s that the provider has access to.  
`[reject](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/reject)` |  `POST /v1/{name=providers/*/accounts/*}:reject`   
Rejects an approval on an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)`.  
`[reset](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/reset)` |  `POST /v1/{name=providers/*/accounts/*}:reset`   
Resets an `[Account](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#Account)` and cancels all associated `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`s.  
  
## REST Resource: [v1.providers.entitlements](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements)

Methods  
---  
`[approve](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/approve)` |  `POST /v1/{name=providers/*/entitlements/*}:approve`   
Approves an entitlement that is in the `[EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVATION_REQUESTED)` state.  
`[approvePlanChange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/approvePlanChange)` |  `POST /v1/{name=providers/*/entitlements/*}:approvePlanChange`   
Approves an entitlement plan change that is in the `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)` state.  
`[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/get)` |  `GET /v1/{name=providers/*/entitlements/*}`   
Gets a requested `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)` resource.  
`[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/list)` |  `GET /v1/{parent=providers/*}/entitlements`   
Lists `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`s for which the provider has read access.  
`[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/patch)` |  `PATCH /v1/{name=providers/*/entitlements/*}`   
Updates an existing `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`.  
`[reject](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/reject)` |  `POST /v1/{name=providers/*/entitlements/*}:reject`   
Rejects an entitlement that is in the `[EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVATION_REQUESTED)` state.  
`[rejectPlanChange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/rejectPlanChange)` |  `POST /v1/{name=providers/*/entitlements/*}:rejectPlanChange`   
Rejects an entitlement plan change that is in the `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)` state.  
`[suspend](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/suspend)` |  `POST /v1/{name=providers/*/entitlements/*}:suspend`   
Requests suspension of an active `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
