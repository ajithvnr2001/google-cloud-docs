---
url: https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/place/
title: Method: billingAccounts.orders.place \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:09.590262+00:00
---

# Method: billingAccounts.orders.place  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/place/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Reference ](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest)



Send feedback 

#  Method: billingAccounts.orders.place Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a new `[Order](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#Order)`.

This API only supports GCP spend-based committed use discounts specified by GCP documentation.

The returned long-running operation is in-progress until the backend completes the creation of the resource. Once completed, the order is in `OrderState.ORDER_STATE_ACTIVE`. In case of failure, the order resource will be removed.

### HTTP request

`POST https://cloudcommerceconsumerprocurement.googleapis.com/v1alpha1/{parent=billingAccounts/*}/orders:place`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the parent resource. This field has the form `billingAccounts/{billing-account-id}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "displayName": string,
      "lineItemInfo": [
        {
          object ([LineItemInfo](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemInfo))
        }
      ],
      "requestId": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The user-specified name of the order being placed.  
`lineItemInfo[]` |  `object (`[LineItemInfo](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders#LineItemInfo)`)` Optional. Places order for offer. Required when an offer-based order is being placed.  
`requestId` |  `string` Optional. A unique identifier for this request. The server will ignore subsequent requests that provide a duplicate request ID for at least 24 hours after the first request.The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `consumerprocurement.orders.place`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
