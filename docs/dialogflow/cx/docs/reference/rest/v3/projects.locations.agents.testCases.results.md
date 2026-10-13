---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results
title: REST Resource: projects.locations.agents.testCases.results \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:20.884611+00:00
---

# REST Resource: projects.locations.agents.testCases.results  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.testCases.results Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TestCaseResult
    * JSON representation
    * TestResult
  * Methods



## Resource: TestCaseResult

Represents a result from running a test case in an agent environment.

JSON representation  
---  
      
    
    {
      "name": string,
      "environment": string,
      "conversationTurns": [
        {
          object ([ConversationTurn](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn))
        }
      ],
      "testResult": enum ([TestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results#TestCaseResult.TestResult)),
      "testTime": string
    }  
  
Fields  
---  
`name` |  `string` The resource name for the test case result. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>/results/<TestCaseResultID>`.  
`environment` |  `string` Environment where the test was run. If not set, it indicates the draft environment.  
`conversationTurns[]` |  `object (`[ConversationTurn](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn)`)` The conversation turns uttered during the test case replay in chronological order.  
`testResult` |  `enum (`[TestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results#TestCaseResult.TestResult)`)` Whether the test case passed in the agent environment.  
`testTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the test was run.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### TestResult

The test result for a test case and an agent environment.

Enums  
---  
`TEST_RESULT_UNSPECIFIED` | Not specified. Should never be used.  
`PASSED` | The test passed.  
`FAILED` | The test did not pass.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results/get)`

|  Gets a test case result.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results/list)`

|  Fetches the list of run results for the given test case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
