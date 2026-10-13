---
url: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/getStatus/
title: Method: projects.locations.getStatus \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:00.117677+00:00
---

# Method: projects.locations.getStatus  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/getStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/document-warehouse/docs/reference/rest)



Send feedback 

#  Method: projects.locations.getStatus Stay organized with collections  Save and categorize content based on your preferences. 

Get the project status.

### HTTP request

`GET https://contentwarehouse.googleapis.com/v1/{location}:getStatus`

### Path parameters

Parameters  
---  
`location` |  `string` Required. The location to be queried Format: projects/{projectNumber}/locations/{location}. It takes the form `projects/{project}/locations/{location}`.  
  
### Request body

The request body must be empty.

### Response body

status of a project, including the project state, dbType, aclMode and etc.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "location": string,
      "state": enum ([ProjectState](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/getStatus#ProjectState)),
      "databaseType": enum ([DatabaseType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/DatabaseType)),
      "accessControlMode": enum ([AccessControlMode](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/AccessControlMode)),
      "documentCreatorDefaultRole": string,
      "qaEnabled": boolean
    }  
  
Fields  
---  
`location` |  `string` The location of the queried project.  
`state` |  `enum (`[ProjectState](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/getStatus#ProjectState)`)` state of the project.  
`databaseType` |  `enum (`[DatabaseType](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/DatabaseType)`)` Database type.  
`accessControlMode` |  `enum (`[AccessControlMode](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/AccessControlMode)`)` Access control mode.  
`documentCreatorDefaultRole` |  `string` The default role for the person who create a document.  
`qaEnabled` |  `boolean` If the qa is enabled on this project.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ProjectState

state of a project.

Enums  
---  
`PROJECT_STATE_UNSPECIFIED` | Default status, required by protobuf best practices.  
`PROJECT_STATE_PENDING` | The project is in the middle of a provision process.  
`PROJECT_STATE_COMPLETED` | All dependencies have been provisioned.  
`PROJECT_STATE_FAILED` | A provision process was previously initiated, but failed.  
`PROJECT_STATE_DELETING` | The project is in the middle of a deletion process.  
`PROJECT_STATE_DELETING_FAILED` | A deleting process was initiated, but failed.  
`PROJECT_STATE_DELETED` | The project is deleted.  
`PROJECT_STATE_NOT_FOUND` | The project is not found.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
