---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/import/
title: Method: projects.locations.spaces.applicationTemplates.import \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:08.612979+00:00
---

# Method: projects.locations.spaces.applicationTemplates.import  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.applicationTemplates.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Imports to an existing application template from a given shared template.

### HTTP request

`POST https://designcenter.googleapis.com/v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:import`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the application template.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "annotations": {
        string: string,
        ...
      },
    
      // Union field source can be only one of the following:
      "applicationTemplateRevisionUri": string,
      "sharedTemplateRevisionUri": string,
      "serializedApplicationTemplate": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "applicationTemplateSystemRevision": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`annotations` |  `map (key: string, value: string)` Optional. Annotations to be stored with the new system revision created as a result of this import. Sample annotations from agentic workflows might look like { "designcenter.googleapis.com/agent_id": "gemini-3-flash-v1", "designcenter.googleapis.com/llm_agent_summary": "Restored to revision Rev-100", "designcenter.googleapis.com/external_ref_id": "trace-uuid-88921-xyz", }An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `source`. The source for setting application template components/connections. `source` can be only one of the following:  
`applicationTemplateRevisionUri` |  `string` Optional. The source URI for application template revision.  
`sharedTemplateRevisionUri` |  `string` Optional. The source URI for catalog template.  
`serializedApplicationTemplate` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Optional. The serialized application template to be imported.  
`applicationTemplateSystemRevision` |  `string` Optional. The system revision to be imported. Used when user tries to Restore (rev X) or perform Undo/Redo operations.  
  
### Response body

If successful, the response body contains an instance of `[ApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationTemplate)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `designcenter.applicationTemplates.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
