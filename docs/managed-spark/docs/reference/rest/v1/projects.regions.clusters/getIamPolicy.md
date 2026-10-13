---
url: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/getIamPolicy/
title: Method: projects.regions.clusters.getIamPolicy \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:29.485617+00:00
---

# Method: projects.regions.clusters.getIamPolicy  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/getIamPolicy/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  Method: projects.regions.clusters.getIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### HTTP request

`POST https://dataproc.googleapis.com/v1/{resource=projects/*/regions/*/clusters/*}:getIamPolicy`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "options": {
        object ([GetPolicyOptions](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/GetPolicyOptions))
      }
    }  
  
Fields  
---  
`options` |  `object (`[GetPolicyOptions](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/GetPolicyOptions)`)` OPTIONAL: A `GetPolicyOptions` object for specifying options to `clusters.getIamPolicy`.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataproc`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
