---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list/
title: Method: accounts.customers.entitlements.list \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:24.252273+00:00
---

# Method: accounts.customers.entitlements.list  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Method: accounts.customers.entitlements.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists `[Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements#Entitlement)`s belonging to a customer.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: A list of the customer's `[Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements#Entitlement)`s.

### HTTP request

`GET https://cloudchannel.googleapis.com/v1alpha1/{parent=accounts/*/customers/*}/entitlements`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the reseller's customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100.  
`pageToken` |  `string` Optional. A token for a page of results other than the first page. Obtained using `[ListEntitlementsResponse.next_page_token](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list#body.ListEntitlementsResponse.FIELDS.next_page_token)` of the previous `[CloudChannelService.ListEntitlements](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list#google.cloud.channel.v1alpha1.CloudChannelService.ListEntitlements)` call.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[CloudChannelService.ListEntitlements](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list#google.cloud.channel.v1alpha1.CloudChannelService.ListEntitlements)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entitlements": [
        {
          object ([Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements#Entitlement))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`entitlements[]` |  `object (`[Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements#Entitlement)`)` The reseller customer's entitlements.  
`nextPageToken` |  `string` A token to list the next page of results. Pass to `[ListEntitlementsRequest.page_token](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers.entitlements/list#body.QUERY_PARAMETERS.page_token)` to obtain that page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/apps.order`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
