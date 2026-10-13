---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyAdvancedReports/legacyReportImport/
title: Method: legacyAdvancedReports.legacyReportImport \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:56.906638+00:00
---

# Method: legacyAdvancedReports.legacyReportImport  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyAdvancedReports/legacyReportImport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyAdvancedReports.legacyReportImport Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * LegacyAdvancedReportCategory



**Full name** : projects.locations.instances.legacyAdvancedReports.legacyReportImport

Imports a report definition into the advanced reporting system.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacyAdvancedReports:legacyReportImport`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to import the report to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "category": enum ([LegacyAdvancedReportCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyAdvancedReports/legacyReportImport#LegacyAdvancedReportCategory)),
      "environments": [
        string
      ],
      "lookML": string,
      "id": string,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string
    }  
  
Fields  
---  
`category` |  `enum (`[LegacyAdvancedReportCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyAdvancedReports/legacyReportImport#LegacyAdvancedReportCategory)`)` Optional. The target category for the advanced report import.  
`environments[]` |  `string` Optional. List of environments associated with the advanced report import.  
`lookML` |  `string` Optional. The LookML content of the advanced report import. LINT: LEGACY_NAMES  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The ID of the advanced report.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The creation time of the advanced report in Unix time in milliseconds.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The modification time of the advanced report in Unix time in milliseconds.  
  
### Response body

If successful, the response body contains an instance of `[LegacyLookerReportResponse](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyLookerReportResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySoarAdvancedReports.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## LegacyAdvancedReportCategory

Enums  
---  
`DEFAULT` | Default.  
`PERSONAL` | Personal.  
`SHARED` | Shared.  
`OTHER` | Other.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
