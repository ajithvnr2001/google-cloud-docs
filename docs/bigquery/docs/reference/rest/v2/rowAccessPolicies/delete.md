---
url: https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/rowAccessPolicies/delete/
title: Method: rowAccessPolicies.delete \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:45.609158+00:00
---

# Method: rowAccessPolicies.delete  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/rowAccessPolicies/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback 

#  Method: rowAccessPolicies.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Deletes a row access policy.

### IAM Permissions

Requires the following IAM permission(s) on the table:

  * `bigquery.rowAccessPolicies.delete`
  * `bigquery.rowAccessPolicies.setIamPolicy`



### HTTP request

`DELETE https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies/{policyId}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` Required. Project ID of the table to delete the row access policy.  
`datasetId` |  `string` Required. Dataset ID of the table to delete the row access policy.  
`tableId` |  `string` Required. Table ID of the table to delete the row access policy.  
`policyId` |  `string` Required. Policy ID of the row access policy.  
  
### Query parameters

Parameters  
---  
`force` |  `boolean` If set to true, it deletes the row access policy even if it's the last row access policy on the table and the deletion will widen the access rather narrowing it.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
