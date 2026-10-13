---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/list/
title: Method: fhirStores.list \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:19.888626+00:00
---

# Method: fhirStores.list  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: fhirStores.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.fhirStores.list

Lists the FHIR stores in the given dataset.

### HTTP request

`GET https://healthcare.googleapis.com/v1/{parent=projects/*/locations/*/datasets/*}/fhirStores`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the dataset. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.fhirStores.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Limit on the number of FHIR stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.  
`pageToken` |  `string` The nextPageToken value returned from the previous List request, if any.  
`filter` |  `string` Restricts stores returned to those matching a filter. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality(`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator(`=`), along with the less than/greater than operators(`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator(`=`) , along with the less than/greater than operators(`<`, `<=`, `>`, `>=`). Note that there is no inequality(`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

Only filtering on labels is supported, for example `labels.key=value`.  
  
### Request body

The request body must be empty.

### Response body

Lists the FHIR stores in the given dataset.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fhirStores": [
        {
          object([FhirStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`fhirStores[]` |  `object(`[FhirStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore)`)` The returned FHIR stores. Won't be more FHIR stores than the value of pageSize in the request.  
`nextPageToken` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
