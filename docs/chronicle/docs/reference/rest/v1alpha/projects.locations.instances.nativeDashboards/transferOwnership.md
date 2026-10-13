---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.nativeDashboards/transferOwnership/
title: Method: nativeDashboards.transferOwnership \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:30.127989+00:00
---

# Method: nativeDashboards.transferOwnership  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.nativeDashboards/transferOwnership/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: nativeDashboards.transferOwnership Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



**Full name** : projects.locations.instances.nativeDashboards.transferOwnership

Transfers ownership of a specified resource to a new principal. The previous owner is automatically granted the editor role on the object. Please note that ownership can only be transferred to a user principal, not a group.

### HTTP request

`POST https://{endpoint}/v1alpha/{name}:transferOwnership`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the object whose ownership is to be transferred. Format: projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{nativeDashboard} projects/{project}/locations/{location}/instances/{instance}/users/{user}/searchQueries/{searchQuery}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "principal": string
    }  
  
Fields  
---  
`principal` |  `string` Required. The IAM principal of the new owner of the Object. The supported formats are: * `user:{emailid}` for Google Account user * `principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE` for Workforce Identity user * `serviceAccount:SA_EMAIL_ADDRESS` for service account * `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE` for Workload Identity user * `principal://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH` for agent identity user. Please note that ownership can only be transferred to a user principal, not a group.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
