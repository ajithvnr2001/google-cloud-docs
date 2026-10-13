---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/transferEntitlementsToGoogle/
title: Method: accounts.customers.transferEntitlementsToGoogle \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:50.068081+00:00
---

# Method: accounts.customers.transferEntitlementsToGoogle  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/transferEntitlementsToGoogle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Method: accounts.customers.transferEntitlementsToGoogle Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Transfers customer entitlements from their current reseller to Google.

Possible error codes:

  * PERMISSION_DENIED: The customer doesn't belong to the reseller.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The customer or offer resource was not found.
  * ALREADY_EXISTS: The SKU was already transferred for the customer.
  * CONDITION_NOT_MET or FAILED_PRECONDITION: 
    * The SKU requires domain verification to transfer, but the domain is not verified.
    * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic).
    * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: 
      * Domain names must start with goog-test.
      * Domain names must include the reseller domain.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the operations.get method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of `OperationMetadata`.

### HTTP request

`POST https://cloudchannel.googleapis.com/v1/{parent=accounts/*/customers/*}:transferEntitlementsToGoogle`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the reseller's customer account where the entitlements transfer from. Parent uses the format: accounts/{account_id}/customers/{customer_id}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entitlements": [
        {
          object ([Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements#Entitlement))
        }
      ],
      "requestId": string
    }  
  
Fields  
---  
`entitlements[]` |  `object (`[Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements#Entitlement)`)` Required. The entitlements to transfer to Google.  
`requestId` |  `string` Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/apps.order`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
