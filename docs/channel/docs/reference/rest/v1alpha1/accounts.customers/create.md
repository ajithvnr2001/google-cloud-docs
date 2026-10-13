---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/create/
title: Method: accounts.customers.create \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:27.185128+00:00
---

# Method: accounts.customers.create  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Method: accounts.customers.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)` resource under the reseller or distributor account.

Possible error codes:

  * PERMISSION_DENIED: 
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to create a customer. See <https://support.google.com/channelservices/answer/9759265>
  * INVALID_ARGUMENT: 
    * Required request parameters are missing or invalid.
    * Domain field value doesn't match the primary email domain.



Return value: The newly created `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)` resource.

### HTTP request

`POST https://cloudchannel.googleapis.com/v1alpha1/{parent=accounts/*}/customers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of reseller account in which to create the customer. Parent uses the format: accounts/{account_id}  
  
### Request body

The request body contains an instance of `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)`.

### Response body

If successful, the response body contains a newly created instance of `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.customers#Customer)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/apps.order`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
