---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboards/list/
title: Method: dashboards.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:59.076351+00:00
---

# Method: dashboards.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboards/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: dashboards.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.dashboards.list

List all dashboards.

### HTTP request

`GET https://{endpoint}/v1alpha/{parent}/dashboards`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of dashboards. Format: projects/{project}/locations/{region}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of dashboards to return. The service may return fewer than this value.  
`pageToken` |  `string` A page token, received from a previous `dashboards.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `dashboards.list` must match the call that provided the page token.  
`view` |  `enum (`[DashboardView](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/DashboardView)`)` View indicates the scope of fields to populate when returning the dashboard resource. If unspecified, defaults to the basic view.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing dashboards.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dashboards": [
        {
          object ([Dashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboards#Dashboard))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dashboards[]` |  `object (`[Dashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboards#Dashboard)`)` The dashboards from the specified chronicle instance.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.dashboards.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
