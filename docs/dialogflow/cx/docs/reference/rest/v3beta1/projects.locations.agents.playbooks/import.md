---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.playbooks/import/
title: Method: projects.locations.agents.playbooks.import \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:34.936463+00:00
---

# Method: projects.locations.agents.playbooks.import  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.playbooks/import/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.playbooks.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * PlaybookImportStrategy
    * JSON representation
  * Try it!



Imports the specified playbook to the specified agent from a binary file.

### HTTP request

`POST https://{endpoint}/v3beta1/{parent=projects/*/locations/*/agents/*}/playbooks:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent to import the playbook into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.playbooks.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "importStrategy": {
        object ([PlaybookImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.playbooks/import#PlaybookImportStrategy))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "playbookUri": string,
      "playbookContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`importStrategy` |  `object (`[PlaybookImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.playbooks/import#PlaybookImportStrategy)`)` Optional. Specifies the import strategy used when resolving resource conflicts.  
Required. The playbook to import. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import playbook from. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`playbookUri` |  `string` [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`playbookContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Uncompressed raw byte content for playbook.A base64-encoded string.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PlaybookImportStrategy

The playbook import strategy used for resource conflict resolution associated with an `ImportPlaybookRequest`.

JSON representation  
---  
      
    
    {
      "mainPlaybookImportStrategy": enum ([ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy)),
      "nestedResourceImportStrategy": enum ([ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy)),
      "toolImportStrategy": enum ([ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy))
    }  
  
Fields  
---  
`mainPlaybookImportStrategy` |  `enum (`[ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy)`)` Optional. Specifies the import strategy used when resolving conflicts with the main playbook. If not specified, 'CREATE_NEW' is assumed.  
`nestedResourceImportStrategy` |  `enum (`[ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy)`)` Optional. Specifies the import strategy used when resolving referenced playbook/flow conflicts. If not specified, 'CREATE_NEW' is assumed.  
`toolImportStrategy` |  `enum (`[ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/ImportStrategy)`)` Optional. Specifies the import strategy used when resolving tool conflicts. If not specified, 'CREATE_NEW' is assumed. This will be applied after the main playbook and nested resource import strategies, meaning if the playbook that references the tool is skipped, the tool will also be skipped.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
