---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list/
title: Method: projects.alertPolicies.list \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.497751+00:00
---

# Method: projects.alertPolicies.list  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.alertPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the existing alerting policies for the workspace.

### HTTP request

`GET https://monitoring.googleapis.com/v3/{name}/alertPolicies`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose alert policies are to be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this field names the parent container in which the alerting policies to be listed are stored. To retrieve a single alerting policy by name, use the `[alertPolicies.get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get#google.monitoring.v3.AlertPolicyService.GetAlertPolicy)` operation, instead. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.alertPolicies.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. If provided, this field specifies the criteria that must be met by alert policies to be included in the response.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`orderBy` |  `string` Optional. A comma-separated list of fields by which to sort the result. Supports the same set of field references as the `filter` field. Entries can be prefixed with a minus sign to sort by the field in descending order.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`pageSize` |  `integer` Optional. The maximum number of results to return in a single response.  
`pageToken` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call.  
  
### Request body

The request body must be empty.

### Response body

The protocol for the `alertPolicies.list` response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "alertPolicies": [
        {
          object ([AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`alertPolicies[]` |  `object (`[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy)`)` The returned alert policies.  
`nextPageToken` |  `string` If there might be more results than were returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
`totalSize` |  `integer` The total number of alert policies in all pages. This number is only an estimate, and may change in subsequent pages. <https://aip.dev/158>  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
