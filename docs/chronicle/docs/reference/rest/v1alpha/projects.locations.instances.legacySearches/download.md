---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download/
title: Method: legacySearches.download \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:15.523559+00:00
---

# Method: legacySearches.download  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySearches.download Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CasePriority
  * CloseReasonEnum
  * SearchTimeRangeType
  * SortBy
    * JSON representation
  * SortOrder
  * SearchEverythingCaseProperty
  * Paging
    * JSON representation



**Full name** : projects.locations.instances.legacySearches.download

Exports case search results to a CSV file. Use this method to retrieve investigation data in a format suitable for external reporting or spreadsheet analysis.

### HTTP request

`GET https://{endpoint}/v1alpha/{name}/legacySearches:legacyGetSearchResultsAsCsv`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name to get the search results for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Defines the UTC start time to search for cases by Creation time (optional - used if TimeRangeFilter is set to Custom filter). The Localization (timezone) settings are taken into consideration (default is the start of epoch time).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Defines the UTC end time to search for cases by Creation time (optional - used if TimeRangeFilter is set to Custom filter). The Localization (timezone) settings are taken into consideration (default is current time).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tags[]` |  `string` Optional. List of strings representing case tags. If one or more tags exist in the case, it will be fetched.  
`caseSource[]` |  `string` Optional. List of strings representing case sources. Available inputs: System / Manual / Test.  
`priorities[]` |  `enum (`[CasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#CasePriority)`)` Optional. List of strings representing case priority  
`importance[]` |  `string` Optional. List of strings representing the case importance (i.e. marked as "is important"). ex. ["True"] will return only cases that were marked as important. ex. ["True","False] Will return only cases marked as important and all cases not marked as important (all). Available inputs: True / False.  
`incident[]` |  `string` Optional. List of strings representing cases marked as incidents. ex. ["True"] will return only cases that were marked as an incident. ex. ["True","False"] Will return all cases marked as an incident and all cases not marked as an incident (all). Available inputs: True / False.  
`environments[]` |  `string` Optional. List of strings representing the environments that the case is associated with. If the case matches at least one environment it will be fetched.  
`assignedUsers[]` |  `string` Optional. A list of strings that represents the Users (analysts) / Roles that are assigned to the case. If the case matches at least one User or Role it will be fetched. Available inputs: Username (GUID) / @Role name.  
`externalAlertId` |  `string` Optional. Represents the 'TicketId' mapped from the original SIEM's alert ID  
`products[]` |  `string` Optional. list of strings that represent the Products that exists in the case. If the case matches at least one Product it will be fetched.  
`ports[]` |  `string` Optional. List of strings that represent the ports that exist in the case. If the case matches at least one Port it will be fetched.  
`stage[]` |  `string` Optional. List of strings that represents the Stages that case is on. If the case matches at least one Stage it will be fetched. Available inputs: Triage / Assessment / Investigation / Incident / Improvement / Research.  
`ruleGenerator[]` |  `string` Optional. List of strings that represents the Rule Generator (Alert Type in the Platform) that exist in the case. If the case matches at least one Rule Generator it will be fetched.  
`categoryOutcomes[]` |  `string` Optional. List of strings that represents whether to fetch cases that contain a specific value in CategoryOutcome. Available inputs: Allowed / Blocked / [] (empty).  
`involvedEntity` |  `string` Optional. A string that represents an entity to search for in cases  
`caseComment` |  `string` Optional. A string that represents a part of the body of a case comment to search for in cases  
`title` |  `string` Optional. A string that represents free text / search term to search for cases. Free text will look for the case's name. Available inputs: free text / Entity: / AlertName: / DestinationEntity: / SourceEntity: / TicketIds: / CaseIDs:  
`sortBy` |  `object (`[SortBy](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SortBy)`)` Optional. The sort by property and order.  
`paging` |  `object (`[Paging](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#Paging)`)`  
`requestedPage` |  `integer` Optional. The requested page.  
`pageSize` |  `integer` Optional. Number of entries to return.  
`searchTerm` |  `string` Optional. Search term.  
`isCaseClosed` |  `boolean` Optional. A boolean field that represents whether to filter by the case status (is closed or not). Available inputs: true / false / null.  
`closeReason` |  `enum (`[CloseReasonEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#CloseReasonEnum)`)` Optional. An integer field that represents the Reason the case was closed and fetches cases that match the value  
`timeRangeFilter` |  `enum (`[SearchTimeRangeType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SearchTimeRangeType)`)` Optional. A SearchTimeRangeType (integer) field that represents the number of days back to search cases by creation. time (for custom time range, use 0 and set the StartTime and EndTime parameters).  
  
### Request body

The request body must be empty.

### Response body

Response for legacySearches.download.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "media": {
        object ([Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media))
      }
    }  
  
Fields  
---  
`media` |  `object (`[Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media)`)` Zipped file with the integration content. Includes the following folders: Actions, Connectors, Jobs, Managers, Dependencies Each folder includes json files and a python file for the script. Includes integration definition json file. Includes metadata.json file Information representing the imported data  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.legacySearches.searchCases`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CasePriority

