---
url: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skuGroups/list/
title: Method: billingAccounts.skuGroups.list \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:22.171108+00:00
---

# Method: billingAccounts.skuGroups.list  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skuGroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Method: billingAccounts.skuGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists SKU groups visible to a `billing account`.

### HTTP request

`GET https://cloudbilling.googleapis.com/v1beta/{parent=billingAccounts/*}/skuGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The `billing account` to list `billing account SKU groups` from. Format: billingAccounts/{billingAccount}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of `billing account SKU groups` to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.  
`pageToken` |  `string` Page token received from a previous `skuGroups.list` call to retrieve the next page of results. If this field is empty, the first page is returned.  
  
### Request body

The request body must be empty.

### Response body

Response message for `skuGroups.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "billingAccountSkuGroups": [
        {
          object ([BillingAccountSkuGroup](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skuGroups#BillingAccountSkuGroup))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`billingAccountSkuGroups[]` |  `object (`[BillingAccountSkuGroup](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skuGroups#BillingAccountSkuGroup)`)` The returned publicly listed `billing account SKU groups`.  
`nextPageToken` |  `string` Token that can be sent as `pageToken` in the subsequent request to retrieve the next page. If this field is empty, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-billing`
  * `https://www.googleapis.com/auth/cloud-billing.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
