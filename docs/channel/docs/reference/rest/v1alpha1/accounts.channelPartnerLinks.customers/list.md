---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks.customers/list/
title: Method: accounts.channelPartnerLinks.customers.list \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:40.860698+00:00
---

# Method: accounts.channelPartnerLinks.customers.list  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks.customers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Method: accounts.channelPartnerLinks.customers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



List `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)`s.

Possible error codes:

  * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.



Return value: List of `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)`s, or an empty list if there are no customers.

### HTTP request

`GET https://cloudchannel.googleapis.com/v1alpha1/{parent=accounts/*/channelPartnerLinks/*}/customers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the reseller account to list customers from. Parent uses the format: accounts/{account_id}.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of customers to return. The service may return fewer than this value. If unspecified, returns at most 10 customers. The maximum value is 50.  
`pageToken` |  `string` Optional. A token identifying a page of results other than the first page. Obtained through `[ListCustomersResponse.next_page_token](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/ListCustomersResponse#FIELDS.next_page_token)` of the previous `[CloudChannelService.ListCustomers](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/list#google.cloud.channel.v1alpha1.CloudChannelService.ListCustomers)` call.  
`filter` |  `string` Optional. Filters applied to the [CloudChannelService.ListCustomers] results. See <https://cloud.google.com/channel/docs/concepts/google-cloud/filter-customers> for more information.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListCustomersResponse](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/ListCustomersResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/apps.order`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