Enum that represents the case priority

Enums  
---  
`UNCHANGED` | Unspecified case priority.  
`INFORMATIVE` | Informative case priority.  
`LOW` | Low case priority.  
`MEDIUM` | Medium case priority.  
`HIGH` | High case priority.  
`CRITICAL` | Critical case priority.  
  
## CloseReasonEnum

Enum that represents the case close reason

Enums  
---  
`MALICIOUS` | Malicious close reason.  
`NOT_MALICIOUS` | Not malicious close reason.  
`MAINTENANCE` | Maintenance close reason.  
`INCONCLUSIVE` | Inconclusive close reason.  
`UNKNOWN` | Unknown close reason.  
  
## SearchTimeRangeType

LINT: LEGACY_NAMES Enum that represents the search time range type

Enums  
---  
`CUSTOM` | Custom search time range type.  
`LAST_DAY` | Last day search time range type.  
`LAST_2_DAYS` | Last 2 days search time range type.  
`LAST_3_DAYS` | Last 3 days search time range type.  
`LAST_4_DAYS` | Last 4 days search time range type.  
`LAST_WEEK` | Last week search time range type.  
`LAST_2_WEEKS` | Last 2 weeks search time range type.  
`LAST_MONTH` | Last month search time range type.  
`LAST_3_MONTHS` | Last 3 months search time range type.  
`LAST_6_MONTHS` | Last 6 months search time range type.  
`LAST_YEAR` | Last year search time range type.  
`LAST_13_MONTHS` | Last 13 months search time range type.  
  
## SortBy

Message that represents the order by.

JSON representation  
---  
      
    
    {
      "sortOrder": enum ([SortOrder](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SortOrder)),
      "sortBy": enum ([SearchEverythingCaseProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SearchEverythingCaseProperty))
    }  
  
Fields  
---  
`sortOrder` |  `enum (`[SortOrder](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SortOrder)`)` Optional. The sort order.  
`sortBy` |  `enum (`[SearchEverythingCaseProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySearches/download#SearchEverythingCaseProperty)`)` Optional. The sort by property.  
  
## SortOrder

Enum that represents the sort order.

Enums  
---  
`DESCENDING` | Descending sort order.  
`ASCENDING` | Ascending sort order.  
  
## SearchEverythingCaseProperty

Enum that represents the properties that can be used to sort the cases.

Enums  
---  
`ID` | Id search everything case property.  
`TITLE` | Title search everything case property.  
`TIME` | Time search everything case property.  
`USER_ASSIGNED` | UserAssigned search everything case property.  
`IS_IMPORTANT` | IsImportant search everything case property.  
`IS_INCIDENT` | IsIncident search everything case property.  
`INVOLVED_SUSPICIOUS_ENTITY` | InvolvedSuspiciousEntity search everything case property.  
`IS_CASE_CLOSED` | IsCaseClosed search everything case property.  
`ENVIRONMENT` | Environment search everything case property.  
`PRIORITY` | Priority search everything case property.  
`STAGE` | Stage search everything case property.  
  
## Paging

JSON representation  
---  
      
    
    {
      "requestedPage": integer,
      "pageSize": integer
    }  
  
Fields  
---  
`requestedPage` |  `integer` Optional. The requested page.  
`pageSize` |  `integer` Optional. Number of entries to return.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
