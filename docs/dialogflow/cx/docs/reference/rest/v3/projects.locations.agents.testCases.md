---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases
title: REST Resource: projects.locations.agents.testCases \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:19.977379+00:00
---

# REST Resource: projects.locations.agents.testCases  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.testCases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TestCase
    * JSON representation
  * TestConfig
    * JSON representation
  * Methods



## Resource: TestCase

Represents a test case.

JSON representation  
---  
      
    
    {
      "name": string,
      "tags": [
        string
      ],
      "displayName": string,
      "notes": string,
      "testConfig": {
        object ([TestConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases#TestConfig))
      },
      "testCaseConversationTurns": [
        {
          object ([ConversationTurn](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn))
        }
      ],
      "creationTime": string,
      "lastTestResult": {
        object ([TestCaseResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results#TestCaseResult))
      }
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the test case. `[TestCases.CreateTestCase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/create#google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase)` will populate the name automatically. Otherwise use format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`.  
`tags[]` |  `string` Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with "#" and has a limit of 30 characters.  
`displayName` |  `string` Required. The human-readable name of the test case, unique within the agent. Limit of 200 characters.  
`notes` |  `string` Additional freeform notes about the test case. Limit of 400 characters.  
`testConfig` |  `object (`[TestConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases#TestConfig)`)` Config for the test case.  
`testCaseConversationTurns[]` |  `object (`[ConversationTurn](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn)`)` The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the test was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastTestResult` |  `object (`[TestCaseResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results#TestCaseResult)`)` The latest test result.  
  
## TestConfig

Represents configurations for a test case.

JSON representation  
---  
      
    
    {
      "trackingParameters": [
        string
      ],
      "flow": string,
      "page": string
    }  
  
Fields  
---  
`trackingParameters[]` |  `string` Session parameters to be compared when calculating differences.  
`flow` |  `string` Flow name to start the test case with. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.Only one of `flow` and `page` should be set to indicate the starting point of the test case. If neither is set, the test case will start with start page on the default start flow.  
`page` |  `string` The `[page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)` to start the test case with. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.Only one of `flow` and `page` should be set to indicate the starting point of the test case. If neither is set, the test case will start with start page on the default start flow.  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/batchDelete)`

|  Batch deletes test cases.  
  
### `[batchRun](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/batchRun)`

|  Kicks off a batch run of test cases.  
  
### `[calculateCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage)`

|  Calculates the test coverage for an agent.  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/create)`

|  Creates a test case for the given agent.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export)`

|  Exports the test cases under the agent to a Cloud Storage bucket or a local file.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/get)`

|  Gets a test case.  
  
### `[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/import)`

|  Imports the test cases from a Cloud Storage bucket or a local file.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/list)`

|  Fetches a list of test cases for a given agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/patch)`

|  Updates the specified test case.  
  
### `[run](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/run)`

|  Kicks off a test case run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
