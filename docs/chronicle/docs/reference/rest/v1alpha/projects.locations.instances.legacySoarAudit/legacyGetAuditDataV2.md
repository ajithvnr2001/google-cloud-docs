---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2/
title: Method: legacySoarAudit.legacyGetAuditDataV2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:12.063565+00:00
---

# Method: legacySoarAudit.legacyGetAuditDataV2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySoarAudit.legacyGetAuditDataV2 Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AuditSettingsRequestTypeEnum
  * AuditSettingsResponse
    * JSON representation
  * AuditSettingsRequestTypeEnum
  * AuditData
    * JSON representation
  * CountData
    * JSON representation
  * MostActiveUsersCountData
    * JSON representation



**Full name** : projects.locations.instances.legacySoarAudit.legacyGetAuditDataV2

Retrieves a paginated list of audit logs and statistical data from SecOps. This includes details about user activities, operations performed, and system-wide audit distributions, with support for filtering by users and API keys.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacySoarAudit:legacyGetAuditDataV2`

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
      "pageNumber": integer,
      "usersNames": [
        string
      ],
      "apiKeys": [
        string
      ],
      "auditSettingsRequestType": enum ([AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsRequestTypeEnum))
    }  
  
Fields  
---  
`pageNumber` |  `integer` Optional. The page number of the audit data.  
`usersNames[]` |  `string` Optional. The users names to get the audit data for.  
`apiKeys[]` |  `string` Optional. The api keys to get the audit data for.  
`auditSettingsRequestType` |  `enum (`[AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsRequestTypeEnum)`)` Optional. The type of the audit request.  
  
### Response body

Response message for LegacySoarAuditService

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": {
        object ([AuditSettingsResponse](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsResponse))
      }
    }  
  
Fields  
---  
`payload` |  `object (`[AuditSettingsResponse](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsResponse)`)` Required. The AuditSettingsResponse response.  
  
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
  
## AuditSettingsResponse

Message that represents a audit settings response.

JSON representation  
---  
      
    
    {
      "auditRecords": [
        {
          object ([AuditData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditData))
        }
      ],
      "operationsDistribution": [
        {
          object ([CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData))
        }
      ],
      "mostCommonOperations": [
        {
          object ([CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData))
        }
      ],
      "mostCommonResulations": [
        {
          object ([CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData))
        }
      ],
      "mostCommonActiveUsers": [
        {
          object ([MostActiveUsersCountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#MostActiveUsersCountData))
        }
      ],
      "mostCommonBrowsers": [
        {
          object ([CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData))
        }
      ],
      "mostCommonAddresses": [
        {
          object ([CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData))
        }
      ],
      "totalCount": integer,
      "pageSize": integer,
      "pageNumber": integer,
      "auditSettingsRequestType": enum ([AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsRequestTypeEnum_1))
    }  
  
Fields  
---  
`auditRecords[]` |  `object (`[AuditData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditData)`)` Optional. Audit records.  
`operationsDistribution[]` |  `object (`[CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData)`)` Optional. Operations distribution.  
`mostCommonOperations[]` |  `object (`[CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData)`)` Optional. Most common operations.  
`mostCommonResulations[]` |  `object (`[CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData)`)` Optional. Most common regulations.  
`mostCommonActiveUsers[]` |  `object (`[MostActiveUsersCountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#MostActiveUsersCountData)`)` Optional. Most common active users.  
`mostCommonBrowsers[]` |  `object (`[CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData)`)` Optional. Most common browsers.  
`mostCommonAddresses[]` |  `object (`[CountData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#CountData)`)` Optional. Most common addresses.  
`totalCount` |  `integer` Optional. Total count.  
`pageSize` |  `integer` Optional. Page size.  
`pageNumber` |  `integer` Optional. Page number.  
`auditSettingsRequestType` |  `enum (`[AuditSettingsRequestTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarAudit/legacyGetAuditDataV2#AuditSettingsRequestTypeEnum_1)`)` Optional. Audit settings request type.  
  
## AuditSettingsRequestTypeEnum

Enum that represents the type of the audit settings request.

Enums  
---  
`GROUP` | Group.  
`COUNT` | Count.  
  
## AuditData

Message that represents an audit data.

JSON representation  
---  
      
    
    {
      "id": string,
      "user": string,
      "userGuid": string,
      "module": string,
      "operation": string,
      "address": string,
      "browser": string,
      "screenSize": string,
      "activityItem": string,
      "currentActivity": string,
      "previousActivity": string,
      "source": string,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The id.  
`user` |  `string` The user name is audited.  
`userGuid` |  `string` Optional. The user guid.  
`module` |  `string` Optional. The module.  
`operation` |  `string` Optional. The operation.  
`address` |  `string` The address.  
`browser` |  `string` The browser.  
`screenSize` |  `string` The screen size.  
`activityItem` |  `string` The activity item.  
`currentActivity` |  `string` Optional. The current activity.  
`previousActivity` |  `string` Optional. The previous activity.  
`source` |  `string` The source.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The creation time of the audit data.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The modification time of the audit data.  
  
## CountData

Message that represents a count data.

JSON representation  
---  
      
    
    {
      "name": string,
      "count": integer,
      "countLabel": string
    }  
  
Fields  
---  
`name` |  `string` The name.  
`count` |  `integer` Optional. The count.  
`countLabel` |  `string` Optional. The count label.  
  
## MostActiveUsersCountData

Message that represents a most active users count data.

JSON representation  
---  
      
    
    {
      "userFullName": string,
      "name": string,
      "count": integer,
      "countLabel": string
    }  
  
Fields  
---  
`userFullName` |  `string` The user full name.  
`name` |  `string` Name of the user.  
`count` |  `integer` Optional. The count.  
`countLabel` |  `string` Optional. The count label.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
