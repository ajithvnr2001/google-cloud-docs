---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete/
title: Method: organizations.delete \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:10.658487+00:00
---

# Method: organizations.delete  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * DeletionRetention
  * Try it!



Delete an Apigee organization. For organizations with BillingType EVALUATION, an immediate deletion is performed. For paid organizations (Subscription or Pay-as-you-go), a soft-deletion is performed. The organization can be restored within the soft-deletion period, which is specified using the `retention` field in the request or by filing a support ticket with Apigee. During the data retention period specified in the request, the Apigee organization cannot be recreated in the same Google Cloud project.

**IMPORTANT: The default data retention setting for this operation is 7 days. To permanently delete the organization in 24 hours, set the retention parameter to`MINIMUM`.**

### HTTP request

`DELETE https://apigee.googleapis.com/v1/{name=organizations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the organization. Use the following structure in your request: `organizations/{org}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.organizations.delete`

  
  
### Query parameters

Parameters  
---  
`retention` |  `enum (`[DeletionRetention](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete#DeletionRetention)`)` Optional. This setting is applicable only for organizations that are soft-deleted (i.e., BillingType is not EVALUATION). It controls how long Organization data will be retained after the initial delete operation completes. During this period, the Organization may be restored to its last known state. After this period, the Organization will no longer be able to be restored.**Note: During the data retention period specified using this field, the Apigee organization cannot be recreated in the same Google Cloud project.**  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## DeletionRetention

Data retention settings for deleting Organizations.

Enums  
---  
`DELETION_RETENTION_UNSPECIFIED` | Default data retention setting of seven days will be applied.  
`MINIMUM` | Organization data will be retained for the minimum period of 24 hours.  
`NO_RETENTION` |  Does not retain organization data and permanently deletes the organization immediately. **Warning:** You will NOT be able to restore the Apigee organization when using this option.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
