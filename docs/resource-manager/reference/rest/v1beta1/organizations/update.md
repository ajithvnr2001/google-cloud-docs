---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/update/
title: Method: organizations.update \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:22.959401+00:00
---

# Method: organizations.update  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: organizations.update Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



This item is deprecated!

Updates an Organization resource identified by the specified resource name.

### HTTP request

`PUT https://cloudresourcemanager.googleapis.com/v1beta1/{name=organizations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Output only. The resource name of the organization. This is the organization's relative path in the API. Its format is "organizations/[organizationId]". For example, "organizations/1234".  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "organizationId": string,
      "displayName": string,
      "owner": {
        object ([OrganizationOwner](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#OrganizationOwner))
      },
      "creationTime": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#LifecycleState))
    }  
  
Fields  
---  
`organizationId  
**(deprecated)**` |  `string` An immutable id for the Organization that is assigned on creation. This should be omitted when creating a new Organization. This field is read-only.  
`displayName` |  `string` A human-readable string that refers to the Organization in the Google Cloud console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, "google.com") of the G Suite customer that owns the organization.  
`owner` |  `object (`[OrganizationOwner](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#OrganizationOwner)`)` The owner of this Organization. The owner should be specified on creation. Once set, it cannot be changed. This field is required.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the Organization was created. Assigned by the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#LifecycleState)`)` The organization's current lifecycle state. Assigned by the server.  
  
### Response body

If successful, the response body contains an instance of `[Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations#Organization)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudplatformorganizations`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
