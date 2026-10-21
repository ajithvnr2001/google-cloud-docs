---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/rejectPlanChange/
title: Method: providers.entitlements.rejectPlanChange \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:11.032740+00:00
---

# Method: providers.entitlements.rejectPlanChange  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/rejectPlanChange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  Method: providers.entitlements.rejectPlanChange Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Rejects an entitlement plan change that is in the `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)` state.

This method is invoked by the provider to reject the plan change on the entitlement resource.

### HTTP request

`POST https://cloudcommerceprocurement.googleapis.com/v1/{name=providers/*/entitlements/*}:rejectPlanChange`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the entitlement. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `commerceprocurement.providerEntitlements.reject`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "reason": string,
      "pendingPlanName": string
    }  
  
Fields  
---  
`reason` |  `string` Free form text string explaining the rejection reason.Max allowed length: 256 bytes. Longer strings will be truncated.  
`pendingPlanName` |  `string` Required. Name of the pending plan that is being rejected.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
