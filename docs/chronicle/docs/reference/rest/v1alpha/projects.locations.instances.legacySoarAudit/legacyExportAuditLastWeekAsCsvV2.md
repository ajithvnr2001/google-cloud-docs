---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2/
title: Method: legacySoarAudit.legacyExportAuditLastWeekAsCsvV2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:34.552427+00:00
---

# Method: legacySoarAudit.legacyExportAuditLastWeekAsCsvV2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySoarAudit.legacyExportAuditLastWeekAsCsvV2 Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AuditSettingsRequestTypeEnum
  * ApiFile
    * JSON representation



**Full name** : projects.locations.instances.legacySoarAudit.legacyExportAuditLastWeekAsCsvV2

Exports the audit logs for the last week as a CSV file for download. The export can be filtered by specific user names and categorized by either audit counts or operation distribution.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacySoarAudit:legacyExportAuditLastWeekAsCsvV2`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance. Format: `projects/{project}/locations/{location}/instances/{instance}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "auditType": enum ([AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2#AuditSettingsRequestTypeEnum)),
      "usersNames": [
        string
      ]
    }  
  
Fields  
---  
`auditType` |  `enum (`[AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2#AuditSettingsRequestTypeEnum)`)` Optional. The type of the audit request.  
`usersNames[]` |  `string` Optional. The users names to export.  
  
### Response body

Response message for LegacySoarAuditService.LegacyExportAuditLastWeekAsCsvV2.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": {
        object ([ApiFile](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2#ApiFile))
      }
    }  
  
Fields  
---  
`payload` |  `object (`[ApiFile](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyExportAuditLastWeekAsCsvV2#ApiFile)`)` Required. The ApiFile response.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySoarAudits.legacySoarAudit`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AuditSettingsRequestTypeEnum

Enum that represents the type of the audit settings request.

Enums  
---  
`GROUP` | Group.  
`COUNT` | Count.  
  
## ApiFile

Message that represents a file.

JSON representation  
---  
      
    
    {
      "fileName": string,
      "blob": string
    }  
  
Fields  
---  
`fileName` |  `string` Optional. File name.  
`blob` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` File blob.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
