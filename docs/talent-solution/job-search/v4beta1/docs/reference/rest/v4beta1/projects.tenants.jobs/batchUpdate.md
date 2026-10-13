---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchUpdate/
title: Method: projects.tenants.jobs.batchUpdate \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:37.985032+00:00
---

# Method: projects.tenants.jobs.batchUpdate  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)
  * [ Reference ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/apis)



Send feedback 

#  Method: projects.tenants.jobs.batchUpdate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



Begins executing a batch update jobs operation.

### HTTP request

`POST https://jobs.googleapis.com/v4beta1/{parent=projects/*/tenants/*}/jobs:batchUpdate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the tenant under which the job is created.The format is "projects/{projectId}/tenants/{tenantId}". For example, "projects/foo/tenant/bar". If tenant id is unspecified, a default tenant is created. For example, "projects/foo".  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "jobs": [
        {
          object ([Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job))
        }
      ],
      "updateMask": string
    }  
  
Fields  
---  
`jobs[]` |  `object (`[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)`)` Required. The jobs to be updated.  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Strongly recommended for the best service experience. Be aware that it will also increase latency when checking the status of a batch operation.If `[updateMask](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchUpdate#body.request_body.FIELDS.update_mask)` is provided, only the specified fields in `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)` are updated. Otherwise all the fields are updated.A field mask to restrict the fields that are updated. Only top level fields of `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)` are supported.If `[updateMask](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants.jobs/batchUpdate#body.request_body.FIELDS.update_mask)` is provided, The `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)` inside `JobResult` will only contains fields that is updated, plus the Id of the Job. Otherwise, `[Job](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job)` will include all fields, which can yield a very large response.A comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.operations#Operation)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/jobs`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
