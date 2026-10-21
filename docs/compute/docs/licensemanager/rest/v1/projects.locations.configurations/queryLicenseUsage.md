---
url: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/queryLicenseUsage/
title: Method: projects.locations.configurations.queryLicenseUsage \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:58.862834+00:00
---

# Method: projects.locations.configurations.queryLicenseUsage  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/queryLicenseUsage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.configurations.queryLicenseUsage Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * UserCountUsage
    * JSON representation



License Usage information for a Configuration.

### HTTP request

`GET https://licensemanager.googleapis.com/v1/{name=projects/*/locations/*/configurations/*}:queryLicenseUsage`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource path of the Configuration.  
  
### Query parameters

Parameters  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The start time for retrieving the usage. If not specified, we will use the first day of the current billing period.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The end time for retrieving the usage. If not specified, we will use the last day of the current billing period.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body must be empty.

### Response body

Message for response to get the license usage per configuration.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field details can be only one of the following:
      "userCountUsage": {
        object ([UserCountUsage](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/queryLicenseUsage#UserCountUsage))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
Union field `details`. Depending on the type of the configuration, one of the following will be populated. `details` can be only one of the following:  
`userCountUsage` |  `object (`[UserCountUsage](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/queryLicenseUsage#UserCountUsage)`)` Usage information for license types which use user-count billing.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `licensemanager.configurations.queryLicenseUsage`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UserCountUsage

Message representing usage for license configurations which use user-count billing.

JSON representation  
---  
      
    
    {
      "uniqueUserCount": integer
    }  
  
Fields  
---  
`uniqueUserCount` |  `integer` Required. Unique number of licensed users.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
