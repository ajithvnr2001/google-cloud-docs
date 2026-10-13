---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/preview/
title: Method: projects.locations.spaces.applications.preview \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:31.308166+00:00
---

# Method: projects.locations.spaces.applications.preview  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.applications.preview Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Previews deployment of an application.

### HTTP request

`POST https://designcenter.googleapis.com/v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:preview`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The application name in the following format: `projects/$project/locations/$location/spaces/$space/applications/$application`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workerPool": string,
      "serviceAccount": string
    }  
  
Fields  
---  
`workerPool` |  `string` Optional. The user-specified Worker Pool resource in which the Cloud Build job will execute. Format: projects/{project}/locations/{location}/workerPools/{workerPoolId} If this flag is omitted, the worker pool already defined on the application will be used. If no worker pool is defined on the application, the default Cloud Build worker pool is used. The worker pool must exist in the same region as the application.  
`serviceAccount` |  `string` Optional. The email address of the service account to use for this preview operation.

  * If provided, this service account will be used to execute the preview process, taking precedence over any serviceAccount specified on the Application resource.
  * The caller must have the 'iam.serviceAccounts.actAs' permission on this service account.
  * If this field is omitted, the system will use the 'serviceAccount' defined within the Application resource.
  * We recommend that you provide a service account here or on the Application resource. If you don't provide a service account, the preview will fail. Format: projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}

  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.applications.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
