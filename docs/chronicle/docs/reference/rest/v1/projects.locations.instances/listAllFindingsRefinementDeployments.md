---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/listAllFindingsRefinementDeployments/
title: Method: instances.listAllFindingsRefinementDeployments \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:24.510323+00:00
---

# Method: instances.listAllFindingsRefinementDeployments  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/listAllFindingsRefinementDeployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.listAllFindingsRefinementDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.listAllFindingsRefinementDeployments

Lists all findings refinement deployments.

### HTTP request

`GET https://{endpoint}/v1/{instance}:listAllFindingsRefinementDeployments`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance to list all findings refinement deployments over. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of findings refinement deployments to return. The service may return fewer than this value. If unspecified, at most 100 rule deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous `instances.listAllFindingsRefinementDeployments` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `instances.listAllFindingsRefinementDeployments` must match the call that provided the page token.  
`filter` |  `string` A filter that can be used to retrieve specific findings refinement deployments. Only the following filters are allowed: detectionExclusionApplication.curated_rule_sets:""", detectionExclusionApplication.curated_rules:""  
  
### Request body

The request body must be empty.

### Response body

Response message for instances.listAllFindingsRefinementDeployments method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "allFindingsRefinementDeployments": [
        {
          object ([FindingsRefinementDeployment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementDeployment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`allFindingsRefinementDeployments[]` |  `object (`[FindingsRefinementDeployment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FindingsRefinementDeployment)`)` List of all findings refinement deployments.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.findingsRefinementDeployments.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
