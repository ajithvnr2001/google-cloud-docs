---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export/
title: Method: projects.locations.agents.testCases.export \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:20.069064+00:00
---

# Method: projects.locations.agents.testCases.export  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.testCases.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * DataFormat
  * Try it!



Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[ExportTestCasesMetadata](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportTestCasesMetadata)`
  * `response`: `[ExportTestCasesResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportTestCasesResponse)`



### HTTP request

`POST https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/testCases:export`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent where to export test cases from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.testcases.export`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataFormat": enum ([DataFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export#DataFormat)),
      "filter": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsUri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`dataFormat` |  `enum (`[DataFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export#DataFormat)`)` The data format of the exported test cases. If not specified, `BLOB` is assumed.  
`filter` |  `string` The filter expression used to filter exported test cases, see [API Filtering](https://aip.dev/160). The expression is case insensitive and supports the following syntax:name =  [OR name = ] ...For example:

  * "name = t1 OR name = t2" matches the test case with the exact resource name "t1" or "t2".

  
The destination to export. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the test cases to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If unspecified, the serialized test cases is returned inline.Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DataFormat

Data format of the exported test cases.

Enums  
---  
`DATA_FORMAT_UNSPECIFIED` | Unspecified format.  
`BLOB` | Raw bytes.  
`JSON` | JSON format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
