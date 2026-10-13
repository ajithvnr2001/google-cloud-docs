---
url: https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary/
title: Method: projects.locations.keyRings.cryptoKeys.getProtectedResourcesSummary \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:24.517695+00:00
---

# Method: projects.locations.keyRings.cryptoKeys.getProtectedResourcesSummary  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)



Send feedback 

#  Method: projects.locations.keyRings.cryptoKeys.getProtectedResourcesSummary Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * FallbackScope
  * Warning
    * JSON representation
  * WarningCode
  * Try it!



Returns aggregate information about the resources protected by the given Cloud KMS `[CryptoKey](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys#CryptoKey)`. By default, summary of resources within the same Cloud organization as the key will be returned, which requires the KMS organization service account to be configured; see <https://docs.cloud.google.com/kms/help/key-usage/required-roles>. If the KMS organization service account is not configured or key's project is not part of an organization, set `[fallbackScope](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#body.QUERY_PARAMETERS.fallback_scope)` to `FALLBACK_SCOPE_PROJECT` to retrieve a summary of protected resources within the key's project.

### HTTP request

`GET https://kmsinventory.googleapis.com/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}/protectedResourcesSummary`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the `[CryptoKey](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys#CryptoKey)`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `cloudkms.cryptoKeys.get`

  
  
### Query parameters

Parameters  
---  
`fallbackScope` |  `enum (`[FallbackScope](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#FallbackScope)`)` Optional. The scope to use if the kms organization service account is not configured.  
  
### Request body

The request body must be empty.

### Response body

Aggregate information about the resources protected by a Cloud KMS key in the same Cloud organization or project as the key.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceCount": string,
      "projectCount": integer,
      "resourceTypes": {
        string: string,
        ...
      },
      "cloudProducts": {
        string: string,
        ...
      },
      "locations": {
        string: string,
        ...
      },
      "warnings": [
        {
          object ([Warning](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#Warning))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The full name of the ProtectedResourcesSummary resource. Example: projects/test-project/locations/us/keyRings/test-keyring/cryptoKeys/test-key/protectedResourcesSummary  
`resourceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of protected resources in the same Cloud organization as the key.  
`projectCount` |  `integer` The number of distinct Cloud projects in the same Cloud organization as the key that have resources protected by the key.  
`resourceTypes` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` The number of resources protected by the key grouped by resource type.  
`cloudProducts` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` The number of resources protected by the key grouped by Cloud product.  
`locations` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` The number of resources protected by the key grouped by region.  
`warnings[]` |  `object (`[Warning](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#Warning)`)` Warning messages for the state of response `[ProtectedResourcesSummary](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#body.ProtectedResourcesSummary)` For example, if the organization service account is not configured, INSUFFICIENT_PERMISSIONS_PARTIAL_DATA warning will be returned.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## FallbackScope

Specifies the scope to use if the organization service agent is not configured.

Enums  
---  
`FALLBACK_SCOPE_UNSPECIFIED` | Unspecified scope type.  
`FALLBACK_SCOPE_PROJECT` | If set to `FALLBACK_SCOPE_PROJECT`, the API will fall back to using key's project as request scope if the kms organization service account is not configured.  
  
## Warning

A warning message that indicates potential problems with the response data.

JSON representation  
---  
      
    
    {
      "warningCode": enum ([WarningCode](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#WarningCode)),
      "displayMessage": string
    }  
  
Fields  
---  
`warningCode` |  `enum (`[WarningCode](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary#WarningCode)`)` The specific warning code for the displayed message.  
`displayMessage` |  `string` The literal message providing context and details about the warnings.  
  
## WarningCode

Different types of warnings that can be returned to the user. The displayMessage contains detailed information regarding the warningCode.

Enums  
---  
`WARNING_CODE_UNSPECIFIED` | Default value. This value is unused.  
`INSUFFICIENT_PERMISSIONS_PARTIAL_DATA` | Indicates that the caller or service agent lacks necessary permissions to view some of the requested data. The response may be partial. Example: - KMS organization service agent {service_agent_name} lacks the `cloudasset.assets.searchAllResources` permission on the scope.  
`RESOURCE_LIMIT_EXCEEDED_PARTIAL_DATA` | Indicates that a resource limit has been exceeded, resulting in partial data. Example: - The project has more than 10,000 assets (resources, crypto keys, key handles, IAM policies, etc).  
`ORG_LESS_PROJECT_PARTIAL_DATA` | Indicates that the project exists outside of an organization resource. Thus the analysis is only done for the project level data and results might be partial.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
