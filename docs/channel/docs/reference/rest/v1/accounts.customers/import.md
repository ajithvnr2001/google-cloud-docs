---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/import/
title: Method: accounts.customers.import \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:47.949717+00:00
---

# Method: accounts.customers.import  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Method: accounts.customers.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Imports a `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers#Customer)` from the Cloud Identity associated with the provided Cloud Identity ID or domain before a customers.transferEntitlements call. If a linked Customer already exists and overwriteIfExists is true, it will update that Customer's data.

Possible error codes:

  * PERMISSION_DENIED: 
    * The reseller account making the request is different from the reseller account in the API request.
    * You are not authorized to import the customer. See <https://support.google.com/channelservices/answer/9759265>
  * NOT_FOUND: Cloud Identity doesn't exist or was deleted.
  * INVALID_ARGUMENT: Required parameters are missing, or the authToken is expired or invalid.
  * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite.



Return value: The `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers#Customer)`.

### HTTP request

`POST https://cloudchannel.googleapis.com/v1/{parent=accounts/*}/customers:import`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the reseller's account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channelPartnerId}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authToken": string,
      "overwriteIfExists": boolean,
      "channelPartnerId": string,
      "customer": string,
    
      // Union field customer_identity can be only one of the following:
      "domain": string,
      "cloudIdentityId": string,
      "primaryAdminEmail": string
      // End of list of possible types for union field customer_identity.
    }  
  
Fields  
---  
`authToken` |  `string` Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See <https://support.google.com/a/answer/7643790> for more details.  
`overwriteIfExists` |  `boolean` Required. Choose to overwrite an existing customer if found. This must be set to true if there is an existing customer with a conflicting region code or domain.  
`channelPartnerId` |  `string` Optional. Cloud Identity ID of a channel partner who will be the direct reseller for the customer's order. This field is required for 2-tier transfer scenarios and can be provided via the request Parent binding as well.  
`customer` |  `string` Optional. Specifies the customer that will receive imported Cloud Identity information. Format: accounts/{account_id}/customers/{customer_id}  
Union field `customer_identity`. Specifies the identity of the transfer customer. A customer's cloud_identity_id or domain is required to look up the customer's Cloud Identity. For Team customers, only the cloud_identity_id option is valid. `customer_identity` can be only one of the following:  
`domain` |  `string` Required. Customer domain.  
`cloudIdentityId` |  `string` Required. Customer's Cloud Identity ID  
`primaryAdminEmail` |  `string` Required. Customer's primary admin email.  
  
### Response body

If successful, the response body contains an instance of `[Customer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers#Customer)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/apps.order`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
