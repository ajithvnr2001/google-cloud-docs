---
url: https://docs.cloud.google.com/resource-manager/docs/folder-error-details/
title: Folder API error details \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:05.373818+00:00
---

# Folder API error details  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/folder-error-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Folder API error details Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes the meaning of the error code strings returned when a folder API operation fails due to a folder constraint violation. When this occurs, a `PreconditionFailure` explaining the violation will be returned.

If the failure occurs synchronously, then the `PreconditionFailure` will be returned using the `Status.details` field. If it occurs asynchronously, then the `PreconditionFailure` will be returned using the `Operation.error` field. These values appear as strings in the type field of the `PreconditionFailure.Violation` message returned in `Status.details`.

Status string | Description  
---|---  
`ERROR_TYPE_UNSPECIFIED` | The error type was unrecognized or unspecified.  
`ACTIVE_FOLDER_HEIGHT_VIOLATION` | The attempted action would cause the folder tree to have a depth greater than the maximum of four.  
`MAX_CHILD_FOLDERS_VIOLATION` | The attempted action would create a child folder beyond the maximum of 300.  
`FOLDER_NAME_UNIQUENESS_VIOLATION` | The attempted action would violate the locally-unique folder `display_name` constraint.  
`RESOURCE_DELETED_VIOLATION` | The resource being moved has been deleted.  
`PARENT_DELETED_VIOLATION` | The resource a folder was being added to has been deleted.  
`CYCLE_INTRODUCED_VIOLATION` | The attempted action would introduce cycle in resource path.  
`FOLDER_BEING_MOVED_VIOLATION` | The attempted action would move a folder that is already being moved.  
`FOLDER_TO_DELETE_NON_EMPTY_VIOLATION` | The folder the caller is trying to delete contains active resources or is associated with firewall policies.  
`DELETED_FOLDER_HEIGHT_VIOLATION` | The attempted action would violate the max deleted folder depth constraint, where the full folder tree's depth (including deleted folders) can be no more than 8.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
