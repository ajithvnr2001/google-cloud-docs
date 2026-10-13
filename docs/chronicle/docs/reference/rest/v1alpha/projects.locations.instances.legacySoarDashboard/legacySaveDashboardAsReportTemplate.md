---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacySaveDashboardAsReportTemplate/
title: Method: legacySoarDashboard.legacySaveDashboardAsReportTemplate \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:47.936807+00:00
---

# Method: legacySoarDashboard.legacySaveDashboardAsReportTemplate  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacySaveDashboardAsReportTemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySoarDashboard.legacySaveDashboardAsReportTemplate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * ReportTemplateCategoryEnum



**Full name** : projects.locations.instances.legacySoarDashboard.legacySaveDashboardAsReportTemplate

Saves the current dashboard configuration as a report template. This enables users to generate static reports or schedule automated reporting based on dashboard views.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacySoarDashboard:legacySaveDashboardAsReportTemplate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to save the dashboard as a report template for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "id": integer,
      "creator": string,
      "creatorFullName": string,
      "category": enum ([ReportTemplateCategoryEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacySaveDashboardAsReportTemplate#ReportTemplateCategoryEnum)),
      "name": string,
      "reportWidgets": [
        {
          object ([LegacySoarDashboardWidgetDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacySoarDashboardWidgetDataModel))
        }
      ],
      "creationTimeUnixTimeInMs": string,
      "lastModifiedTimeUnixTimeInMs": string,
      "isSystem": boolean,
      "hasScheduler": boolean
    }  
  
Fields  
---  
`id` |  `integer` Optional. The dashboard id to save as a report template.  
`creator  
**(deprecated)**` |  `string` Optional. The creator of the report template.  
`creatorFullName  
**(deprecated)**` |  `string` Optional. The creator full name of the report template.  
`category` |  `enum (`[ReportTemplateCategoryEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarDashboard/legacySaveDashboardAsReportTemplate#ReportTemplateCategoryEnum)`)` Optional. The category of the report template.  
`name` |  `string` Optional. The name of the report template.  
`reportWidgets[]` |  `object (`[LegacySoarDashboardWidgetDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacySoarDashboardWidgetDataModel)`)` Optional. The report widgets of the report template.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The creation time of the report template.  
`lastModifiedTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The last modified time of the report template.  
`isSystem` |  `boolean` Optional. Is the report template a system report template.  
`hasScheduler` |  `boolean` Optional. Does the report template has scheduler.  
  
### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySoarDashboards.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ReportTemplateCategoryEnum

ReportTemplateCategoryEnum is an enum that represents the report template category.

Enums  
---  
`ROI` | Roi category  
`MANAGEMENT` | Management category  
`SLA` | Sla category  
`TIER1` | Tier1 category  
`GENERAL` | General category  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
