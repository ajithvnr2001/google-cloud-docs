---
url: https://docs.cloud.google.com/billing/docs/reference/rest/
title: Cloud Billing API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:35.652995+00:00
---

# Cloud Billing API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Cloud Billing API Stay organized with collections  Save and categorize content based on your preferences. 

Allows developers to manage billing for their Google Cloud Platform projects programmatically.

  * REST Resource: v1.billingAccounts
  * REST Resource: v1.billingAccounts.projects
  * REST Resource: v1.billingAccounts.subAccounts
  * REST Resource: v1.organizations.billingAccounts
  * REST Resource: v1.projects
  * REST Resource: v1.services
  * REST Resource: v1.services.skus



## Service: cloudbilling.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudbilling.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudbilling.googleapis.com`



## REST Resource: [v1.billingAccounts](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts)

Methods  
---  
`[create](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/create)` |  `POST /v1/billingAccounts`   
This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts).  
`[get](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/get)` |  `GET /v1/{name=billingAccounts/*}`   
Gets information about a billing account.  
`[getIamPolicy](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/getIamPolicy)` |  `GET /v1/{resource=billingAccounts/*}:getIamPolicy`   
Gets the access control policy for a billing account.  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/list)` |  `GET /v1/billingAccounts`   
Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).  
`[move](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/move)` |  `POST /v1/{name=billingAccounts/*}:move`   
Changes which parent organization a billing account belongs to.  
`[patch](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/patch)` |  `PATCH /v1/{name=billingAccounts/*}`   
Updates a billing account's fields.  
`[setIamPolicy](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/setIamPolicy)` |  `POST /v1/{resource=billingAccounts/*}:setIamPolicy`   
Sets the access control policy for a billing account.  
`[testIamPermissions](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts/testIamPermissions)` |  `POST /v1/{resource=billingAccounts/*}:testIamPermissions`   
Tests the access control policy for a billing account.  
  
## REST Resource: [v1.billingAccounts.projects](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts.projects)

Methods  
---  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts.projects/list)` |  `GET /v1/{name=billingAccounts/*}/projects`   
Lists the projects associated with a billing account.  
  
## REST Resource: [v1.billingAccounts.subAccounts](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts.subAccounts)

Methods  
---  
`[create](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts.subAccounts/create)` |  `POST /v1/{parent=billingAccounts/*}/subAccounts`   
This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts).  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts.subAccounts/list)` |  `GET /v1/{parent=billingAccounts/*}/subAccounts`   
Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).  
  
## REST Resource: [v1.organizations.billingAccounts](https://docs.cloud.google.com/billing/docs/reference/rest/v1/organizations.billingAccounts)

Methods  
---  
`[create](https://docs.cloud.google.com/billing/docs/reference/rest/v1/organizations.billingAccounts/create)` |  `POST /v1/{parent=organizations/*}/billingAccounts`   
This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts).  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/organizations.billingAccounts/list)` |  `GET /v1/{parent=organizations/*}/billingAccounts`   
Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).  
`[move](https://docs.cloud.google.com/billing/docs/reference/rest/v1/organizations.billingAccounts/move)` |  `GET /v1/{destinationParent=organizations/*}/{name=billingAccounts/*}:move`   
Changes which parent organization a billing account belongs to.  
  
## REST Resource: [v1.projects](https://docs.cloud.google.com/billing/docs/reference/rest/v1/projects)

Methods  
---  
`[getBillingInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/projects/getBillingInfo)` |  `GET /v1/{name=projects/*}/billingInfo`   
Gets the billing information for a project.  
`[updateBillingInfo](https://docs.cloud.google.com/billing/docs/reference/rest/v1/projects/updateBillingInfo)` |  `PUT /v1/{name=projects/*}/billingInfo`   
Sets or updates the billing account associated with a project.  
  
## REST Resource: [v1.services](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services)

Methods  
---  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services/list)` |  `GET /v1/services`   
Lists all public cloud services.  
  
## REST Resource: [v1.services.skus](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus)

Methods  
---  
`[list](https://docs.cloud.google.com/billing/docs/reference/rest/v1/services.skus/list)` |  `GET /v1/{parent=services/*}/skus`   
Lists all publicly available SKUs for a given cloud service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
