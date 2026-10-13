---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.versions.specs/setIamPolicy/
title: Method: projects.locations.apis.versions.specs.setIamPolicy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:15.686539+00:00
---

# Method: projects.locations.apis.versions.specs.setIamPolicy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis.versions.specs/setIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Method: projects.locations.apis.versions.specs.setIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!

**Note:** You are viewing the legacy Apigee Registry API documentation which is no longer supported. For the latest API hub functionality, it's recommended to use the [Apigee API hub APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest).

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

### HTTP request

`POST https://apigeeregistry.googleapis.com/v1/{resource=projects/*/locations/*/apis/*/versions/*/specs/*}:setIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policy": {
        object ([Policy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/Policy))
      }
    }  
  
Fields  
---  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/Policy)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
