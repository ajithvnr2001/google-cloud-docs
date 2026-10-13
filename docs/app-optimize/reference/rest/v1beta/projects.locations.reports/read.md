---
url: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read/
title: Method: projects.locations.reports.read \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:40.858188+00:00
---

# Method: projects.locations.reports.read  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  Method: projects.locations.reports.read Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Column
    * JSON representation
  * Try it!



Reads data within a specified report.

### HTTP request

`POST https://appoptimize.googleapis.com/v1beta/{name=projects/*/locations/*/reports/*}:read`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the report to query.Format: `projects/{project}/locations/{location}/reports/{reportId}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`pageSize` |  `integer` Optional. The maximum number of rows to return. The service may return fewer than this value. If unspecified, at most 10,000 rows will be returned per page. The maximum allowed value is 25,000; values above 25,000 are coerced to 25,000.  
`pageToken` |  `string` Optional. A page token, received from a previous `reports.read` call, to retrieve the subsequent page of results. When `pageToken` is specified, `job_reference` must also be provided from the previous response, and the `statement` field must not be set.  
  
### Response body

Response message for the `reports.read` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rows": [
        array
      ],
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read#Column))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`rows[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` A list of rows, where each row represents a record from the report.  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read#Column)`)` The columns describing the structure of the data in the `rows` field.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` in a subsequent `reports.read` request to retrieve the next page of results. If this field is empty, there are no further pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `appoptimize.reports.getData`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Column

Describes a single column within `Columns`.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "mode": string,
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read#Column))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of the column.This field:

  * Contains only letters (a-z, A-Z), numbers (0-9), or underscores (_);
  * Start with a letter or underscore; and
  * Has a maximum length is 128 characters.

  
`type` |  `string` The data type of the column.Supported values include:

  * `STRING`
  * `INT64`
  * `FLOAT64`
  * `BOOLEAN`
  * `TIMESTAMP`
  * `RECORD`

`RECORD` indicates that the field contains a nested schema, described in the `columns` property of this `Column`.  
`mode` |  `string` The mode of the column, indicating if it is nullable, required, or repeated.Possible values:

  * `NULLABLE`: The column allows NULL values.
  * `REQUIRED`: The column does not allow NULL values.
  * `REPEATED`: The column contains an array of values.

  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read#Column)`)` If the `type` of this column is `RECORD`, this sub-field describes the nested structure.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
