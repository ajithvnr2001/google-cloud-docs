---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability/
title: Method: projects.locations.ipamAdminScopes.checkAvailability \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:42:51.710887+00:00
---

# Method: projects.locations.ipamAdminScopes.checkAvailability  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Method: projects.locations.ipamAdminScopes.checkAvailability Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * IpamAdminScopeAvailability
    * JSON representation
  * Availability
  * Try it!



Checks the availability of IpamAdminScopes in a given project and location.

### HTTP request

`GET https://cloudnumberregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/ipamAdminScopes:checkAvailability`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, for example `projects/*/locations/*`.  
  
### Query parameters

Parameters  
---  
`scopes[]` |  `string` Required. The administrative scopes to check for availability.  
  
### Request body

The request body must be empty.

### Response body

Response message for the `[CloudNumberRegistry.CheckAvailabilityIpamAdminScopes](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability#google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "scopeAvailabilities": [
        {
          object ([IpamAdminScopeAvailability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability#IpamAdminScopeAvailability))
        }
      ]
    }  
  
Fields  
---  
`scopeAvailabilities[]` |  `object (`[IpamAdminScopeAvailability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability#IpamAdminScopeAvailability)`)` The details of the requested scopes.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudnumberregistry.ipamAdminScopes.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## IpamAdminScopeAvailability

Availability details for a specific IpamAdminScope.

JSON representation  
---  
      
    
    {
      "scope": string,
      "adminProject": string,
      "availability": enum ([Availability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability#Availability))
    }  
  
Fields  
---  
`scope` |  `string` The scope of the IpamAdminScope.  
`adminProject` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The admin project of the IpamAdminScope if it exists.  
`availability` |  `enum (`[Availability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability#Availability)`)` The availability of the scope.  
  
## Availability

Enum for the availability of a given scope.

Enums  
---  
`AVAILABILITY_UNSPECIFIED` | Unspecified availability.  
`AVAILABLE` | The scope is available.  
`UNAVAILABLE` | The scope is not available.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
