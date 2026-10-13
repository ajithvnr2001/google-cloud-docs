---
url: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.reportConfigs.reports/list/
title: Method: projects.locations.reportConfigs.reports.list \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:19.038445+00:00
---

# Method: projects.locations.reportConfigs.reports.list  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.reportConfigs.reports/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Reference ](https://docs.cloud.google.com/migration-center/docs/api)



Send feedback 

#  Method: projects.locations.reportConfigs.reports.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists Reports in a given ReportConfig.

### HTTP request

`GET https://migrationcenter.googleapis.com/v1alpha1/{parent=projects/*/locations/*/reportConfigs/*}/reports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for `ListReportsRequest`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default value.  
`pageToken` |  `string` A token identifying a page of results that the server should return.  
`filter` |  `string` Filtering results.  
`orderBy` |  `string` Field to sort by. See <https://google.aip.dev/132#ordering> for more details.  
`view` |  `enum (`[ReportView](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/ReportView)`)` Determines what information to retrieve for each Report.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing Reports.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "reports": [
        {
          object ([Report](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.reportConfigs.reports#Report))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`reports[]` |  `object (`[Report](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/projects.locations.reportConfigs.reports#Report)`)` The list of Reports.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
