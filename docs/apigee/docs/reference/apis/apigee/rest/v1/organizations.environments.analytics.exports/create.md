---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create/
title: Method: organizations.environments.analytics.exports.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:48.047178+00:00
---

# Method: organizations.environments.analytics.exports.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.analytics.exports.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * ExportRequest
    * JSON representation
  * DateRange
    * JSON representation
  * Try it!



Submit a data export job to be processed in the background. If the request is successful, the API returns a 201 status, a URI that can be used to retrieve the status of the export job, and the `state` value of "enqueued".

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/analytics/exports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Names of the parent organization and environment. Must be of the form `organizations/{org}/environments/{env}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.exports.create`

  
  
### Request body

The request body contains an instance of `[ExportRequest](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create#ExportRequest)`.

### Response body

If successful, the response body contains a newly created instance of `[Export](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Export)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## ExportRequest

Request body for [CreateExportRequest]

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "dateRange": {
        object ([DateRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create#DateRange))
      },
      "outputFormat": string,
      "csvDelimiter": string,
      "datastoreName": string
    }  
  
Fields  
---  
`name` |  `string` Required. Display name of the export job.  
`description` |  `string` Optional. Description of the export job.  
`dateRange` |  `object (`[DateRange](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.exports/create#DateRange)`)` Required. Date range of the data to export.  
`outputFormat` |  `string` Optional. Output format of the export. Valid values include: `csv` or `json`. Defaults to `json`. Note: Configure the delimiter for CSV output using the `csvDelimiter` property.  
`csvDelimiter` |  `string` Optional. Delimiter used in the CSV file, if `outputFormat` is set to `csv`. Defaults to the `,` (comma) character. Supported delimiter characters include comma (`,`), pipe (`|`), and tab (`\t`).  
`datastoreName` |  `string` Required. Name of the preconfigured datastore.  
  
## DateRange

Date range of the data to export.

JSON representation  
---  
      
    
    {
      "start": string,
      "end": string
    }  
  
Fields  
---  
`start` |  `string` Required. Start date of the data to export in the format `yyyy-mm-dd`. The date range begins at 00:00:00 UTC on the start date.  
`end` |  `string` Required. End date (exclusive) of the data to export in the format `yyyy-mm-dd`. The date range ends at 00:00:00 UTC on the end date- which will not be in the output.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
