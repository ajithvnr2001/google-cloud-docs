---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups
title: REST Resource: projects.groups \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:39.353486+00:00
---

# REST Resource: projects.groups  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  REST Resource: projects.groups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ErrorGroup
    * JSON representation
    * TrackingIssue
      * JSON representation
    * ResolutionStatus
  * Methods



## Resource: ErrorGroup

Description of a group of similar error events.

JSON representation  
---  
      
    
    {
      "name": string,
      "groupId": string,
      "trackingIssues": [
        {
          object ([TrackingIssue](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup.TrackingIssue))
        }
      ],
      "resolutionStatus": enum ([ResolutionStatus](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup.ResolutionStatus))
    }  
  
Fields  
---  
`name` |  `string` The group resource name. Written as `projects/{projectID}/groups/{groupId}` or `projects/{projectID}/locations/{location}/groups/{groupId}`Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/us-central1/groups/my-group`In the group resource name, the `groupId` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
`groupId` |  `string` An opaque identifier of the group. This field is assigned by the Error Reporting system and always populated.In the group resource name, the `groupId` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`trackingIssues[]` |  `object (`[TrackingIssue](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup.TrackingIssue)`)` Associated tracking issues.  
`resolutionStatus` |  `enum (`[ResolutionStatus](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups#ErrorGroup.ResolutionStatus)`)` Error group's resolution status.An unspecified resolution status will be interpreted as OPEN  
  
### TrackingIssue

Information related to tracking the progress on resolving the error.

JSON representation  
---  
      
    
    {
      "url": string
    }  
  
Fields  
---  
`url` |  `string` A URL pointing to a related entry in an issue tracking system. Example: `https://github.com/user/project/issues/4`  
  
### ResolutionStatus

Resolution status of an error group.

Enums  
---  
`RESOLUTION_STATUS_UNSPECIFIED` | Status is unknown. When left unspecified in requests, it is treated like OPEN.  
`OPEN` | The error group is not being addressed. This is the default for new groups. It is also used for errors re-occurring after marked RESOLVED.  
`ACKNOWLEDGED` | Error Group manually acknowledged, it can have an issue link attached.  
`RESOLVED` | Error Group manually resolved, more events for this group are not expected to occur.  
`MUTED` | The error group is muted and excluded by default on group stats requests.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/get)`

|  Get the specified group.  
  
### `[update](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/update)`

|  Replace the data for the specified group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
