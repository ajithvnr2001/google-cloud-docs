---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp/
title: Method: projects.locations.apps.importApp \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:29.168399+00:00
---

# Method: projects.locations.apps.importApp  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.importApp Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * ImportAppRequest.ImportOptions
    * JSON representation
  * ImportAppRequest.ImportOptions.ConflictResolutionStrategy



Imports the specified app.

### HTTP request

`POST https://ces.googleapis.com/v1/{parent=projects/*/locations/*}/apps:importApp`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name with the location of the app to import.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "displayName": string,
      "appId": string,
      "importOptions": {
        object ([ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp#ImportAppRequest.ImportOptions))
      },
      "ignoreAppLock": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsUri": string,
      "appContent": string
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "jsonPatchContent": string,
      "jsonPatchGcsUri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The display name of the app to import. * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique. * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.  
`appId` |  `string` Optional. The ID to use for the imported app. * If not specified, a unique ID will be automatically assigned for the app. * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.  
`importOptions` |  `object (`[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp#ImportAppRequest.ImportOptions)`)` Optional. Options governing the import process for the app.  
`ignoreAppLock` |  `boolean` Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock.  
The app to import. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.  
`appContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Raw bytes representing the compressed zip file with the app folder structure.A base64-encoded string.  
End of mutually exclusive fields.  
The JSON patches to apply to the imported app. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`jsonPatchContent` |  `string` Optional. Patch content as a JSON string.  
`jsonPatchGcsUri` |  `string` Optional. A Cloud Storage URI pointing to a JSON file containing the patches.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ImportAppRequest.ImportOptions

Configuration options for the app import process. These options control how the import behaves, particularly when conflicts arise with existing app data.

JSON representation  
---  
      
    
    {
      "conflictResolutionStrategy": enum ([ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp#ImportAppRequest.ImportOptions.ConflictResolutionStrategy)),
      "validateOnly": boolean
    }  
  
Fields  
---  
`conflictResolutionStrategy` |  `enum (`[ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp#ImportAppRequest.ImportOptions.ConflictResolutionStrategy)`)` Optional. The strategy to use when resolving conflicts during import.  
`validateOnly` |  `boolean` Optional. Flag for dry-running the import process. If set to true, the import process will only perform validations and will not make any changes to the existing app or create a new one.  
  
## ImportAppRequest.ImportOptions.ConflictResolutionStrategy

Defines the strategy for handling conflicts when an app with the same ID already exists, or when imported resources (like Agents, Tools, etc.) have the same display names as existing resources within that app.

Enums  
---  
`CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED` | The conflict resolution strategy is unspecified.  
`REPLACE` | Replace existing data with imported data. If an app with the same `appId` already exists, its content will be updated based on the imported app. - Resources (App, Agents, Tools, Examples, Guardrails, Toolsets) in the imported app that have the same display name as existing resources will overwrite the existing ones. - Imported resources with new display names will be created. - Existing resources that do not have a matching display name in the imported app will remain untouched.  
`OVERWRITE` | Overwrite existing data with imported data. If an app with the same `appId` already exists, its content will be overwritten with the imported app. - Existing resources (Agents, Tools, Examples, Guardrails, Toolsets) in the app will be deleted. - Imported resources will be created as new resources.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
