---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.osPolicyAssignments.reports/list/
title: Method: projects.locations.instances.osPolicyAssignments.reports.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:26.382163+00:00
---

# Method: projects.locations.instances.osPolicyAssignments.reports.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.osPolicyAssignments.reports/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.instances.osPolicyAssignments.reports.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



List OS policy assignment reports for all Compute Engine VM instances in the specified zone.

### HTTP request

`GET https://osconfig.googleapis.com/v1alpha/{parent=projects/*/locations/*/instances/*/osPolicyAssignments/*}/reports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name.Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports`For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`.For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of results to return.  
`filter` |  `string` If provided, this field specifies the criteria that must be met by the `OSPolicyAssignmentReport` API resource that is included in the response.  
`pageToken` |  `string` A pagination token returned from a previous call to the `reports.list` method that indicates where this listing should continue from.  
  
### Request body

The request body must be empty.

### Response body

A response message for listing OS Policy assignment reports including the page of results and page token.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "osPolicyAssignmentReports": [
        {
          object ([OSPolicyAssignmentReport](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`osPolicyAssignmentReports[]` |  `object (`[OSPolicyAssignmentReport](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport)`)` List of OS policy assignment reports.  
`nextPageToken` |  `string` The pagination token to retrieve the next page of OS policy assignment report objects.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `osconfig.osPolicyAssignmentReports.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
