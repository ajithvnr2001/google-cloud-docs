---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/getConfig/
title: Method: projects.locations.getConfig \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:55.027652+00:00
---

# Method: projects.locations.getConfig  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/getConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Method: projects.locations.getConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SkaffoldVersion
    * JSON representation
  * Try it!



Gets the configuration for a location.

### HTTP request

Choose a location:

global asia-south1 asia-south2 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://clouddeploy.googleapis.com/v1/{name=projects/*/locations/*/config}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of requested configuration.  
  
### Request body

The request body must be empty.

### Response body

Service-wide configuration.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "supportedVersions": [
        {
          object ([SkaffoldVersion](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/getConfig#SkaffoldVersion))
        }
      ],
      "defaultSkaffoldVersion": string,
      "defaultToolVersions": {
        object ([ToolVersions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersions))
      }
    }  
  
Fields  
---  
`name` |  `string` Name of the configuration.  
`supportedVersions[]` |  `object (`[SkaffoldVersion](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/getConfig#SkaffoldVersion)`)` All supported versions of Skaffold.  
`defaultSkaffoldVersion` |  `string` Default Skaffold version that is assigned when a Release is created without specifying a Skaffold version.  
`defaultToolVersions` |  `object (`[ToolVersions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersions)`)` Output only. Default tool versions. These tool versions are assigned when a Release is created without specifying tool versions.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `clouddeploy.config.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SkaffoldVersion

Details of a supported Skaffold version.

JSON representation  
---  
      
    
    {
      "version": string,
      "maintenanceModeTime": string,
      "supportExpirationTime": string,
      "supportEndDate": {
        object ([Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date))
      }
    }  
  
Fields  
---  
`version` |  `string` Release version number. For example, "1.20.3".  
`maintenanceModeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this version of Skaffold will enter maintenance mode.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`supportExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this version of Skaffold will no longer be supported.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`supportEndDate` |  `object (`[Date](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#Date)`)` Date when this version is expected to no longer be supported.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
